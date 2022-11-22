# https://www.kaggle.com/usdot/flight-delays/download#airports.csv

library(data.table)
library(arrow)

dt = fread('~/Downloads/archive/flights.csv')
dt[, date := as.Date(paste0(YEAR, '-', MONTH, '-', DAY))]
dt[, departure_time := sprintf('%04d', SCHEDULED_DEPARTURE)]
dt[, departure := paste0(date, ' ', substr(departure_time, 1, 2), ':', substr(departure_time, 3, 4))]
dt = dt[, .(departure, AIRLINE, ORIGIN_AIRPORT, DESTINATION_AIRPORT, DEPARTURE_DELAY, ARRIVAL_DELAY)]
setnames(dt, tolower(names(dt)))
set.seed(123)
# down-sample from 5.8m flights to 100k flights
dt = dt[sample(1:nrow(dt), 100000)]
fwrite(dt, 'airlines/flights_100k.parquet')

ap = fread('~/Downloads/archive/airports.csv')
fwrite(ap, 'airlines/airports.parquet')
