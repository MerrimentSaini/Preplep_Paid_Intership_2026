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
student = {"Name" : "AviSaini",
           "Email" : "merrimentsaini@gmail.com",
           "PhoneNo" : "7351****22",
           "Course" : "BCA-2nd Year",
           "Marks" : 456}

print(student)

# --------- UPDATE MARKS ----------- .
student.update({"Marks" : 550})
print("\nAfter updating the student dictionary marks: ")
print(student)

# --------- COPY DICTIONARY & MODIFY COPIED DATA ---------- .
student2 = student.copy()
print("\nAfter copying the student dictionary to student2: \n",student2)

#-------- UPDATE THE STUDENT NAME ----------- .
student2.update({"Name" : "Harsh"})
print("\nAfter updating the student dictionary key-name: \n",student2)

print("\nI observed the difference between the oringinal and copied dictionary is that only the"
      "copied dictionary impacted throught the dictionary method and rest of the dictionary remains the same..!")


