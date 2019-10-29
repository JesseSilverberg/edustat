#Itamar Fiorino
#10/4/2019

# Library
library(tidyverse)
library(RCurl)
library(ggplot2)
library(dplyr)
library(maps)
library(ggmap)
library(viridis)
library(leaflet)

props=read.csv(file="props.csv", header=TRUE, sep=",")


# Data
data <-read.csv(file="clusters.csv", header=T)

data$Val <- data$Charter.Count/data$Charter.Total-data$Other.Count/data$Other.Total
data$charterProp <- data$Charter.Count/data$Charter.Total
data$otherProp <- data$Other.Count/data$Other.Total

data <- data %>%
  arrange(abs(Val)) %>%
  mutate(Val=Val*100)

# data <- data %>% filter(60 < Val) %>%
#   filter(70 > Val)

# Create a color palette with handmade bins.
mybins <- seq(-20, 20, by=10)
mypalette <- colorBin( palette="Spectral", domain=data$Val, na.color="transparent", bins=mybins)

# Prepare the text for the tooltip:
mytext <- paste(
  "Difference: ", round(data$Val, digits=2), " %<br/>", sep="") %>%
  lapply(htmltools::HTML)


# Final Map
m <- leaflet(data) %>% 
  addTiles()  %>% 
  setView( lat=27, lng=-83 , zoom=6) %>%
  addProviderTiles("Esri.WorldImagery") %>%
  addCircleMarkers(~Long, ~Lat, 
                   fillColor = ~mypalette(Val), fillOpacity = .5, color="white", radius=~10, stroke=FALSE,
                   label = mytext,
                   labelOptions = labelOptions( style = list("font-weight" = "normal", padding = "3px 8px"), textsize = "13px", direction = "auto")
  ) %>%
  addLegend( pal=mypalette, values=~Val, opacity=0.9, title = "Difference", position = "bottomright" )

m 

# save the widget in a html file if needed.
library(htmlwidgets)
saveWidget(m, file=paste0( getwd(), "bubblemapCharters.html"))

