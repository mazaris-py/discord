import random
import string
from selenium import webdriver
import time
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Discord Account Generator - Web Controlled")

ttk.Style().configure("TButton", padding=2, relief="flat",
   background="#ccc")

# userame creation/input
usernameText = Label(root, text="IMPORTANT: Use a unique username. Something like \"Test\" or any other generic word as a username will not work due to limitations by discord.\n").pack()

username = Entry(root, width=50)
username.pack()

def usernameClick():
	global usernameEntry
	usernameEntry = username.get()
	usernameCon = Label(root, text="CONFIRMED USERNAME: " + usernameEntry)
	usernameCon.pack()
	usernameButton.state(["disabled"])

usernameButton = ttk.Button(root, text="Submit Name", command=usernameClick)
usernameButton.pack()
#password creation/input
passwordText = Label(root, text="Enter a password, use Discord's password guidelines.").pack()

password = Entry(root, width=50)
password.pack()

def passwordClick():
	global passwordEntry
	passwordEntry = password.get()
	passwordCon = Label(root, text="CONFIRMED PASSWORD: " + passwordEntry)
	passwordCon.pack()
	passwordButton.state(["disabled"])

passwordButton = ttk.Button(root, text="Submit Password", command=passwordClick)
passwordButton.pack()
#generate fake email address
def emailGenerator():
	email = (emailRandomString + "@gmail.com")
	emailCon = Label(root, text="GENERATED EMAIL: " + email)
	emailCon.pack()
	emailButton.state(["disabled"])

emailRandomString = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
email = (emailRandomString + "@gmail.com")
emailButton = ttk.Button(root, text="Generate Email", command=emailGenerator)
emailButton.pack()
#launch chrome and utilize generated/input to create discord account.
finalButtonLabel = Label(root, text="Submit username, password, and generate email before clicking.", fg="red")
finalButtonLabel.pack()

def chromeOp():
	#opens chrome
	url = "https://discordapp.com/register"
	driver = webdriver.Chrome("chromedriver.exe")
	driver.get(url)
	launchButton.state(["disabled"])
	time.sleep(3)
	#autofills info
	driver.find_element_by_name("email").send_keys(email)
	driver.find_element_by_name("username").send_keys(usernameEntry)
	driver.find_element_by_name("password").send_keys(passwordEntry)
	driver.find_element_by_class_name("contents-18-Yxp").click()
	#write to txt
	fh = open('account information.txt', 'w')
	fh.write('U: ' + email)
	fh.write(' P: ' + passwordEntry)
	fh.close()


launchButton = ttk.Button(root, text="Generate Account", command=chromeOp)
launchButton.pack()
eDisclaimer = Label(root, text="You will have to do the recaptcha to access the account. Account information is saved to account information.txt", fg='red')
eDisclaimer.pack()

root.mainloop()