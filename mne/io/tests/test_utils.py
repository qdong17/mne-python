# -*- coding: utf-8 -*-
"""Run tests for the utilities."""
# Author: Stefan Appelhoff <stefan.appelhoff@mailbox.org>
#
# License: BSD (3-clause)

from ..utils import _check_orig_units


def test_check_orig_units():
    """Test the checking of original units."""
    orig_units = dict(FC1='nV', Hfp3erz='n/a', Pz='uV', greekMu=u'μV',
                      microSign=u'µV')
    orig_units = _check_orig_units(orig_units)
    assert orig_units['FC1'] == 'nV'
    assert orig_units['Hfp3erz'] == 'n/a'
    assert orig_units['Pz'] == u'µV'
    assert orig_units['greekMu'] == u'µV'
    assert orig_units['microSign'] == u'µV'
