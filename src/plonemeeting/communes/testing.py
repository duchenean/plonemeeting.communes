# -*- coding: utf-8 -*-

from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.testing import z2
from plone.testing import zca
from plonemeeting.core.testing import PMLayer

import plonemeeting.communes


class MCLayer(PMLayer):
    """ """


MC_ZCML = zca.ZCMLSandbox(filename="testing.zcml",
                          package=plonemeeting.communes,
                          name='MC_ZCML')

MC_Z2 = z2.IntegrationTesting(bases=(z2.STARTUP, MC_ZCML),
                              name='MC_Z2')

MC_TESTING_PROFILE = MCLayer(
    zcml_filename="testing.zcml",
    zcml_package=plonemeeting.communes,
    additional_z2_products=('imio.dashboard',
                            'plonemeeting.communes',
                            'plonemeeting.core',
                            'Products.CMFPlacefulWorkflow',
                            'Products.PasswordStrength'),
    gs_profile_id='plonemeeting.communes:testing',
    name="MC_TESTING_PROFILE")

MC_TESTING_PROFILE_FUNCTIONAL = FunctionalTesting(
    bases=(MC_TESTING_PROFILE,), name="MC_TESTING_PROFILE_FUNCTIONAL")

MC_DEMO_TESTING_PROFILE = MCLayer(
    zcml_filename="testing.zcml",
    zcml_package=plonemeeting.communes,
    additional_z2_products=('imio.dashboard',
                            'plonemeeting.communes',
                            'plonemeeting.core',
                            'Products.CMFPlacefulWorkflow',
                            'Products.PasswordStrength'),
    gs_profile_id='plonemeeting.communes:demo',
    name="MC_TESTING_PROFILE")

MC_TESTING_ROBOT = FunctionalTesting(
    bases=(
        MC_DEMO_TESTING_PROFILE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="MC_TESTING_ROBOT",
)
