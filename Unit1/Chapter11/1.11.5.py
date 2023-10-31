def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


num1 = 12
num2 = 14
result = gcd(num1, num2)
print(f"{num1} 和 {num2} 的最大公约数是 {result}")
# GPT写的
