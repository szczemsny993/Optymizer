import time

import colorama
from colorama import Fore

from Optimalizations.Disable8dot3 import Disable8dot3
from Optimalizations.Disablelastaccess import DisableLastAccess
from Optimalizations.Indexing import Indexing
from Optimalizations.Prefetch import Prefetch
from Optimalizations.Superprefetch import SuperPrefetcher

colorama.init(autoreset=True)

class SSDMode():
    def __init__(self):
        pass

    def execute(self):
        """function which performs all optimalization for ssd drive"""

        #disable 'disable8dot3 in fsutil
        self.__disable8dot3()
        time.sleep(2)

        #disable 'disablelastaccess in fsutil
        self.__disableLastAccess()
        time.sleep(2)

        #disable indexing service
        self.__disableIndexing()
        time.sleep(2)

        #disable prefetch function in regedit
        self.__disablePrefetch()
        time.sleep(2)

        #disable superprefetch service
        self.__disableSuperPrefetch()
        time.sleep(2)

    def undoChanges(self):
        pass

    def verify(self):
        """func to verify state of services etc"""
        dot8 = Disable8dot3()
        print('Usluga Disable8dot3: '
            + self.__disable8dot3Status(dot8.getStatus()))
        
        lastAccess = DisableLastAccess()
        print('Usluga DisableLastAccess: ' 
        + self.__disableLastAccessStatus(lastAccess.getStatus()))

        indexing = Indexing()
        print("Usluga indeksowania: "
         + self.__indexingStatus(indexing.getServiceStatus()))

        prefetch = Prefetch()
        print("Funkcja Prefetch: " + 
        self.__prefetchStatus(prefetch.getStatus()))

        superprefetch = SuperPrefetcher()
        print("Usluga SuperPrefetch: " + 
        self.__superPrefetchStatus(superprefetch.getServiceStatus()))

    def __disable8dot3(self):
        """disable fsutil disable8dot3"""
        dot3 = Disable8dot3()
        dot3.disable()

    def __disable8dot3Status(self, status):
        """return 'DISABLE' if status == True
        'ENABLE' if anything else"""
        if status == True:
            return f"{Fore.GREEN}DISABLE"
        else:
            return f"{Fore.RED}ENABLED"

    def __disableLastAccess(self):
        """disable fsutil disablelastaccess"""
        lastaccess = DisableLastAccess()
        lastaccess.disable()

    def __disableLastAccessStatus(self, status):
        """return 'DISABLE' if status == False
        return 'ENABLE' if status == True"""
        if status == True:
            return f"{Fore.RED}DISABLE"
        else:
            return f"{Fore.GREEN}ENABLED"

    def __disableIndexing(self):
        """disable indexing service"""
        indexing = Indexing()
        indexing.disable()

    def __indexingStatus(self, status):
        """return 'DISABLE' if status == 0
        return ENABLE if status == 1"""
        if status == 0:
            return f"{Fore.GREEN}DISABLE"
        elif status == 1:
            return f"{Fore.RED}ENABLED"
        else:
            return

    def __disablePrefetch(self):
        """disable prefetch windows func"""
        prefetch = Prefetch()
        prefetch.disable()

    def __prefetchStatus(self, status):
        """return DISABLE if status == 0
        return ENABLE if status > 0"""
        if status == 0:
            return f"{Fore.GREEN}DISABLE"
        elif status > 0:
            return f"{Fore.RED}ENABLED"


    def __disableSuperPrefetch(self):
        """disable superprefetch service"""
        superprefetch = SuperPrefetcher()
        superprefetch.disable()

    def __superPrefetchStatus(self, status):
        """return DISABLED if status == 0
        return ENABLED if status != 0"""
        if status == 0:
            return f"{Fore.GREEN}DISABLED"
        else:
            return f"{Fore.RED}ENABLED"
