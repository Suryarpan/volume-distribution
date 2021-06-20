from reader import dataReader
from findDistribution import findDistribution
from comparison import comparison
import matplotlib.pyplot as plt
from scipy import stats


def plotConcTime(rData):
    """Plots the concentration vs time curve

    :param rData: Data read by the reader
    :type rData: compData.compData
    """
    plt.plot(rData.timeData, rData.concData, 'o')
    plt.title('Concentration Vs Time')
    plt.xlabel('Time (hr)')
    plt.ylabel('Concentration (ng/mL)')
    plt.savefig('ConcVsTime.svg')
    plt.close()


def plotLogConcTime(rData):
    """Plots the concentration times time vs time curve

    :param rData: Data read by the reader
    :type rData: compData.compData
    """
    # Calculating log of concentration data
    logConc = rData.logConc()
    res = stats.linregress(rData.timeData, logConc)
    # Plotting the values and fitted curve
    plt.plot(rData.timeData, logConc, 'o', label='Original Data')
    plt.plot(rData.timeData, (res.intercept + (res.slope * rData.timeData)),
             'r', label='Fitted Line')
    plt.title('log(Concentration) Vs Time')
    plt.xlabel('Time')
    plt.ylabel('log(Conc)')
    plt.text(17.5, 4, f'Slope = {round(res.slope, 5)}')
    plt.legend()
    plt.savefig('logConcVsTime.svg')
    plt.close()


def makeOutput(drugData, knwnMediData):
    """Making the final output

    :param drugData: The dataset containing the concentration vs time information
    :type drugData: str
    :param knwnMediData: The dataset containing names and distribution data of known drugs
    :type knwnMediData: str
    """
    rData = dataReader(drugData)
    (elim_const, AreaVol, StdyStVol) = findDistribution(rData)

    with open("output.txt", "w") as outFile:
        print(f"Computation Result Log:\n----------------------\n", file=outFile)
        print(
            f"Elimination Constant for provided drug: {elim_const}", file=outFile)
        print(
            f"Areal Volume Distribution (V_area) for provided drug: {AreaVol}", file=outFile)
        print(
            f"Steady State Volume Distribution (V_ss) for provided drug: {StdyStVol}", file=outFile)

    plotConcTime(rData)
    plotLogConcTime(rData)

    comparison(knwnMediData, StdyStVol)


if __name__ == '__main__':
    FileName1 = '~/internship/RAWAL_LAB/volume-distribution/dataset1.csv'
    FileName2 = '~/internship/RAWAL_LAB/volume-distribution/dataset2.csv'

    makeOutput(FileName1, FileName2)
