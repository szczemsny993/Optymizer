#class to manage prefetch function in windows 10
#possible value of prefetch in reg:
#0 - completly disable
#1 - enable for application launch only
#2 - enable for boot only
#3 - optimal setting
# from AbstractRegOperation import AbstractRegOperation

import winreg

class Prefetch():
    def __init__(self):
        self.path = winreg.HKEY_LOCAL_MACHINE
        self.k = 'EnablePrefetcher'
        self.regpath = r'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters'

    def getStatus(self):
        """Returning a current value of prefetch in 
        windows registry"""
        try:
            key = winreg.OpenKeyEx(self.path, self.regpath)
            value = winreg.QueryValueEx(key, self.k)[0]
            # print(winreg.QueryValueEx(key, self.k))
            if key:
                winreg.CloseKey(key)
                return value
        except Exception as e:
            print(e)
        return None

    def enable(self):
        """Enabling prefetch in windows registry"""
        try:
            key = winreg.OpenKey(self.path, self.regpath, 0,
            winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, self.k, 1,
            winreg.REG_DWORD, 3)
        except Exception as e:
            print(e)
        return True

    def disable(self):
        """Disabling prefetch in windows registry"""
        try:
            key = winreg.OpenKey(self.path, self.regpath,
             0, winreg.KEY_SET_VALUE)
            # print(winreg.QueryInfoKey(key))
            winreg.SetValueEx(key, self.k, 1,
             winreg.REG_DWORD, 0)
        except Exception as e:
            print(e)
        return True

#simple debbuging
prefetch = Prefetch()
prefetch.disable()
# print(prefetch.getStatus())