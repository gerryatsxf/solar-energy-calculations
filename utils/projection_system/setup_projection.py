import utils.projection_system.setup_projection_irradiance as setup_projection_irradiance
import utils.projection_system.setup_projection_plane as setup_projection_plane
import utils.projection_system.setup_optimized_projection_irradiance as setup_optimized_projection_irradiance
import utils.projection_system.setup_optimized_projection_plane as setup_optimized_projection_plane
import numpy as np

def main(nrel_df,B,BETA,optimized=False):
    nrel_df = setup_projection_plane.main(nrel_df,B,BETA)
    nrel_df = setup_projection_irradiance.main(nrel_df)
    if optimized:
        nrel_df = setup_optimized_projection_plane.main(nrel_df)
        nrel_df = setup_optimized_projection_irradiance.main(nrel_df)
    return np.round(nrel_df,2)