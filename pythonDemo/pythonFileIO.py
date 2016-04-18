import Employee as e
#write file
#fo=open('C:\Users\jzhang\Desktop\PSA\sest.csv','wb')
#fo.write("Name;Sex;Salary\n")
#fo.write("Jianli;Male;100k\n")
#fo.write("Jialin;Female;70k\n")
#read file

fo=open('C:\Users\jzhang\Desktop\PSA\sest.csv','r+')
str = fo.readline()

fo.close();
#loop read file
fo=open('C:\Users\jzhang\Desktop\PSA\sest.csv','r+')
listEmploye=[]

for line in fo:
    instance=line.split(';')
    employee=e.Employee(instance[0],instance[1],instance[2])
    listEmploye.append(employee)
print('end of the loop1')
print(e.Employee.empCount)

for em in listEmploye:
    fo.write(em.displayEmployee())

print('end of the loop2')
#Use Case Employee
#emp1 = e.Employee("Zara","Male",2000)
#emp1.displayEmployee()