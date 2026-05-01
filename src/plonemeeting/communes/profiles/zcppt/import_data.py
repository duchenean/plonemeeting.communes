# -*- coding: utf-8 -*-

from copy import deepcopy
from plonemeeting.communes.profiles.simple import import_data as simple_import_data
from plonemeeting.core.profiles import PloneMeetingConfiguration


config = deepcopy(simple_import_data.simpleMeeting)
config.id = 'cppt'
config.title = 'CPPT'
config.folderTitle = 'CPPT'
config.shortName = 'CPPT'

data = PloneMeetingConfiguration(
    meetingFolderTitle='Mes séances',
    meetingConfigs=(config, ),
    orgs=[])
