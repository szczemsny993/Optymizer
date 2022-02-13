import subprocess

class PSAppRemover():
    APP_ALREADY_INSTALLED = 0
    APP_REMOVED = 1
    app = ''

    def __init__(self, app):
        self.app = app

    def uninstall(self):
        """uninstalling app via powershell subprocess system"""
        result = subprocess.run(['powershell.exe', 'Get-AppxPackage', 
        self.app, '|', 'Remove-AppxPackage'],
         capture_output=True)

    def getAppStatus(self):
        """Function to check app statis in windows 10.
        Function can return 3 values:
        0 if app is installed
        1 if app is removed
        None if raised exception"""
        try:
            result = subprocess.run(['powershell.exe',
             'Get-AppxPackage', '%s' % self.app], capture_output=True)
            outputData = result.stdout.decode()
        except subprocess.SubprocessError as e:
            print(e)

        if self.app.lower() in outputData.lower():
            return self.APP_ALREADY_INSTALLED
        elif len(outputData) < 2:
            return self.APP_REMOVED
        else:
            return None