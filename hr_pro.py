from datetime import datetime
class Employee:
   #Employee class here
   def __init__(self,name ,age,salary ,year):
	   self.name=name
	   self.age=age
	   self.salary=salary
	   self.employment_year=year
   def get_working_years(self):
	   today = datetime.today()
	   today=today.year
	   return today - self.employment_year

   def __str__(self):
	   return "Name:%s , Age: %s ,Salary:%d,Working Years: %d" % (self.name, self.age, int(self.salary), self.get_working_years())

#listem=[]

#Name: shosho, Age: 24, Salary: 666, Working Years: 1



class Manager(Employee):
	#Manager class here
	def __init__(self,name ,age,salary ,year,bonus_percentage):
		Employee.__init__(self,name ,age,salary ,year)
		self.bonus_percentage=bonus_percentage
	def __str__(self):
		return "Name:%s , Age: %s ,Salary:%d,Working Years: %d ,bonus: %d" % (self.name, self.age,int(self.salary), self.get_working_years(), self.get_bonus())

#super().__str__()+ f'



	def get_working_years( self):
		today = datetime.today()
		today=today.year
		return today - self.employment_year
	def get_bonus(self):
		return self.bonus_percentage * self.salary

def main():
	# main code here

				print ("Welcome to HR Pro 2019")
				print("Options:")
				print("1. Show Employees")
				print("2. Show Managers")
				print("3. Add An Employee")
				print("4. Add A Manager")
				print("5. Exit")
				n=input("What would you like to do? ")
				print("-----------------")
				listem=[]
				listm=[]
				while n!="5":
					if n=="1" :
						print("Employees")
						print(" ")
						for i in listem:
							print (i.__str__())
					   #p = Person('Pankaj', 34)

				#print(p.__repr__())
					elif n=="2" :
						#for i in listm:
						print("Managers")
						print(" ")
						for i in listm:
							print (i.__str__())

					elif n=="3":
						name=input("name")
						age=input("Age:")# 24
						salary=input("Salary:") #666
						year=int(input("Employement year:"))# 2018
						obj1=Employee(name ,age,salary ,year)
						listem.append(obj1)
						#print(listem)
						print("Employee added succesfully")
					elif n=="4" :
						name=input("name")
						age=input("Age:")# 24
						salary=int(input("Salary:")) #666
						year=int(input("Employement year:"))# 2018
						bonus=float(input("Bonus Percentage:"))
						obj1=Manager(name ,age,salary ,year,bonus)
						listm.append(obj1)
						print("Manager added succesfully")
					#elif n=="5":
					print ("Welcome to HR Pro 2019")
					print("Options:")
					print("1. Show Employees")
					print("2. Show Managers")
					print("3. Add An Employee")
					print("4. Add A Manager")
					print("5. Exit")
					n=input("What would you like to do? ")
					print ("-----------------")



	#listem=[]
	#listm=[]


if __name__ == '__main__':
	main()
