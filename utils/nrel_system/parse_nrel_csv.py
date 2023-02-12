import pandas as pd

def main(csv_path):
    """
    Reads raw NREL csv file and pours it into a structured dictionary 
    Arguments:
        csv_path: absolute or relative path to the csv file provided by the NREL
    Returns:
    {
        "nrel_csv": {
            "headers": {
                "SOURCE": str,
                "LOCATION_ID": int,
                "CITY": str,
                "STATE": str,
                "COUNTRY": str,
                "LATITUDE": float,
                "LONGITUDE": float,
                "TIME_ZONE": int,
                "ELEVATION": int,
                "LOCAL_TIME_ZONE": int,
                "VERSION": str
            },        
            "units": {
                "CLEARSKY_DHI_UNITS": str,
                "CLEARSKY_DNI_UNITS": str,
                "CLEARSKY_GHI_UNITS": str,
                "DEW_POINT_UNITS": str,
                "DHI_UNITS": str,
                "DNI_UNITS": str,
                "GHI_UNITS": str,
                "SOLAR_ZENITH_ANGLE_UNITS": str,
                "TEMPERATURE_UNITS": str,
                "PRESSURE_UNITS": str,
                "RELATIVE_HUMIDITY_UNITS": str,
                "PRECIPITABLE_WATER_UNITS": str,
                "WIND_DIRECTION_UNITS": str,
                "WIND_SPEED_UNITS": str,
                "SURFACE_ALBEDO_UNITS": str
            },
            "cloud_types": {
                "CLOUD_TYPE_-15": str,
                "CLOUD_TYPE_0": str,
                "CLOUD_TYPE_1": str,
                "CLOUD_TYPE_2": str,
                "CLOUD_TYPE_3": str,
                "CLOUD_TYPE_4": str,
                "CLOUD_TYPE_5": str,
                "CLOUD_TYPE_6": str,
                "CLOUD_TYPE_7": str,
                "CLOUD_TYPE_8": str,
                "CLOUD_TYPE_9": str,       
                "CLOUD_TYPE_10": str,
                "CLOUD_TYPE_11": str,
                "CLOUD_TYPE_12": str
            },
            "fill_flags": {
                "FILL_FLAG_0": str,
                "FILL_FLAG_1": str,
                "FILL_FLAG_2": str,
                "FILL_FLAG_3": str,
                "FILL_FLAG_4": str,
                "FILL_FLAG_5": str
            },
            "data": Pandas Dataframe with the following schema -> {
                "YEAR": int,
                "MONTH": int,
                "DAY": int,
                "HOUR": int,
                "MINUTE": int,
                "DHI": int,
                "DNI": int,
                "GHI": int,
                "TEMPERATURE": float,
                "SOLAR_ZENITH_ANGLE": float
            }
        }
    }
    """
    nrel_df = pd.read_csv(csv_path, nrows=1)
    nrel_df.columns = [x.upper() for x in nrel_df.columns]
    nrel_df.columns = nrel_df.columns.str.replace("[ ]", "_", regex=True)
    nrel_dict = nrel_df.to_dict('records')[0]
    
    rows_to_skip = [0,1]
    nrel_data = pd.read_csv(csv_path, skiprows = lambda x: x in rows_to_skip, low_memory=False)
    nrel_data.columns = [x.upper() for x in nrel_data.columns]
    nrel_data.columns = nrel_data.columns.str.replace("[ ]", "_", regex=True)
    
    parsed = {"data":nrel_data}
    
    parsed["headers"] = {}
    #parsed["headers"]["SOURCE"] = nrel_dict["SOURCE"]
    #parsed["headers"]["LOCATION_ID"] = nrel_dict["LOCATION_ID"]
    #parsed["headers"]["CITY"] = nrel_dict["CITY"]
    #parsed["headers"]["STATE"] = nrel_dict["STATE"]
    #parsed["headers"]["COUNTRY"] = nrel_dict["COUNTRY"]
    parsed["headers"]["LATITUDE"] = nrel_dict["LATITUDE"]
    parsed["headers"]["LONGITUDE"] = nrel_dict["LONGITUDE"]
    #parsed["headers"]["TIME_ZONE"] = nrel_dict["TIME_ZONE"]
    #parsed["headers"]["ELEVATION"] = nrel_dict["ELEVATION"]
    #parsed["headers"]["LOCAL_TIME_ZONE"] = nrel_dict["LOCAL_TIME_ZONE"]
    #parsed["headers"]["VERSION"] = nrel_dict["VERSION"]
    
    parsed["units"] = {}
    #parsed["units"]["CLEARSKY_DHI_UNITS"] = nrel_dict["CLEARSKY_DHI_UNITS"]
    #parsed["units"]["CLEARSKY_DNI_UNITS"] = nrel_dict["CLEARSKY_DNI_UNITS"]
    #parsed["units"]["CLEARSKY_GHI_UNITS"] = nrel_dict["CLEARSKY_GHI_UNITS"]
    #parsed["units"]["DEW_POINT_UNITS"] = nrel_dict["DEW_POINT_UNITS"]
    #parsed["units"]["DHI_UNITS"] = nrel_dict["DHI_UNITS"]
    #parsed["units"]["DNI_UNITS"] = nrel_dict["DNI_UNITS"]
    #parsed["units"]["GHI_UNITS"] = nrel_dict["GHI_UNITS"]
    #parsed["units"]["SOLAR_ZENITH_ANGLE_UNITS"] = nrel_dict["SOLAR_ZENITH_ANGLE_UNITS"]
    #parsed["units"]["TEMPERATURE_UNITS"] = nrel_dict["TEMPERATURE_UNITS"]
    #parsed["units"]["PRESSURE_UNITS"] = nrel_dict["PRESSURE_UNITS"]
    #parsed["units"]["RELATIVE_HUMIDITY_UNITS"] = nrel_dict["RELATIVE_HUMIDITY_UNITS"]
    #parsed["units"]["PRECIPITABLE_WATER_UNITS"] = nrel_dict["PRECIPITABLE_WATER_UNITS"]
    #parsed["units"]["WIND_DIRECTION_UNITS"] = nrel_dict["WIND_DIRECTION_UNITS"]
    #parsed["units"]["WIND_SPEED_UNITS"] = nrel_dict["WIND_SPEED_UNITS"]
    #parsed["units"]["SURFACE_ALBEDO_UNITS"] = nrel_dict["SURFACE_ALBEDO_UNITS"
    
    
    parsed["cloud_types"] = {}
    #parsed["cloud_types"]["CLOUD_TYPE_-15"]= nrel_dict["CLOUD_TYPE_-15"]
    #parsed["cloud_types"]["CLOUD_TYPE_0"] = nrel_dict["CLOUD_TYPE_0"]
    #parsed["cloud_types"]["CLOUD_TYPE_1"] = nrel_dict["CLOUD_TYPE_1"]
    #parsed["cloud_types"]["CLOUD_TYPE_2"] = nrel_dict["CLOUD_TYPE_2"]
    #parsed["cloud_types"]["CLOUD_TYPE_3"] = nrel_dict["CLOUD_TYPE_3"]
    #parsed["cloud_types"]["CLOUD_TYPE_4"] = nrel_dict["CLOUD_TYPE_4"]
    #parsed["cloud_types"]["CLOUD_TYPE_5"] = nrel_dict["CLOUD_TYPE_5"]
    #parsed["cloud_types"]["CLOUD_TYPE_6"] = nrel_dict["CLOUD_TYPE_6"]
    #parsed["cloud_types"]["CLOUD_TYPE_7"] = nrel_dict["CLOUD_TYPE_7"]
    #parsed["cloud_types"]["CLOUD_TYPE_8"] = nrel_dict["CLOUD_TYPE_8"]
    #parsed["cloud_types"]["CLOUD_TYPE_9"] = nrel_dict["CLOUD_TYPE_9"]
    #parsed["cloud_types"]["CLOUD_TYPE_10"] = nrel_dict["CLOUD_TYPE_10"]
    #parsed["cloud_types"]["CLOUD_TYPE_11"] = nrel_dict["CLOUD_TYPE_11"]
    #parsed["cloud_types"]["CLOUD_TYPE_12"] = nrel_dict["CLOUD_TYPE_12"
    
    
    parsed["FILL_FLAGS"] = {}
    #parsed["FILL_FLAGS"]["FILL_FLAG_0"] = nrel_dict["FILL_FLAG_0"]
    #parsed["FILL_FLAGS"]["FILL_FLAG_1"] = nrel_dict["FILL_FLAG_1"]
    #parsed["FILL_FLAGS"]["FILL_FLAG_2"] = nrel_dict["FILL_FLAG_2"]
    #parsed["FILL_FLAGS"]["FILL_FLAG_3"] = nrel_dict["FILL_FLAG_3"]
    #parsed["FILL_FLAGS"]["FILL_FLAG_4"] = nrel_dict["FILL_FLAG_4"]
    #parsed["FILL_FLAGS"]["FILL_FLAG_5"] = nrel_dict["FILL_FLAG_5"]
    
    
    return {"nrel_csv": parsed}