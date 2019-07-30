# -*- coding: utf-8 -*-

"""Constants for Bio2BEL ADEPTUS."""

import os

from bio2bel import get_data_dir

__all__ = [
    'VERSION',
    'MODULE_NAME',
    'DATA_DIR',
    'ADEPTUS_DATA_URL',
    'ADEPTUS_DATA_PATH',
]

VERSION = '0.0.2-dev'
MODULE_NAME = 'adeptus'
DATA_DIR = get_data_dir(MODULE_NAME)

ADEPTUS_DATA_URL = 'https://raw.githubusercontent.com/dhimmel/adeptus/master/data/gene-sets.tsv'
ADEPTUS_DATA_PATH = os.path.join(DATA_DIR, 'gene-sets.tsv')
