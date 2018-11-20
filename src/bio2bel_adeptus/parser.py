# -*- coding: utf-8 -*-

"""Parsers and downloaders for ADEPTUS."""

from bio2bel.downloading import make_df_getter

from .constants import ADEPTUS_DATA_PATH, ADEPTUS_DATA_URL

__all__ = ['get_adeptus_df']

get_adeptus_df = make_df_getter(
    ADEPTUS_DATA_URL,
    ADEPTUS_DATA_PATH,
    sep='\t',
)
