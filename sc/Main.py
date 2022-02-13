import argparse
from difflib import restore
import time

import colorama
from colorama import Fore

from Programs import Programs
from HddMode import HddMode
from SsdMode import SSDMode
from ClearLog import ClearLog
from RestorePoint import RestorePoint
from Welcome import Welcome

colorama.init(autoreset=True)

class Main():
    verify = False
    driveType = ''
    programs = ''

    def __init__(self):
        self.parseArgs()
        
        Welcome()
        self.execute()

    def execute(self):
        """execute operations like a veryfy and 
        operation for choosed drive type"""

        #verify only mode
        if self.verify == True:
            self.verifyMode()
            return

        #choose type of operation for hard drive
        match self.driveType:
            case 'SSD':
                self.ssdOperations()
            case 'SSHD':
                self.hddOperations()
            case 'HDD':
                self.hddOperations()

        #install programs in directory
        if self.programs == 1:
            programs = Programs()
            programs.install()

        #set checkpoint   
        self.restorePoint()

        #clearing logs
        self.deleteSystemLogs()

    def deleteSystemLogs(self):
        """Function deleting whole logs in system windows"""

        systemLogs = ClearLog()
        systemLogs.clear()

        time.sleep(3)

        if systemLogs.checkEventLog() == True:
            print(f"{Fore.GREEN}Wszystkie logi zostaly wyczyszczone")
        else:
            print(f"{Fore.RED}Logi nie zostaly wyczyszczone")

    def parseArgs(self):
        """Function to parse input arguments for script"""
        parser = argparse.ArgumentParser(description=
        """Program do automatycznej konfiguracji i optymalizacji 
        windows 10""")
        parser.add_argument('-v',
         '--verifyonly', dest='verifyonly',
         action='store_true', help='Parametr sluzacy do weryfikacji')
        parser.add_argument('-d',
         '--drive', type=str,
          help="""Przelacznik do okreslenia dla jakiego 
          typu dysku ma byc zastosowana optymalizacja""")
        parser.add_argument('-p', '--programs',
         type=str, help="""Okresla czy uruchamiac tryb instalacji 
         programow zawartch w folderze""")
        args = parser.parse_args()

        #args turn script into verifyonly mode
        if(args.verifyonly):
            self.verify = True
            return 0
        else:
            self.verify = False

        self.driveType = self.checkDiskType(args.drive)
        if(self.driveType is None):
            return 1
        
        self.programs = args.programs
        if self.programs == '1':
            self.programs = 1
        elif self.programs == '0':
            self.programs = 0
        else:
            self.programs = -1


    def checkDiskType(self, drive):
        """Validate hard drive value from argparse"""
        if not (isinstance(drive, str)):
            return None

        driveType = drive.upper()

        if(driveType == 'HDD'):
            driveType = 'HDD'
        elif(driveType == 'SSD'):
            driveType = 'SSD'
        elif(driveType == 'SSHD'):
            driveType = 'SSHD'
        else:
            return None

        return driveType

    def ssdOperations(self):
        ssd = SSDMode()
        ssd.execute()

        hdd = HddMode()
        hdd.psAppRemove()

    def hddOperations(self):
        #powershell apps remove
        mode = HddMode()
        mode.psAppRemove()

    def programInstall(self):
        pass

    def verifyMode(self):
        # hddmode = HddMode()
        # hddmode.psVerify()

        ssdmode = SSDMode()
        ssdmode.verify()

        hdd = HddMode()
        hdd.psVerify()

    def restorePoint(self):
        """func to create operation on creating restore point"""
        restorePnt = RestorePoint()

        restorePnt.enableRestore()
        restorePnt.createRestorePoint()
        statement = restorePnt.checkRestorePoint()
        if statement == True:
            f"{Fore.GREEN}Utworzono punkt przywracania"
        else:
            f"{Fore.RED}Punkt przywracania nie zostal utworzony"

if __name__ == '__main__':
    main = Main()


