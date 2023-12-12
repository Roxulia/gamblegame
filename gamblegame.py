from tkinter import *
import tkinter.font as F
import tkinter.messagebox as mb
import random as rand

class point:
    total=0

selectNumber=0
betAmount=0
app=Tk()
app.geometry('800x400+250+250')
app.title('Gambling Game')

start=Frame(app,width=800,height=400)
menu=Frame(app)
game1=Frame(app)
game2=Frame(app)

for frame in (start,menu,game1,game2):
    frame.grid(row=0,column=0,sticky='nesw')

start.tkraise()
#for start page
lblpt=Label(start,text='Points - '+str(point.total),font=F.Font(size=12,weight='bold'))
lblpt.place(x=650,y=10)
lblpt1=Label(menu,text='Points - '+str(point.total),font=F.Font(size=12,weight='bold'))
lblpt1.place(x=650,y=10)
lblpt2=Label(game1,text='Points - '+str(point.total),font=F.Font(size=12,weight='bold'))
lblpt2.place(x=650,y=10)
lblpt3=Label(game2,text='Points - '+str(point.total),font=F.Font(size=12,weight='bold'))
lblpt3.place(x=650,y=10)
Label(start,text='Enter amount of cash ',font=F.Font(size=20,weight='bold')).place(x=100,y=150)
input1=Entry(start,width=15,justify=RIGHT,font=F.Font(size=15,weight='bold'))
input1.place(x=400,y=155)
btnChange=Button(start,text='Convert',font=F.Font(size=12,weight='bold'))
btnChange.place(x=600,y=150)
btnGame=Button(start,text='Enter Game',borderwidth=0,font=F.Font(size=20,weight='bold',slant='italic'),fg='#cd1122')
btnGame.place(x=350,y=250)

def CTP():
    global input1,lblpt
    value=input1.get()
    if(not value.isnumeric()):
        mb.showerror(title='Invalid',message='Invalid Input')
    else:
        if(int(value)<0):
            mb.showerror(title='Invalid',message='Input cant be less than 0')
        else:
            point.total+=int(value)+int(int(value)/10)
            lblpt.configure(text='Points - '+str(point.total))
            input1.delete(0,'end')

def changeFrame(name,num):
    if(num):
        name.tkraise()
    else:
        res=mb.askyesno(title='Confirm pls',message='Are u sure u want to exit?')
        if(res==True):
            name.tkraise()
            reset1()
            reset2()

    lblpt.configure(text='Points - ' + str(point.total))
    lblpt1.configure(text='Points - ' + str(point.total))
    lblpt2.configure(text='Points - ' + str(point.total))
    lblpt3.configure(text='Points - ' + str(point.total))

btnChange.configure(command=CTP)
btnGame.configure(command=lambda:changeFrame(menu,True))

#for menu
Button(menu,text='Back',borderwidth=0,font=F.Font(size=20,weight='bold',slant='italic'),fg='#cd1212',activeforeground='#55aaff',command=lambda:changeFrame(start,True)).place(x=400,y=300)
Button(menu,text='Play\nGame 1',borderwidth=0,font=F.Font(size=20,weight='bold',slant='italic'),fg='#efcd55',activeforeground='#55ff55',command=lambda : changeFrame(game1,True)).place(x=200,y=150)
Button(menu,text='Play\nGame 2',borderwidth=0,font=F.Font(size=20,weight='bold',slant='italic'),fg='#efcd55',activeforeground='#55ff55',command=lambda : changeFrame(game2,True)).place(x=500,y=150)

#for game 1
Button(game1,text='Back',borderwidth=0,font=F.Font(size=20,weight='bold',slant='italic'),fg='#cd1212',activeforeground='#55aaff',command=lambda:changeFrame(menu,False)).place(x=10,y=10)
lblres1=Label(game1,text='Result Number : ',font=F.Font(size=20,weight='bold'))
lblres1.place(x=150,y=125)
btnNum1=Button(game1,text='1',borderwidth=0,width=10,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=15))
btnNum1.place(x=100,y=250)
btnNum2=Button(game1,text='2',borderwidth=0,width=10,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=15))
btnNum2.place(x=200,y=250)
btnNum3=Button(game1,text='3',borderwidth=0,width=10,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=15))
btnNum3.place(x=300,y=250)
btnNum4=Button(game1,text='4',borderwidth=0,width=10,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=15))
btnNum4.place(x=400,y=250)
btnNum5=Button(game1,text='5',borderwidth=0,width=10,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=15))
btnNum5.place(x=500,y=250)
btnNum6=Button(game1,text='6',borderwidth=0,width=10,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=15))
btnNum6.place(x=600,y=250)
buttons=[btnNum1,btnNum2,btnNum3,btnNum4,btnNum5,btnNum6]
inputBet1=Entry(game1,justify=RIGHT,font=F.Font(size=15,weight='bold'))
inputBet1.place(x=275,y=205)
btnBet1=Button(game1,text='BET',borderwidth=0,fg='#cd1212',activeforeground='#1212cd',font=F.Font(size=15,weight='bold'),state=DISABLED)
btnBet1.place(x=500,y=200)
btnSG1=Button(game1,text='Start Game',borderwidth=0,fg='#cd1212',activeforeground='#1212cd',font=F.Font(size=15,weight='bold'),state=DISABLED)
btnSG1.place(x=600,y=200)


def selectNum1(n):
    global buttons,selectNumber
    selectNumber =n+1
    print('selected number = '+str(n+1))
    i=0
    while i<6:
        if(i != n):
            buttons[i].configure(bg='#00aaff',fg='#ff0000',state=NORMAL)
        else:
            buttons[i].configure(bg='#ff0000',fg='#00aaff',state=DISABLED)
        i+=1
    btnBet1.configure(state=NORMAL)

def bet1():
    global betAmount,buttons
    b=inputBet1.get()
    if(not b.isnumeric()):
        b=0
    else:
        if(int(b)>point.total):
            mb.showerror(title='Invalid',message='Not Enough Points')
        else:
            point.total -= int(b)
            betAmount = int(b)
            lblpt2.configure(text='Points - ' + str(point.total))
            btnSG1.configure(state=NORMAL)
            btnBet1.configure(state=DISABLED)
            for btn in buttons:
                btn.configure(state=DISABLED)

def reset1():
    global buttons,btnBet1,btnSG1,lblres1
    lblpt2.configure(text='Points - '+str(point.total))
    for btn in buttons:
        btn.configure(bg='#00aaff',fg='#ff0000',state=NORMAL)
    btnBet1.configure(state=DISABLED)
    btnSG1.configure(state=DISABLED)
    lblres1.configure(text='Result Number : ')
    inputBet1.delete(0,'end')

def startGame1():
    global lblres1,selectNumber
    num=0
    for i in range(12):
        num = rand.randint(1, 6)
    lblres1.configure(text='Result Number : '+str(num))
    print('SN-'+str(selectNumber))
    if(num==selectNumber):
        point.total+=betAmount*5
        mb.showinfo(title='Congratulation',message='U win'+str(betAmount*5))
    else:
        mb.showinfo(title='Sad',message='U lost !!')
    reset1()

btnNum1.configure(command=lambda :selectNum1(0))
btnNum2.configure(command=lambda :selectNum1(1))
btnNum3.configure(command=lambda :selectNum1(2))
btnNum4.configure(command=lambda :selectNum1(3))
btnNum5.configure(command=lambda :selectNum1(4))
btnNum6.configure(command=lambda :selectNum1(5))
btnBet1.configure(command=bet1)
btnSG1.configure(command=startGame1)

#for game 2

Button(game2,text='Back',borderwidth=0,font=F.Font(size=20,weight='bold',slant='italic'),fg='#cd1212',activeforeground='#55aaff',command=lambda:changeFrame(menu,False)).place(x=10,y=10)
lblres2=Label(game2,text='Result Number : ',font=F.Font(size=20,weight='bold'))
lblres2.place(x=150,y=125)
#btnN1=Button(game2,text='1',borderwidth=0,width=5,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=11))
#btnN1.place(x=50,y=250)
btnN2=Button(game2,text='2',borderwidth=0,width=5,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=11))
btnN2.place(x=100,y=250)
btnN3=Button(game2,text='3',borderwidth=0,width=5,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=11))
btnN3.place(x=150,y=250)
btnN4=Button(game2,text='4',borderwidth=0,width=5,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=11))
btnN4.place(x=200,y=250)
btnN5=Button(game2,text='5',borderwidth=0,width=5,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=11))
btnN5.place(x=250,y=250)
btnN6=Button(game2,text='6',borderwidth=0,width=5,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=11))
btnN6.place(x=300,y=250)
btnN7=Button(game2,text='7',borderwidth=0,width=5,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=11))
btnN7.place(x=350,y=250)
btnN8=Button(game2,text='8',borderwidth=0,width=5,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=11))
btnN8.place(x=400,y=250)
btnN9=Button(game2,text='9',borderwidth=0,width=5,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=11))
btnN9.place(x=450,y=250)
btnN10=Button(game2,text='10',borderwidth=0,width=5,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=11))
btnN10.place(x=500,y=250)
btnN11=Button(game2,text='11',borderwidth=0,width=5,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=11))
btnN11.place(x=550,y=250)
btnN12=Button(game2,text='12',borderwidth=0,width=5,height=5,bg='#00aaff',fg='#ff0000',font=F.Font(size=11))
btnN12.place(x=600,y=250)
buttons2=[btnN2,btnN3,btnN4,btnN5,btnN6,btnN7,btnN8,btnN9,btnN10,btnN11,btnN12]
inputBet2=Entry(game2,justify=RIGHT,font=F.Font(size=15,weight='bold'))
inputBet2.place(x=275,y=205)
btnBet2=Button(game2,text='BET',borderwidth=0,fg='#cd1212',activeforeground='#1212cd',font=F.Font(size=15,weight='bold'),state=DISABLED)
btnBet2.place(x=500,y=200)
btnSG2=Button(game2,text='Start Game',borderwidth=0,fg='#cd1212',activeforeground='#1212cd',font=F.Font(size=15,weight='bold'),state=DISABLED)
btnSG2.place(x=600,y=200)


def selectNum2(n):
    global buttons2,selectNumber
    selectNumber =n+2
    #print('selected number = '+str(n+1))
    i=0
    while i<11:
        if(i != n):
            buttons2[i].configure(bg='#00aaff',fg='#ff0000',state=NORMAL)
        else:
            buttons2[i].configure(bg='#ff0000',fg='#00aaff',state=DISABLED)
        i+=1
    btnBet2.configure(state=NORMAL)

def bet2():
    global betAmount,buttons2
    b=inputBet2.get()
    if(not b.isnumeric()):
        b=0
    else:
        if(int(b)>point.total):
            mb.showerror(title='Invalid',message='Not Enough Points')
        else:
            point.total -= int(b)
            betAmount = int(b)
            lblpt3.configure(text='Points - ' + str(point.total))
            btnSG2.configure(state=NORMAL)
            btnBet2.configure(state=DISABLED)
            for btn in buttons2:
                btn.configure(state=DISABLED)

def reset2():
    global buttons2,btnBet2,btnSG2,lblres2
    lblpt3.configure(text='Points - '+str(point.total))
    for btn in buttons2:
        btn.configure(bg='#00aaff',fg='#ff0000',state=NORMAL)
    btnBet2.configure(state=DISABLED)
    btnSG2.configure(state=DISABLED)
    lblres2.configure(text='Result Number : ')
    inputBet2.delete(0,'end')

def startGame2():
    global lblres2,selectNumber
    num=0
    for i in range(12):
        num = rand.randint(2, 12)
    lblres2.configure(text='Result Number : '+str(num))
    print('SN-'+str(selectNumber))
    if(num==selectNumber):
        point.total+=betAmount*10
        mb.showinfo(title='Congratulation',message='U win'+str(betAmount*10))
    else:
        mb.showinfo(title='Sad',message='U lost !!')
    reset2()

#btnNum1.configure(command=lambda :selectNum1(0))
btnN2.configure(command=lambda :selectNum2(0))
btnN3.configure(command=lambda :selectNum2(1))
btnN4.configure(command=lambda :selectNum2(2))
btnN5.configure(command=lambda :selectNum2(3))
btnN6.configure(command=lambda :selectNum2(4))
btnN7.configure(command=lambda :selectNum2(5))
btnN8.configure(command=lambda :selectNum2(6))
btnN9.configure(command=lambda :selectNum2(7))
btnN10.configure(command=lambda :selectNum2(8))
btnN11.configure(command=lambda :selectNum2(9))
btnN12.configure(command=lambda :selectNum2(10))
btnBet2.configure(command=bet2)
btnSG2.configure(command=startGame2)

app.mainloop()