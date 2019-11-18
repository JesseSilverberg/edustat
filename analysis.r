library(ggplot2)
library(tidyverse)
library(plotly)

clusters<- read.csv(file="clusters.csv", header=TRUE, sep=",")

clusters <- clusters %>% 
  rowwise %>%
  mutate(
    pvals = prop.test(x=c(Charter.Count,Other.Count),n=c(Charter.Total,Other.Total), alternative="two.sided")$p.value
  ) %>%
  mutate(
    Fold.Change = log2((Charter.Count/Charter.Total)/(Other.Count/Other.Total))
  )

clusters$threshold <- clusters$pvals < 0.05 
k <- ggplot(clusters) +
  geom_point(aes(x=Fold.Change, y=-log10(pvals), colour=threshold, text=School.Name))  +xlim(-3,3)+
  ggtitle("Volcano Plot") +
  xlab("log2 Fold Change") + 
  ylab("-log10 p-value") +
  #scale_y_continuous(limits = c(0,50)) +
  theme(legend.position = "none",
        plot.title = element_text(size = rel(1.5), hjust = 0.5),
        axis.title = element_text(size = rel(1.25)))  

ggplotly(k, tooltip="text")




charterFunds<- read.csv(file="charterFunds.csv", header=TRUE, sep=",")
otherFunds<- read.csv(file="otherFunds.csv", header=TRUE, sep=",")

funds.lm<-lm(charterFunds[["funds"]]~charterFunds[["prop"]])
summary(funds.lm)

funds.lm<-lm(otherFunds[["funds"]]~otherFunds[["prop"]])
summary(funds.lm)

j <- ggplot(charterFunds, aes(prop, funds)) + geom_point(aes(text=sprintf("Name: %s", School.Name))) + geom_smooth(method=lm)+ggtitle("Funding vs SWD, Charter Schools")
k <- ggplot(otherFunds, aes(prop, funds)) + geom_point(aes(text=sprintf("Name: %s", School.Name))) + geom_smooth(method=lm)+ggtitle("Funding vs SWD, Public Schools")

ggplotly(j, tooltip="text")
ggplotly(k, tooltip="text")

