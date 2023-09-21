#Simple Python Program

#by Jabonillo and Lumanas

#Personal Details
Full_name = input("Enter your Full Name: ")
Id_number = input("Enter your ID number: ")
Course = input("Enter your Course: ")
Section = input("Enter your Section: ")

#Grades
Fq = eval(input("Enter your First Quarter Grade: "))
Sq = eval(input("Enter your Second Quarter Grade: "))
Tq = eval(input("Enter your Third Quarter Grade: "))
Fourthq = eval(input("Enter your Fourth Quarter Grade: "))

#formula
average = ((Fq + Sq + Tq + Fourthq) /4)

#disp
print("\n", Full_name, "\n", Id_number, "\n", Course, "\n", Section, "\n")
print("Your Average Grade is : " + str(average))
