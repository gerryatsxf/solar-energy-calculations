import pandas as pd
import datetime 
import numpy as np
def set_energy_production(nrel_df):
    nrel_df['DATETIME'] = pd.to_datetime(nrel_df[['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE']])
    nrel_df = nrel_df.set_index('DATETIME').sort_index().reset_index()
    nrel_df['DATETIME_SHIFT'] = nrel_df['DATETIME'].shift(1)
    nrel_df['PROJ_TIME'] = (nrel_df['DATETIME'] - nrel_df['DATETIME_SHIFT'])/pd.Timedelta(seconds=60)
    nrel_df.loc[0,['PROJ_TIME']] = 0
    nrel_df['WH_SQM'] = nrel_df['I_PROJ']*nrel_df['PROJ_TIME']/60 # Wh per square meter
    return nrel_df.drop(columns=['DATETIME','DATETIME_SHIFT'])

def main(nrel_df):
    nrel_df = set_energy_production(nrel_df)
    return np.round(nrel_df,2)