import colorama
from colorama import Fore

from AppDeinstaller.PSAppRemover import PSAppRemover

class HddMode():
    # ps apps to remove from windows
    psApps = [
        'Microsoft.549981C3F5F10' #cortana
        'Microsoft.BingWeather',
        'Microsoft.GetHelp',
        'Microsoft.Getstarted',
        'Microsoft.Microsoft3DViewer',
        'Microsoft.MicrosoftEdge.Stable',
        'Microsoft.MicrosoftOfficeHub',
        'Microsoft.MicrosoftSolitairecollection',
        'Microsoft.MixedReality.Portal',
        'Microsoft.MsPaint',
        'Microsoft.Office.onenote',
        'Microsoft.People',
        'Microsoft.Screensketch',
        'Microsoft.Storepurchaseapp',
        'Microsoft.Wallet',
        'Microsoft.WebMediaExtensions',
        'Microsoft.WebpImageExtension',
        'Microsoft.WindowsAlarms',
        'Microsoft.WindowsFeedbackHub',
        'Microsoft.WindowsMaps',
        'Microsoft.YourPhone', 
        'Microsoft.ZuneMusic',
        'Microsoft.ZuneVideo',
        'Microsoft.Windows.Photos',
        'Microsoft.DesktopAppInstaller',
        'Microsoft.WindowsCommunicationsApps'
    ]

    def __init__(self):
        pass

    def psAppRemove(self):
        """deleting windows default apps via powershell"""
        for x in self.psApps:
            remover = PSAppRemover(x)
            remover.uninstall()

    def psVerify(self):
        """function to verify app status"""
        for x in self.psApps:
            remover = PSAppRemover(x)
            status = remover.getAppStatus()
            if status == 0:
                print(f"App %s is {Fore.RED}installed" % x)
            elif status == 1:
                print(f"App %s is {Fore.GREEN}uninstalled" % x)
            else:
                print("Unknown error")