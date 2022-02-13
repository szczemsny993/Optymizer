#turn off command: sc.exe stop "sysmain" && 
# sc.exe config "sysmain" start=disabled

#turn on command: sc.exe config "sysmain" start=deployed-auto
#sc.exe start "sysmain"

import subprocess

class SuperPrefetcher:
    def __init__(self):
        self.SERVICE_RUNNING = 1
        self.SERVICE_STOPPED = 0

    def enable(self):
        """turn on sysmain service"""
        result = subprocess.run(
            'sc.exe config "sysmain" start=auto',
         capture_output=True)
        result = subprocess.run(
            'sc.exe start "sysmain"'
        , capture_output=True)
        # print(result.stdout.decode('ISO-8859-1'))

    def disable(self):
        """turn off sysmain service"""
        result = subprocess.run(
            'sc.exe stop "sysmain"',
         capture_output=True)
        result = subprocess.run(
            'sc.exe config "sysmain" start=disabled',
             capture_output=True)        

    def getServiceStatus(self):
        """get start of sysmain service"""
        result = subprocess.run('sc.exe query "sysmain"'
        , capture_output=True).stdout.decode('ISO-8859-1')
        # print(result)
        if 'RUNNING' in result or 'START_PENDING' in result:
            return self.SERVICE_RUNNING
        elif 'STOPPED' in result:
            return self.SERVICE_STOPPED
        else:
            return None

# test = SuperPrefetcher()
# # test.enable()
# # test.enable()
# print(test.getServiceStatus())
