library(lubridate)
library(dplyr)
library(readxl)
library(purr)
library(stringr)

# loading data file which has been converted to csv from xlsx
df = read.csv("~/Desktop/Projects/tj_locations/E-5_2020_by_Geo_Internet.csv", header = T)
df = df[-c(1:33),] #remove statewide records
View(df)

#simplify dates into years
df = df %>% mutate(Year = as.factor(paste("20",str_sub(Date,-2,-1),sep="")))
df = df %>% select(-"Date")
