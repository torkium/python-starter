import logging
from colorama import Fore
from utils.Log import Log

class Message:
    def info(message):
        message = f'{Fore.LIGHTBLUE_EX} {message}{Fore.RESET}'
        Log.insert(message, logging.INFO)
        return message

    def ask(message):
        return f'[{Fore.LIGHTBLUE_EX}>{Fore.RESET}] {message} > '

    def success(message):
        message = f'[{Fore.GREEN}v{Fore.RESET}] {Fore.LIGHTGREEN_EX}{message}{Fore.RESET}'
        Log.insert(message, logging.INFO)
        return message

    def error(message):
        message = f'[{Fore.RED}!{Fore.RESET}] {Fore.LIGHTRED_EX}{message}{Fore.RESET}'
        Log.insert(message, logging.ERROR)
        return message