from datetime import date
import yaml
import os
import re

PORTAL_CONFIG = os.path.join(os.path.dirname(__file__), '../configs/configs.yml')
CONFIG = yaml.load(file(PORTAL_CONFIG, 'r'))


class ConfigHelper(object):
    """Manage all configuration information for the application"""
    def __init__(self):
        self.halo_key = os.getenv("HALO_API_KEY")
        self.halo_secret = os.getenv("HALO_API_SECRET_KEY")
        self.match_list = CONFIG["target_events"]
        self.jira = CONFIG["jira"]
        self.start_timestamp = ConfigHelper.get_timestamp()
        self.ua_string = "CP-JIRA-Community-Tool"
        self.max_threads = 10
        self.halo_batch_size = 20

    @classmethod
    def get_timestamp(cls):
        env_time = os.getenv("HALO_EVENTS_START", "")
        if env_time == "":
            env_time = ConfigHelper.iso8601_today()
        return env_time

    @classmethod
    def iso8601_today(cls):
        today = date.today()
        retval = today.isoformat()
        return retval
