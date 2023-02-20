class Customer:
    def __init__(self, customerid, name, address, email, phone, member_status):
        self.__customerid = customerid
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__member_status = member_status

    def get_customerid(self):
        return self.customerid

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_member_status(self):
        return self.member_status


class Transaction:
    def __init__(self, data, item, name, cost, customerid):
        self.__data = data
        self.__item = item
        self.__name = name
        self.__cost = cost
        self.__customerid = customerid

    def get_date(self):
        return self.date

    def get_item_name(self):
        return self.item

    def get_cost(self):
        return self.name

    def get_customer_id(self):
        return self.customerid
