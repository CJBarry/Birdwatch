# load in bird data by county and lat long county data and plot on map (color ramp not working properly)

if(!require("maptools")){
  install.packages("maptools")
  require("maptools")
}

bdata <- read.csv("birds/county_2015.csv")
bdata$species <- trimws(bdata$species)
counties <- readShapePoly("shapefiles/counties_ll.shp")

plot.abund <- function(species){
  abunds <- bdata[bdata$species == species, c("county", "Mean")]
  df <- merge(slot(counties, "data"), abunds, by.x = "NAME_2", by.y = "county", all.x = TRUE, all.y = FALSE)
  df$Mean[is.na(df$Mean)] <- 0
  plot(counties, asp = 2, col = colorRamp(c("lightgreen", "green", "darkgreen"), space = "rgb", interpolate = "linear")(df$Mean/max(df$Mean)))
}
