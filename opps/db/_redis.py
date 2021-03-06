#!/usr/bin/env python
# -*- coding: utf-8 -*-
from opps.db.conf import settings

from redis import ConnectionPool
from redis import Redis as RedisClient


class Redis:
    def __init__(self, key_prefix, key_sufix):
        self.key_prefix = key_prefix
        self.key_sufix = key_sufix
        self.host = settings.OPPS_DB_HOST
        self.port = settings.OPPS_DB_PORT
        self.db = 0

        pool = ConnectionPool(host=self.host,
                              port=self.port,
                              db=self.db)
        self.conn = RedisClient(connection_pool=pool)

    def object(self):
        return self.conn

    def close(self):
        self.conn = None
        return True

    @property
    def key(self):
        return u'{}_{}_{}'.format(settings.OPPS_DB_NAME,
                                  self.key_prefix,
                                  self.key_sufix).lower()

    def save(self, document):
        return self.conn.set(self.key, document)

    def publish(self, document):
        return self.conn.publish(self.key, document)

    def get(self):
        return self.conn.get(self.key)
