import pandas as pd

def comparison(FileName, VolumeDistribution):
    """Produces a sorted .xlsx file, where one can compare the volume distribution of sample with some known drugs

    :param FileName: Name/Path of dataset containg name and volume distribution data of known drugs
    :type FileName: str
    :param VolumeDistribution: volume distribution of the sample
    :type VolumeDistribution: float
    """

    df1 = pd.DataFrame({'Name': ['Sample'],
                        'V': [VolumeDistribution]})
    df2 = pd.read_csv('FileName')

    df2 = df2.append(df1, ignore_index=True)
    sorted_df = df2.sort_values(by=['V'], ascending=True)

    sorted_df.to_excel('Comparison_Dataset.xlsx')
