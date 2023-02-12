import numpy as np

def set_optimized_inclination_angle(nrel_df):
    ALPHA = np.deg2rad(nrel_df['ALPHA'])
    A = np.deg2rad(nrel_df['A'])
    nrel_df['B_OPT'] = 0 # because optimized plane will always look south
    numerator = nrel_df['GI']*nrel_df['X_DIR']*np.cos(ALPHA)*np.cos(A-nrel_df['B_OPT'])
    denominator = nrel_df['GI']*nrel_df['X_DIR']*np.sin(ALPHA)
    nrel_df['BETA_OPT'] = np.rad2deg(np.nan_to_num(np.arctan(
        numerator / denominator
    )))
    return nrel_df

def main(nrel_df):
    nrel_df = set_optimized_inclination_angle(nrel_df)
    return nrel_df