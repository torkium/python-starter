import easygui

class View:
    def print(message):
        print(message)

    def askFile(default='*.txt', fileType=['*.txt'], title="Select file", multiple=False):
        return easygui.fileopenbox(default=default, filetypes=fileType, title=title, multiple=multiple)