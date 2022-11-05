import os, sys, threading, yaml
from threading import Lock
from typing import Dict
from yaml.loader import SafeLoader
from utils.Log import Log

class AppContext:
    config:Dict
    output_lock:Lock = threading.Lock()

    def get_application_path():
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        return os.path.dirname(os.path.abspath(__file__))

    def init() -> bool:
        # Get Config Infos
        try:
            with open(AppContext.get_application_path() + "\\config.yaml") as f:
                AppContext.config = yaml.load(f, Loader=SafeLoader)
                if "debug" not in AppContext.config:
                    AppContext.config["debug"] = False
        except:
            AppContext.config = {
                "debug":False
            }
        Log.init(AppContext.get_application_path() + "\\logs\\")
        Log.insert("Config Getted")