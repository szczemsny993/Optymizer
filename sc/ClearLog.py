# command to clear all log in powershell: 
# wevtutil el | Foreach-Object {wevtutil cl "$_"}
# Get-EventLog -LogName * | ForEach { Clear-EventLog $_.Log}
from PSOperation.PSTime import PSTime

import subprocess

class ClearLog:
    def __init__(self):
        pass

    def clear(self):
        """func to clear using data in windows"""
        #clear ps history
        subprocess.run(['powershell.exe', 
        'Clear-History'], capture_output=True)

        #clear windows logs
        subprocess.run(['powershell.exe',
        'Get-EventLog -LogName * | ForEach { Clear-EventLog $_.Log }']
            ,capture_output=True)

    def checkEventLog(self):
        """func check how """
        result = subprocess.run(['powershell.exe',
            (f"Get-EventLog System -Before "
            f"'{PSTime.getCurrentTimeForPowerShell()}'")],
             capture_output=True)
        output = result.stdout.decode('ISO-8859-1')

        if 'wyczyszczony' in output:
            return True
        else:
            return False

# test = ClearLog()
# test.clear()
# time.sleep(2)
# print(test.checkEventLog())