#class to manage ntfsdisablelastaccessupdate for windows 10
import subprocess

class DisableLastAccess:

    def __init__(self):
        """
        0 - user managed, disabled
        1 - user managed, enabled
        2 - system managed, disabled
        3 - system managed, enabled
        """

    def disable(self):
        """disable ntfsdisablelastaccessupdate"""
        result = subprocess.run(['fsutil.exe', 'behavior',
        'set', 'disablelastaccess', '0'], capture_output=True)


    def enable(self):
        """enable ntfsdisablelastaccessupdate"""
        subprocess.run(['fsutil.exe', 'behavior',
        'set', 'disablelastaccess', '1'])

    def getStatus(self):
        """get status of ntfsdisablelastaccessupdate
        if 0 in status mean service is disable
        1 or 2 or 3 means service is enabled"""
        result = subprocess.run(['fsutil.exe', 'behavior', 
        'query', 'disablelastaccess'], capture_output=True)
        outputData = result.stdout.decode()

        if '0' or '2' or '3' in outputData:
            return False
        elif '1' in outputData:
            return True
        else:
            return None

#simple debbuging
# testfunc = DisableLastAccess()
# print(testfunc.enable())