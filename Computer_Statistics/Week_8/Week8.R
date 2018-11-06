Medicine <- c("A","A","A","A","A","B","B","B","B","B","C","C","C","C","C")
Effect <- c(0.62, 0.77, 0.33, 0.27, 0.84, 0.15, 0.13, 0.29, 0.18, 0.62, 0.72, 0.13, 0.09, 0.57, 0.44)
Problem <- c(0.11, 0.05, 0.16, 0.89, 0.77, 0.13, 0.77, 0.22, 0.10, 0.21, 0.33, 0.31, 0.42, 0.55, 0.66)

yak <- data.frame(Medicine,Effect, Problem)
write.csv(yak, "./Desktop/Hanyang/semester2_2/R/R_practice/Week_8/yak.csv")

data <- read.csv("./Desktop/Hanyang/semester2_2/R/R_practice/Week_8/yak.csv")

avg_effect <- tapply(data$Effect, data$Medicine, mean)
avg_problem <- tapply(data$Problem, data$Medicine, mean)
order <- sort(avg_effect,decreasing = TRUE)
order(avg_effect)
print(avg_effect)
print(avg_problem)
result <- avg_effect/avg_problem
result