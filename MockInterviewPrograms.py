# ============== Top-20 Python Coding Programs for Mock Interview =================== .

# 1). ------------------- WAP to print the Fibonacci Series --------------- ..!
n = 10
a,b = 0,1
print("Fibonacci Series of ",n," numbers are: ")
for i in range(n):
    print(a,end=" ")
    a,b = b,a+b

# 2). -------------------- WAP to check Prime Number -------------------- ..!
num = 5
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print("\nNot a prime nmbr.!")

    else:
        print("\nPrime Nmbr.!")

else:
    print("\nNot a prime nmbr.!")


# 3). -------------  WAP to find factorial ---------------- ..!
fact = 1
for i in range(1,num+1):
    fact *= i
print(f"\nFactorial of {num} is: ",fact)



# 4). ------------- WAP to check palindrome --------------- ..!
txt = "madam"
if txt == txt[::-1]:
    print("\nPalindrome.!")
else:
    print("\nNot a palindrome.!")


# 5). ------------ Check even or odd nmbr ------------- ..!
n = 88
if n % 2 == 0:
    print("\nEven nmbr.!")

else:
    print("\nOdd nmbr.!")


#6. --------------- Reverse a String ---------------- ..!
string  = 'MerrimentSaini'
print("\nReverse of the string is: ",string[::-1])



#7. ---------------- Count Vowels ------------------ ..!
msg = 'university'
count = 0
for ch in msg.lower():
    if ch in 'aeiou':
        count += 1
print("\nTotal vowels are: ",count)

#8. ------------------ List Comprehension ~ Even Numbers ---------------- ..!
even = [x for x in range(1,101)
        if x % 2 == 0]
print("\nEven nmbrs from 1 to 100 are: ",even)



#9. ------------------- List Comprehension ~ Squares -------------------- ..!
sqrt = [x**2 for x in range(5)]
print("\n Square is: ",sqrt)


#10. ----------------- Nmbrs Divisible by 3 and 5 -------------------- ..!
rslt = [x for x in range(1,101)
        if x % 3 == 0 and x % 5 == 0]

print("\nNmbrs from 1-100 that are totally divisible by 3 and 5 : ",rslt)


#11). ----------------- Dictionary Comprehension ~ Student Pass/Fail Status -------------- ..!
marks = {
    'AviSaini' : 76,
    'MayankPrajapati' : 45,
    'HarshShah' : 54,
    'MradulSaxena' : 39,
    'VaibhavArya' : 40
}
rptCrd = {name : 'Pass' if mark > 40 else 'Fail'
          for name,mark in marks.items() }
print("\n",rptCrd)


#12). ------------------ Dictionary ~ Comprehension -------------------- ..!
squares = {x : x**2 for x in range(6)}
print("\nSquare is: ",squares)


#13). ----------------- Create Student Dictionary ---------------------- ..!
student = {
    "Name" : ['AviSaini',"HarshShah",'MayankPrajapati','VaibhavArya',"MradulSaxena"],
    "Marks" : [23,45,67,87,45],
    "ClgName":['imsuc','imsuc','imsuc','imsuc','imsuc']
}
print("\nStudent Details are: \n",student)


#14). ----------------- Function to Calculate Percentage(%) ---------------- ..!
def calc_percentage(totalMarks,obtainedMarks):
    return (obtainedMarks/totalMarks)*100

print("\nPercentage is: ",calc_percentage(600,456))


#15). ----------------- Function to Check Pass/Fail Status ----------------- ..!
def reslt(marks):
    if marks >= 45:
        return "Pass.!"
    return "Fail."
print("\n",reslt(47))