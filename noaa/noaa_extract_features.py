from operator import index
import xarray as xr
import pandas as pd
import os
import sys
sys.path.append('..')
import warnings
warnings.filterwarnings("ignore")


class NOAAFeatureExtractor():
    """Extract features out of NOAA files .FXXX"""
    def extract_feature(self, file_name: str, feature: str):
        """
        file_name
            (required, str) Name of file which contains features
        feature
            (required, str) Feature which should get extracted
        """

        # https://spire.com/tutorial/spire-weather-tutorial-intro-to-processing-grib2-data-with-python/
        ds = xr.open_dataset(file_name, engine="pynio")
        ds = ds.get(feature)
        df = ds.to_dataframe()

        latitudes = df.index.get_level_values("lat_0")
        longitudes = df.index.get_level_values("lon_0")

        map_function = lambda lon: (lon - 360) if (lon > 180) else lon
        remapped_longitudes = longitudes.map(map_function)

        df["longitude"] = remapped_longitudes
        df["latitude"] = latitudes

        # Filter only for South Africa
        min_lon = 15.0
        max_lon = 33.0
        min_lat = -35.0
        max_lat = -22.0
        lat_filter = (df["latitude"] >= min_lat) & (df["latitude"] <= max_lat)
        lon_filter = (df["longitude"] >= min_lon) & (df["longitude"] <= max_lon)

        df = df.loc[lat_filter & lon_filter]

        if feature == 'TMP_P0_L103_GLL0':
            df['TMP_P0_L103_GLL0'] = df['TMP_P0_L103_GLL0']-273  # K to C

        df.reset_index(inplace=True)

        if feature == 'TMP_P0_L103_GLL0':
            df = df.query('lv_HTGL2 == 2.0')
        if feature == 'UGRD_P0_L103_GLL0' or feature == 'VGRD_P0_L103_GLL0':
            df = df.query('lv_HTGL7 == 10.0')

        df = df[['longitude', 'latitude', feature]]

        if os.path.exists(f'{file_name}_features.csv'):
            df_all = pd.read_csv(f'{file_name}_features.csv', index_col=0)
            df_result = pd.merge(df_all, df,  how='outer', left_on=['longitude','latitude'], right_on = ['longitude','latitude'])
            df_result.to_csv(f'{file_name}_features.csv')
        else:
            df.to_csv(f'{file_name}_features.csv')

        print(f'Extraction of feature {feature} finished')