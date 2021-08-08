import json
import os
from .config_exception import IncorrectConfigFile


class Config:
    """Base configuration class

    Loads from JSON-file configuration by keywords.
    All specified fields are required.
    If default_file specified, then missing fields loading from it.
    """
    config_keywords = []

    def __init__(self, filename: str = '', **kwargs):
        """Constructor that loads configuration info from specific file

        Params:
        filename: name of configuration file to load

        Keyword arguments:
        default_file: name of default configuration file
        """
        default_file = kwargs.get('default_file')
        if default_file:
            default_info = self.__load_info(default_file)

        custom_info = self.__load_info(filename)
        for keyword in Config.config_keywords:
            info_value = custom_info.get(keyword)
            if info_value:
                setattr(self, keyword, info_value)
            else:
                if default_file:
                    default_info_value = default_info.get(keyword)
                    if default_info_value is not None:
                        setattr(self, keyword, default_info_value)
                    else:
                        raise IncorrectConfigFile(f'{keyword} not found in default configuration file')
                else:
                    raise IncorrectConfigFile(
                        f'Default configuration file is not initialized to set default value to \'{keyword}\'')

    def __load_info(self, filename: str):
        """Open and parse JSON-file to dict"""
        if os.path.exists(filename):
            config_file = open(filename)
            config_info = json.loads(config_file.read())
            config_file.close()
            return config_info
        else:
            return {}

    def __str__(self):
        return str(dict(map(lambda k: (k, getattr(self, k, None)), Config.config_keywords)))
