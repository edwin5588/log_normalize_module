import pandas as pd


def read_gct(GCT_file, summary = False):
    """
    Reads a GCT data file and outputs a Pandas dataframe.

    GCT_file(string) --> filepath to GCT dataset
    summary(boolean) --> if true, print rows and columns of GCT file

    returns a Pandas dataframe

    """
    data = pd.read_csv(GCT_file, delimiter = "\t")
    if summary = True:
        print("Data has: %d rows and %d columns")%(len(data), len(data.loc[0]))
    return data


def log_normalize(df):
    """
    Takes in a dataframe and log_normalizes the data
    """

    
