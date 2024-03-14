#print("Nagendra")
"""from flask import Flask     
app = Flask(__name__)   # Flask constructor 
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def hello(): 
    return ("Nagendra Nag Palla")
  
if __name__=='__main__': 
   app.run()"""
   
   
   
"""n=7 
for i in range(0,n):
    for j in range(0,i+1):
     print("*",end="")
    print()""" 
    
    
"""def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # If the number is divisible by any number in this range, it's not prime

    return True  # If the number isn't divisible by any number in the range, it's prime

# Example usage:
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")"""  
    
    
    
"""from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Registration Form")


Fullname=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()



def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   prog=var1.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Programming) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog,))
   conn.commit()
   
   
             
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=280)

label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var2= IntVar()
Checkbutton(root, text="java", variable=var1).place(x=235,y=330)

Checkbutton(root, text="python", variable=var2).place(x=290,y=330)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)

root.mainloop()"""


"""name ='Nagendra'
age=23
a=20 
b=43
fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange') 
print(fruits)
print(f"My name is {name} iam {age} years old")
print(name)
print(a+b)
cars =['honda','toyata','suzuki']
print(cars)
print(cars[0])
name=input('my name is?')
print(name)"""

"""class person:
  def __init__(self, name, age):
    self.name=name
    self.age=age
p1=person("Nagendra",23)
print(p1.name)
print(p1.age)""" 


"""from flask import Flask 
app=Flask(__name__)

@app.route('/')
def Hello_World():
    return 'Hello World '

if __name__ == '__main__':
    
     app.run()"""
     
"""from flask import Flask, redirect, url_for, request
app = Flask(__name__)
 
 
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name
 
 
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
 
 
if __name__ == '__main__':
    app.run(debug=True)"""
    
    
  
"""from flask import Flask, render_template
app = Flask(__name__)  
 
@app.route('/')  
def message():  
 #return "<html><body><h1>Hii My name is Palla Nagendra</h1></body></html>"  
 return render_template('login.html')
  
if __name__ =="__main__":  
    app.run(debug = True) """ 
    
    
    
    
"""from flask import *  
   
app = Flask(__name__)  
  
@app.route('/admin')  
def admin():  
    return 'admin'  
  
@app.route('/librarion')  
def librarion():  
    return 'librarion'  
  
@app.route('/student')  
def student():  
    return 'student'  
  
@app.route('/user/<name>')  
def user(name):  
    if name == 'admin':  
        return redirect(url_for('admin'))  
    if name == 'librarion':  
        return redirect(url_for('librarion'))  
    if name == 'student':  
        return redirect(url_for('student'))  
if __name__ =='__main__':  
    app.run(debug = True) """ 
    
    
"""from flask import *  
app = Flask(__name__)  
  
@app.route('/login',methods = ['POST','GET'])  
def login():  
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="ayush" and passwrd=="google":  
          return "Welcome %s" %uname  
   
if __name__ == '__main__':  
   app.run(debug = True)  """
   
   
"""num=int(input("Enter a number: "))
p=0
for i in range(2,num):
    if num%i==0:
        p=1
        break
if p==0:
        print("this is a prime no.")
else:
        print("this is a not prime no.")"""  

"""n=int(input("enter a number:"))
if n%2==0:
    print("given number is even:")
else:
    print("given number is odd:")"""  


"""n=int(input("enter a number:"))  
fact=1
for i in range(1,n+1):
    fact=fact*i
#print(fact) 
print("the factorial of" ,n, "is:",fact)""" 

"""num=int(input("enter a number:"))
sum=0
for i in range(1,num+1):
    sum+=i
print("sum of n numbers is:",sum)"""  

"""num=int(input("enter a number:"))
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=int(num/10)
print(sum)"""  

#num=int(input("enter a number:"))

"""n1,n2=0,1-
print("the series is",n1,n2,end=" ")
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
print()"""  

"""sum=0 
temp=num 
while temp > 0:
    digit =temp % 10
    sum +=digit **3 
    temp //=10
if num==sum:
     print("it is a aremstrong no:")
else:
    print("nag")""" 
    
    
print(2**3)

    


   