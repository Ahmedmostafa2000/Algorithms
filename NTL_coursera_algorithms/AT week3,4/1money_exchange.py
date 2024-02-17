money = int(input())
coins = 0
coins += money//10
money = money%10

coins += money//5
money = money%5
coins += money
print(coins)