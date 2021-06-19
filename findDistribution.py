import numpy as np
from scipy import stats
from scipy import integrate


def findDistribution(DoseData, ConcData, TimeData):
    """Finds the Volume of distribution

    :param DoseData: Dose administered
    :type DoseData: numpy.ndarray
    :param ConcData: Concentration of drug is plasma
    :type ConcData: numpy.ndarray
    :param TimeData: Time
    :type TimeData: numpy.ndarray
    :return: Areal volume distribution, Steady state volume distribution
    :rtype: float
    """
    # Manipulating Necessary Parameters
    dose = DoseData[0]
    lnConcData = np.log(ConcData)
    ConcTimeData = ConcData * TimeData
    res = stats.linregress(TimeData, lnConcData)
    k_el = res.slope
    areaConcTime = integrate.trapezoid(ConcData, TimeData)
    areaConcTimeTime = integrate.trapezoid(ConcTimeData, TimeData)
    meanResidenceTime = areaConcTimeTime/areaConcTime

    # Calculating Volume Distribution
    vArea = (dose)/(k_el * areaConcTime)
    vSs = ((dose)/(areaConcTime)) * meanResidenceTime

    return vArea, vSs, k_el
