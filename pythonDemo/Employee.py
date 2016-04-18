class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, sex, salary):
      self.name = name
      self.sex=sex
      self.salary = salary

      Employee.empCount += 1

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      return "Name : "+self.name+", Salary: "+self.salary


