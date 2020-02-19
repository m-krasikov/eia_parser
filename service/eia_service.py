import logging
from yaml import safe_load
from os import path

log = logging.getLogger('service')


class EiaParserService:
    def __init__(self, config_file=None):
        global log
        log = logging.getLogger('service')
        if config_file is None:
            config_file = path.dirname(path.dirname(path.abspath(__file__))) + '/config/config.yaml'
        with open(config_file) as general_config:
            config = safe_load(general_config)
        self.db_type = config["db"]
        self.db_name = config["db"]["db_name"]
        self.table_name = config["db"]["table_name"]

    def run(self):
        pass
