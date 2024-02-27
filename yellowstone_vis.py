import csv
from datetime import datetime

import matplotlib.pyplot as plt

import numpy as np

data = open(file='weather_data/yellowstone_2023.csv', mode='r')

reader = csv.reader(data)
header = next(reader)
print(header)

for index, column_name in enumerate(header):
    print(index, column_name)

for index, column_name in enumerate(header):
    data.seek(0)
    col_len = 0
    for row in reader:
        if(row[index]):
            col_len += 1
        else:
            pass
    print(f"Number of data points for {column_name}: {col_len}")
        
stations = []
station_locations = {}
data_by_station = {}

data.seek(0)
next(reader)

for row in reader:
    station_name = row[1]
    if station_name not in stations:
        stations.append(station_name)

print(stations)
print(len(stations))



for station in stations:
    data.seek(0)
    station_data = []
    for row in reader:
        if row[1] == station:
            try:
                latitude = float(row[2])
                longitude = float(row[3])
                elevation = float(row[4])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                location = [
                    latitude,
                    longitude,
                    elevation
                ]

            current_date = datetime.strptime(row[5], '%Y-%m-%d')
            try:
                # average = int(row[18])
                high = int(row[20])
                low = int(row[22])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                data_point = [
                    current_date,
                    # average,
                    high,
                    low
                ]
                station_data.append(data_point)
    
    if location:
        station_locations[station] = location
    
    data_by_station[station] = np.array(station_data)

for station in stations:
    print(f"Location of station {station}: {station_locations[station]}")

# for station in stations:
#     data_by_station[station] = np.array(data_by_station[station])

# data_sylvan_lake = data_by_station['SYLVAN LAKE, WY US']

print("Data for station: SYLVAN LAKE, WY US")
print(data_by_station['SYLVAN LAKE, WY US'])

# print(data_by_station['SYLVAN LAKE, WY US'][:,1])
# print(type(data_by_station['SYLVAN LAKE, WY US'][:,1]))
# print(data_by_station['SYLVAN LAKE, WY US'][:,1].shape)
# print(np.std(data_by_station['SYLVAN LAKE, WY US'][:,1]))

station_stds = {}

# for station in stations:
#     print(f"Data for station: {station}")
#     print(data_by_station[station])
    # print(data_by_station[station][:,0])
    # std = np.std(data_by_station[station][:,1])     # Standard deviation of average temperature
    # station_stds[station] = std
    # print(data_by_station[station].shape)    

latitudes = []
longitudes = []
elevations = []

for station in stations:
    latitudes.append(station_locations[station][0])
    longitudes.append(station_locations[station][1])
    elevations.append(station_locations[station][2])

grid = np.meshgrid(latitudes, longitudes)
print(grid)
for val in grid:
    print(val)

elevs = np.empty(shape=(len(latitudes), len(longitudes)))

# for idx, elevation in enumerate(elevations):
    # elevs[latitudes[idx]][longitudes[idx]] = elevation

figl, axl = plt.subplots()
axl.contour(elevs)

# fig, ax = plt.subplots(nrows=len(stations[:5]))
fig, ax = plt.subplots()
first_5_stations = stations[:5]
first_5_stations_highs = [data_by_station[station][:,2].astype(int) for station in first_5_stations]
print(first_5_stations)
print(first_5_stations_highs)
ax.boxplot(first_5_stations_highs, labels=first_5_stations)

fig2, ax2 = plt.subplots()
# ax2.hist(first_5_stations_highs[0], label='SYLVAN LAKE, WY US')
# ax2.hist(first_5_stations_highs, label=first_5_stations)

fig3, ax3 = plt.subplots()
ax3.violinplot(first_5_stations_highs)
ax3.set_xticks(ticks=np.arange(1, len(first_5_stations) + 1), labels=first_5_stations)

for idx, station in enumerate(stations[:5]):
    # dates = data_by_station[station][:,0]
    # averages = data_by_station[station][:,1]
    highs = data_by_station[station][:,2]
#     lows = data_by_station[station][:,3]
#     ax.plot(dates, averages, label=f"{station} averages")
    # ax.plot(dates, highs, label=f"{station} highs")
    # ax.plot(dates, lows, label=f"{station} lows")
    # ax.fill_between(dates.astype(np.datetime64), highs.astype(np.int64), lows.astype(np.int64), facecolor='palegoldenrod')
    ax2.hist(highs, label=station)
    # ax.boxplot(highs, labels=station)
# ax.plot(data_sylvan_lake[:,0], data_sylvan_lake[:,1], label='Sylvan Lake highs')
# ax.plot(data_sylvan_lake[:,0], data_sylvan_lake[:,2], label='Sylvan Lake lows')
# ax.fill_between(data_sylvan_lake[:,0], 1, 2)
# ax.fill_between(data_sylvan_lake[:,0].astype(np.datetime64), data_sylvan_lake[:,1].astype(np.int64), data_sylvan_lake[:,2].astype(np.int64), facecolor='palegoldenrod')
# fig.autofmt_xdate()
plt.legend()
plt.show()