# read file content into orders list
orders = []
with open("orders.txt") as f:
    for line in f:
        orders.append(line.strip())


# process every other order in orders list
for i in range(0, len(orders), 2):
    print(orders[i])


# eacher order in csv file has columns, id, title, date, amount, and customer id, read to list
# read file content into orders list


