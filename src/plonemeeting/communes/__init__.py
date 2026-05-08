# -*- coding: utf-8 -*-
from __future__ import absolute_import

from Products.CMFCore import DirectoryView

import logging
import os


logger = logging.getLogger('plonemeeting.communes')
logger.debug('Installing Product')

product_globals = globals()
DirectoryView.registerDirectory('skins', product_globals)

__author__ = """Gauthier Bastien <g.bastien@imio.be>, Stephan Geulette <s.geulette@imio.be>"""
__docformat__ = 'plaintext'


# P6 migration: AT model extensions dropped (Products.Archetypes removed).
# from plonemeeting.communes.model import pm_updates  # noqa
from plonemeeting.communes import adapters  # noqa


def initialize(context):
    """initialize product (called by zope)"""
