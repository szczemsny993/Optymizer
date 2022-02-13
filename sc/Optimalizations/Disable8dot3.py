#class to manage ntfsdisable8dot3namecreation for windows 10
import subprocess

class Disable8dot3:
    def __init__(self):
        """        
        0 - enable 8dot3 name creation on all volumes
        1 - disable 8dot3 name creation on all volumes
        2 - per volume setting - the default
        3 - disable 8dot 3 name creation on all volumes
        except the system volume"""

    def disable(self):
        """Disabling ntfsdisable8dot3namecreation."""
        result = subprocess.run(['fsutil.exe', 'behavior',
         'set', 'Disable8dot3', '1'], capture_output=True)

    def enable(self):
        """Enabling ntfsdisable8dot3namecreation
        Return true if operation success"""
        result = subprocess.run(['fsutil.exe', 'behavior',
         'set', 'Disable8do3', 0], capture_output=True)

    def getStatus(self):
        """function to get status of disable8dot3 service
        1 mean the service is stopped
        anything else means service is running"""
        result = subprocess.run(['fsutil.exe', 'behavior', 'query',
         'disable8dot3'], capture_output=True)
        outputData = result.stdout.decode()

        if '0' or '2' or '3' in outputData:
            return True
        elif '1' in outputData:
            return False
        else:
            return None

# #simple debbuging
# test = Disable8dot3()
# test.disable()