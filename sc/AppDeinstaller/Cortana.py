# import subprocess
# import os

# class CortanaRemover:
#     def __init__(self):
#         self.APP_ALREADY_INSTALLED = 0
#         self.APP_REMOVED = 1

#     def uninstall(self):
#         """Removing cortana from apps"""
#         result = subprocess.run(['powershell.exe', 'Get-AppxPackage', '-allusers',
#                             'Microsoft.549981C3F5F10', '|' 'Remove-AppxPackage'], capture_output=True)
#         print(result.stdout.decode())

#     def install(self):
#         """Function can install cortana from manifest.xml, TO DO"""
#         result = os.system("""runas.exe /user:User "powershell.exe Get-AppxPackage -AllUsers Microsoft.549981C3F5F10 | 
#                         Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}" """)
#         print(result)

#     def getCortanaStatus(self):
#         result = subprocess.run(['powershell', 'Get-AppxPackage', '*Microsoft.549981C3F5F10*'], capture_output=True)
#         outputData = result.stdout.decode()
#         if 'Microsoft.549981C3F5F10' in outputData:
#             return self.APP_ALREADY_INSTALLED
#         if len(outputData) < 2:
#             return self.APP_REMOVED

# example = CortanaRemover()
# print(example.getCortanaStatus())