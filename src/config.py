import os


class Config(object):
    SERVER_KEY = os.urandom(24)
