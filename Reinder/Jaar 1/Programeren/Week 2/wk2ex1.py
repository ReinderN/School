#Opdrachten met numers in lijsten.

e = [2, 7, 1]
pi = [3, 1, 4, 1, 5, 9]

answer0 = e[0:2] + pi[-2:]
print(answer0)

answer1 = e[1:3]
print(answer1)

answer2 = pi[1:2] + pi[3:4] + e[0:1]
print(answer2)

answer3 = pi[1:]
print(answer3)

answer4 = e[-1:] + e[0:1] + pi[0:1] + pi[2:3] + pi[4:5]
print(answer4)

#Opdracht met strings.

h = "hanze"
s = "hogeschool"
g = "groningen"

answer5 = s[0:2] + g[4]
print(answer5)

answer6 = s[4:8] + g[-2:] + g[-2:]
print(answer6)

answer7 = h[1:5] + s[1:4] + s[-6:]
print(answer7)

answer8 = 2*(g[0] + g[3] + h[1]) + 5*(h[0:2])
print(answer8)

answer9 = s[-1:] + s[3:0:-1] + g[3:1:-1] + s[3:0:-1]
print(answer9)

answer10 = s[-1:] + s[3] + 2*s[2] +g[4:7] + s[4]
print(answer10)
