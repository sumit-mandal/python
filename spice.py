from abc import ABCMeta,abstractmethod

class Customer(metaclass=ABCMeta):
    def __init__(self,customer_name): #__init__ is constructor
        self.__customer_name=customer_name #customer name isiliye likha qki ye is class k baahir b call hoga
        self.bill_amount=None
        self.bill_id=None #everything inside constructor is instnce variable

    def get_customer_name(self):
        return self.__customer_name

    @abstractmethod
    def calculate_bill_amount(self):
        pass

class OccasionalCustomer(Customer):
    __counter=1000
    def __init__(self,customer_name,distance_in_kms):
        super().__init__(customer_name)
        OccasionalCustomer.__counter+=1
        self.bill_id="O"+str(OccasionalCustomer.__counter)
        self.__distance_in_kms=distance_in_kms

    def get_distance_in_kms(self):
        return self.__distance_in_kms

    def validate_distance_in_kms(self):
        if self.__distance_in_kms>=1 and self.__distance_in_kms<=5:
            return True
        return False

    def calculate_bill_amount(self):
        if self.validate_distance_in_kms():
            bill_amount=50
            if self.__distance_in_kms<=2:
                bill_amount+=self.__distance_in_kms*5
            elif self.__distance_in_kms<=5 and self.__distance_in_kms>2:
                bill_amount+=(self.__distance_in_kms)*7.5
            self.bill_amount=bill_amount
            return self.bill_amount
        else:
            self.bill_amount=-1
            return self.bill_amount

class RegularCustomer(Customer):
    __counter=100
    def __init__(self,customer_name,no_of_tiffin):
        super().__init__(customer_name)
        RegularCustomer.__counter+=1
        self.bill_id="R"+str(RegularCustomer.__counter)
        self.__no_of_tiffin=no_of_tiffin

    def get_no_of_tiffin(self):
        return self.__no_of_tiffin

    def validate_no_of_tiffin(self):
        if self.__no_of_tiffin>=1 and self.__no_of_tiffin<=7:
            return True
        return False

    def calculate_bill_amount(self):
        if self.validate_no_of_tiffin():
            self.bill_amount=50*7*self.__no_of_tiffin
            return self.bill_amount
        else:
            self.bill_amount=-1
            return self.bill_amount



a=RegularCustomer('sum',2)
a.calculate_bill_amount()
a.get_customer_name()
b=OccasionalCustomer('bhau',3)
b.get_customer_name()
b.get_distance_in_kms()
b.calculate_bill_amount()
