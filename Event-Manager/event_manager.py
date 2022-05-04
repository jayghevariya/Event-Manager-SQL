import pymysql
import subprocess as sp
import pymysql.cursors
from tabulate import tabulate
from datetime import datetime
import os
conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        db='EVENT_MANAGER',
        )

cur = conn.cursor()

def Retrieve():
    try:
        date = input("Enter date in yyyy-mm-dd format only: ")
        query = """SELECT * FROM Event WHERE `Date` = %s;"""
        cur.execute(query, (date))
        output = cur.fetchall()
        print(tabulate(output, headers="keys", tablefmt='psql'))
    except Exception as e:
        conn.rollback()
        print("Error Occured: Unable to retreive from database -", e)

    return

def Equipments():
    try:
        cur.execute("SELECT Equipment_id FROM Equipments WHERE Availability = TRUE")
        output = cur.fetchall()
        print(tabulate(output, headers="keys", tablefmt='psql'))
    except Exception as e:
        conn.rollback()
        print("Error Occured: Unable to retreive from database -", e)

    return

def Name():
    try:
        string = input("Enter the substring to be searched : ")
        query = """SELECT * FROM Employee WHERE INSTR(`Name` , %s) = 1;"""
        cur.execute(query , (string))
        output = cur.fetchall()
        print(tabulate(output, headers="keys", tablefmt='psql'))
    except Exception as e:
        conn.rollback()
        print("Error Occured: Unable to retreive from database -", e)

    return

def Print_amount():
    try:
        query = """SELECT SUM(Salary) FROM Salaried_Employee;"""
        cur.execute(query)
        output = cur.fetchall()
        print(tabulate(output, headers="keys", tablefmt='psql'))
    except Exception as e:
        conn.rollback()
        print("Error Occured: Unable to retreive from database -", e)
    return

def Print_equipments():
    try:
        num = input("Enter Threshold Cost ")
        query = """SELECT * FROM Equipments WHERE `Cost` > %s;"""
        cur.execute(query , (num))
        output = cur.fetchall()
        print(tabulate(output, headers="keys", tablefmt='psql'))
    except Exception as e:
        conn.rollback()
        print("Error Occured: Unable to retreive from database -", e)
    return

def ShowTable():
    try:
        string = input("Enter table Name : ")
        query = """SELECT * FROM %s ;""" %(string)
        cur.execute(query)
        output = cur.fetchall()
        print(tabulate(output, headers="keys", tablefmt='psql'))

    except Exception as e:
        conn.rollback()
        print("Error Occured: Unable to retreive from database -", e)

    return

def Event_details():
    try:
        row = {}
        print("Enter new event's details: ")
        row["id"] = (int)(input("New Event's Event_id: "))
        row["Name"] = input("Name: ")
        row["Location"] = input("Location: ")
        row["Date"] = input("Date (YYYY-MM-DD): ")
        row["Start_time"] = input("Start time(HH:MM:SS): ")
        row["End_time"] = input("End time(HH:MM:SS): ")
        row["Event_type"] = input("Event_type: ")
        row["Profits_expected"] = (int)(input("Expected Profits: "))
        row["Profits_gained"] = (int)(input("Gained Profits: "))

        query = "INSERT INTO Event VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s', %d, %d)" % (row["id"], row["Name"], row["Location"], row["Date"], row["Start_time"], row["End_time"], row["Event_type"], row["Profits_expected"], row["Profits_gained"])
        cur.execute(query)
        conn.commit()
        time_1 = datetime.strptime(row["Start_time"],"%H:%M:%S")
        time_2 = datetime.strptime(row["End_time"],"%H:%M:%S")
        time_interval = time_2 - time_1
        query = "INSERT INTO Time VALUES('%d', '%s' )" % (row["id"], time_interval)
        cur.execute(query)
        conn.commit()

        print("Inserted Into Database")

    except Exception as e:
        conn.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def Admin_details():
    try:
        row = {}
        print("Enter admin details: ")
        row["Name"] = input("Name: ")
        row["Contact_Number"] = input("Contact Number: ")
        row["Building_Name"] = input("Building Name: ")
        row["Street"] = input("Street Name: ")
        row["City"] = input("City Name: ")
        row["Date_of_Birth"] = input("Date of Birth (YYYY-MM-DD): ")
        row["Email_Id"] = input("Email-id")
        row["Event_id"] = (int)(input("Id of event to be administered: "))
        row["Salary"] = (int)(input("Salary: "))
        row["Number_Of_Employees_working_under"] = (int)(input("Number of employees working under the admin: "))

        query = "INSERT INTO Admin VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', %d, %d, %d)" % (row["Name"], row["Contact_Number"], row["Building_Name"], row["Street"], row["City"], row["Date_of_Birth"], row["Email_Id"], row["Event_id"], row["Salary"], row["Number_Of_Employees_working_under"])
        cur.execute(query)
        conn.commit()
        val = row["Date_of_Birth"]
        now = datetime.now()
        year = now.strftime("%Y")
        curr_year = (int)(year)
        birth_year = (int)(val[0:4])
        age = curr_year - birth_year
        query = "INSERT INTO Admin_age VALUES('%s', '%d')" % ( row["Contact_Number"], age)
        cur.execute(query)
        conn.commit()
        print("Inserted Into Database")

    except Exception as e:
        conn.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def Spectator_details():
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter Spectator details: ")
        row["Name"] = input("Name: ")
        row["Ticket_Number"] = (int)(input("Ticket Number: "))
        row["Contact_Number"] = input("Contact Number: ")
        row["Event_id"] = (int)(input("Id of the event: "))

        query = "INSERT INTO Spectators VALUES('%s', '%d', '%s', '%d')" % (row["Name"], row["Ticket_Number"], row["Contact_Number"], row["Event_id"])

        cur.execute(query)
        conn.commit()

        print("Inserted Into Database")

    except Exception as e:
        conn.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def Partner_details():
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter Partner details: ")
        row["Owner_Name"] = input("Owner Name: ")
        row["Company_Name"] = input("Company Name: ")
        row["Building_Name"] = input("Building Name: ")
        row["Street"] = input("Street: ")
        row["City"] = input("City: ")
        row["Event_id"] = (int)(input("Enter Event id of the event if you want to insert details related to specific event (Press 0 otherwise): "))
        if row["Event_id"] != 0:
            row["Payment_details"] = (int)(input("Payment Amount: "))
            row["Partner_role"] = input("Role of Partner: ")

        query = "INSERT INTO Partners VALUES('%s', '%s', '%s', '%s', '%s')" % (row["Owner_Name"], row["Company_Name"], row["Building_Name"], row["Street"], row["City"])
        cur.execute(query)
        conn.commit()
        if row["Event_id"] != 0 :
            query = "INSERT INTO Partner_payment VALUES('%d', '%s', '%s', '%d')" % (row["Event_id"], row["Owner_Name"], row["Company_Name"], row["Payment_details"])
            cur.execute(query)
            conn.commit()
            query = "INSERT INTO Role VALUES('%d', '%s', '%s', '%s')" % (row["Event_id"], row["Owner_Name"], row["Company_Name"], row["Partner_role"])
            cur.execute(query)
            conn.commit()

        print("Inserted Into Database")

    except Exception as e:
        conn.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def Update_employee():
    try:
        row = {}
        print("Update Employee Details: ")
        id = (int)(input("Enter Employee_id: "))
        response = (int)(input("Update Contact Number (1/0)"))
        if response == 1 :
            ContactNumber = input("Enter New Contact Number")
            query = "UPDATE Employee SET `Contact_Number` = '%s' WHERE `Employee_id` = '%d';" %(ContactNumber,id)
            cur.execute(query)
            conn.commit()
        response = (int)(input("Update Email id (1/0)"))
        if response == 1 :
            ContactNumber = input("Enter New Email id")
            query = "UPDATE Employee SET `Email_id` = '%s' WHERE `Employee_id` = '%d';" %(ContactNumber,id)
            cur.execute(query)
            conn.commit()
        response = (int)(input("Update Address (1/0)"))
        if response == 1 :
            Building_Name = input("Enter New Building Name: ")
            Street = input("Enter New Street Name: ")
            City = input("Enter New City Name: ")
            query = "UPDATE Employee SET `Building_Name` = '%s', `Street` = '%s', `City` = '%s' WHERE `Employee_id` = '%d';" %(Building_Name,Street,City,id)
            cur.execute(query)
            conn.commit()
        response = (int)(input("Update Salary or Pay Scale (1/0)"))
        if response == 1 :
            ContactNumber = (int)(input("Enter New Salary or Pay Scale"))
            query = "UPDATE Salaried_Employee SET `Salary` = '%d' WHERE `Employee_id` = '%d';" %(ContactNumber,id)
            cur.execute(query)
            conn.commit()
            query = "UPDATE Hourly_Employee SET `Pay_scale` = '%d' WHERE `Employee_id` = '%d';" %(ContactNumber,id)
            cur.execute(query)
            conn.commit()

    except Exception as e:
        conn.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)

    return

def Update_equipments():
    try:
        row = {}
        print("Update Equipment Details: ")
        id = (int)(input("Enter Equipment_id: "))
        response = (int)(input("Update Availability (1/0)"))
        if response == 1 :
            Av = input("Enter New Availability(1/0) ")
            query = "UPDATE Equipments SET `Availability` = '%s' WHERE `Equipment_id` = '%d';" %(Av,id)
            cur.execute(query)
            conn.commit()
        response = (int)(input("Update Quantity (1/0)"))
        if response == 1 :
            Av = (int)(input("Enter New Quantity: "))
            query = "UPDATE Equipments SET `Quantity` = '%d' WHERE `Equipment_id` = '%d';" %(Av,id)
            cur.execute(query)
            conn.commit()
        response = (int)(input("Update Cost (1/0)"))
        if response == 1 :
            Av = (int)(input("Enter New Cost: "))
            query = "UPDATE Equipments SET `Cost` = '%d' WHERE `Equipment_id` = '%d';" %(Av,id)
            cur.execute(query)
            conn.commit()
        response = (int)(input("Update Role (1/0)"))
        if response == 1 :
            Av = input("Enter New Role: ")
            query = "UPDATE Equip_Role SET `Role` = '%s' WHERE `Equipment_id` = '%d';" %(Av,id)
            cur.execute(query)
            conn.commit()


    except Exception as e:
        conn.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)

    return

def Update_profits():
    try:
        print("Update Profits: ")
        id = (int)(input("Enter Event_id: "))
        Profit = (int)(input("Enter gained profit "))
        query = "UPDATE Event SET `Profits_gained` = '%d' WHERE `Event_id` = '%d';" %(Profit,id)
        cur.execute(query)
        conn.commit()

    except Exception as e:
        conn.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)

    return

def Delete_equipment():
    try:
        id = (int)(input("Enter Equipment_id: "))
        query = "DELETE FROM Equipments WHERE `Equipment_id` = '%d';" %(id)
        cur.execute(query)
        conn.commit()

    except Exception as e:
        conn.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)

    return

def Delete_employee():
    try:
        id = (int)(input("Enter Employee_id: "))
        query = "DELETE FROM Employee WHERE `Employee_id` = '%d';" %(id)
        cur.execute(query)
        conn.commit()

    except Exception as e:
        conn.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)

    return

def Delete_performer():
    try:
        id = (int)(input("Enter Performer_id: "))
        query = "DELETE FROM Performers WHERE `Performer_id` = '%d';" %(id)
        cur.execute(query)
        conn.commit()

    except Exception as e:
        conn.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)

    return

def Update_performer():
    try:
        print("Update Performer Details: ")
        id = (int)(input("Enter Performer_id: "))
        response = (int)(input("Update Contact Number (1/0)"))
        if response == 1 :
            ContactNumber = input("Enter New Contact Number")
            query = "UPDATE Performers SET `Contact_Number` = '%s' WHERE `Performer_id` = '%d';" %(ContactNumber,id)
            cur.execute(query)
            conn.commit()
        response = (int)(input("Update Address (1/0)"))
        if response == 1 :
            Building_Name = input("Enter New Building Name: ")
            Street = input("Enter New Street Name: ")
            City = input("Enter New City Name: ")
            query = "UPDATE Performers SET `Building_Name` = '%s', `Street` = '%s', `City` = '%s' WHERE `Performer_id` = '%d';" %(Building_Name,Street,City,id)
            cur.execute(query)
            conn.commit()

    except Exception as e:
        conn.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)

    return

def Performer_details():
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter performer details: ")
        row["Name"] = input("Name: ")
        row["Contact_Number"] = input("Contact Number: ")
        row["Building_Name"] = input("Building Name: ")
        row["Street"] = input("Street Name: ")
        row["City"] = input("City Name: ")
        row["Date_of_Birth"] = input("Date of Birth (YYYY-MM-DD): ")
        row["Performer_id"] = (int)(input("Performer_id: "))
        row["Age"] = (int)(input("Age: "))
        query = "INSERT INTO Performers VALUES('%s', '%s', '%s', '%s', '%s', '%s', %d);" % (row["Name"], row["Contact_Number"], row["Building_Name"], row["Street"], row["City"], row["Date_of_Birth"], row["Performer_id"])
        cur.execute(query)
        conn.commit()
        query = "INSERT INTO Performer_age VALUES('%d', '%d');" % (row["Age"], row["Performer_id"])
        cur.execute(query)
        conn.commit()
        inp = (int)(input("Enter Event_id in which the performer participates(If no such event press 0): "))
        if inp!=0:
            query = "INSERT INTO Performer_events VALUES('%d', '%d');" % (row["Performer_id"], inp)
            cur.execute(query)
            conn.commit()
        print("Inserted Into Database")

    except Exception as e:
        conn.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def Employee_details():
    try:
        row = {}
        print("Enter Employee details: ")
        row["Employee_id"] = (int)(input("Employee_id: "))
        row["Name"] = input("Name: ")
        row["Building_Name"] = input("Building Name: ")
        row["Street"] = input("Street Name: ")
        row["City"] = input("City Name: ")
        row["Contact_Number"] = input("Contact Number: ")
        row["Email_id"] = input("Email-id: ")
        row["Work_Role"] = input("Work Role: ")
        query = "INSERT INTO Employee VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (row["Employee_id"], row["Name"],  row["Building_Name"], row["Street"], row["City"], row["Contact_Number"], row["Email_id"],row["Work_Role"])
        cur.execute(query)
        conn.commit()
        inp = (int)(input("Enter Event_id in which the employee contributes(If no such event press 0): "))
        if inp!=0:
            query = "INSERT INTO Employee_Events VALUES('%d', '%d')" % (inp,row["Employee_id"])
            cur.execute(query)
            conn.commit()
        inp = (int)(input("Enter 1 if salaried and 0 if hourly"))
        amount = (int)(input("Salary"))
        if inp == 0:
            query = "INSERT INTO Hourly_Employee VALUES('%d', '%d')" % (row["Employee_id"],amount)
            cur.execute(query)
            conn.commit()
        if inp == 1:
            query = "INSERT INTO Salaried_Employee VALUES('%d', '%d')" % (row["Employee_id"],amount)
            cur.execute(query)
            conn.commit()
        print("Inserted Into Database")

    except Exception as e:
        conn.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def Performance_details():
    try:
        row = {}
        print("Enter Performance details: ")
        row["Performer_id"] = (int)(input("Performer_id: "))
        row["Name_of_Performance"] = input("Name of Performance ")
        row["Number_of_Performers"] = (int)(input("Number of Performers: "))
        row["Payment_amount"] = (int)(input("Payment amount "))
        row["Equipment_id"] = (int)(input("Equipment_id : "))
        query = "INSERT INTO Performance VALUES('%d','%s', '%d', '%d', '%d')" % (row["Performer_id"], row["Name_of_Performance"], row["Number_of_Performers"], row["Payment_amount"], row["Equipment_id"])
        cur.execute(query)
        conn.commit()

        print("Inserted Into Database")

    except Exception as e:
        conn.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def Equipments_details():
     try:
        row = {}
        print("Enter equipment details: ")
        row["Equipment_id"] = (int)(input("Equipment_id: "))
        row["Name"] = input("Name: ")
        row["Availability"] = (int)(input("Available or not(1/0): "))
        row["Quantity"] = (int)(input("Quantity: "))
        row["Cost"] = (int)(input("Cost : "))
        row["Role"] = (input("Work Role: "))
        row["Event_id"]=(int)(input("Enter Event_id in which the equipment was used(If no such event press 0): "))
        query = "INSERT INTO Equipments VALUES('%d','%s', '%d', '%d', '%d')" % (row["Equipment_id"], row["Name"], row["Availability"], row["Quantity"], row["Cost"])
        cur.execute(query)
        conn.commit()

        query = "INSERT INTO Equip_Role VALUES('%d','%s')" % (row["Equipment_id"],row["Role"])
        cur.execute(query)
        conn.commit()
        if row["Event_id"] !=0:
            query = "INSERT INTO Equipments_events VALUES('%d','%d')" % (row["Equipment_id"],row["Event_id"])
            cur.execute(query)
            conn.commit()
        print("Inserted Into Database")

     except Exception as e:
        conn.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

     return
while(1):
    print("Event Managers!")
    print("1.Retrieve details of events on a particular date.")
    print("2.Print ids of all available equipments")
    print("3.Details of employee whose names contain the given substring")
    print("4.Print the amount spent on paying salaries")
    print("5.Print Details of all equipments that cost above a particular threshold value")
    print("6.Show a particular table")
    print("7.Insert Event details")
    print("8.Insert Admin details")
    print("9.Insert Spectator details")
    print("10.Insert Partner details ")
    print("11.Insert Performance details ")
    print("12.Insert Employee details ")
    print("13.Insert Equipment details ")
    print("14.Insert Performer details ")
    print("15.Update Employee details")
    print("16.Update Equipment details")
    print("17.Update Profits")
    print("18.Update Performer Details")
    print("19.Remove an equipment")
    print("20.Resignation of an employee")
    print("21.Delete records of a performer")
    print("22.Logout")
    num = (int)(input("Enter a number > "))
    if num == 1:
        Retrieve()
    if num == 2:
        Equipments()
    if num == 3:
        Name()
    if num == 4:
        Print_amount()
    if num == 5:
        Print_equipments()
    if num == 6:
        ShowTable()
    if num == 7:
        Event_details()
    if num == 8:
        Admin_details()
    if num == 9:
        Spectator_details()
    if num == 10:
        Partner_details()
    if num == 11:
        Performance_details()
    if num == 12:
        Employee_details()
    if num == 13:
        Equipments_details()
    if num == 14:
        Performer_details()
    if num == 15:
        Update_employee()
    if num == 16:
        Update_equipments()
    if num == 17:
        Update_profits()
    if num == 18:
        Update_performer()
    if num == 19:
        Delete_equipment()
    if num == 20:
        Delete_employee()
    if num == 21:
        Delete_performer()
    if num == 22:
        exit(0)


    # To close the connection
conn.close()
