import numpy as np

def set_irradiance_components(nrel_df):
    nrel_df['X_DIF'] = np.nan_to_num(nrel_df['DHI']/(nrel_df['DHI']+nrel_df['DNI']))
    nrel_df['X_DIR'] = np.nan_to_num(nrel_df['DNI']/(nrel_df['DHI']+nrel_df['DNI']))
    ALPHA = np.deg2rad(nrel_df['ALPHA'])
    A = np.deg2rad(nrel_df['A'])
    # GI -> Global Irradiance: basically the clearsky irradiance we get directly from the sun
    nrel_df['GI'] = np.nan_to_num(nrel_df['GHI']/(nrel_df['X_DIR']*np.sin(ALPHA)+nrel_df['X_DIF']))
    return nrel_df

def main(nrel_df):
    return set_irradiance_components(nrel_df)