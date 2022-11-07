n = int(input())

memo = {}
mod = 10 ** 9 + 7


def memo_combination(number1, number2):
    return memo_factorial(number2) // memo_factorial(number1)


def memo_factorial(number):
    if number == 1:
        return 1
    if number in memo:
        return memo[number]
    result = number * memo_factorial(number - 1) % mod
    memo[number] = result
    return result


reversed_result = [memo_factorial(n)]
for i in range(1, n):
    n - i
    # reversed_result[i - 1]

for answer in reversed(reversed_result):
    print(answer)
