
import numpy as np
import pandas as pd
import datetime


def set_mins_since_equinox(nrel_df):
    years_available = list(set(nrel_df['YEAR']))
    nrel_df['DATETIME'] = pd.to_datetime(nrel_df[['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE']])
    nrel_df = nrel_df.set_index('DATETIME').sort_index().reset_index()
    nrel_df['MINS_SINCE_EQUINOX'] = 0
    for year in years_available:
        last_year_equinox = datetime.date(year-1, 12, 21)
        current_year_equinox = datetime.date(year, 12, 21)
        nrel_df.loc[(nrel_df['YEAR'] == year) & (nrel_df['DATETIME'] < pd.Timestamp(current_year_equinox)), ['MINS_SINCE_EQUINOX']] = (nrel_df['DATETIME'] - pd.Timestamp(last_year_equinox)) / pd.Timedelta(seconds=60)
        nrel_df.loc[(nrel_df['YEAR'] == year) & (nrel_df['DATETIME'] >= pd.Timestamp(current_year_equinox)), ['MINS_SINCE_EQUINOX']] = (nrel_df['DATETIME'] - pd.Timestamp(current_year_equinox)) / pd.Timedelta(seconds=60)
    return nrel_df.drop(columns=['DATETIME'])

def set_solar_declination_angle(nrel_df):
    """
    minutes_since_equinox refers to the number of minutes that have gone through since december 21st at 00:00 hrs
    minimum value is 0 and maximum value is 364
    """
    nrel_df = set_mins_since_equinox(nrel_df)
    minutes_in_a_year = 365.25*24*60
    nrel_df['D'] = np.rad2deg(np.arcsin(-np.cos(np.deg2rad(360*(nrel_df['MINS_SINCE_EQUINOX']/minutes_in_a_year))) * np.sin(np.deg2rad(23.5))) )
    return nrel_df

def set_hour_angle(nrel_df):
    minutes_in_a_day = 24*60
    minutes_at_midday = 12*60
    nrel_df['DAY_MINUTES'] = nrel_df['HOUR']*60 + nrel_df['MINUTE']
    nrel_df['H'] =  (360/minutes_in_a_day)*(nrel_df['DAY_MINUTES'] - minutes_at_midday)
    return nrel_df.drop(columns=['DAY_MINUTES'])

def set_azimuth_angle(nrel_df, L):
    D = np.deg2rad(nrel_df['D'])
    H = np.deg2rad(nrel_df['H'])
    L = np.deg2rad(L)
    # angulo hora de salida y puesta de sol 
    H_sp = np.abs(np.rad2deg(np.arccos(-np.tan(D)*np.tan(L))))
    nrel_df['A'] = np.round(np.rad2deg(np.arctan((np.cos(D)*np.sin(H))/(np.cos(D)*np.sin(L)*np.cos(H)-np.sin(D)*np.cos(L)))),10)
    nrel_df.loc[np.abs(nrel_df['H']) > H_sp, ['A','H'] ] = 0
    return nrel_df
    
# not a necessary function since zenith angle is provided already in data but placing here just in case is needed
# it was verified that calcualtions coincide with the provided data
def set_zenith_angle(nrel_df, L):
    D = np.deg2rad(nrel_df['D'])
    H = np.deg2rad(nrel_df['H'])
    L = np.deg2rad(L)
    nrel_df['Z'] = np.round(np.rad2deg(np.arccos(np.sin(D)*np.sin(L) + np.cos(D)*np.cos(L)*np.cos(H))),5)
    return nrel_df

def set_solar_altitude_angle(nrel_df):
    nrel_df['ALPHA'] = 90 - nrel_df['SOLAR_ZENITH_ANGLE']
    nrel_df.loc[nrel_df['ALPHA'] < 0, ['ALPHA']] = 0
    return nrel_df.rename(columns={'SOLAR_ZENITH_ANGLE':'Z'})

def main(nrel, L):
    #nrel = set_irradiance_components(nrel)
    nrel = set_solar_declination_angle(nrel)
    nrel = set_hour_angle(nrel)
    nrel = set_azimuth_angle(nrel, L)
    nrel = set_solar_altitude_angle(nrel)
    # nrel = set_optimized_inclination_angle(nrel)
    return np.round(nrel,2)