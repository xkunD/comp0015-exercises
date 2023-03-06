# Name: course_manager.py
# Description:
#
# This program prompts the user for a course code and then asks the user for the names of students on the course. 
#
# Author: Rae Harbird
# Date: August 2018
#

MINIMUM_NAME_LENGTH = 5


## Checks the name is valid
#  @param name a student's name
#  @return True or False depending on whether the name was valid
#
def checkStudentName(name):
    if len(name) < MINIMUM_NAME_LENGTH:
        print("Student name is less than {} characters, try again.".format(MINIMUM_NAME_LENGTH))
        return False
    else:
        return True
    

## Get the names of students in a class from the user
#  @param studentSet a set containing student names
#  @return updatedSet this is a copy of studentSet with the additional names
#   
def getStudentNames(studentSet):
    newStudents = set()
    nextStudentName = input("\nEnter the student's name or '*' to finish: ")
    
    while nextStudentName[0] != '*':
        if checkStudentName(nextStudentName) :
            newStudents.add(nextStudentName)
        nextStudentName = input("\nEnter the student's name or '*' to finish: ")
    
    return studentSet.union(newStudents)

            
## Prints names of students in a class
#  @param className the name of the class
#  @param studentSet a set containing student names
#   
def displayClassNames(className, studentSet):
    print("\nClass: ", className)
    if len(studentSet) == 0:
        print("\tThere are no students in this class.")
    else:
        for student in sorted(studentSet):
            print("\t", student)


# Start the program
def main():
    
    studentNameSet = set()
    
    courseCode = input("Enter the course code: ")
    
    finalStudentNameSet = getStudentNames(studentNameSet)
            
    displayClassNames(courseCode, finalStudentNameSet)


if __name__ == "__main__":
    main()