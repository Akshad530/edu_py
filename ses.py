import time
import streamlit as st
import streamlit as st

# Custom CSS to style the title with neon purple and bounce effect
import streamlit as st

st.markdown("""
    <style>
    .glow-text {
        color: #000000; /* Black text */
        font-size: 70px;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 5px grey, 0 0 10px grey, 0 0 15px grey;
        animation: glowAnimation 2s ease-in-out infinite alternate,
                   floatAnimation 3s ease-in-out infinite;
        margin: 0 auto;
        display: block;
        width: fit-content;
    }

    @keyframes glowAnimation {
        from {
            text-shadow: 0 0 5px grey, 0 0 10px grey, 0 0 15px grey;
        }
        to {
            text-shadow: 0 0 10px #aaa, 0 0 20px #aaa, 0 0 30px #aaa;
        }
    }

    @keyframes floatAnimation {
        0% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0); }
    }

    .center-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 200px;
    }
    </style>

    <div class="center-wrapper">
        <span class="glow-text">Welcome to PyCode Academy!</span>
    </div>
""", unsafe_allow_html=True)


# Example content





import streamlit as st
from datetime import datetime

# --- Set Page Config ---


import streamlit as st
from datetime import datetime

# --- Page Config ---


# --- Credentials ---
import streamlit as st
import random

# GitHub username
github_username = "akshadyeole"
avatar_url = f"https://github.com/{github_username}.png"

# Initialize Tic Tac Toe board in session
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None

# Reset function for Tic Tac Toe
def reset_ttt():
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None

# Check winner
def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for a,b,c in wins:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if "" not in board:
        return "Draw"
    return None

with st.sidebar:
    st.title("👤 Akshad Sunil Yeole")
    st.caption("Python Learner")

    # Navigation
    section = st.selectbox("Choose Section", ["Profile", "Number Guessing", "Rock Paper Scissors"])

    if section == "Profile":
        st.subheader("📄 Profile")

        st.write("**Name:** Akshad Sunil Yeole")
        st.write("**Role:** Python Learner")
        st.write(f"**GitHub:** https://github.com/Akshad530/demo_ak")

    elif section == "Number Guessing":
        st.subheader("🎯 Number Guessing Game")
        if "number" not in st.session_state:
            st.session_state.number = random.randint(1, 20)

        guess = st.number_input("Guess a number (1-20):", min_value=1, max_value=20, step=1)
        if st.button("Guess"):
            if guess == st.session_state.number:
                st.success("Correct! 🎉")
                st.session_state.number = random.randint(1, 20)
            elif guess < st.session_state.number:
                st.info("Too low ⬇️")
            else:
                st.info("Too high ⬆️")

    elif section == "Rock Paper Scissors":
        st.subheader("🪨📄✂️ Rock Paper Scissors")
        moves = ["Rock", "Paper", "Scissors"]
        user = st.selectbox("Your move", moves)
        if st.button("Play"):
            bot = random.choice(moves)
            st.write(f"🤖 Bot chose: **{bot}**")
            if user == bot:
                st.warning("It's a tie!")
            elif (user == "Rock" and bot == "Scissors") or \
                 (user == "Paper" and bot == "Rock") or \
                 (user == "Scissors" and bot == "Paper"):
                st.success("You win! 🎉")
            else:
                st.error("You lose! 😢")
            
    




    











st.title("Let's Learn Python !")
st.subheader("What is Python ?")
st.write("""
Python is a programming language that is used for a variety of tasks, including web development, data science, and software development. It is a general-purpose language that is easy to learn and use. 

         
         """)
VIDEO_URL = "https://www.youtube.com/watch?v=xkZMUX_oQX4&list=PLP9IO4UYNF0UgPfkTBECSKIJGdc_9FYZ9.mp4"
st.video(VIDEO_URL,"subtitles.vtt")

st.subheader("Features of Python :-")
st.write("""
Easy to learn : Python is a beginner-friendly language with easy-to-read syntax. 

Versatile : Python can be used for a variety of tasks, including scientific computing, web development, and automation. 

Open-source : Python is an open-source community language, so many independent programmers are constantly building libraries and functionality for it. 


""")
st.subheader("Uses of Python:-")
st.write("""


         
Web development : Python is used to create websites and web applications. 

Data science : Python is used for data analysis, data visualization, and machine learning. 

Software development  : Python is used to develop software, including software testing, bug tracking, and build control. 

Automation : Python is used to automate tasks, such as organizing finances. 



""")
st.subheader("Data analysis and machine learning")
st.write("""
Python has become a staple in data science, allowing data analysts and other professionals to use the language to conduct complex statistical calculations, create data visualisations, build machine learning algorithms, manipulate and analyse data, and complete other data-related tasks.

Python can build various data visualisations, like line and bar graphs, pie charts, histogrammes, and 3D plots. Python also has many libraries that enable coders to write programs for data analysis and machine learning more quickly and efficiently, like TensorFlow and Keras.
         """)
st.subheader("Web development")
st.write("""
Python is often used to develop the back end of a website or application—the parts that a user doesn’t see. Python’s role in web development includes sending data to and from servers, processing data and communicating with databases, routing URLs, and ensuring security. Python offers several frameworks for web development. Commonly used ones include Django and Flask.

Some web development jobs that use Python include back-end engineers, full-stack engineers, Python developers, software engineers, and DevOps engineers. 
         """)
st.subheader("Automation or scripting")
st.write("""
If you perform a task repeatedly, you can work more efficiently by automating it with Python. Writing code used to build these automated processes is called scripting. In the coding world, automation can be used to check for errors across multiple files, convert files, execute simple math, and remove duplicates in data.

Relative beginners can even use Python to automate simple tasks on the computer—such as renaming files, finding and downloading online content, or sending emails or texts at desired intervals.
         """)
st.subheader("Software testing and prototyping")
st.write("""
Python can aid in software development tasks like build control, bug tracking, and testing. With Python, software developers can automate testing for new products or features. Some Python tools used for software testing include Green and Requestium.
""")
st.subheader("Everyday tasks")
st.write("""
Python isn't only for programmers and data scientists. Learning Python can open new possibilities for those in less data-heavy professions, like journalists, small business owners, or social media marketers. Python can also enable non-programmers to simplify certain tasks in their lives. Here are just a few of the tasks you could automate with Python:

Send yourself a text reminder to carry an umbrella anytime it’s raining

Update your grocery shopping list

Renaming large batches of files

Converting text files to spreadsheets

Randomly assign household tasks to family members

Fill out online forms automatically
         """)
st.subheader("Why is Python so popular?")
st.write("""
Python is popular for several reasons. Here's a deeper look at what makes it versatile and easy for coders to use.

It has a simple syntax that mimics natural language, so it’s easier to read and understand. This makes it quicker to build projects and faster to improve on them.

It’s versatile. Python can be used for many different tasks, from web development to machine learning.

It’s beginner friendly, making it popular for entry-level coders.

It’s open source, which means it’s free to use and distribute, even for commercial purposes.

Python’s archive of modules and libraries—bundles of code that third-party users have created to expand Python’s capabilities—is vast and growing.

Python has a large and active community that contributes to Python’s pool of modules and libraries and acts as a helpful resource for other programmers. The vast support community means that when coders need help, finding a solution is relatively easy; somebody has likely encountered the same problem before.
         """)
st.subheader("Why Was Python Created?")
st.write("""
Python was created as a replacement for ABC language and to resolve its limitations. Though ABC language has prominent features, its drawbacks were restricting its widespread adoption.

Some of its limitations that encouraged Guido Van Rossum to create Python were:

One of the major disadvantages with ABC language was that developers could not add new features or libraries which made it less flexible for real-world use cases.
Another drawback was that you could not integrate ABC with third-party language, system or software components.
Also, with ABC, you did not have access to the operating system. This made it difficult for developers to use the language for projects that required system-level access.
ABC lacked a large user base or community. Developers could not get access to support, libraries, or tools, things that make a language attractive for adoption.
These limitations of ABC language irritated Guido to the point where he created Python which is known for its high performance, versatility, module system, object-oriented design and is supported by a large community of contributors.
""")
st.subheader("How to learn Python easily?")
st.write("""
Python is the programming language which is easiest of them all. It has a simple format, English-like syntax, and high flexibility. Here are some tips on how to learn Python easily.
""")
st.subheader("1) Code regularly")
st.write("""

Needless to say that practice makes a man perfect. It develops muscle memory and helps in avoiding silly mistakes.""")
st.subheader("2) Use Pen and Paper")
st.write("""
Anything written by hand has high retention. While practising makes sure to use pen and paper as it would work in subconscious training for codes.
         
""")
st.subheader("3) Program as pair")
st.write("""
One’s a loner, two’s a team. Find yourself a friend or learner who wants to learn this programing language. One should be the ‘driver’ and the other should be the ‘navigator’. The Diver writes the code and the Navigator helps in solving the problems and ensures the code is error-free. Swap the roles from time to time to learn at the best pace.
""")
st.subheader("4) Build new things")
st.write("""
There are a lot of short exercises for python beginners. Start creating various programs with Python. This will make your output oriented.
""")
st.subheader("Now! we will take a few examples of Python:")
st.code("""
        
        print("Hello World")
        
        """)
st.write("In the above example the statement PRINT is used to display , if we write firstly PRINT and then add brackets , add double quotes and write Hello World in it , it will display Hello World in terminal box ")

st.subheader("Python Indentation")
st.write("""
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.

""")
st.code("""

if 5 > 2:
  print("Five is greater than two!")
""")
st.write("Python will give you an error if you skip the indentation:")
st.subheader("Python Syntax")
st.write("""



Comments can be used to explain Python code.

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.
         """)
st.code("""
#This is a comment
print("Hello, World!")


""")
st.subheader("Variable")
st.write("""
Variables are containers for storing data values.

""")
st.subheader("Creating a Variable")
st.write("""
         
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it. 
         
         """)
st.code("""

a = 4
A = "Sally"
#A will not overwrite a
""")
st.subheader("Python Data Types")
st.write("""

In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type :	str
         
Numeric Types :	int, float, complex
         
Sequence Types :	list, tuple, range
         
Mapping Type :	dict
         
Set Types :	set, frozenset
         
Boolean Type :	bool
         
Binary Types :	bytes, bytearray, memoryview
         
None Type :	NoneType
         



""")
st.code("""




x = 5
print(type(x))
        """)
st.subheader("Python Numbers")
st.write("""There are three numeric types in Python:

int
float
complex
Variables of numeric types are created when you assign a value to them
         """)
st.subheader("Example :")
st.code("""




x = 1    # int
        
y = 2.8  # float
        
z = 1j   # complex
        
        """)
st.subheader("Int")
st.write("""



Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
         """)
st.subheader("Example :")
st.write("""

x = 1
         
y = 35656222554887711
         
z = -3255522
         

print(type(x))
         
print(type(y))
         
print(type(z))
         
         """)
st.subheader("Float")
st.write("""

Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
         """)
st.subheader("Examples :")
st.code("""


x = 1.10
        
y = 1.0
        
z = -35.59
        

print(type(x))
        
print(type(y))
        
      
print(type(z))

        """)
st.subheader("Random")
st.write("""


Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:""")
st.subheader("Example :")
st.code("""


import random

print(random.randrange(1, 10))
        """)

st.subheader("Python List")
st.write("""


Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
         """)
st.code("""


thislist = ["apple", "banana", "cherry"]
print(thislist)
        """)
st.subheader("Python Tuples")
st.write("""

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
         """)
st.code("""
thistuple = ("apple", "banana", "cherry")
print(thistuple)
        """)
st.subheader("Python Loops")
st.write("""

Python has two primitive loop commands:

1 . While loops
         
2 . For loops
         
3 . The while Loop
         
With the while loop we can execute a set of statements as long as a condition is true.
         """)
st.code("""
        i = 1
      
while i < 6:
        
  print(i)
        
  i += 1
        
  """)
st.subheader("The Break Statement")
st.write("""
With the break statement we can stop the loop even if the while condition is true
  """)
st.code("""
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
""")
import streamlit as st



# 1. continue
st.subheader(" Continue")
st.write("Skips the current loop iteration and continues with the next one.")
st.code("""
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output: 0 1 3 4
""")

# 2. pass
st.subheader(" Pass")
st.write("Does nothing  used as a placeholder when code is required syntactically.")
st.code("""
for i in range(3):
    if i == 1:
        pass
    print(i)
# Output: 0 1 2
""")

# 3. while loop
st.subheader(" While Loop")
st.write("Repeats a block of code while a condition is true.")
st.code("""
i = 0
while i < 3:
    print(i)
    i += 1
""")

# 4. Nested loop
st.subheader(" Nested Loops")
st.write("Loops inside loops useful for multi-level iteration.")
st.code("""
for i in range(2):
    for j in range(2):
        print(i, j)
""")

# 5. Functions
st.subheader(" Functions")
st.write("Reusable blocks of code defined using `def`.")
st.code("""
def greet(name):
    print("Hello", name)

greet("Akshad")
""")

# 6. Lambda function
st.subheader(" Lambda Function")
st.write("A short anonymous function using `lambda` keyword.")
st.code("""
square = lambda x: x * x
print(square(5))
""")

# 7. List
st.subheader(" List")
st.write("Ordered, changeable collection.")
st.code("""
fruits = ["apple", "banana"]
print(fruits[0])
""")

# 8. Tuple
st.subheader(" Tuple")
st.write("Ordered, unchangeable collection.")
st.code("""
point = (10, 20)
print(point)
""")

# 9. Dictionary
st.subheader(" Dictionary")
st.write("Key-value pairs, like a real-world dictionary.")
st.code("""
student = {"name": "Akshad", "age": 20}
print(student["name"])
""")

# 10. Set
st.subheader(" Set")
st.write("Unordered collection with no duplicates.")
st.code("""
nums = {1, 2, 2, 3}
print(nums)  # {1, 2, 3}
""")

# 11. Exception handling
st.subheader(" Exception Handling")
st.write("Catches and handles errors gracefully.")
st.code("""
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
""")

# 12. List comprehension
st.subheader(" List Comprehension")
st.write("Short way to create a list.")
st.code("""
squares = [x*x for x in range(5)]
print(squares)
""")

# 13. File handling
st.subheader("File Handling")
st.write("Read/write files using `open()`.")
st.code("""
with open("demo.txt", "w") as f:
    f.write("Hello!")
""")

# 14. Modules
st.subheader("Modules")
st.write("Reusable code libraries using `import`.")
st.code("""
import math
print(math.sqrt(16))
""")

# 15. if __name__ == "__main__"
st.subheader("__Name__ Guard")
st.write("Ensures code runs only when the file is executed directly.")
st.code("""
def main():
    print("This runs directly")

if __name__ == "__main__":
    main()
""")
st.subheader("What is Module")
st.write("""

Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.
""")

st.subheader("Creating Module")
st.write("""
To create a module just save the code you want in a file with the file extension .py:
""")

st.code("""
        
        def greeting(name):
  print("Hello, " + name)
        """)
st.subheader("Use a Module")
st.write("""

Now we can use the module we just created, by using the import statement:
         """)
st.code("""

import mymodule

mymodule.greeting("Jonathan")
        """)
st.header("Python Datetime")
st.subheader("Python Dates")
st.write("""
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
         """)

st.code("""

import datetime

x = datetime.datetime.now()
print(x)
        """)
st.subheader("Date Output")
st.write("""
When we execute the code from the example above the result will be:

2025-04-17 18:59:07.296250
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.

Here are a few examples, you will learn more about them later in this chapter:
""")
st.code("""

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
        """)
st.header("Python Math")
st.subheader("Built-in Math Functions")
st.write("""

The min() and max() functions can be used to find the lowest or highest value in an iterable:
         """)
st.code("""
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)
        """)
st.write("The abs() function returns the absolute (positive) value of the specified number:")
st.code("""

x = abs(-7.25)

print(x)
        """)
st.header("Python JSON")
st.write("""JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.
""")
st.subheader("JSON in Python")
st.write("""
Python has a built-in package called json, which can be used to work with JSON data.
""")
st.code("""
Import the json module:

import json
""")
st.header("Python PIP")
st.subheader("What is PIP?")
st.write("""
PIP is a package manager for Python packages, or modules if you like.
         
""")
st.subheader("What is a Package?")
st.write("""
A package contains all the files you need for a module.

Modules are Python code libraries you can include in your project.
         """)
st.subheader("Check if PIP is Installed")
st.write("""
Navigate your command line to the location of Python's script directory, and type the following:
         """)


st.subheader("Install PIP")
st.write("""

If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/
         """)
st.subheader("Download a Package")
st.write("""

Downloading a package is very easy.

Open the command line interface and tell PIP to download the package you want.

Navigate your command line to the location of Python's script directory, and type the following:

""")
st.header("Python Try Except")
st.write("""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
         """)
st.subheader("Exception Handling")
st.write("""
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:
""")
st.code("""
try:
  print(x)
except:
  print("An exception occurred")
""")
st.header("Python Input")
st.subheader("User Input")
st.write("""
Python allows for user input.

That means we are able to ask the user for input.

The method is a bit different in Python 3.6 than Python 2.7.

Python 3.6 uses the input() method.

Python 2.7 uses the raw_input() method.

The following example asks for the username, and when you entered the username, it gets printed on the screen:
         """)
st.code("""
username = input("Enter username:")
print("Username is: " + username)
        """)
st.subheader("Numpy Tutorial")
st.write("""
NumPy (Numerical Python) is a Python library used for fast numerical operations, especially on large arrays and matrices.

🔧 Key Features:
Efficient n-dimensional arrays (ndarray)

Mathematical functions (mean, sum, std, etc.)

Broadcasting (automatic dimension handling)

Linear algebra, FFT, random numbers, etc.


         """)
st.code("""
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4])

# Perform operations
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Squared:", arr ** 2)

        """)
VIDEO_URL = "https://www.youtube.com/watch?v=awP79Yb3NaU.mp4"
st.video(VIDEO_URL,"subtitles.vtt")
st.subheader("Pandas")
st.write("""
Pandas is a powerful Python library for data analysis and manipulation.
It provides two main data structures:

Series: 1D labeled array (like a column)

DataFrame: 2D table (like an Excel sheet or SQL table)
         """)
st.code("""
import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}

df = pd.DataFrame(data)

# Display info
print(df)
print("Average Age:", df["Age"].mean())

        """)
VIDEO_URL = "https://www.youtube.com/watch?v=RhEjmHeDNoA.mp4"
st.video(VIDEO_URL,"subtitles.vtt")
st.title("Python MySQL")
st.write("""
Python can be used in database applications.

One of the most popular databases is MySQL.""")
st.subheader("MySQL Database")
st.write("""
To be able to experiment with the code examples in this tutorial, you should have MySQL installed on your computer.

You can download a MySQL database at https://www.mysql.com/downloads/.

""")
st.subheader("Install MySQL Driver")
st.write("""

Python needs a MySQL driver to access the MySQL database.

In this tutorial we will use the driver "MySQL Connector".

We recommend that you use PIP to install "MySQL Connector".

PIP is most likely already installed in your Python environment.

Navigate your command line to the location of PIP, and type the following:

Download and install "MySQL Connector":""")

st.subheader("Test MySQL Connector")
st.write("""
To test if the installation was successful, or if you already have "MySQL Connector" installed, create a Python page with the following content:

demo_mysql_test.py:

import mysql.connector""")
st.subheader("Create Connection")
st.write("""
Start by creating a connection to the database.

Use the username and password from your MySQL database:

demo_mysql_connection.py:

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb)""")
st.header("Python MySQL Create Database")
st.subheader("Creating a Database")
st.write("""
To create a database in MySQL, use the "CREATE DATABASE" statement:""")

st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
        """)
st.subheader("Check if Database Exists")
st.write("""
You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement:""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)""")
st.header('Python MySQL Create Table')
st.subheader("Creating a Table")
st.write("""
To create a table in MySQL, use the "CREATE TABLE" statement.

Make sure you define the name of the database when you create the connection
         """)
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")""")
st.subheader("Check if Table Exists")
st.write("""
You can check if a table exist by listing all tables in your database with the "SHOW TABLES" statement:""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
""")
st.subheader("Primary Key")
st.write("""
When creating a table, you should also create a column with a unique key for each record.

This can be done by defining a PRIMARY KEY.

We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each record. Starting at 1, and increased by one for each record.""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")""")
st.header("Insert Into Table")
st.write("""
To fill a table in MySQL, use the "INSERT INTO" statement.""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")""")
st.subheader("Insert Multiple Rows")
st.write("""
To insert multiple rows into a table, use the executemany() method.

The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")""")
st.subheader("Get Inserted ID")
st.write("""
You can get the id of the row you just inserted by asking the cursor object.
         """)
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
        """)
st.header("Python MySQL Select From")
st.subheader("Select From a Table")
st.write("""
To select from a table in MySQL, use the "SELECT" statement:""")
st.code("""import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

""")
st.subheader("Selecting Columns")
st.write("""
To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s)""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)""")
st.subheader("Using the fetchone() Method")
st.write("""
The fetchone() method will return the first row of the result:""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)""")
st.header("Python MySQL Where")
st.subheader("Select With a Filter")
st.write("""
When selecting records from a table, you can filter the selection by using the "WHERE" statement:""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)""")
st.subheader("Wildcard Characters")
st.write("""
You can also select the records that starts, includes, or ends with a given letter or phrase.

Use the %  to represent wildcard characters:""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)""")
st.subheader("Prevent SQL Injection")
st.write("""
When query values are provided by the user, you should escape the values.

This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.

The mysql.connector module has methods to escape query values:""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)""")
st.header("Python MySQL Order By")
st.subheader("Sort the Result")
st.write("""
Use the ORDER BY statement to sort the result in ascending or descending order.

The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order, use the DESC keyword.

""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)""")
st.subheader("ORDER BY DESC")
st.write("""
Use the DESC keyword to sort the result in a descending order.""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)""")
st.header("Python MySQL Delete From By")
st.subheader("Delete Record")
st.write("""
You can delete records from an existing table by using the "DELETE FROM" statement:""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
        """)
st.header("Python MySQL Drop Table")
st.subheader("Delete a Table")
st.write("""
         You can delete an existing table by using the "DROP TABLE" statement:""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)""")
st.subheader("Drop Only if Exist")
st.write("""
If the table you want to delete is already deleted, or for any other reason does not exist, you can use the IF EXISTS keyword to avoid getting an error.""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)
        """)
st.header("Python MySQL Update Table")
st.subheader("Update Table")
st.write("""
You can update existing records in a table by using the "UPDATE" statement:""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")""")
st.subheader("Prevent SQL Injection")
st.write("""
It is considered a good practice to escape the values of any query, also in update statements.

This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.

The mysql.connector module uses the placeholder %s to escape values in the update statement:""")
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")""")
st.header("Python MySQL Limit")
st.subheader("Limit the Result")
st.write("""
You can limit the number of records returned from the query, by using the "LIMIT" statement:
         """)
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)""")
st.subheader("Start From Another Position")
st.write("""
If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:
         """)
st.code("""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)""")
st.header("Python MySQL Join")
st.subheader("Join Two or More Tables")
st.write("""
You can combine rows from two or more tables, based on a related column between them, by using a JOIN statement.

Consider you have a "users" table and a "products" table:""")
st.code("""
        import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)""")

st.subheader("LEFT JOIN")
st.write("""
In the example above, Hannah, and Michael were excluded from the result, that is because INNER JOIN only shows the records where there is a match.

If you want to show all users, even if they do not have a favorite product, use the LEFT JOIN statement:""")

st.subheader("RIGHT JOIN")
st.write("""
If you want to return all products, and the users who have them as their favorite, even if no user have them as their favorite, use the RIGHT JOIN statement:""")


# --------------------------
# Python Quiz Data
# --------------------------
questions = {
    "What is the output of print(2 ** 3)?": {
        "options": ["6", "8", "9", "Error"],
        "answer": "8"
    },
    "Which of these is a valid variable name in Python?": {
        "options": ["2var", "var_2", "var-2", "var 2"],
        "answer": "var_2"
    },
    "What does the len() function do?": {
        "options": ["Adds numbers", "Returns length", "Counts letters only", "None"],
        "answer": "Returns length"
    },
    "Which keyword is used to define a function in Python?": {
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    "What is the correct file extension for Python files?": {
        "options": [".python", ".pt", ".py", ".pyt"],
        "answer": ".py"
    }
}

# --------------------------
# Streamlit UI
# --------------------------
st.title("🐍 Python Basics Quiz")

st.subheader("📋 Answer the following questions:")

score = 0
total = len(questions)

# Track answers
user_answers = {}

for q, data in questions.items():
    user_answer = st.radio(q, data["options"], key=q)
    user_answers[q] = user_answer
    if user_answer == data["answer"]:
        score += 1

# --------------------------
# Submit Button
# --------------------------
if st.button("✅ Submit Quiz"):
    st.success(f"🎉 You scored {score} out of {total}!")

    st.markdown("---")
    st.subheader("📊 Review Your Answers")
    for q, data in questions.items():
        correct = data["answer"]
        user_choice = user_answers[q]
        if user_choice == correct:
            st.write(f"✅ **{q}** — Your answer: `{user_choice}`")
        else:
            st.write(f"❌ **{q}** — Your answer: `{user_choice}`, Correct answer: `{correct}`")

    if score == total:
        st.balloons()


import streamlit as st
import io
import contextlib


import streamlit as st
import random

st.title("🧩 Simple Python Code Puzzle")

# Original correct code
correct_code = [
    "def say_hello():",
    "    print('Hello, World!')",
    "say_hello()"
]

# Shuffle for puzzle
shuffled_code = correct_code.copy()
random.seed(1)
random.shuffle(shuffled_code)

st.write("Arrange the following lines in the correct order:")

# Create a set to keep track of selected lines (avoiding duplicates)
selected_lines = set()

# Keep track of user selections
user_selection = []

# Create dropdowns with dynamic options to avoid duplicates
for i in range(3):
    # Filter available choices based on what has already been selected
    available_choices = [line for line in shuffled_code if line not in selected_lines]
    selected_line = st.selectbox(f"Line {i + 1}", available_choices, key=f"line_{i}")
    
    # Add the selected line to the set of selected lines
    selected_lines.add(selected_line)
    user_selection.append(selected_line)

# Check the answer when the button is clicked
if st.button("Check Answer", key="check_button"):
    if user_selection == correct_code:
        st.success("✅ Correct! You solved the puzzle!")
    else:
        st.error("❌ Try again! That's not the right order.")

# Optionally, show the correct code
with st.expander("💡 Show Correct Code"):
    st.code("\n".join(correct_code), language="python")

import streamlit as st
import csv
import pandas as pd

# Set up the title and description
st.title("Feedback Form")
st.markdown("""
Please provide your feedback about the course. Your feedback helps us improve!
""")

# Set up the form
with st.form(key="feedback_form"):
    name = st.text_input("Your Name (Optional)")
    email = st.text_input("Your Email (Optional)")
    message = st.text_area("Your Feedback")
    rating = st.slider("Rate the Course (1-5)", 1, 5, 3)  # Rating slider
    
    submit_button = st.form_submit_button("Submit Feedback")

    if submit_button:
        # Save the feedback to a CSV file in a systematic way
        feedback_data = [name, email, message, rating]

        # Check if the CSV file exists and write header if it's the first entry
        try:
            with open("feedbacks.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                if file.tell() == 0:  # If the file is empty, write the header first
                    writer.writerow(["Name", "Email", "Feedback", "Rating"])
                writer.writerow(feedback_data)  # Store feedback data
                
            st.success("Thank you for your feedback! It has been saved.")
            st.balloons()  # Adds a nice touch with balloon animation
        except Exception as e:
            st.error(f"An error occurred while saving the feedback: {e}")
        
        # Optionally display the latest feedback entry
        st.subheader("Your Feedback:")
        st.write(f"**Name:** {name if name else 'Anonymous'}")
        st.write(f"**Email:** {email if email else 'Not provided'}")
        st.write(f"**Feedback:** {message}")
        st.write(f"**Rating:** {rating} stars")

# Optionally, display all collected feedback (for your review)
st.subheader("All Collected Feedback:")
try:
    feedback_df = pd.read_csv("feedbacks.csv")
    st.dataframe(feedback_df)  # Display feedback in a table format
except FileNotFoundError:
    st.write("No feedback yet!")
