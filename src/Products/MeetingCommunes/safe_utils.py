# -*- coding: utf-8 -*-

from Products.MeetingCommunes.utils import get_finance_advice_esign_signatories
# make available on PM.safe_utils
from Products.PloneMeeting import safe_utils
safe_utils.get_finance_advice_esign_signatories = get_finance_advice_esign_signatories
