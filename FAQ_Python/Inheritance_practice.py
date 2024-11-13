class employee :
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
    def display_Details(self):
        print("Your Name is :",self.name,"and Your Employee id is :",self.employee_id)
#end of 1st class
class FullTimeEmployee(employee) :
    def __init__(self,salary):
        self.salary = salary
        print("Your salary is :",self.salary)
#end of 2nd class
class PartTimeEmployee(employee) :
    def __init__(self,Hours_count) :
        self.Hours_count = Hours_count
    def display_count(self) :
        print("Total no of working hours : ",self.Hours_count)
# end of 3rd class

#object of employee
amitPartTime = employee("amit","12340",)
amitPartTime.display_Details()
amitcount = PartTimeEmployee("45")
amitcount.display_count()
#another object of employee
akashFullTime = employee("akash","12345")
akashFullTime.display_Details()
akashsalary = FullTimeEmployee("5000000 INR")