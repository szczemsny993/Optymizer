# cmd: taskkill /f /im onedrive.exe
# cmd: %systemroot%\sysWOW64\OneDriveSetup.exe /uninstall
import subprocess

class OneDriveUninstaller:
    def __init__(self):
        pass

    def uninstall(self):
        """func to uninstall onedrive via powershell"""
        result = subprocess.run(['cmd.exe', 
        r'%systemroot%/sysWOW64/OneDriveSetup.exe',
        r'/uninstall'], capture_output=True)

    def taskKill(self):
        pass

test = OneDriveUninstaller()
test.uninstall()