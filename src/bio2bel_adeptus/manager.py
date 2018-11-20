# -*- coding: utf-8 -*-

"""Manager for Bio2BEL ADEPTUS."""

from typing import Mapping

import pybel.dsl
from bio2bel.manager.bel_manager import BELManagerMixin
from pybel import BELGraph
from pybel.constants import NEGATIVE_CORRELATION, POSITIVE_CORRELATION
from tqdm import tqdm

from .constants import MODULE_NAME
from .models import Base
from .parser import get_adeptus_df


class Manager(BELManagerMixin):
    """Manages the Bio2BEL ADEPTUS database."""

    module_name = MODULE_NAME
    _base = Base

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def _get_connection(cls):
        return ''

    def is_populated(self) -> bool:
        """Check if the Bio2BEL ADEPTUS database is populated."""
        raise NotImplementedError

    def summarize(self) -> Mapping[str, int]:
        """Summarize the contents of the Bio2BEL ADEPTUS database."""
        raise NotImplementedError

    def populate(self) -> None:
        """Populate the Bio2BEL ADEPTUS database."""
        raise NotImplementedError

    def to_bel(self) -> BELGraph:
        """Output ADEPTUS as a BEL graph."""
        graph = BELGraph(
            name='ADEPTUS',
            version='0.0.0',
            description="""ADEPTUS conversion to BEL using Daniel Himmelstein's data at https://raw.githubusercontent.com/dhimmel/adeptus/master/data/gene-sets.tsv"""
        )
        graph.annotation_pattern['Database'] = '.*'
        graph.annotation_pattern['ADEPTUS_PB_ROC'] = '.*'
        graph.annotation_pattern['ADEPTUS_PN_ROC'] = '.*'

        df = get_adeptus_df()

        for _, (disease_doid, disease_name, entrez_id, entrez_name, pb_roc, pn_roc, direction) in tqdm(df.iterrows()):
            disease = pybel.dsl.Pathology(
                namespace='doid',
                name=disease_name,
                identifier=disease_doid,
            )
            gene = pybel.dsl.Gene(
                namespace='ncbigene',
                name=entrez_name,
                identifier=entrez_id,
            )

            relation = POSITIVE_CORRELATION if direction == 'up' else NEGATIVE_CORRELATION

            graph.add_qualified_edge(
                disease,
                gene,
                relation=relation,
                citation='26261215',
                evidence='ADEPTUS database',
                annotations={
                    'Database': 'ADEPTUS',
                    'ADEPTUS_PB_ROC': pb_roc,
                    'ADEPTUS_PN_ROC': pn_roc,
                }
            )

        return graph
