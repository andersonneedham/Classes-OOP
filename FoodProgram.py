import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

customers = {
    570: {
        "customer_id": 570,
        "Name": "Danni Sellyar",
        "address": "97 Mitchell Way Hewitt Texas 76712",
        "email": "dsellyarft@gmpg.org",
        "phone": "254-555-9362",
        "member_status": False,
    },
    569: {
        "customer_id": 569,
        "Name": "Aubree Himsworth",
        "address": "1172 Moulton Hill Waco Texas 76710",
        "email": "ahimsworthfs@list-manage.com",
        "phone": "254-555-2273",
        "member_status": True,
    },
}

for cust_id, customer in customers.items():
    order_total = 0
    print(f"Customer Name: {customer['Name']}")
    print(f"Phone Number: {customer['phone']}")

    # loop thru the order
    for transaction_id, transaction in dict.items():
        if customer["customer_id"] == transaction[3]:
            if customer["member_status"]:
                order_total += round(transaction[2] * 0.8, 2)
                print(
                    f"Order Item: {transaction[1]}  Price: ${round(transaction[2], 2):.2f}"
                )
            else:
                order_total += transaction[2]
                print(
                    f"Order Item: {transaction[1]}  Price: ${round(transaction[2], 2):.2f}"
                )
    if customer["member_status"]:
        order_total -= order_total * 0.2
        print(f"Total Cost: ${order_total:.2f}")
        print(f"Member Discount: ${order_total * 0.2:.2f}")
        print(f"Total Cost after discount: ${order_total - (order_total * 0.2):.2f}")
    else:
        print(f"Total Cost: ${order_total:.2f}")
    print("")
