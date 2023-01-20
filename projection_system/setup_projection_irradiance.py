import numpy as np
import projection_system.irradiance_projection_dot_product as dot_product

def set_projected_irradiance(nrel_df):
    A = np.deg2rad(nrel_df['A'])
    B = np.deg2rad(nrel_df['B'])
    ALPHA = np.deg2rad(nrel_df['ALPHA'])
    BETA = np.deg2rad(nrel_df['BETA'])
    nrel_df['I_PROJ'] = nrel_df['GI']*(nrel_df['X_DIR']*dot_product.main(ALPHA,BETA,A,B)  +nrel_df['X_DIF'])
    nrel_df.loc[nrel_df['ALPHA']==0,['I_PROJ']] = 0
    return nrel_df

def main(nrel_df):
    return set_projected_irradiance(nrel_df)