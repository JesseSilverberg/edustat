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
  geom_point(aes(x=Fold.Change, y=-log10(pvals), colour=threshold, text=sprintf("%s<br>Fold Change: %s <br> P-Value: %s", School.Name, Fold.Change, -log10(pvals))))  +xlim(-3,3)+
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

j <- ggplot(charterFunds, aes(prop, funds)) + geom_point(aes(text=sprintf("%s<br>Proportion: %s <br> Funds: %s", School.Name, prop, funds))) + geom_smooth(method=lm)+ggtitle("Funding vs SWD, Charter Schools")
k <- ggplot(otherFunds, aes(prop, funds)) + geom_point(aes(text=sprintf("%s<br>Proportion: %s <br> Funds: %s", School.Name, prop, funds))) + geom_smooth(method=lm)+ggtitle("Funding vs SWD, Public Schools")

ggplotly(j, tooltip="text")
ggplotly(k, tooltip="text")






###Achievement Analysis

#Totals

achieveCharter<- read.csv(file="charterAchievement.csv", header=TRUE, sep=",")
achieveOther<- read.csv(file="otherAchievement.csv", header=TRUE, sep=",")


proficiency=t(data.frame(c(sum(achieveCharter$e1),sum(achieveCharter$e2),sum(achieveCharter$e3),sum(achieveCharter$e4),sum(achieveCharter$e5)),c(sum(achieveOther$e1),sum(achieveOther$e2),sum(achieveOther$e3),sum(achieveOther$e4),sum(achieveOther$e5))))
chisq.test(proficiency)


proficiency=t(data.frame(c(sum(achieveCharter$m1),sum(achieveCharter$m2),sum(achieveCharter$m3),sum(achieveCharter$m4),sum(achieveCharter$m5)),c(sum(achieveOther$m1),sum(achieveOther$m2),sum(achieveOther$m3),sum(achieveOther$m4),sum(achieveOther$m5))))
chisq.test(proficiency)


proficiency=t(data.frame(c(sum(achieveCharter$s1),sum(achieveCharter$s2),sum(achieveCharter$s3),sum(achieveCharter$s4),sum(achieveCharter$s5)),c(sum(achieveOther$s1),sum(achieveOther$s2),sum(achieveOther$s3),sum(achieveOther$s4),sum(achieveOther$s5))))
chisq.test(proficiency)


proficiency=t(data.frame(c(sum(achieveCharter$sc1),sum(achieveCharter$sc2),sum(achieveCharter$sc3),sum(achieveCharter$sc4),sum(achieveCharter$sc5)),c(sum(achieveOther$sc1),sum(achieveOther$sc2),sum(achieveOther$sc3),sum(achieveOther$sc4),sum(achieveOther$sc5))))
chisq.test(proficiency)


#By Cluster

achieve<- read.csv(file="clusterAchievement.csv", header=TRUE, sep=",")


achieve <- achieve %>% 
  rowwise %>%
  mutate(
    pvals = prop.test(x=c(cpe,ope),n=c(cte,ote), alternative="two.sided")$p.value
  ) %>%
  mutate(
    Fold.Change = log2((cpe/cte)/(ope/ote))
  )

achieve$threshold <- achieve$pvals < 0.05
k <- ggplot(achieve) +
  geom_point(aes(x=Fold.Change, y=-log10(pvals), colour=threshold, text=sprintf("%s<br>Fold Change: %s <br> P-Value: %s", School.Name, Fold.Change, -log10(pvals))))  +xlim(-3,3)+
  ggtitle("Volcano Plot English") +
  xlab("log2 Fold Change") + 
  ylab("-log10 p-value") +
  #scale_y_continuous(limits = c(0,50)) +
  theme(legend.position = "none",
        plot.title = element_text(size = rel(1.5), hjust = 0.5),
        axis.title = element_text(size = rel(1.25)))  

ggplotly(k, tooltip="text")



achieve <- achieve %>% 
  rowwise %>%
  mutate(
    pvals = prop.test(x=c(cpm,opm),n=c(ctm,otm), alternative="two.sided")$p.value
  ) %>%
  mutate(
    Fold.Change = log2((cpm/ctm)/(opm/otm))
  )

achieve$threshold <- achieve$pvals < 0.05
k <- ggplot(achieve) +
  geom_point(aes(x=Fold.Change, y=-log10(pvals), colour=threshold, text=sprintf("%s<br>Fold Change: %s <br> P-Value: %s", School.Name, Fold.Change, -log10(pvals))))  +xlim(-3,3)+
  ggtitle("Volcano Plot Math") +
  xlab("log2 Fold Change") + 
  ylab("-log10 p-value") +
  #scale_y_continuous(limits = c(0,50)) +
  theme(legend.position = "none",
        plot.title = element_text(size = rel(1.5), hjust = 0.5),
        axis.title = element_text(size = rel(1.25)))  

ggplotly(k, tooltip="text")




achieve <- achieve %>% 
  rowwise %>%
  mutate(
    pvals = prop.test(x=c(cps,ops),n=c(cts,ots), alternative="two.sided")$p.value
  ) %>%
  mutate(
    Fold.Change = log2((cps/cts)/(ops/ots))
  )

achieve$threshold <- achieve$pvals < 0.05
k <- ggplot(achieve) +
  geom_point(aes(x=Fold.Change, y=-log10(pvals), colour=threshold, text=sprintf("%s<br>Fold Change: %s <br> P-Value: %s", School.Name, Fold.Change, -log10(pvals))))  +xlim(-3,3)+
  ggtitle("Volcano Plot Social Studies") +
  xlab("log2 Fold Change") + 
  ylab("-log10 p-value") +
  #scale_y_continuous(limits = c(0,50)) +
  theme(legend.position = "none",
        plot.title = element_text(size = rel(1.5), hjust = 0.5),
        axis.title = element_text(size = rel(1.25)))  

ggplotly(k, tooltip="text")




achieve <- achieve %>% 
  rowwise %>%
  mutate(
    pvals = prop.test(x=c(cpsc,opsc),n=c(ctsc,otsc), alternative="two.sided")$p.value
  ) %>%
  mutate(
    Fold.Change = log2((cpsc/ctsc)/(opsc/otsc))
  )

achieve$threshold <- achieve$pvals < 0.05
k <- ggplot(achieve) +
  geom_point(aes(x=Fold.Change, y=-log10(pvals), colour=threshold, text=sprintf("%s<br>Fold Change: %s <br> P-Value: %s", School.Name, Fold.Change, -log10(pvals))))  +xlim(-3,3)+
  ggtitle("Volcano Plot Science") +
  xlab("log2 Fold Change") + 
  ylab("-log10 p-value") +
  #scale_y_continuous(limits = c(0,50)) +
  theme(legend.position = "none",
        plot.title = element_text(size = rel(1.5), hjust = 0.5),
        axis.title = element_text(size = rel(1.25)))  

ggplotly(k, tooltip="text")


