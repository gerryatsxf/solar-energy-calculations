import numpy as np

def set_inclination_angle(nrel_df, BETA):
    nrel_df['BETA'] = 0
    nrel_df.loc[nrel_df['ALPHA']>0,['BETA']] = BETA
    return nrel_df
    
def set_plane_orientation_angle(nrel_df,B):
    nrel_df['B'] = B
    return nrel_df

def main(nrel_df,B,BETA):
    nrel_df = set_plane_orientation_angle(nrel_df,B)
    nrel_df = set_inclination_angle(nrel_df, BETA)
    return np.round(nrel_df,2)