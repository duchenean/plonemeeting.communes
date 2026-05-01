# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#

from plonemeeting.communes.tests.MeetingCommunesTestCase import MeetingCommunesTestCase
from plonemeeting.core.tests.testAdvices import testAdvices as pmta


class testAdvices(MeetingCommunesTestCase, pmta):
    '''Tests various aspects of advices management.
       Advices are enabled for PloneGov Assembly, not for PloneMeeting Assembly.'''


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testAdvices, prefix='test_pm_'))
    return suite
