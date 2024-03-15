import numpy as np  
import pandas as pd
pd.set_option('html', False)

#Define enrollment class
class Enrollment:
    def __init__(self, name, email, school, grade, course, classcode, teacher, session, year, alsession, seq):
        self.name = name
        self.email = email
        self.school = school
        self.grade = grade
        self.course = course
        self.classcode = classcode
        self.teacher = teacher
        self.session = session
        self.year = year
        self.alsession = alsession
        self.seq = seq

#A function that converts a list of enrollment objects into a readable list (data frame)
def enr2lst(lst):
    h = ['Name', 'Email', 'School', 'Grade', 'Course', 'Classcode', 'Teacher', 'Session', 'Year', 'Alsession', 'SEQ'];
    d = []    
    for a in lst:
        d.append([a.name, a.email, a.school, a.grade, a.course, a.classcode, a.teacher, a.session, a.year, a.alsession, a.seq])
        df = pd.DataFrame(d, columns=h)
    return(df)

#Checks if the name is the same on two enrollments
def samename(enr1, enr2):
    same = False
    if enr1.name == enr2.name:
        same = True
    return same

#Checks if the email is the same on two enrollments
def sameemail(enr1, enr2):
    same = False
    if enr1.email == enr2.email:
        same = True
    return same   

#Returns the number of enrollments in lst that satisfy criteria crit
def ct(lst,crit):
    n = len(select(lst,crit))
    return n

#A function that reutrns a list containing enrollments that satisfy given criteria
#It searches through a list of enrollment objects (lst) and applies a list of criteria (crit)
#The criteria is in pairs of (criterion, value)
#It applies the criteria one at a time recursively and cuts down the list of objects
def select(lst,crit):
    n = []    
    if len(lst)==0:          #list is empty 
        pass
    elif len(crit)==0:       #no cireteria
        n = lst
    elif True:               #creates shorter list (lst2) that satisfied the last criterion in crit
        crv = crit.pop()
        cr = crit.pop()
        for i in lst:
            if eval('i.'+cr) == crv:
                n.append(i)  
        n = select(n,crit)       #call same function sending reduced list and reduced list of criteria
    return n

#A fucntion that applies two orthogonal criteria to a list, and generates two sublists
#It then calculates the overlap between the two lists
#Uses email address as the basis for deciding if the studnent in one enrollment is the same as the other
def compare(lst,crit1,crit2):
    lst1 = select(lst,crit1)
    n1 = len(lst1)              #list satisfying criterion 1
    lst2 = select(lst,crit2)
    n2 = len(lst2)              #list satisfying criterion 2
    lst1b = []                  #lst1b contains enrollments satisfying criterion 1, of students that satisfy criterion 2
    lst2b = []                  #lst2b contains enrollments satisfying criterion 2, of students that satisfy criterion 1
    for i in lst1:
        for j in lst2: 
            if i.email == j.email:
                lst1b.append(i)
                lst2b.append(j)  #NEED TO CHECK IF I CAN REMOVE ENROLLMENTS FROM THE LIST IF THEY MATCH 
    n1b = len(lst1b)
    n2b = len(lst2b)
    return [lst1b,n1b,lst2b,n2b]

