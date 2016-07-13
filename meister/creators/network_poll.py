# -*- coding: utf-8 -*-

import meister.creators
from farnsworth.models import NetworkPollJob
from farnsworth.models import RawRoundTraffic

LOG = meister.creators.LOG.getChild('networkpoll')


class NetworkPollCreator(meister.creators.BaseCreator):
    @property
    def jobs(self):
        # get only unprocessed traffic files and schedule them.
        for curr_round_traffic in RawRoundTraffic.select().where(RawRoundTraffic.processed == False):
            job, _ = NetworkPollJob.get_or_create(limit_cpu=1, limit_memory=2, payload={'rrt_id': curr_round_traffic.id})
            job.priority = 50
            LOG.debug("Creating NetworkPollJob for %s ", curr_round_traffic.id)
            yield job