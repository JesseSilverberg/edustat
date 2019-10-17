library(ggplot2)
library(tidyverse)

clusters<- read.csv(file="clusters.csv", header=TRUE, sep=",")

clusters <- clusters %>% 
  rowwise %>%
  mutate(
    pvals = prop.test(x=c(Charter.Count,Other.Count),n=c(Charter.Total,Other.Total), alternative="two.sided")$p.value
  ) %>%
  mutate(
    Fold.Change = log2((Charter.Count/Charter.Total)/(Other.Count/Other.Total))
  )

<<<<<<< HEAD
clusters$threshold <- clusters$pvals < 0.05 
ggplot(clusters) +
  geom_point(aes(x=Fold.Change, y=-log10(pvals), colour=threshold)) + ylim(0, 100) +
  ggtitle("Volcano Plot") +
  xlab("log2 Fold Change") + 
  ylab("-log10 p-value") +
  #scale_y_continuous(limits = c(0,50)) +
  theme(legend.position = "none",
        plot.title = element_text(size = rel(1.5), hjust = 0.5),
        axis.title = element_text(size = rel(1.25)))  
=======





####
c(clusters[["Charter.Count"]],clusters[["Other.Count"]])
chisq.test(c(clusters[["Charter.Count"]],clusters[["Other.Count"]]),n=c(clusters[["Charter.Total"]],clusters[["Other.Total"]]))
contingency<-data.frame(clusters["Charter.Count"],clusters["Other.Count"])
>>>>>>> fd3eb022731740e486fbbe1e48bee3c4a785dfb5
