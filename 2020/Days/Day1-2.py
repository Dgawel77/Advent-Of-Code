def solve(n1, n2, n3):
    if(n3 > k):
       return False
    if(numbers[n1] + numbers[n2] + numbers[n3] == 2020):
        print(numbers[n1] * numbers[n2] * numbers[n3])
        return True
    if(numbers[n1] + numbers[n2] + numbers[n3] > 2020):
        if(numbers[n1] + numbers[n2] > 2020):
            solve(n1+1, n2+2, n3+3)
        solve(n1, n2+1, n2+2)
    else:
        solve(n1, n2, n3+1)
    return True

numbers = []
k = 0
while True:
    try:
        m = int(input())
    except:
        break
    numbers.append(m)
    k += 1
numbers.sort()
print(solve(0, 1, 2))
