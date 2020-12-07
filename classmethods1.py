#class method can only use instance variable of the class
#We can access it from any instance or class

class Employee:
    no_of_leaves = 8 #Instance variable

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"The name is {self.name}.salary is {self.salary} and role is {self.role}"

    @classmethod
    #hhere we only want toa access number of leaves and nothing else
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves


har = Employee("Harry",255,"Instructor")
roh = Employee("Rohan",455,"Student")

har.change_leaves(34)

print(har.no_of_leaves)
