# ============== INTERNSHIP ~ WEEK-2 ================ .

# ---------- Day-6 ----------- .

# MODULE/TOPIC: List Comprehension..!

list = [i for i in range(1,100+1)]
print(list)

#i) Extract EvenNmbrs from the list..!
EvenNmbr = [i for i in list
            if i%2 == 0]
print("\nEvenNmbrs from the list are: \n",EvenNmbr)


#ii) Extract numbers divisible by 3 and 5.
Nmbrs = [i for i in list
         if i%3 == 0 and i%5 == 0]
print("\nNmbrs from the list divisible by 3 and 5 are: \n",Nmbrs)

#iii) Square of the existing list elements.
sqrt = [i*i for i in list]
print("\nSquares of the list elements are: \n",sqrt)



# ------------ Day-7 -------------- ..!

# MODULE/TOPIC: Dictionary Comprehension..!

#i). Create a dictionary of students_Name and marks..!
Stu_Names = ['AviSaini','Mayank Prajapati','Harsh Shah','Mradul Saxena','Vaibhav Arya']
Marks = [45,67,54,32,34]
dict = { Stu_Names[i] : Marks[i]  for i in range (len(Stu_Names)) }
print("\nStudents Name and their obtained Marks are:\n",dict)

#ii). Filter Students_Names who obtained more than 40 marks..!
Scored = {'AviSaini':45,'Mayank Prajapati':67,'Harsh Shah':54,'Mradul Saxena':32,'Vaibhav Arya':34}
stu_Names = {name:mark for name,mark in Scored.items()
            if mark > 40 }
print("\nStudents name who scored/obtained more than 40 marks are: \n",stu_Names)


#iii). Create a dictionary with student names and their pass/fail status..!
result = {name : "Pass" if mark >= 33 else "Fail"
          for name,mark in Scored.items() }
print("\nStudents Name and their results are: \n",result)



# ---------------- Day-8 ---------------- ..!

#MODULE/TOPIC: Functions..!

#i). Create a function to calculate percentage..!
def calc_prcntage(marks=(12,45,67,86,49)):
    total = sum(marks)
    percentage = total/len(marks)
    return percentage

# Give the marks(Parameter/Arguments) data..!
#m = [12,45,67,86,49]
# Call the calc_prcntage function..!
#print("\nTotal Percentage is: ",calc_prcntage(m))
print("\nTotal Percentage is: ",calc_prcntage())

#ii). Create a function to check pass/fail result..!
def result(marks):
    if marks >= 33:
        return "Congrats! You'r Pass."

    else:
        return "Fail Try Again!"

#m = int(input("\nEnter student obtained marks: "))
#Function calling..!
#print("\nYour result is: ",result(m))
m = 45
print("\n",result(m))

#iii). Create a function to validate mobile number..!
import re
def valid_Nmbr(phNo):
    pattern = r'^[6-9]\d{9}$'

    if re.match(pattern,phNo):
        return "Phone Number is Valid."

    else:
        return "Invalid Phone Number."

# Taking phnmbr from the user..!
phone_nmbr = (input("\nEnter your phone number: "))
#Funcion Calling..!
print(valid_Nmbr(phone_nmbr))


#iv). Create a function to calculate total marks..!
def total_Marks(mark=(12,45,67,86,49)):
    total = sum(mark)
    return total

#Function calling..!
print("\nTotal marks is: ",total_Marks())