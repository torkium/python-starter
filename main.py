from utils.View import View
from utils.Message import Message
from AppContext import AppContext
import traceback

try:
    AppContext.init()
    if AppContext.config["debug"]:
        View.print(Message.info("Debug Mode"))

    View.print(Message.info("End"))
except Exception as err:
    print("Exception occured: {}".format(err))
    print(traceback.format_exc())
input("Push key to exit...")