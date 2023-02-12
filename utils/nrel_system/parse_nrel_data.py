import pandas as pd

def get_nrel_latitude(nrel):
    return nrel['nrel_csv']['headers']['LATITUDE']

def merge_nrel_list(nrel_list):
    df = pd.DataFrame({})
    L = 0
    if type(nrel_list) == list:
        if len(nrel_list) > 0:
            df = nrel_list[0]['nrel_csv']['data']
            L = get_nrel_latitude(nrel_list[0])
            if len(nrel_list) > 1:
                for nrel in nrel_list[1:]:
                    df = pd.concat([df, nrel['nrel_csv']['data']], axis=0)
    return df, L
    
def normalize_leap_year(df):
    index_leap = df[ (df['MONTH'] == 2) & (df['DAY'] == 29) ].index
    df.drop(index_leap , inplace=True)
    return df
    
def get_yearly_mean_nrel(nrel_df):
    return nrel_df.drop(columns='YEAR').groupby(['MONTH','DAY','HOUR','MINUTE'], as_index=False).mean()

def main(nrel_list):
    nrel, L = merge_nrel_list(nrel_list)
    #nrel = get_yearly_mean_nrel(nrel)
    nrel = normalize_leap_year(nrel)
    return nrel, L