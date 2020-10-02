
# example part 7-8

# DBSCAN 군집분석

import pandas as pd
import folium

# step 1 데이터 준비/기본 설정

file_path = './2016_middle_school_graduates_report.xlsx'
df = pd.read_excel(file_path, header=0, index_col='Unnamed: 0')

pd.set_option('display.width', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)

print(df.columns.values)

# step 2 데이터 탐색

print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()

# 지도에 위치 표시
mschool_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', zoom_start=12)

for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    folium.CircleMarker([lat,lng], radius=5, color='brown', fill=True, fill_color='coral', fill_opacity=0.7, popup=name).add_to(mschool_map)

mschool_map.save('./seoul_mschool_loc.html')
