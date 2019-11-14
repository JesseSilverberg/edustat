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
  geom_point(aes(x=Fold.Change, y=-log10(pvals), colour=threshold, name=School.Name))  +xlim(-3,3)+
  ggtitle("Volcano Plot") +
  xlab("log2 Fold Change") + 
  ylab("-log10 p-value") +
  #scale_y_continuous(limits = c(0,50)) +
  theme(legend.position = "none",
        plot.title = element_text(size = rel(1.5), hjust = 0.5),
        axis.title = element_text(size = rel(1.25)))  

ggplotly(k)



props<- read.csv(file="props.csv", header=TRUE, sep=",")
m<-c(0.05,0.07,0.09,0.11,0.15,0.19,0.23)
x<-c(0.001,0.005,0.006,0.009,0.013,0.02,0.025)

funds.lm<-lm(m ~ x)
summary(k.lm)
k.df=data.frame(m,x)
ggplot(props, aes(x=funds, y=prop)) + geom_point() + geom_smooth(method=lm)+ggtitle("Funding vs SWD")


