import csv

file_path = 'employees.csv'

localData = [] 

def initalData(readData):
    with open(file_path, 'w', newline='') as file:
        writeValues = csv.writer(file)
        writeValues.writerow(['EmployeeID', 'Name', 'Department', 'Salary'])
        print("@@", readData)
        writeValues.writerows(readData)

def getDatFunction():
    print("work")
    try:
        with open(file_path, 'r') as file:
            readValues = csv.reader(file)
            for data in readValues:
                if data:
                    localData.append(data)
    except FileNotFoundError:
        initalData([])
        print("File Not found. Creating File")
    finally:
        print("Execution Finished")

def InsertFunction(addData):
    try:
        with open(file_path, 'a', newline='') as file:
            addingNewValue = csv.writer(file)
            addingNewValue.writerow(addData)
    except FileNotFoundError:
        print("File Not found.")
    finally:
        print("Add Execution Finished")

def ViewDatFunction():
    try:
        with open(file_path, 'r') as file:
            readValues = csv.reader(file)
            for data in readValues:
                print(data)
    except FileNotFoundError:
        initalData([])
        print("File Not found. Creating File")
    finally:
        print("Execution Finished")

def DeleteDataFunction(data):
    tempData = []
    try:
        with open(file_path, 'r') as file:
            readValues = csv.reader(file)
            for row in readValues:
                if data not in row:
                    tempData.append(row)
        initalData(tempData)
    except FileNotFoundError:
        initalData([])
        print("File Not found. Creating File")
    finally:
        print("Execution Finished")

# Main program
check = 1
c = ""
print("main")
getDatFunction()

while check:
    print("Insert - 1, View - 2, Delete - 3, LogOut - 0")
    if c == "":
        c = int(input("Enter your Choice: "))
    match c:
        case 1 | "1":
            print("Add New Data")
            empid = input("Enter EmployeeID: ")
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            salary = input("Enter Salary: ")
            if empid and name and dept and salary:
                InsertFunction([empid, name, dept, salary])
                print("Successfully Added!")
                c = ""
            else:
                print("Please enter all details.")
                c = 1
        case 2:
            ViewDatFunction()
            c = ""
        case 3:
            deleteName = input("Enter EmployeeID: ")
            if deleteName:
                DeleteDataFunction(deleteName)
                print("Deleted Successfully.")
                c = ""
            else:
                c = 3
        case 0:
            print("Thank you!")
            check = 0
            break
        case _:
            c = ""

print("Report:", localData)
