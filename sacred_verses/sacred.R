
library(data.table)
library(sacred)
data(king_james_version)
b <- as.data.table(king_james_version)
fwrite(b, 'sacred/sacred.csv.gz')
