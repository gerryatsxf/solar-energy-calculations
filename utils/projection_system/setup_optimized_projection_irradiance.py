import numpy as np
import utils.projection_system.irradiance_projection_dot_product as dot_product

def set_optimized_projected_irradiance(nrel_df):
    A = np.deg2rad(nrel_df['A'])
    B = np.deg2rad(nrel_df['B_OPT'])
    ALPHA = np.deg2rad(nrel_df['ALPHA'])
    BETA_OPT = np.deg2rad(nrel_df['BETA_OPT'])
    nrel_df['I_PROJ_OPT'] = nrel_df['GI']*(nrel_df['X_DIR']*dot_product.main(ALPHA,BETA_OPT,A,B)+nrel_df['X_DIF'])
    return nrel_df

def main(nrel_df):
    return set_optimized_projected_irradiance(nrel_df)