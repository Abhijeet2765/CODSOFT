from tkinter import*
from tkinter import messagebox
import mysql.connector
from tkinter.tix import *
import customtkinter
from tkinter import ttk

class Contact_book:
    def __init__(self, root):
        self.root=root
        self.root.geometry("350x600+450+30")
        self.root.title("")
        bg_color="#212121"
        self.vectorimage1=PhotoImage(file="Search.png")
        self.vectorimage2=PhotoImage(file="Dot.png")
        self.vectorimage3=PhotoImage(file="Add.png")
        self.tip= Balloon(root)
        self.count=0
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        F1=Frame(self.root,relief=FLAT,bg="maroon",pady=2)
        F1.place(x=0,y=0,relwidth=1,height=40)

        Label_cont=Label(F1,text="Contacts",fg="black",font=("times new roman",20),bg="maroon").place(x=5,y=0)
        Label_search=Button(F1,image=self.vectorimage1,command=self.Profile,relief=FLAT,bg="maroon")
        Label_search.place(x=260,y=2)
        Label_add=Button(F1,image=self.vectorimage3,command=self.contact,relief=FLAT,bg="maroon")
        Label_add.place(x=290,y=2)
        self.tip.bind_widget(Label_add,balloonmsg="Add New Contact")
        Label_menu=Button(F1,image=self.vectorimage2,command=self.Connect,relief=FLAT,bg="maroon")
        Label_menu.place(x=320,y=2)
        self.tip.bind_widget(Label_menu,balloonmsg="Contacts settings")

        F2=customtkinter.CTkFrame(self.root,height=550,width=340)
        F2.place(x=5,y=42)

        self.listbox=Listbox(F2,width=280,height=530,font=("times new roman",15,"bold"))
        self.listbox.place(x=0,y=0)
        
        self.Connect()


    def contact(self):
        screen1=Toplevel()
        screen1.title("New Contact")
        screen1.geometry("350x600+450+30")



    def Profile(self):
        print("hello")

    def Connect(self):
        try:
            mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
            )
            mycursor=mydb.cursor()
            mycursor.execute("SHOW DATABASES")
            lst=mycursor.fetchall()
            database_name="tel_directory"
            if(database_name,)in lst:
                mycursor.execute("SHOW TABLES FROM {}".format(database_name))
                tab=mycursor.fetchall()
                tab_name="contacts"
                if(tab_name,)in tab:
                    mycursor.execute("SELECT Name FROM {}.{} ORDER BY Name ASC".format(database_name,tab_name))
                    data=mycursor.fetchall()
                    for i in data:
                        for j in i:
                            self.listbox.insert(self.count,j)
                            self.count+1

                else:
                    messagebox.showerror("Error ","Table Doesnot Exist")

            else:
                messagebox.showerror("Error ","Database Doesnot Exist")


        except Exception as e:
            print(e)

root=Tk()
obj=Contact_book(root)
root.mainloop()