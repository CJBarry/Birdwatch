from met import met_hist

# get_tmin(lat, lon, year, month)
min_temp = met_hist.get_tmin(50.0, 1.1, 2015, 5)
print(min_temp)

# get_tmax(lat, lon, year, month)
max_temp = met_hist.get_tmax(50.0, 1.1, 2015, 5)
print(min_temp)
