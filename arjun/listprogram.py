# 1. Input entry
# 2. Name total details student
# 3. Check pass fail subject : name
# 4. Total marks student name : marks

Student_db = {} #creating dictionary of student database

print(" Hi Welcome to Student Database Please enter your valid options in numeric value between 1 -4  ")


print(  "\n1 Input Student Information\n" 
          "2. Retrive Details for Student ( Search by Name) \n" 
          "3. Check Student Pass/ Fail ( Search by Subject Name) \n" 
          "4. Total Marks of a Student ( Search by Marks")

opt =int(input(" You Choose : "  ))
  
if opt == 1 :  
    
    name = input( "Enter name of Student :  ")

    classs = int(input("Enter Class :  "))

    age = int(input("Enter age of Student :  "))

    rollnumber = int(input("Enter Roll Number :  "))

    subjects = str(input("Enter Subject Names (comma-seperated) : ")).split(",")

    marks = {}

    for subject in subjects :
        subject = subject.strip()
        marks[subject]= int(input(f"Enter Marks for {subject} :  "))

    Student_db = { 
     
    "name" : name,
    "class": classs,
    "rollnumber" : rollnumber,
    "age"  : age,
    "subjects" : subjects,
    "marks" : marks
 }

    Res = input("Press Y to print the above table else input N : ")

    if Res == "Y" or Res =="y" :

     print(Student_db)

    elif Res == "N" or Res == "n":

     print("No problem , Student added Succesfully")

    

 

#elif opt == 2 :

#Search by Name

 Student_name = input("Enter Student Name to Find the Student :    ")

if Student_name == Student_db["name"]:
  


#     break


# elif opt == 3 :
#     break


# elif opt == 4 :
#     break


l=[] #list
v = input("value comma sepearated") 
l = v.split(',')


d={}

for i in range(n)

key = input("key : ")

d[key] = Value 

print d 