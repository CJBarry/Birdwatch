# load in bird data by county and lat long county data and plot on map (color ramp not working properly)

if(!require("maptools")){
  install.packages("maptools")
  require("maptools")
}

if(!exists("year")) stop("define the year you wish to plot for by using year <- __")

bdata <- read.csv(paste0("birds/county_", year, ".csv"))
bdata$species <- gsub(" ", "_", str_to_lower(trimws(bdata$species)))
counties <- readShapePoly("shapefiles/counties_ll.shp")

correct.match <- cbind(bd = {
  c("Aberdeen City", "County Durham", "Greater London",
    "Greater Manchester", "City of Edinburgh", "Dundee City",
    "Linconshire (part of)", "Isle of Angelsey", "Perth and Kinross",
    "East Yorkshire")
}, shp = {
  c("Aberdeen", "Durham", "London",
    "Manchester", "Edinburgh", "Dundee",
    "North Lincolnshire", "Anglesey", "Perthshire and Kinross",
    "East Riding of Yorkshire")
})

for(m in 1:nrow(correct.match)){
  levels(bdata$county)[levels(bdata$county) == correct.match[m, 1L]] <- correct.match[m, 2L]
}

plot.abund <- function(species, key = T, ...){
  abunds <- bdata[bdata$species == species, c("county", "Mean")]
  df <- merge(slot(counties, "data"), abunds, by.x = "NAME_2", by.y = "county", all.x = TRUE, all.y = FALSE)
  # df$Mean[is.na(df$Mean)] <- 0
  colmtx <<- colorRamp(c("yellow", "green", "darkgreen"))(df$Mean/max(df$Mean, na.rm = TRUE))
  colmtx[is.na(colmtx)] <- 255
  col <- rgb(colmtx, maxColorValue = 255)
  plot(counties, asp = 2, col = col, ...)
  if(key){
    points(rep(-15, 6L), 50:55, pch = 21, cex = 3, bg = c("white", rgb(colorRamp(c("yellow", "green", "darkgreen"))(seq(0, 1, .25)), maxColorValue = 255)))
    text(rep(-14.5, 6L), 50:55, c("unknown", signif(seq(0, max(df$Mean, na.rm = TRUE), length.out = 5L), 3L)), pos = 4L)
    text(-15, 55.5, "Mean", cex = 1.3, pos = 3L)
  }
}
