from tkinter import*
from tkinter import messagebox
import random

class Random_pass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x300+0+0")
        self.root.title("Random Password")
        self.root.resizable(False,False)
        bg_color="#074463"


        self.letters=['a','b','c','d','e','f','g','h','i','j','k','l','m',
                      'n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.numbers=['0','1','2','3','4','5','6','7','8','9']
        self.symbols=['!','@','#','$','%','^','&','*','(',')','-','+']

        self.p_length=IntVar()
        self.r_state=IntVar(value=0)
        self.s_password=StringVar()
        self.pass_str=StringVar()
        self.l1=[]
        self.str=""

        title=Label(self.root,text="Password Generator",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill="x")
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        lbl1=Label(F1,text="Length",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        txt1=Entry(F1,width=15,textvariable=self.p_length,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5) 
        r_b1=Radiobutton(F1,text="Easy",variable=self.r_state,value=1).grid(row=1,column=0,padx=20,pady=5)
        r_b2=Radiobutton(F1,text="Medium",variable=self.r_state,value=2).grid(row=1,column=1,padx=20,pady=5)
        r_b3=Radiobutton(F1,text="Hard",variable=self.r_state,value=3).grid(row=1,column=2,padx=20,pady=5)
        txt2=Entry(F1,width=40,textvariable=self.s_password,font="arial 15",bd=7,relief=SUNKEN).grid(row=2,column=0,columnspan=3,padx=15,pady=5)
        Bll_btn=Button(F1,text="Generate",command=self.gen,bg="cadetblue",fg="white",bd=2,pady=10,width=11,font="arial 12 bold").grid(row=3,column=0,padx=5,pady=10)




    def gen(self):
        self.s_password.set("")
        self.pass_str.set("")
        self.l1.clear()
        self.str=""
        if(self.r_state.get()==0):
            messagebox.showerror("Error","Selection Expected (Easy/Medium/Hard)")

        if(self.r_state.get()==1):
            messagebox.showinfo("Information","Password Generates")
            if(self.p_length.get()==0):
                messagebox.showwarning("Warning","Length field cannot be kept Empty")

            elif(self.p_length.get()<6):
                messagebox.showinfo("Info","Length of password cannot be Below 6")
            elif(self.p_length.get()<11):
                self.l=self.p_length.get()
                for i in range(1,self.l+1):
                    self.ltr=random.choice(self.letters)
                    self.pass_str.set(self.pass_str.get() + self.ltr) 
                self.s_password.set(self.pass_str.get())  
            else:
                messagebox.showinfo("Info","Length should be less then 11")





        if(self.r_state.get()==2):
            messagebox.showinfo("Information","Password Generated")
            if(self.p_length.get()==0):
                messagebox.showwarning("Warning","Length field cannot be kept Empty")

            elif(self.p_length.get()<6):
                messagebox.showinfo("Info","Length of password cannot be Below 6")
            else:
                self.l=self.p_length.get()
                if (self.l<10):
                    for i in range(1,self.l-2):
                        self.ltr=random.choice(self.letters)
                        self.pass_str.set(self.pass_str.get() + self.ltr) 

                    for i in range(1,4):
                        self.num=random.choice(self.numbers)
                        self.pass_str.set(self.pass_str.get() + self.num)  

                elif(self.l<20):
                    for i in range(1,self.l-4):
                        self.ltr=random.choice(self.letters)
                        self.pass_str.set(self.pass_str.get() + self.ltr) 

                    for i in range(1,6):
                        self.num=random.choice(self.numbers)
                        self.pass_str.set(self.pass_str.get() + self.num)  

                else:
                    messagebox.showinfo("Info","Length should be less then 20")

                for i in self.pass_str.get():
                    self.l1+=i
                
                random.shuffle(self.l1)
                for i in self.l1:
                    self.str+=i
                self.s_password.set(self.str)




        if(self.r_state.get()==3):
            messagebox.showinfo("Information","Password Generated")
            if(self.p_length.get()==0):
                messagebox.showwarning("Warning","Length field cannot be kept Empty")

            elif(self.p_length.get()<8):
                messagebox.showinfo("Info","Length of password cannot be Below 6")
            else:
                self.l=self.p_length.get()
                if (self.l<12):
                    for i in range(1,self.l-5):
                        self.ltr=random.choice(self.letters)
                        self.pass_str.set(self.pass_str.get() + self.ltr) 

                    for i in range(1,4):
                        self.num=random.choice(self.numbers)
                        self.pass_str.set(self.pass_str.get() + self.num)
                    for i in range(1,4):
                        self.sym=random.choice(self.symbols)
                        self.pass_str.set(self.pass_str.get() + self.sym)  

                elif(self.l<20):
                    for i in range(1,self.l-7):
                        self.ltr=random.choice(self.letters)
                        self.pass_str.set(self.pass_str.get() + self.ltr) 

                    for i in range(1,5):
                        self.num=random.choice(self.numbers)
                        self.pass_str.set(self.pass_str.get() + self.num)  

                    for i in range(1,5):
                        self.sym=random.choice(self.symbols)
                        self.pass_str.set(self.pass_str.get() + self.sym) 

                else:
                    messagebox.showinfo("Info","Length should be less then 20")

                for i in self.pass_str.get():
                    self.l1+=i
                
                random.shuffle(self.l1)
                for i in self.l1:
                    self.str+=i
                self.s_password.set(self.str)
        
       

root=Tk()
obj=Random_pass(root)
root.mainloop()