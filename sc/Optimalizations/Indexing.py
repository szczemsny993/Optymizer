import subprocess
import os

class Indexing:
    def __init__(self):
        #variables like enum values
        self.SERVICE_RUNNING = 1
        self.SERVICE_STOPPED = 0

    def disable(self):
        """func disable indexing in windows 10"""
        result = subprocess.run('sc.exe stop "wsearch"',
         capture_output=True)
        result = subprocess.run(
            'sc.exe config "wsearch" start=disabled', 
            capture_output=True)

    def enable(self):
        """enable func indexing in windows 10"""
        result = subprocess.run('sc.exe config "wsearch" start=auto',
        capture_output=True)
        result = subprocess.run('sc.exe start "wsearch"',
         capture_output=True)
        print(result.stdout.decode())

    def getServiceStatus(self):
        """get current status of service indexing"""
        result = subprocess.run(['sc', 'query',
         'wsearch'], capture_output=True).stdout.decode()
        outputData = str(result)
        if 'STOPPED' in outputData:
            return self.SERVICE_STOPPED
        elif 'RUNNING' or 'START_PENDING' in outputData:
            return self.SERVICE_RUNNING
        else:
            return 0

# text = Indexing()
# text.disable()
# print(text.getServiceStatus())