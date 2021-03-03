import tkinter

from tkinter import *

def start1():
    label1.destroy()
    rules.destroy()
    bt1.destroy()
    bt2.destroy()
    bt3.destroy()
    start4()
def start2():
    label1.destroy()
    rules.destroy()
    bt1.destroy()
    bt2.destroy()
    bt3.destroy()
    start5()
def start3():
    label1.destroy()
    rules.destroy()
    bt1.destroy()
    bt2.destroy()
    bt3.destroy()
    start6()
root=tkinter.Tk()
root.title('Quiz')

label1=Label(root,text='Welcome To The Quiz',font=('Algerian',50),)
label1.grid(row=0,column=50)
rules=Label(root, text='The rules of the quiz are:\n * Select any topic given below \n  *Each correct answer selected will give one point' ,font=30)
rules.grid()

bt1=Button(text='Topic 1',command=start1,font=40,bg='red')
bt1.grid(row=60,column=10)
bt2=Button(text='Topic 2',command=start2,font=40,bg='blue')
bt2.grid(row=60,column=15)
bt3=Button(text='Topic 3',command=start3,font=40,bg='green')
bt3.grid(row=60,column=20)

count=0

def start4():
    global q1,btnext,r1,r2,r3,r4
    q1=Label(text='question1',font=30)
    q1.grid()

    r1=Radiobutton(root,text='option1',font=20,value=0)
    r1.grid(row=4,column=2)
    r2=Radiobutton(root,text='option2',font=20,value=1)
    r2.grid(row=4,column=42)
    r3=Radiobutton(root,text='option3',font=20,value=2)
    r3.grid(row=7,column=2)
    r4=Radiobutton(root,text='option4',font=20,value=3)
    r4.grid(row=7,column=42)
    btnext=Button(text='Next',command=nextq,font=20)
    btnext.grid(row=15,column=50)
def nextq():
        q1.destroy()
        btnext.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        question2()

def question2():
    global q2,btnext,r1,r2,r3,r4
    q2=Label(text='question2',font=30)
    q2.grid()

    r1=Radiobutton(root,text='option1',font=20,value=0)
    r1.grid(row=4,column=2)
    r2=Radiobutton(root,text='option2',font=20,value=1)
    r2.grid(row=4,column=42)
    r3=Radiobutton(root,text='option3',font=20,value=2)
    r3.grid(row=7,column=2)
    r4=Radiobutton(root,text='option4',font=20,value=3)
    r4.grid(row=7,column=42)
    btnext=Button(text='Next',command=nextq1,font=20)
    btnext.grid(row=15,column=50)

def nextq1():
        q2.destroy()
        btnext.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        question3()



def question3():
    global q3,btnext,r1,r2,r3,r4
    q3=Label(text='question3',font=30)
    q3.grid()

    r1=Radiobutton(root,text='option1',font=20,value=0)
    r1.grid(row=4,column=2)
    r2=Radiobutton(root,text='option2',font=20,value=1)
    r2.grid(row=4,column=42)
    r3=Radiobutton(root,text='option3',font=20,value=2)
    r3.grid(row=7,column=2)
    r4=Radiobutton(root,text='option4',font=20,value=3)
    r4.grid(row=7,column=42)
    btnext=Button(text='Next',command=nextq2,font=20)
    btnext.grid(row=15,column=50)

def nextq2():
        q3.destroy()
        btnext.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        question4()

def question4():
    global q4,btnext,r1,r2,r3,r4
    q4=Label(text='question4',font=30)
    q4.grid()

    r1=Radiobutton(root,text='option1',font=20,value=0)
    r1.grid(row=4,column=2)
    r2=Radiobutton(root,text='option2',font=20,value=1)
    r2.grid(row=4,column=42)
    r3=Radiobutton(root,text='option3',font=20,value=2)
    r3.grid(row=7,column=2)
    r4=Radiobutton(root,text='option4',font=20,value=3)
    r4.grid(row=7,column=42)
    btnext=Button(text='Next',command=nextq3,font=20)
    btnext.grid(row=15,column=50)

def nextq3():
        q4.destroy()
        btnext.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        question5()

def question5():
    global q5,btsubmit,r1,r2,r3,r4
    q5=Label(text='question5',font=30)
    q5.grid()

    r1=Radiobutton(root,text='option1',font=20,value=0)
    r1.grid(row=4,column=2)
    r2=Radiobutton(root,text='option2',font=20,value=1)
    r2.grid(row=4,column=42)
    r3=Radiobutton(root,text='option3',font=20,value=2)
    r3.grid(row=7,column=2)
    r4=Radiobutton(root,text='option4',font=20,value=3)
    r4.grid(row=7,column=42)
    btsubmit=Button(text='Submit',command=nextq4,font=20)
    btsubmit.grid(row=15,column=50)

def nextq4():
        q5.destroy()
        btsubmit.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()

def start5():
    global q1,btnext,r1,r2,r3,r4
    q1=Label(text='question1',font=30)
    q1.grid()

    r1=Radiobutton(root,text='option1',font=20,value=0)
    r1.grid(row=4,column=2)
    r2=Radiobutton(root,text='option2',font=20,value=1)
    r2.grid(row=4,column=42)
    r3=Radiobutton(root,text='option3',font=20,value=2)
    r3.grid(row=7,column=2)
    r4=Radiobutton(root,text='option4',font=20,value=3)
    r4.grid(row=7,column=42)
    btnext=Button(text='Next',command=nextq,font=20)
    btnext.grid(row=15,column=50)
def nextq():
        q1.destroy()
        btnext.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        question2()

def question2():
    global q2,btnext,r1,r2,r3,r4
    q2=Label(text='question2',font=30)
    q2.grid()

    r1=Radiobutton(root,text='option1',font=20,value=0)
    r1.grid(row=4,column=2)
    r2=Radiobutton(root,text='option2',font=20,value=1)
    r2.grid(row=4,column=42)
    r3=Radiobutton(root,text='option3',font=20,value=2)
    r3.grid(row=7,column=2)
    r4=Radiobutton(root,text='option4',font=20,value=3)
    r4.grid(row=7,column=42)
    btnext=Button(text='Next',command=nextq1,font=20)
    btnext.grid(row=15,column=50)

def nextq1():
        q2.destroy()
        btnext.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        question3()



def question3():
    global q3,btnext,r1,r2,r3,r4
    q3=Label(text='question3',font=30)
    q3.grid()

    r1=Radiobutton(root,text='option1',font=20,value=0)
    r1.grid(row=4,column=2)
    r2=Radiobutton(root,text='option2',font=20,value=1)
    r2.grid(row=4,column=42)
    r3=Radiobutton(root,text='option3',font=20,value=2)
    r3.grid(row=7,column=2)
    r4=Radiobutton(root,text='option4',font=20,value=3)
    r4.grid(row=7,column=42)
    btnext=Button(text='Next',command=nextq2,font=20)
    btnext.grid(row=15,column=50)

def nextq2():
        q3.destroy()
        btnext.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        question4()

def question4():
    global q4,btnext,r1,r2,r3,r4
    q4=Label(text='question4',font=30)
    q4.grid()

    r1=Radiobutton(root,text='option1',font=20,value=0)
    r1.grid(row=4,column=2)
    r2=Radiobutton(root,text='option2',font=20,value=1)
    r2.grid(row=4,column=42)
    r3=Radiobutton(root,text='option3',font=20,value=2)
    r3.grid(row=7,column=2)
    r4=Radiobutton(root,text='option4',font=20,value=3)
    r4.grid(row=7,column=42)
    btnext=Button(text='Next',command=nextq3,font=20)
    btnext.grid(row=15,column=50)

def nextq3():
        q4.destroy()
        btnext.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        question5()

def question5():
    global q5,btsubmit,r1,r2,r3,r4
    q5=Label(text='question5',font=30)
    q5.grid()

    r1=Radiobutton(root,text='option1',font=20,value=0)
    r1.grid(row=4,column=2)
    r2=Radiobutton(root,text='option2',font=20,value=1)
    r2.grid(row=4,column=42)
    r3=Radiobutton(root,text='option3',font=20,value=2)
    r3.grid(row=7,column=2)
    r4=Radiobutton(root,text='option4',font=20,value=3)
    r4.grid(row=7,column=42)
    btsubmit=Button(text='Submit',command=nextq4,font=20)
    btsubmit.grid(row=15,column=50)

def nextq4():
        q5.destroy()
        btsubmit.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
def start6():
    global q1,btnext,r1,r2,r3,r4
    q1=Label(text='question1',font=30)
    q1.grid()

    r1=Radiobutton(root,text='option1',font=20,value=0)
    r1.grid(row=4,column=2)
    r2=Radiobutton(root,text='option2',font=20,value=1)
    r2.grid(row=4,column=42)
    r3=Radiobutton(root,text='option3',font=20,value=2)
    r3.grid(row=7,column=2)
    r4=Radiobutton(root,text='option4',font=20,value=3)
    r4.grid(row=7,column=42)
    btnext=Button(text='Next',command=nextq,font=20)
    btnext.grid(row=15,column=50)
def nextq():
        q1.destroy()
        btnext.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        question2()

def question2():
    global q2,btnext,r1,r2,r3,r4
    q2=Label(text='question2',font=30)
    q2.grid()

    r1=Radiobutton(root,text='option1',font=20,value=0)
    r1.grid(row=4,column=2)
    r2=Radiobutton(root,text='option2',font=20,value=1)
    r2.grid(row=4,column=42)
    r3=Radiobutton(root,text='option3',font=20,value=2)
    r3.grid(row=7,column=2)
    r4=Radiobutton(root,text='option4',font=20,value=3)
    r4.grid(row=7,column=42)
    btnext=Button(text='Next',command=nextq1,font=20)
    btnext.grid(row=15,column=50)

def nextq1():
        q2.destroy()
        btnext.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        question3()



def question3():
    global q3,btnext,r1,r2,r3,r4
    q3=Label(text='question3',font=30)
    q3.grid()

    r1=Radiobutton(root,text='option1',font=20,value=0)
    r1.grid(row=4,column=2)
    r2=Radiobutton(root,text='option2',font=20,value=1)
    r2.grid(row=4,column=42)
    r3=Radiobutton(root,text='option3',font=20,value=2)
    r3.grid(row=7,column=2)
    r4=Radiobutton(root,text='option4',font=20,value=3)
    r4.grid(row=7,column=42)
    btnext=Button(text='Next',command=nextq2,font=20)
    btnext.grid(row=15,column=50)

def nextq2():
        q3.destroy()
        btnext.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        question4()

def question4():
    global q4,btnext,r1,r2,r3,r4
    q4=Label(text='question4',font=30)
    q4.grid()

    r1=Radiobutton(root,text='option1',font=20,value=0)
    r1.grid(row=4,column=2)
    r2=Radiobutton(root,text='option2',font=20,value=1)
    r2.grid(row=4,column=42)
    r3=Radiobutton(root,text='option3',font=20,value=2)
    r3.grid(row=7,column=2)
    r4=Radiobutton(root,text='option4',font=20,value=3)
    r4.grid(row=7,column=42)
    btnext=Button(text='Next',command=nextq3,font=20)
    btnext.grid(row=15,column=50)

def nextq3():
        q4.destroy()
        btnext.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        question5()

def question5():
    global q5,btsubmit,r1,r2,r3,r4
    q5=Label(text='question5',font=30)
    q5.grid()

    r1=Radiobutton(root,text='option1',font=20,value=0)
    r1.grid(row=4,column=2)
    r2=Radiobutton(root,text='option2',font=20,value=1)
    r2.grid(row=4,column=42)
    r3=Radiobutton(root,text='option3',font=20,value=2)
    r3.grid(row=7,column=2)
    r4=Radiobutton(root,text='option4',font=20,value=3)
    r4.grid(row=7,column=42)
    btsubmit=Button(text='Submit',command=nextq4,font=20)
    btsubmit.grid(row=15,column=50)

def nextq4():
        q5.destroy()
        btsubmit.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()



root.mainloop()
