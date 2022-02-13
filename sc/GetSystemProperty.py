import os

class GetSystemProperty():
    userName = ''

    def __init__(self):
        self.getUserNameFromSystem()

    def getUserName(self):
        return self.userName

    def getUserNameFromSystem(self):
        self.userName = os.getlogin()