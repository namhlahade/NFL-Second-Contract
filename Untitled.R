quarterbackStats <- read.csv("/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/relevantMetrics.csv")
quarterbackStats
summary(quarterbackStats)
head(quarterbackStats)
plot(quarterbackStats)
#Splitting the data into training and test data
set.seed(2)
install.packages('caTools')
library(caTools)
split <- sample.split(quarterbackStats, SplitRatio=0.5)
split
train <- subset(quarterbackStats, split="TRUE")
test <- subset(quarterbackStats, split="FALSE")
train
