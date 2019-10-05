library(ggplot2)

clusters<- read.csv(file="clusters.csv", header=TRUE, sep=",")

p<-c()
for (row in 1:nrow(clusters)) {
    p<-c(p,prop.test(x=c(clusters[row,"Charter.Count"],clusters[row,"Other.Count"]),n=c(clusters[row,"Charter.Total"],clusters[row,"Other.Total"]))$p.value)
}
qplot(p,binwidth=0.05)
