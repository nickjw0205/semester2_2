smoke <- c(15,5,7,13)
class <- matrix(smoke, nrow = 2, ncol = 2)

rownames(class) <- c("drink", "non-drink")
colnames(class) <- c("smoke", "non-smoke")

sum_of_row <- c(sum(class[1,]), sum(class[2,]))
sum_of_column <- c(sum(class[,1]), sum(class[,2]), sum(sum_of_row))

class <- cbind(class, sum_of_row)
class <- rbind(class, sum_of_column)
print(class)
