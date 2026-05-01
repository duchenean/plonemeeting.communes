# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#

from plonemeeting.core.interfaces import IMeetingAdviceWorkflowActions
from plonemeeting.core.interfaces import IMeetingAdviceWorkflowConditions
from plonemeeting.core.interfaces import IMeetingItemWorkflowActions
from plonemeeting.core.interfaces import IMeetingItemWorkflowConditions
from plonemeeting.core.interfaces import IMeetingWorkflowActions
from plonemeeting.core.interfaces import IMeetingWorkflowConditions
from plonemeeting.core.interfaces import IPloneMeetingLayer


class IMeetingCommunesWorkflowActions(IMeetingWorkflowActions):
    '''This interface represents a meeting as viewed by the specific meeting
       workflow that is defined in this MeetingCommunes product.'''
    def doDecide():
        """
          Triggered while doing the 'decide' transition
        """
    def doBackToPublished():
        """
          Triggered while going back to the 'published' state
        """


class IMeetingCommunesWorkflowConditions(IMeetingWorkflowConditions):
    '''This interface represents a meeting as viewed by the specific meeting
       workflow that is defined in this MeetingCommunes product.'''
    def mayDecide():
        """
          Guard for the 'decide' transition
        """


class IMeetingItemCommunesWorkflowActions(IMeetingItemWorkflowActions):
    '''This interface represents a meeting item as viewed by the specific
       item workflow that is defined in this MeetingCommunes product.'''
    def doAcceptButModify():
        """
          Triggered while doing the 'accept_but_modify' transition
        """
    def doPreAccept():
        """
          Triggered while doing the 'pre_accept' transition
        """


class IMeetingItemCommunesWorkflowConditions(IMeetingItemWorkflowConditions):
    '''This interface represents a meeting item as viewed by the specific
       meeting item workflow that is defined in this MeetingCommunes product.'''
    def mayDecide():
        """
          Guard for the 'decide' transition
        """
    def mayPublish():
        """
          Guard for the 'publish' transition
        """


class IMeetingAdviceCommunesWorkflowActions(IMeetingAdviceWorkflowActions):
    ''' '''


class IMeetingAdviceCommunesWorkflowConditions(IMeetingAdviceWorkflowConditions):
    ''' '''

class IMeetingCommunesLayer(IPloneMeetingLayer):
    ''' '''
