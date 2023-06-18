def power_mod(x, power, mod):
    result = 1
    y = x
    
    while(power > 0):
        if(power % 2 == 1):
            result = (result * y) % mod
        
        y = (y*y) % mod
        power = power >> 1
    
    return result

def get_remainder(exponent, mod):
    remainder = 0
    
    for i in range(len(exponent)):
        remainder = (remainder * 10 + int(exponent[i])) % mod
    
    return remainder

a = int(input())
exponent = input()

MOD = 10**9 + 7
net_exponent = get_remainder(exponent, MOD - 1)

answer = power_mod(a, net_exponent, MOD)
print(answer)
