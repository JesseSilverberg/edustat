library(shiny)
library(tidyverse)
library(RCurl)
library(ggplot2)
library(dplyr)
library(maps)
library(ggmap)
library(viridis)
library(leaflet)

# Data
set.seed(100)
data <-read.csv(text=getURL("https://raw.githubusercontent.com/JesseSilverberg/edustat/master/clusters.csv"), header=T)

data$Val <- data$Charter.Count/data$Charter.Total-data$Other.Count/data$Other.Total

data <- data %>%
    arrange(abs(Val)) %>%
    mutate(Val=Val*100)

# Create a color palette with handmade bins.
mybins <- seq(-100, 100, by=40)
mypalette <- colorBin( palette="Spectral", domain=data$Val, na.color="transparent", bins=mybins)

# Prepare the text for the tooltip:
mytext <- paste(
    "Difference: ", round(data$Val, digits=2), " %<br/>", sep="") %>%
    lapply(htmltools::HTML)


ui <- fluidPage(
    div(class="outer",
        
        tags$head(
            # Include our custom CSS
            includeCSS("style.css")
        ),
        
    leafletOutput("mymap", width="100%", height="100%"),
    absolutePanel(id = "controls", class = "panel panel-default", fixed = TRUE,
                  draggable = TRUE, top = 60, left = "auto", right = 20, bottom = "auto",
                  width = 330, height = "auto",
                  
                  h2("Data Selection"),
                  sliderInput("slider", h3("Data Range"), min=-1, max=1, value=c(-1,1), step=0.05)
                    )
))

server <- function(input, output, session) {
    
    points <- reactive({
        data %>% subset(input$slider[1] *100< Val & input$slider[2] *100> Val)
    })
    
    output$mymap <- renderLeaflet({
        leaflet(points()) %>% 
            addTiles()  %>% 
            setView( lat=27, lng=-83 , zoom=6) %>%
            addProviderTiles("Esri.WorldImagery")
            
    })
    observe({
        

        leafletProxy("mymap", data = points()) %>%
            clearShapes() %>%
            addCircleMarkers(~Long, ~Lat, 
                             fillColor = ~mypalette(points()$Val), fillOpacity = .5, color="white", radius=5*log(abs(points()$Val)), stroke=FALSE,
                             label = mytext,
                             labelOptions = labelOptions( style = list("font-weight" = "normal", padding = "3px 8px"), textsize = "13px", direction = "auto")
            ) %>%
            addLegend( pal=mypalette, values=~points()$Val, opacity=0.9, title = "Difference", position = "bottomright" )
    })
    
}

shinyApp(ui, server)