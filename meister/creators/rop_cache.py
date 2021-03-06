#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from farnsworth.models.job import RopCacheJob

import meister.creators
LOG = meister.creators.LOG.getChild('rop_cache')


class RopCacheCreator(meister.creators.BaseCreator):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

    @property
    def _jobs(self):
        LOG.debug("Collecting jobs...")
        for cs in self.single_cb_challenge_sets():
            job = RopCacheJob(cs=cs, request_cpu=1, request_memory=2048, limit_memory=8192)
            priority = 90  # A rop cache should probably always be created
            LOG.debug("Yielding RopCacheJob for %s", cs.name)
            yield (job, priority)
