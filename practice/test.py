student_data = {
    1:{
        "name":"riya",
        "age":22,
        "marks":80,
        "rollno":4
    },
    2:{
        "name":"ishita",
        "age":22,
        "marks":90,
        "rollno": 3
    },
    3:{
        "name":"ayush",
        "age":23,
        "marks":70,
        "rollno": 1
    },
    4:{
        "name":"chetna",
        "age":2,
        "marks":95,
        "rollno":2
    }
}

def toList(student_data):
    mylist = list(student_data.values())
    mysublist = []
    for i in mylist:
        templist = list(i.values())
        mysublist.append(templist)
    return mysublist


def sortAccordingToMarks(mysublist):
    n = len(mysublist)
    for i in range(n):
        for j in range(n-1):
            if mysublist[j][2] > mysublist[j+1][2]:
                mysublist[j], mysublist[j+1] = mysublist[j+1], mysublist[j]


def sortAccordingToName(mysublist):
    n = len(mysublist)
    for i in range(n):
        for j in range(n-1):
            if mysublist[j][0] > mysublist[j+1][0]:
                mysublist[j], mysublist[j+1] = mysublist[j+1], mysublist[j]


def sortAccordingToRollNo(mysublist):
    n = len(mysublist)
    for i in range(n):
        for j in range(n-1):
            if mysublist[j][3] > mysublist[j+1][3]:
                mysublist[j], mysublist[j+1] = mysublist[j+1], mysublist[j]
                
                
                
def toDictionary(mysublist):
    k=1
    for i in range(len(mysublist)):
        student_data[k]={"name":mysublist[i][0],
                         "marks":mysublist[i][2],
                         "age":mysublist[i][1],
                         "rollno":mysublist[i][3]
                         },
                         
        k+=1
    return student_data



# def findMaxMarks():
    
    


studentdatalist = toList(student_data)
sortAccordingToMarks(studentdatalist)
student_data = toDictionary(studentdatalist)
 
print("student data sorted according to marks : ")
print(student_data)

print('\n')

sortAccordingToName(studentdatalist)
print("sort according to names : ")
print(student_data)
print('\n')

sortAccordingToRollNo(studentdatalist)
print("sort according to roll no: ")
print(student_data)
