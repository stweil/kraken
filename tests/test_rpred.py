# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os
import unittest

from PIL import Image
from nose.tools import raises

from kraken.lib import lstm
from kraken.rpred import rpred
from kraken.lib.exceptions import KrakenInputException


thisfile = os.path.abspath(os.path.dirname(__file__))
resources = os.path.abspath(os.path.join(thisfile, 'resources'))

class TestRecognition(unittest.TestCase):

    """
    Tests of the recognition facility and associated routines.
    """
    def setUp(self):
        self.im = Image.open(os.path.join(resources, 'bw.png'))

    def tearDown(self):
        self.im.close()

    @raises(KrakenInputException)
    def test_rpred_outbounds(self):
        """
        Tests correct handling of invalid line coordinates.
        """
        pred = rpred(None, self.im, [(-1, -1, 10000, 10000)])
        next(pred)
