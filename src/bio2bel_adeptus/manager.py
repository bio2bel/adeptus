# -*- coding: utf-8 -*-

"""Manager for Bio2BEL ADEPTUS."""

from typing import Mapping

from tqdm import tqdm

from bio2bel.manager.bel_manager import BELManagerMixin
from pybel import BELGraph
from pybel.constants import NEGATIVE_CORRELATION, POSITIVE_CORRELATION
from pybel.dsl import Pathology, Rna
from .constants import MODULE_NAME
from .models import Base
from .parser import get_adeptus_df


class Manager(BELManagerMixin):
    """Disease-specific differential gene expression."""

    module_name = MODULE_NAME
    _base = None

    def __init__(self, *args, **kwargs):  # noqa: D107
        self.graph = get_graph()

    @classmethod
    def _get_connection(cls):
        pass

    @staticmethod
    def is_populated() -> bool:
        """Check if the Bio2BEL ADEPTUS database is populated."""
        return True

    def summarize(self) -> Mapping[str, int]:
        """Summarize the contents of the Bio2BEL ADEPTUS database."""
        return dict(
            correlations=self.count_relations(),
            diseases=self.count_diseases(),
            rnas=self.count_rnas(),
        )

    def populate(self) -> None:
        """Populate the Bio2BEL ADEPTUS database."""
        raise NotImplementedError

    def count_diseases(self) -> int:
        """Count the number of diseases."""
        return sum(
            isinstance(node, Pathology)
            for node in self.graph
        )

    def count_rnas(self) -> int:
        """Count the number of RNAs."""
        return sum(
            isinstance(node, Rna)
            for node in self.graph
        )

    def count_relations(self) -> int:
        """Count the number of disease-differential expressed gene relations."""
        return self.graph.number_of_edges()

    def to_bel(self) -> BELGraph:
        """Output ADEPTUS as a BEL graph."""
        return self.graph


def get_graph(use_tqdm: bool = False) -> BELGraph:
    graph = BELGraph(
        name='ADEPTUS',
        version='0.0.0',
        description="""ADEPTUS conversion to BEL using Daniel Himmelstein's data at https://raw.githubusercontent.com/dhimmel/adeptus/master/data/gene-sets.tsv"""
    )
    graph.annotation_pattern['Database'] = '.*'
    graph.annotation_pattern['ADEPTUS_PB_ROC'] = '.*'
    graph.annotation_pattern['ADEPTUS_PN_ROC'] = '.*'

    df = get_adeptus_df()

    it = df.iterrows()
    if use_tqdm:
        it = tqdm(it, desc='ADEPTUS to BEL', total=len(df.index))
    for _, (disease_doid, disease_name, entrez_id, entrez_name, pb_roc, pn_roc, direction) in it:
        disease = Pathology(
            namespace='doid',
            name=disease_name,
            identifier=disease_doid,
        )
        gene = Rna(
            namespace='ncbigene',
            name=entrez_name,
            identifier=str(entrez_id),
        )

        relation = POSITIVE_CORRELATION if direction == 'up' else NEGATIVE_CORRELATION

        graph.add_qualified_edge(
            disease,
            gene,
            relation=relation,
            citation='26261215',
            evidence='ADEPTUS database',
            annotations={
                'bio2bel': MODULE_NAME,
                'ADEPTUS_PB_ROC': pb_roc,
                'ADEPTUS_PN_ROC': pn_roc,
            }
        )

    return graph
