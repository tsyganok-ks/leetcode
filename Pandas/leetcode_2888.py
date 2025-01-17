import pandas as pd

def concatenateTables(df1, df2):
    """
    Concatenate 2 DF
    :param df1: pandas DF
    :param df2: pandas DF
    :return: concatenated DF
    """
    #return df1.merge(df2)
    return pd.concat([df1, df2], ignore_index=True)


if __name__ == '__main__':
    df1 = pd.DataFrame(data=[[1, 'A'], [2, 'B']], columns=["col1", 'col2'])
    df2 = pd.DataFrame(data=[[3, 'C'], [4, 'D'], [5, 'E']], columns=["col1", 'col2'])
    print(concatenateTables(df1, df2))