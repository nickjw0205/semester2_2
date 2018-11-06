library(MASS)
str(Cars93)

v <- c(Cars93$Price)

mean <- mean(v)
print(mean)

sum <- sum(v)
print(sum)

sorted <- sort(v)
print(sorted)

