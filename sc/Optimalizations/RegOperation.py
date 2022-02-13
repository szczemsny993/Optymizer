import winreg
from abc import ABC, abstractmethod

class AbstractRegOperation(ABC):
    def __init__(self, path, key, regpath):
        self.path = path
        self.key = key
        self.regpath = regpath
    
    @abstractmethod
    def getStatus(self) -> bool:
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

class RegOperation:
    def __init__(self, path, key, regpath):
        self.path = path
        self.k = key
        self.regpath = regpath

    def getStatus(self) -> int:
        """return a current value of given key"""
        try:
            key = winreg.OpenKeyEx(self.path, self.regpath)
            value = winreg.QueryValueEx(key, self.k)[0]

            if key:
                winreg.CloseKey(key)
                return value
        except Exception as e:
            print(e)

        return None

    def disable(self, value) -> bool:
        """turn off feature via reg and given value"""
        try:
            key = winreg.OpenKey(self.path, self.regpath,
            0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, self.k, 1, winreg.REG_DWORD, value)
        except Exception as e:
            print(e)

    def enable(self, value) -> bool:
        pass