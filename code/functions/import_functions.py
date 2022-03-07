import pandas as pd
import geopandas as gpd


def import_policy(country, path_to_data):
    """
    This function imports a Oxford Policy file for a given country
    :param country: name of country
    :param path_to_data: path to the data
    :return policy df
    """
    return pd.read_csv(path_to_data + country + "/oxford-policy-report/oxford_policy_report.csv", index_col="date",
                       parse_dates=True)


def import_gadm(country, path_to_data):
    """
    This function imports a GADM file for a given country
    :param country: name of country
    :param path_to_data: path to the data
    :return GADM df
    """
    # import data
    gadm2 = gpd.read_file(
        path_to_data + country + "/master-files/master_file.shp").join(pd.read_csv(
        path_to_data + country + "/master-files/master_file.csv"))

    gadm2["area"] = gadm2.geometry.to_crs({'init': 'epsg:3857'}).area / 10 ** 6
    gadm2["pop_density"] = gadm2["pop2020"] / gadm2["area"]
    return gadm2


def import_range_maps(country, path_to_data):
    """
    This function imports a Range Maps file for a given country
    :param country: name of country
    :param path_to_data: path to the data
    :return range maps df
    """
    df = pd.read_csv(path_to_data + country + "/fb-movement-range-maps/movement_range_maps.csv", sep=',')
    df.ds = pd.to_datetime(df.ds)
    return df


def import_epi(country, path_to_data):
    """
    Import epidemiological data for a given country
    :param country: name of country
    :param path_to_data: path to the data
    """
    df = pd.read_csv(path_to_data + country + "/epidemiological-data/df_new_data_municipio.csv")
    df.date = pd.to_datetime(df.date)
    return df
