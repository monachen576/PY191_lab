# '''
# Activity 1
for i in range(10): 
    print(i, end=' ') if i%2==1 else None


print("\n")

# Activity 2
exchange_rate_usd_eur = 0.92
countries = ["UK", "Italy", "Spain"]
print(f"The exchange rate for {countries[0]} is {exchange_rate_usd_eur}.")
# incomplete i dont understand the instructions :(

print()


# Activity 3
for i in range(1, 26): 
    print(i, end=' ')
    if (i % 4 == 0): print("Quack", end='')
    if (i % 6 == 0): print("Moo", end='')
    print()

print()
# '''
# Activity 4
def factorial(n):
    if (n==1): return 1
    return n * factorial(n-1)
print(factorial(int(input())))