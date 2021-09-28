e = [2, 7, 1]
pi = [3, 1, 4, 1, 5, 9]

answer0 = e[0:2] + pi[-2:]
print(answer0)

answer1 = e[1:2] + e[-1:]
print(answer1)

answer2 = e[-1:] + e[-1:] + e[:1]
print(answer2)

answer3 = pi[1:]
print(answer3)

answer4 = e[2:] + e[:-2] + pi[0:1] + pi[2:3] + pi[4:5]
print(answer4)

#---------------------------------------------------------

h = "hanze"
s = "hogeschool"
g = "groningen"

answer5 = s[0:2] + g[4]
print(answer5)

answer6 = s[4:8] + h[4] + h[2] + g[7:]
print(answer6)

answer7 = h[1:] + s[1:]
print(answer7)

answer8 = (s[2] + h[2] + h[1])*2 + 5*(h[0:2])
print(answer8)

answer9 = s[9] + s[3:0:-1] + h[2] + s[1:4:2] + g[0:3:2]
print(answer9)

answer10 = s[9] + s[3:1:-1] + s[2] + g[4:7] + s[4]
print(answer10)