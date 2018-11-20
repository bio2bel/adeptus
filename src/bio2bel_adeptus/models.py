# -*- coding: utf-8 -*-

"""SQLAlchemy models for Bio2BEL ADEPTUS."""

import logging

from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

__all__ = [
    'Base',
]

logger = logging.getLogger(__name__)

Base: DeclarativeMeta = declarative_base()
