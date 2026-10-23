'''
Develop a simple contact form application with input fields for Name, Email, and Message. 
The submitted data should be securely stored in a database.

'''
import sqlite3
name = input("Enter the name : ")
email = input("Enter the email: ")
message = input("Enter the message to convey: ")

"""
db = {
    name: "vishnu",
    email: "vishnu123@gmail.com",
    message: "Hi lets! meet tommorrow",
    
    name: "amal",
    email: "amal123@gmail.com",
    message:"get together meet"   
}
"""


connection = sqlite3.connect("db.py")


