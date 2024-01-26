# coding=utf-8
import os
import configparser

current_dir = os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.abspath(os.path.join(current_dir, os.pardir)) + '\\config.ini'

class ReadConfig(object):
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)

    def get_cookie(self):
        return self.cf.get("COOKIES", "cookie")

    def get_model_version(self):
        return self.cf.get("LLM", "version")

    def get_model_api_key(self):
        return self.cf.get("LLM", "api_key")