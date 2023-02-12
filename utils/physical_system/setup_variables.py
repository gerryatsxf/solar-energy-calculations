import numpy as np
import utils.physical_system.setup_geometric_variables as setup_geometric_variables
import utils.physical_system.setup_irradiance_variables as setup_irradiance_variables

def reorder_physical_system_columns(nrel_df):
    cols = [
        'YEAR','MONTH','DAY','HOUR','MINUTE','MINS_SINCE_EQUINOX',
        'TEMPERATURE',
        'DNI','DHI','GHI','GI','X_DIF','X_DIR',
        'Z','D','H','A','ALPHA'
    ]
    return nrel_df[cols]

def setup_physical_system(nrel_df, L):
    nrel_df = setup_geometric_variables.main(nrel_df, L)
    nrel_df = setup_irradiance_variables.main(nrel_df)
    nrel_df = reorder_physical_system_columns(nrel_df)
    return nrel_df

def main(nrel_df, L):
    return np.round(setup_physical_system(nrel_df, L),2)