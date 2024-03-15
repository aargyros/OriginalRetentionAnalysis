import numpy as np  
import pandas as pd
pd.set_option('html', False)

#Define SEQ object class
class SEQ:
    def __init__(self, grade, course, classcode, teacher, session, year, seq):
        self.grade = grade
        self.course = course
        self.classcode = classcode
        self.teacher = teacher
        self.session = session
        self.year = year
        self.seq = seq

#Calculates the SEQ based on a list of criteria. If no data sent to routine returns -1.
def SEQcalc(lst,crit):
    n = []
    seq = -1
    if len(lst)==0:
        pass
    elif len(crit)==0:
        seq = 0        
        for i in lst:
            seq += i.seq
        seq = seq/len(lst)          
    elif True:
        crv = crit.pop()
        cr = crit.pop()
        for i in lst:
            if eval('i.'+cr) == crv:
                n.append(i)
        seq = SEQcalc(n,crit)
    return seq


#Creates the criteria for an SEQ query for a particular enrollment (i.e. that class) by using grade, course, classcode, session and year
def seqenr(enr):
    g = int(enr.classcode[:2])    #Takes the grade from the SIS class code, forst two digits, e.g. 11CHEM-EW11    

 #   if len(g)==7:                                                                   
 #       grade = int(g[-2::]) 
 #   elif True:
 #       grade = int(g[-1])   
    
    c = enr.course  #converts course from SIS forma to SEQ DB format; Sciences are the same. 
    if c=='Year 11 English ADV':                  #English is fine for 7-10, Y11 and 12 SIS is (ADV), SEQ DB is (Advanced)
        c = 'Year 11 English Advanced'
    elif c=='Year 12 English ADV':
        c = 'Year 12 English Advanced'
    elif c=='Year 7 Mathematics':               #Maths: SIS (Mathematics/ACC) -> SEQ DB (Maths/Accelerated)
        c = 'Year 7 Maths'
    elif c=='Year 8 Mathematics':
        c = 'Year 8 Maths'
    elif c=='Year 9 Mathematics':
        c = 'Year 9 Maths'
    elif c=='Year 9 Mathematics ACC':
        c = 'Year 9 Maths Accelerated'
    elif c=='Year 10 Mathematics':
        c = 'Year 10 Maths'
    elif c=='Year 10 Mathematics ACC':
        c = 'Year 10 Maths Accelerated'
    elif c=='Year 11 Mathematics ADV':
        c = 'Year 11 Maths'
    elif c=='Year 11 Mathematics Ext 1':
        c = 'Year 11 Maths Extension 1'
    elif c=='Year 11 Mathematics Ext 1 ACC':
        c = 'Year 11 Maths Extension 1 ACC'
    elif c=='Year 12 Mathematics ADV':
        c = 'Year 12 Maths'
    elif c=='Year 12 Mathematics Ext 1':
        c = 'Year 12 Maths Extension 1'
    elif c=='Year 12 Mathematics Ext 2':
        c = 'Year 12 Maths Extension 2'
    
    cc = enr.classcode[-4::]       #Classcode: SIS (Y12PHYS-SA11) -> SEQ DB (SA11)
    
#    tchr = enr.teacher[3::]         #Remove title from SIS name
#    if tchr=='Tom Godfrey':
#        tchr = 'Thomas Godfrey'
#    elif tchr=='Chris Rudge':
#        tchr = 'Christopher Rudge'
#    elif tchr=='Pat Rockett':
#        tchr = 'Patricia Rockett'
    
    ssn = enr.session
    
    yr = int(enr.year)
    
    #return ['classcode', cc, 'session', ssn, 'year', yr, 'grade', g, 'course', c, 'teacher', tchr]
    return ['classcode', cc, 'session', ssn, 'year', yr, 'grade', g, 'course', c]
    
    
    
    