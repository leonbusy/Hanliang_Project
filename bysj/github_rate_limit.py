import logging
import os
import time

from datetime import datetime

from github import Github


logger = logging.getLogger(__name__)


def manage_sleep_time(requester):

    remaining, limit = requester.rate_limiting
    reset_time = requester.rate_limiting_resettime

    now = datetime.now().timestamp()
    sleep_period = reset_time - now

    while remaining < 5 and sleep_period > 0:
        logger.info(
            "Sleeping from [%s] for [%d]s until [%s].", str(datetime.fromtimestamp(now)), sleep_period,
            str(datetime.fromtimestamp(reset_time)))
        time.sleep(30)
        now = datetime.now().timestamp()
        sleep_period = reset_time - now


def apply_api_rate_limiting(github_instance):

    requester = getattr(github_instance, '_Github__requester')
    original__requestRaw = getattr(requester, '_Requester__requestRaw')

    def rate_limited__requestRaw(cnx, verb, url, requestHeaders, input):
        manage_sleep_time(requester)

        return original__requestRaw(cnx, verb, url, requestHeaders, input)

    setattr(requester, '_Requester__requestRaw', rate_limited__requestRaw)


def rate_limited_github_instance():
    github_instance = Github('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')
    apply_api_rate_limiting(github_instance)
    return github_instance
