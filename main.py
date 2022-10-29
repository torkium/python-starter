from utils.View import View
from utils.Message import Message
from AppContext import AppContext

AppContext.init()
if AppContext.config["debug"]:
    View.print(Message.info("Debug Mode"))

View.print(Message.info("End"))
input(Message.ask("Push key to exit..."))