# Christopher Barry
# repackages met station data into new data frame
# new data frame can then be written to file with write.csv(data frame object, file name)

# package requirement, including installation if necessary
if(!require("stringr")){
  install.packages("stringr")
  require("stringr")
}
source("td.R")

tdata <- read.csv("station_data-201411010000-201412312359_all_uk.csv")

#split date time into ymdhm
t.datetime <- str_split(levels(tdata$ob_end_time)[tdata$ob_end_time], " ")
t.ymd <- do.call(rbind, str_split(sapply(t.datetime, `[`, 1), "-"))
t.hm <- do.call(rbind, str_split(sapply(t.datetime, `[`, 2), ":"))
mode(t.ymd) <- "integer"; mode(t.hm) <- "integer"
colnames(t.ymd) <- c("y", "m", "d"); colnames(t.hm) <- c("h", "min")

#unique day reference, where each day has an integer reference (consistent with MS Excel)
t.dref <- apply(t.ymd, 1L, function(r) td(r[3], r[2], r[1]))

#whether the observation was over night (assumes that times are given for the end of the observation period which are all 12 hours long)
# TRUE or FALSE
night <- t.hm[, 1] < 11

tdata2 <- with(tdata, data.frame(dref = t.dref,
                                 datetime_end = ob_end_time,
                                 t.ymd, t.hm,
                                 night = night,
                                 id = id,
                                 met_domain_name = met_domain_name,
                                 src_id = src_id,
                                 minAT = min_air_temp,
                                 maxAT = max_air_temp,
                                 meanAT = rowMeans(cbind(min_air_temp, max_air_temp))))

str(tdata2)
