from datetime import date, datetime

class PSTime:
    def __init__(self):
        pass

    @staticmethod
    def getCurrentTimeForPowerShell():
        now = datetime.now()
        psCurrentTime = (
        f"{now.day}/{now.month}/{now.year}"   
        f" {now.hour}:{now.minute}:{now.second}"
        )
        return psCurrentTime

    @staticmethod
    def getCurrentDateForPowershell():
        now = datetime.now()
        psCurrentDate = (
            f"{now.day}/{now.month}/{now.year}"
        )
        return psCurrentDate

# test = PSTime()
# print(test.getCurrentTimeForPowerShell())
# print(test.getCurrentDateForPowershell())