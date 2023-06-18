n = int(input())
cnt = 0
for i in range(1, n+1):
    if i*i > n:
        break
    if n % i == 0:
        x = i
        y = n // i
        if (x+y) % 2 == 0:
            cnt += 1
print(cnt)
