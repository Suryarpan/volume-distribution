import numpy as np
import scipy.integrate as si
import scipy.stats as st


class compData:

    def __init__(self, concData, timeData, doseData) -> None:
        self.concData = np.array(concData)
        self.timeData = np.array(timeData)
        self.doseData = np.array(doseData)
        self.areaConcByTimeVal = self.areaConcByTime()

    def logConc(self) -> np.ndarray:
        return np.log(self.concData)

    def concMulTime(self) -> np.ndarray:
        return self.concData * self.timeData

    def elimConst(self) -> np.float64:
        res = st.linregress(self.timeData, self.logConc())
        return res.slope

    def areaConcByTime(self) -> np.float64:
        self.areaConcByTimeVal = si.trapezoid(self.concData, self.timeData)
        return self.areaConcByTimeVal

    def areaConcTimeByTime(self) -> np.float64:
        return si.trapezoid(self.concMulTime(), self.timeData)

    def meanRsdncTime(self) -> np.float64:
        return self.areaConcTimeByTime() / self.areaConcByTimeVal

    def arealVolDist(self) -> np.float64:
        return self.doseData[0] / (self.elimConst() * self.areaConcByTimeVal)

    def sdStVolDist(self) -> np.float64:
        return (self.doseData[0] / self.areaConcByTimeVal)*self.meanRsdncTime()
