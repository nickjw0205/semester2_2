
data <- read.csv("/Users/seojiwon/Downloads/data.csv")
data

plot(data$weight, data$total, xlim = c(35,104), ylim = c(7000, 700000))

