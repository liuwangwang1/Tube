# -*- coding:utf-8 -*-
from faker import Faker

class Singleton(object):
    _instance = None

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance
