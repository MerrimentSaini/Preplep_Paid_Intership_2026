# ''' Create a student profile program .
#       Take user input for name, age, marks, email and phone number.
#         Print the formatted output.'''
#
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# marks = int(input("Enter your marks: "))
# email = input("Enter your email: ")
# phone = input("Enter your phone number: ")
#
# # ---------  Print all the Details of the Student Profile ---------- ...!
# print()
# print("*"*40)
# print(f'Name of the Student is: {name}')
# print(f"Age is: {age}")
# print("Obtained marks by the student is: ",marks)
# print(f"Email is: {email}")
# print(f"Phone number is: {phone}")
# print("*"*40)

#List creation..
# l = [1,'a','False',89.8]
# print('List elements are: ',l)
# print(l[-2])
# print('Length of the list is: ',len(l))
# print(l[1::2])
# print(l[-2::-1])
# l2 = [1,12,43,3]
# l2.append(90)
# print(l2)
# l2.insert(2,100)
# print(l2)
# l2.pop()
# print(l2)
# l2[3] = 44 #Update the existing list.
# print(l2)
# l2.remove(44) #Remove any specific value/data/element
# print(l2)
# l2.sort() #Sorting the list.
# print(l2)
# l2.reverse()
# print(l2)


# Dictionary..!
# student = {'Name': 'Avi',
#      'Age': 20,
#      'Course': 'BCA',
#      'ClgName': 'Ims'}
#
# print(student.items())
# student2= student
# student2['Name']='Harri'
# print(student)
#
# print(student2)

#Day-5 Dictionary Basics Practice Assignment..!

#------ Create a student directory with name,email,phone, course, and marks -----------.
# student = {"Name" : "AviSaini",
#            "Email" : "merrimentsaini@gmail.com",
#            "PhoneNo" : "7351****22",
#            "Course" : "BCA-2nd Year",
#            "Marks" : 456}
#
# print(student)
#
# # --------- UPDATE MARKS ----------- .
# student.update({"Marks" : 550})
# print("\nAfter updating the student dictionary marks: ")
# print(student)
#
# # --------- COPY DICTIONARY & MODIFY COPIED DATA ---------- .
# student2 = student.copy()
# print("\nAfter copying the student dictionary to student2: \n",student2)
#
# #-------- UPDATE THE STUDENT NAME ----------- .
# student2.update({"Name" : "Harsh"})
# print("\nAfter updating the student dictionary key-name: \n",student2)
#
# print("\nI observed the difference between the oringinal and copied dictionary is that only the"
#       "copied dictionary impacted throught the dictionary method and rest of the dictionary remains the same..!")
#






# ------------- INTERNSHIP ~ WEEK-2 (DAY-7) ---------------- .
# Dictionary Comprehension..!
# sqrt = {x: x*x for x in range(1,6)
#         if x >=3}
# print("\nSquare of the number of 1-5 through dictionary comprehension: \n", sqrt)
#
#
# # First 20 even numbers..!
# EvenNmbr = {x: x for x in range(1,21)
#             if x%2 == 0}
# print("\nEven Numbers are: \n",EvenNmbr)
#
#
# # Sum of the first 10-Natural Numbers..!
# total = 0
# nmbrs  = {x : x for x in range(1,11)}
# total = sum(nmbrs.values())
# print("\nDictionary: ",nmbrs)
# print("\nSum of first 10-natural nmbrs is: ",total)
#
#
# # Creating Dictionaries from the Lists..!
# students = ['Merriment','Monarch','Mayank','Mradul']
# stu_Dict = {name: len(name) for name in students}
# print("\nStudents Name are: \n",stu_Dict)
#
#
# # Create the dictionary through the list names and marks..!
# names = ['Avi','Mayank','Harsh','Mradul']
# marks = [34,56,78,37]
# stu_Marks = {names[i]:marks[i] for i in range (len(names))}
# print("\nStudents Name and their Obtained marks are: \n",stu_Marks)
#
# # Filtering Dictionary Data..!
# marks = {'Avi':34,'Mayank':56,'Harsh':78,'Mradull':37}
# passed_students = {
#     name:mark
#     for name,mark in marks.items()
#     if mark >= 50
# }
# print("\nPassed Students are: \n",passed_students)
#
# # Conver Marks into Percentage..!
# percentage = {
#     name:str(mark) + "%"
#     for name,mark in marks.items()
# }
# print("\nStudent marks in percentage are: \n",percentage)



# ------------------ Functions -------------------- .
def calculate_percentage(marks):
    total = sum(marks)
    percentage = total/len(marks)
    return percentage

list1 = [55,67,87,34]
a = calculate_percentage(list1)
print(a)



#MODULE/TOPIC: Lambda Function..!
#Syntax: variable_Name = lambda keyword arguments : expression

sqrt = lambda nmbr : nmbr*nmbr
print("\nSquare through lambda function: ",sqrt(5))

#i). Lambda with map()..!
#Syntax: map(function, iterable)

nmbrs = [1,2,3,4,5]
square = list(map(lambda x: x**2 , nmbrs))
print("\nSquare of the mentioned list through map() function are: ",square)

#ii). Convert marks into percentage..!
mark = [80,90,45,65]
percentage = list(map(lambda x: x/100*100, mark))
print("\nPercentage is: ",percentage)

#iii). Lambda with filter()..!
# Syntax: filter(function,iterable)

evens = list(filter(lambda x: x%2 == 0, mark))
print("\nEven marks are: ",evens)
passed = list(filter(lambda x: x >= 48, mark))
print("\nMarks greater than 48 are: ",passed)

#iv). Lambda with sorted()..!

sorted_marks = sorted(mark, key = lambda mark: mark)
print("\n",sorted_marks)


# ---------- Error Handling -------------- ..!

try:
    a = int(input("\nEnter an int value: "))
    #print("Try and Except")

except ValueError:
    print("\nIt supports only integer value.")


finally: #It'll run always.
    print("It'll run always. Either try is true or not.!")

