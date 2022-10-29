import logging
import os
import threading
from threading import Lock
import traceback
from typing import Dict
import yaml
from yaml.loader import SafeLoader
from utils.Log import Log

class AppContext:
    config:Dict
    output_lock:Lock = threading.Lock()

    def init() -> bool:
        try:
            # Get Config Infos
            try:
                with open(os.path.realpath(os.path.dirname(__file__)) + "\\config.yaml") as f:
                    AppContext.config = yaml.load(f, Loader=SafeLoader)
                    if "debug" not in AppContext.config:
                        AppContext.config["debug"] = False
            except:
                Log.insert("config.yaml not found.", logging.DEBUG)
                AppContext.config = {
                    "debug":False
                }
            Log.init(os.path.realpath(os.path.dirname(__file__)) + "\\logs\\")
            Log.insert("Config Getted")
        except Exception as err:
            Log.insert(
                "Une erreur est survenue: {}".format(err),
                logging.ERROR,
            )
            Log.insert(
                traceback.format_exc(),
                logging.ERROR,
            )