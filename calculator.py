from tkinter import *
from tkinter import ttk

class calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("calculator")
        self.grid()
        self.p1 = PhotoImage(file ="cal.png")
        self.master.iconphoto(False, self.p1)

        self.data=StringVar()
        self.value=[]
        self.data.set("")
        self.op=" "
        self.entry=ttk.Entry(self,textvariable=self.data,width=40)
        self.entry.grid(row=0,column=0,columnspan=3)
        
        self.buttonc=Button(self,text="c",command=self.clear,width=10)
        self.buttonc.grid(row=0,column=3,columnspan=1)


        self.button7=Button(self,text="7",command=self.num7,width=10)
        self.button7.grid(row=1,column=0,columnspan=1)

        self.button8=Button(self,text="8",command=self.num8,width=10)
        self.button8.grid(row=1,column=1,columnspan=1)

        self.button9=Button(self,text="9",command=self.num9,width=10)
        self.button9.grid(row=1,column=2,columnspan=1)
        
        self.buttonp=Button(self,text="+",command=self.plus,width=10)
        self.buttonp.grid(row=1,column=3,columnspan=1)

        
        self.button4=Button(self,text="4",command=self.num4,width=10)
        self.button4.grid(row=2,column=0,columnspan=1)

        self.button5=Button(self,text="5",command=self.num5,width=10)
        self.button5.grid(row=2,column=1,columnspan=1)

        self.button6=Button(self,text="6",command=self.num6,width=10)
        self.button6.grid(row=2,column=2,columnspan=1)

        self.buttonm=Button(self,text="-",command=self.minus,width=10)
        self.buttonm.grid(row=2,column=3,columnspan=1)


        self.button1=Button(self,text="1",command=self.num1,width=10)
        self.button1.grid(row=3,column=0,columnspan=1)

        self.button2=Button(self,text="2",command=self.num2,width=10)
        self.button2.grid(row=3,column=1,columnspan=1)

        self.button3=Button(self,text="3",command=self.num3,width=10)
        self.button3.grid(row=3,column=2,columnspan=1)

        self.buttonx=Button(self,text="x",command=self.multi,width=10)
        self.buttonx.grid(row=3,column=3,columnspan=1)


        self.button0=Button(self,text="0",command=self.num0,width=10)
        self.button0.grid(row=4,column=0,columnspan=1)

        self.buttond=Button(self,text=".",command=self.dot,width=10)
        self.buttond.grid(row=4,column=1,columnspan=1)

        self.buttone=Button(self,text="=",command=self.equal,width=10)
        self.buttone.grid(row=4,column=2,columnspan=1)

        self.buttonb=Button(self,text="/",command=self.div,width=10)
        self.buttonb.grid(row=4,column=3,columnspan=1)
        
    def num1(self):
        self.data.set(self.data.get()+"1")

    def num2(self):
        self.data.set(self.data.get()+"2")
    
    def num3(self):
        self.data.set(self.data.get()+"3")
    
    def num4(self):
        self.data.set(self.data.get()+"4")

    def num5(self):
        self.data.set(self.data.get()+"5")
    
    def num6(self):
        self.data.set(self.data.get()+"6")
    
    def num7(self):
        self.data.set(self.data.get()+"7")

    def num8(self):
        self.data.set(self.data.get()+"8")
    
    def num9(self):
        self.data.set(self.data.get()+"9")

    def num0(self):
        self.data.set(self.data.get()+"0")

    def dot(self):
        self.data.set(self.data.get()+".")

    def plus(self):
        self.n=len(self.value)
        if self.n<1:
            self.value.append(float(self.data.get()))
            self.op='+'
            self.data.set("")
        else:
            if self.op=="+":
                self.value.append(float(self.data.get()))
                self.value[0]=self.value[0]+self.value[1]
                self.value.pop()
                self.op="+"
                self.data.set("")
            elif self.op=="-":
                self.value.append(float(self.data.get()))
                self.value[0]=self.value[0]-self.value[1]
                self.value.pop()
                self.op="+"
                self.data.set("")
            elif self.op=="x":
                self.value.append(float(self.data.get()))
                self.value[0]=self.value[0]-self.value[1]
                self.value.pop()
                self.op="+"
                self.data.set("")
            elif self.op=="/":
                self.value.append(float(self.data.get()))
                if self.value!=0:
                    self.value[0]=self.value[0]/self.value[1]
                    self.value.pop()
                    self.op="+"
                    self.data.set("")
                else:
                    self.data.set("MATH ERROR!!")
                    self.clear()

    def minus(self):
        self.n=len(self.value)
        if self.n<1:
            self.value.append(float(self.data.get()))
            self.op='-'
            self.data.set("")
        else:
            if self.op=="+":
                self.value.append(float(self.data.get()))
                self.value[0]=self.value[0]+self.value[1]
                self.value.pop()
                self.op="-"
                self.data.set("")
            elif self.op=="-":
                self.value.append(float(self.data.get()))
                self.value[0]=self.value[0]-self.value[1]
                self.value.pop()
                self.op="-"
                self.data.set("")
            elif self.op=="x":
                self.value.append(float(self.data.get()))
                self.value[0]=self.value[0]-self.value[1]
                self.value.pop()
                self.op="-"
                self.data.set("")
            elif self.op=="/":
                self.value.append(float(self.data.get()))
                if self.value!=0:
                    self.value[0]=self.value[0]/self.value[1]
                    self.value.pop()
                    self.op="-"
                    self.data.set("")
                else:
                    self.data.set("MATH ERROR!!")
                    self.clear()

    def multi(self):
        self.n=len(self.value)
        if self.n<1:
            self.value.append(float(self.data.get()))
            self.op='x'
            self.data.set("")
        else:
            if self.op=="+":
                self.value.append(float(self.data.get()))
                self.value[0]=self.value[0]+self.value[1]
                self.value.pop()
                self.op="x"
                self.data.set("")
            elif self.op=="-":
                self.value.append(float(self.data.get()))
                self.value[0]=self.value[0]-self.value[1]
                self.value.pop()
                self.op="x"
                self.data.set("")
            elif self.op=="x":
                self.value.append(float(self.data.get()))
                self.value[0]=self.value[0]-self.value[1]
                self.value.pop()
                self.op="x"
                self.data.set("")
            elif self.op=="/":
                self.value.append(float(self.data.get()))
                if self.value!=0:
                    self.value[0]=self.value[0]/self.value[1]
                    self.value.pop()
                    self.op="x"
                    self.data.set("")
                else:
                    self.data.set("MATH ERROR!!")
                    self.clear()

    def div(self):
        self.n=len(self.value)
        if self.n<1:
            self.value.append(float(self.data.get()))
            self.op='/'
            self.data.set("")
        else:
            if self.op=="+":
                self.value.append(float(self.data.get()))
                self.value[0]=self.value[0]+self.value[1]
                self.value.pop()
                self.op="/"
                self.data.set("")
            elif self.op=="-":
                self.value.append(float(self.data.get()))
                self.value[0]=self.value[0]-self.value[1]
                self.value.pop()
                self.op="/"
                self.data.set("")
            elif self.op=="x":
                self.value.append(float(self.data.get()))
                self.value[0]=self.value[0]-self.value[1]
                self.value.pop()
                self.op="/"
                self.data.set("")
            elif self.op=="/":
                self.value.append(float(self.data.get()))
                if self.value!=0:
                    self.value[0]=self.value[0]/self.value[1]
                    self.value.pop()
                    self.op="/"
                    self.data.set("")
                else:
                    self.data.set("MATH ERROR!!")
                    self.clear()

    def equal(self):
        self.value.append(float(self.data.get()))
        if self.op=='+':
            self.value[0]=self.value[0]+self.value[1]
            self.value.pop()
            self.data.set(str(self.value[0]))
            self.value.pop()
        elif self.op=='-':
            self.value[0]=self.value[0]-self.value[1]
            self.value.pop()
            self.data.set(str(self.value[0]))
            self.value.pop()
        elif self.op=='x':
            self.value[0]=self.value[0]*self.value[1]
            self.value.pop()
            self.data.set(str(self.value[0]))
            self.value.pop()
        elif self.op=='/':
            if self.value[1]!=0:
                self.value[0]=self.value[0]/self.value[1]
                self.value.pop()
                self.data.set(str(self.value[0]))
                self.value.pop()
            else:
                self.data.set("MATH ERROR")
                self.clear()
        
        
    def clear(self):
        self.data.set("") 
        self.n=len(self.value)
        for i in range(self.n):
            self.value.pop()

    


def main():
    calculator().mainloop()

main()