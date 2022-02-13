#first step: turn on Computer Restore
#ps: Enable-ComputerRestore -Drive "C:"
#second step: create restore point
#optional (powershell.exe -ExecutionPolicy Bypass -NoExit -Command)
#Checkpoint-Computer -Description "Ks RestorePoint $today"
#  -RestorePointType "MODIFY_SETTINGS"
#third step: check 
#command ps: Get-ComputerRestorePoint
import subprocess

from PSOperation.PSTime import PSTime

class RestorePoint:
    def __init__(self):
        pass

    def enableRestore(self):
        """enable restore points"""
        subprocess.run('powershell.exe', 
        'Enable-ComputerRestore =Drive, "C:"', capture_output=True)

    def createRestorePoint(self) -> bool:
        """create restore point with date od creation in name
        func return True if success, anything else return False"""
        operationResult = subprocess.run(['powershell.exe', 
        self.conCreateRestorePoint()], capture_output=True).stdout.decode()

        if 'WARNING' in operationResult:
            return False
        elif len(operationResult) > 2:
            return False
        else:
            return True

    def conCreateRestorePoint(self):
        """creating restore point command to run in powershell"""
        command = ('CheckPoint-Computer -Description '
        '"KS RestorePoint ' + PSTime.getCurrentDateForPowershell() + '"'
        ' -RestorePointType "MODIFY_SETTINGS"'
        )

        return command

    def checkRestorePoint(self):
        """check restore point"""
        output = subprocess.run(['powershell.exe', 
        'Get-ComputerRestorePoint'], capture_output=True).stdout.decode()

        if PSTime.getCurrentDateForPowershell() in output:
            return True
        else:
            return False

# test = RestorePoint()
# # print(test.conCreateRestorePoint())
# # test.createRestorePoint()
# print(test.checkRestorePoint())