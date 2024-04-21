import random 
from tkinter import*
import tkinter as tk
from tkinter import messagebox
from typing import Sized

class SPS_game:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x500+0+0")
        self.root.title("Stone, Papper, Sissor")
        self.root.resizable(False,False)
        self.Lst=["Stone","Paper","Scissor"]
        bg_color="#A7FF19"

        self.state=IntVar(value=0)
        self.player_img=tk.PhotoImage(file="blank.png")
        self.computer_img=tk.PhotoImage(file="blank.png")

        F1=LabelFrame(self.root,relief=GROOVE,bd=10,bg=bg_color)
        F1.place(x=0,y=0,height=500,width=700)

        F3=LabelFrame(F1,relief=GROOVE,bd=10)
        F3.place(x=0,y=0,height=300, width=250)
        player=Label(F3,text="Player",bd=12,relief=GROOVE,fg="black",font=("times new roman",20,"bold")).pack(fill=X)
        self.img1=Label(F3,image=self.player_img)
        self.img1.pack()
        self.img1.image=self.player_img


        vs=Label(F1,text="V/s", fg="black",font=("times new roman",30,"bold"),bg=bg_color)
        vs.place(x=300,y=150)

        F4=LabelFrame(F1,relief=GROOVE,bd=10)
        F4.place(x=420,y=0,height=300, width=250)
        computer=Label(F4,text="Computer",bd=12,relief=GROOVE,fg="black",font=("times new roman",20,"bold")).pack(fill=X)
        self.img2=Label(F4,image=self.computer_img)
        self.img2.pack()
        self.img2.image=self.computer_img


        r_b1=Radiobutton(F1,text="Stone",variable=self.state,value=1,font=("times new roman",15,"bold"),command=self.stone,bg=bg_color).place(x=200,y=350)
        r_b2=Radiobutton(F1,text="Paper",variable=self.state,value=2,font=("times new roman",15,"bold"),command=self.paper,bg=bg_color).place(x=300,y=350)
        r_b3=Radiobutton(F1,text="Scissor",variable=self.state,value=3,font=("times new roman",15,"bold"),command=self.scissor,bg=bg_color).place(x=400,y=350)

        b1=Button(F1,text="New_game",command=self.new_game,bg="#FFF01F",fg="Black",width=11,font=("arial",12,"bold")).place(x=120,y=420)
        b2=Button(F1,text="EXIT",command=self.close_window,bg="#FFF01F",fg="Black",width=11,font=("arial",12,"bold")).place(x=420,y=420)



        F2=Frame(self.root,bd=10,relief=GROOVE,bg=bg_color)
        F2.place(x=710,y=0,height=500,width=290)
        score_title=Label(F2,text="Score", font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F2,orient=VERTICAL)
        self.txtarea=Text(F2,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)



    def stone(self):
        self.state.set(0)
        self.s_choice = random.choice(self.Lst)
        self.player_img = tk.PhotoImage(file="Stone.png")
        self.img1.config(image=self.player_img) 
        self.img1.image = self.player_img
        self.computer_img = tk.PhotoImage(file=f"{self.s_choice}.png")
        self.img2.config(image=self.computer_img)
        self.img2.image = self.computer_img
        
    def paper(self):
        self.state.set(0)
        self.s_choice = random.choice(self.Lst)
        self.player_img = tk.PhotoImage(file="Paper.png")
        self.img1.config(image=self.player_img) 
        self.img1.image = self.player_img
        self.computer_img = tk.PhotoImage(file=f"{self.s_choice}.png")
        self.img2.config(image=self.computer_img)
        self.img2.image = self.computer_img

    def scissor(self):
        self.state.set(0)
        self.s_choice = random.choice(self.Lst)
        self.player_img = tk.PhotoImage(file="Scissor.png")
        self.img1.config(image=self.player_img) 
        self.img1.image = self.player_img
        self.computer_img = tk.PhotoImage(file=f"{self.s_choice}.png")
        self.img2.config(image=self.computer_img)
        self.img2.image = self.computer_img

    def new_game(self):
        result=messagebox.askyesno("Confirmation", "Do you want to start a New Game:")
        
        if result:
                self.txtarea.set(command=root.destroy)
        else:
                print("No button clicked")
        

    def close_window(self):
        root.destroy()
    
root=Tk()
obj=SPS_game(root)
root.mainloop()