class Customer:
    def __init__(self, customerid, name, address, email, phone, member_status):
        self.__customerid = customerid
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__member_status = member_status

    def get_attributes(self):
        attributes = [
            self.__customerid,
            self.__name,
            self.__address,
            self.__email,
            self.__phone,
            self.__member_status,
        ]
        for attribute in attributes:
            return attribute


class Transaction:
    def __init__(self, data, item, name, cost, customerid):
        self.__data = data
        self.__item = item
        self.__name = name
        self.__cost = cost
        self.__customerid = customerid

    def get_attributes(self):
        attributes = [
            self.__data,
            self.__item,
            self.__name,
            self.__cost,
            self.__customerid,
        ]
        for attribute in attributes:
            return attribute
