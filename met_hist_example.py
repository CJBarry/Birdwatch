from met import met_hist

# get_tmin(lat, lon, year, month)
min_temp = met_hist.get_tmin(50.0, 1.2, 2015, 5)
print(min_temp)


# get_tmax(lat, lon, year, month)
max_temp = met_hist.get_tmax(51.0, 1.1, 2015, 5)
print(max_temp)

for year in [2013, 2014, 2015]:
    min_temp = met_hist.get_tmin(52.0, 1.1, year, 11)
    print(min_temp)
