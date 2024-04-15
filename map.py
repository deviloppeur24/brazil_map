import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

file_path_excel = "C:/Users/louan/Desktop/projet_bresil/csv_et_shp/brazil.xlsx"
brazil_data = pd.read_excel(file_path_excel, sheet_name="2015 - 2030")

file_path_shapefile = "C:/Users/louan/Desktop/projet_bresil/csv_et_shp/Brazil_adm2_uscb_2022.shp"
geo_data = gpd.read_file(file_path_shapefile)

merged_data = geo_data.merge(brazil_data, on="GEO_MATCH", how="inner")

fig, ax = plt.subplots(figsize=(10, 10))
merged_data.plot(ax=ax, column="VARIABLE_A_REPRESENTER", cmap="Blues", legend=True)
plt.title("Carte du Brésil avec des données")
plt.show()
