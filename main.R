# Itamar Fiorino
# Basic Bubble Map


## Imports
library(tidyverse)
library(RCurl)
library(ggplot2)
library(dplyr)
library(maps)
library(ggmap)
library(viridis)

# Data
data <-read.csv(text=getURL("https://raw.githubusercontent.com/JesseSilverberg/edustat/master/heatmap.csv"), header=F)
names(data) = c("lat", "long", "Val")

# Heatmap
# Create breaks for the color scale
mybreaks <- c(.81, .9, 1.25, 1.37, 1.49)

# Reorder data to show biggest cities on top
data <- data %>%
  arrange(Val) %>%
  mutate(Val=Val*100) 

# Extract region
Florida <- map_data("state") %>% filter(region=="florida")

# Build the map
ggplot() +
  geom_polygon(data = Florida, aes(x=long, y = lat, group = group), fill="grey") +
   geom_point( data=data, aes(x=long, y=lat, size=Val, color=Val, alpha=Val)) +
   scale_color_viridis(option="magma", trans="log", breaks=mybreaks, name="Value" ) +
   scale_alpha_continuous(name="Value", trans="log", range=c(0.1, .5), breaks=mybreaks) +
   scale_size_continuous(name="Value", trans="log", range=c(1,12), breaks=mybreaks) +
  guides( colour = guide_legend()) +
   theme_void() + coord_map() + xlim(-88, -78) + 
    theme(
      legend.position = c(0.85, 0.7),
      text = element_text(color = "#22211d"),
      plot.background = element_rect(fill = "#f5f5f2", color = NA), 
      panel.background = element_rect(fill = "#f5f5f2", color = NA), 
      legend.background = element_rect(fill = "#f5f5f2", color = NA),
      plot.title = element_text(size= 16, hjust=0.1, color = "#4e4d47", margin = margin(b = -0.1, t = 0.4, l = 2, unit = "cm")),
    )
