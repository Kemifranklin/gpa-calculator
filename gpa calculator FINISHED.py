# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:58:16 2023

@author: kemi franklin
"""
"""
NAME:
    collectGrades
    
DESCRIPTION:
    This function accepts keyboard input of courses= codes and assosiated letter 
    grades The input is stored in a DICTIONARY with KEY= course code and 
    VALUE = course grade.
INPUT:
    None
        
OUTPUT:
    Dictionary contains entries such as:
    KEY   = course code
    VALUE = course letter grade
"""

def collectGrades( ) -> dict: #defines the return type
    #remeber use atleast 4 space indention
    gradeCollection = dict( )
    
    #ask student/user for input 
    print("We will collect your grades to begin calculations.")
    print("Please provide course number as a 6 -7 charater course identifier,")
    print(" in the form of IS3003 or ACC3414")
    print( )
    print("Please enter grades as 1 or 2 characters.")
    print( )
    
    #set a loop control
    
    another = 'yes'
    
    while( another == 'yes'):
        
        #accept input of course code 
        course = input("Please enter the course identifier:  ").strip( )
        
        #accept input of the letter grade 
        grade = input("Please enter the course LETTER GRADE:  ").strip( )
        
        #MIRROR the input back to the user 
        print("You recieved a letter grade of %s in course %s." %
              ( grade, course ))
        
        #add input to our dictionary
        gradeCollection[ course ] = grade
        
        #ask another student /user wishes to continue
    another = input( "Enter Yes to add another course.  " ).lower( )
    
    #end of iteration// course and grade input
    
    return gradeCollection 
#end Function collectGrades
         
def calculateQualityPts( grades : dict ) -> tuple:
            #begin with defing a lookup structure for assesing quality points
            
            
            qualityPts = {"A+" : 4.00,
                          "A"  : 4.00,
                          "A-" : 3.67,
                          
                          "B+" : 3.33,
                          "B"  : 3.00,
                          "B-" : 2.67,
                          
                          "C+" : 2.33,
                          "C"  : 2.00,
                          "C-" : 1.67,
                          
                          "D+" : 1.33,
                          "D"  : 1.00,
                          "D-" : 0.67,
                          
                          "F"  : 0.00
                          
                          #end of dictionary          
                }
            #traverse the recieved dictionary to accumulate credit hoours and 
             #  quality points.
             
            credits = 0
            points = 0.0
             
            for course, grade in grades.items():
                 # retrieving credit hours from course code
                 #could also write....hours= int(course[-1]).... the result is identical
                 hours = int( course [ len(course) -1])
                 credits += hours
                 #credits equal credit plus hours
                 
                 #retrive quality points for the grade 
                 quality = qualityPts[ grade ]
                 points += (quality * hours)
                 #end iteration
                 
                 # return the tuple containing sumed credits and quality points
                 return (credits, points)
                
             #end function
             
"""
This is a simple GPA calculator
Functional:
              1. For each class attempted collect the letter grade 
                    and course hours
              2. For each class calculate quality pts, sum the calc results
              3. Across all hours, sum credit hours attempted
              4. Divide total quality pts by total credit hours
              5. Display reults to user
             ~  numbers important as a roadmap ~
              
               
Non functional:
              1.No considerations of drops/ withdraws
              2.No considration of transfer courses
              3.No consideration of CR/NR courses
              4.Limit user inupt as much is functional
              5.Design the app to function to make it more flexible 
                    and allow for code reuse

"""
#pull it all together 

#call the collect grades function
myGrades = collectGrades( )

gpaInfo = calculateQualityPts( myGrades )
#myGrades couples these two  functions 

#unpack the tuple 
creditHours, qualityPoints = gpaInfo

#use the unpacked tuple values to calculate overall GPA

gpa = qualityPoints / creditHours

#present the reult to the user 
print( "My GPA is {:.f}".format(gpa) )  


      
      
      
       
       








    
    