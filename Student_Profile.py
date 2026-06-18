''' Create a student profile program .
      Take user input for name, age, marks, email and phone number.
        Print the formatted output.'''

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
email = input("Enter your email: ")
phone = input("Enter your phone number: ")

# ---------  Print all the Details of the Student Profile ---------- ...!
print()
print("*"*40)
print(f'Name of the Student is: {name}')
print(f"Age is: {age}")
print("Obtained marks by the student is: ",marks)
print(f"Email is: {email}")
print(f"Phone number is: {phone}")
print("*"*40)