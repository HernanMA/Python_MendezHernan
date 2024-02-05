def calculate_coins(amount):
    coins_10 = amount // 10
    amount %= 10
    coins_5 = amount // 5
    amount %= 5
    coins_1 = amount

    return coins_1, coins_5, coins_10

while True:
    try:
        entered_value = int(input(""))
        if entered_value > 0 and entered_value < 1000:
            break
        else:
            print("Number invalid")
    except ValueError:
        print("")

print(entered_value)
result = calculate_coins(entered_value)
    
print("")
print(f"Input = {entered_value}")
print("")
print("            $1   $5   $10")
print(f"Output= {entered_value} = {result[0]} + {result[1]} + {result[2]}")