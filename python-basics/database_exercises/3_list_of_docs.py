# Get the list Of doctors as per the given specialty and salary

import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='pynative',
                                         password='pynative@#29')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_specialist_doctors_list(speciality, salary):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """ select * from Doctor where Speciality = %s and salary > %s"""
        cursor.execute(query,(speciality,salary))
        records = cursor.fetchall()
        print("Printing doctors whose specialty is Garnacologist and salary greater than 30000")
        for row in records:
            print("Doctor Id: ", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

print("Question 3: Get Doctors as per given Speciality\n")
get_specialist_doctors_list("Garnacologist", 30000)
