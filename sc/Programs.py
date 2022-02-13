import os
from ScanFolder import ScanFolder

class Programs():
    appList = []

    def __init__(self):
        scanFolder = ScanFolder()
        self.appList = scanFolder.getListsOfFullPaths()

    def install(self):
        """Install apps from directory"""
        for x in self.appList:
            result = os.system()

# """Do przetestowania ranu"""
# test = Programs()
# print(test.appList)
# for x in test.appList:
#     os.system(x)