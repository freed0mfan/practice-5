amount = []
for i in range(3):
    amount.append(int(input(f'{i+1} день: ')))

if amount.count(amount[0]) > 1:
    print(amount.count(amount[0]))
elif amount.count(amount[1]) > 1:
    print(amount.count(amount[1]))
else:
    print(0)
