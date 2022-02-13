import os

class ScanFolder():
    finalList = []

    def __init__(self):
        self.__getCurrentWorkDir()
        self.__substractPaths('instalki')
        self.__setListOfFullPaths()

    def __getCurrentWorkDir(self):
        """pobiera bierzący folder roboczy"""
        self.currentPath = os.getcwd()

    def __substractPaths(self, folderName):
        """dodaje do ścieżki podany podfolder"""
        self.finalPath = self.currentPath + '\\sc\\' + folderName

    def __makeFullPath(self, fileName):
        """tworzy pełną ścieżkę do pliku"""
        return self.finalPath + '\\' + fileName

    def __setListOfFullPaths(self):
        """wypełnia liste pełnymi ścieżkami do plików"""
        lists = self.__getFileList()
        for x in lists:
            self.finalList.append(self.__makeFullPath(x))

    def __getFileList(self):
        """pobiera nazwy plików instalacyjnych z folderu"""
        return os.listdir(self.finalPath)

    def getListsOfFullPaths(self):
        """zwraca pełną listę plików"""
        return self.finalList