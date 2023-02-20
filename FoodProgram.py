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

order_total = 0

customer1 = {
    "customer_id": 570,
    "Name": "Danni Sellyar",
    "address": "97 Mitchell Way Hewitt Texas 76712",
    "email": "dsellyarft@gmpg.org",
    "phone": "254-555-9362",
    "member_status": False,
}

customer2 = {
    "customer_id": 569,
    "Name": "Aubree Himsworth",
    "address": "1172 Moulton Hill Waco Texas 76710",
    "email": "ahimsworthfs@list-manage.com",
    "phone": "254-555-2273",
    "member_status": True,
}
