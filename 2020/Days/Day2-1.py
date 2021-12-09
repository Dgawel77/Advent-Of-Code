total = 0
while True:
    m = input().split()
    if m == []:
        break
    m[0] = m[0].split("-")
    value1 = m[2][int(m[0][0])-1]
    value2 = m[2][int(m[0][1])-1]
    if (m[1][0] == value1) != (m[1][0] == value2):
        total += 1
print(total)
