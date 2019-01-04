pro = 0

p = ppois(q = 99, lambda = 30, lower.tail = (FALSE))
pro = pro + p


print(pro)


rock = dbinom(16, 30, 0.76)
sissor = dbinom(16, 30, 0.32)
paper = dbinom(16, 30, 0.66)

print(rock)
print(sissor)
print(paper)
