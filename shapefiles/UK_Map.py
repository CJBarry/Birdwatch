#import Basemap, numpy and matplotlib.pyplot
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import cm
import shapefile
%matplotlib inline

#create map of the UK
#projection 'tmerc' is a flattened map
# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# resolution = 'i' means use intermediate resolution coastlines.
# lon_0, lat_0 are the central longitude and latitude of the projection.
uk_map = Basemap(llcrnrlon=-10.5,llcrnrlat=49.5,urcrnrlon=3.5,urcrnrlat=59.5,
            resolution='i',projection='tmerc',lon_0=-4.36,lat_0=54.7)

uk_map.drawparallels(np.arange(-40,61.,2.))
uk_map.drawmeridians(np.arange(-20.,21.,2.))
uk_map.drawcoastlines()
#uk_map.fillcontinents(color='aqua',lake_color='blue')

uk_map.drawmapboundary()

plt.title("UK Map")
plt.show()
