library(MASS)
str(Cars93)

plot(Cars93$RPM,Cars93$Price)
cov(x = Cars93$RPM, y = Cars93$Price, use = "everything", method = ("pearson"))

t.test(Cars93$Price, alternative = c("less"), mu=19.2)

