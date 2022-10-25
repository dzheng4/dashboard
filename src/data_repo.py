from json import load
import numpy as np
import time
import numpy as np
import pandas as pd
import plotly.express as px
import pathlib

from app import load_data


# # Load Penn csv file
# penn_retail_df = pd.read_csv('states_data\\PA\\Pennsylvania_Retail_Pharmacy_Vaccine_Allocation2022_06_23.csv', dtype = {
#         'Retail Pharmacy Partner Name' : str,
#         'Address 1' : str,
#         'City' : str,
#         'County' : str,
#         'State' : str,
#         'Zip Code' : str,
#         'Vaccine' : str,
#         'Date' : str,
#         'Doses' : float,
#         'Georeferenced Latitude & Longitude' : str
#     },
#     parse_dates = ['Date'],
#     infer_datetime_format=True
# )

# # Load State link csv file
# summary_df = pd.read_csv('states_data\\Official_State_COVID_LINKS.csv', dtype = {
#         'State' : str,
#         'Link' : str,
#         'Data Score' : float,
#         'Distribution' : str,
#         'Provider' : str,
#         'Wastage' : str
#     }
# )

penn_retail_df = load_data('states_data/PA/9_22_2022/Pennsylvania_Retail_Pharmacy_Vaccine_Allocation2022_09_22.csv')

# summary_df = load_data('states_data/Official_State_COVID_LINKS.csv')

summary_df = load_data('states_data/State_By_State.csv')

illinois_df = load_data('states_data/IL/IL_county.csv')

newyork_df = load_data('states_data/NY/8_14_2022/New York_Vaccination_By_County2022_08_14.csv')

connecticut_df = load_data('states_data/CT/9_22_2022/Connecticut_Vaccination By Week-2022_09_22.csv')

maryland_hospital_df = load_data('states_data/MD/10_24_2022/Maryland_Hospital_Status2022_10_24.csv')

maryland_vaccination_df = load_data('states_data/MD/10_24_2022/Maryland_Daily_Vaccinations2022_10_24.csv')

california_df = load_data('states_data/CA/10_5_2022/covid19vaccinesshipped_delivered_onhand.csv')

ohio_df = load_data('states_data/OH/9_28_2022/Ohio_Vaccine_Summary2022_09_28.csv')

## Minnesota file name different every time (Manual)
## Need to delete first row (Because date column not valid)
minnesota_vaccination_df = load_data('states_data/MN/9_28_2022/Doses Administered By Week_tcm1148-513629.csv')


### cdc data
cdc_df = load_data('country_data/COVID-19_Vaccinations_in_the_United_States_Jurisdiction.csv')



path = "fips2county.tsv"
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath(path).resolve()
fips_df = pd.read_csv(DATA_PATH, sep='\t', header='infer', dtype=str, encoding='latin-1')