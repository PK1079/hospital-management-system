import tkinter as tk
from tkinter import*
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk


class Doc_info:
    def __init__(self,root):
        self.root=root
        self.root.title("Doctor Details")
        self.root.geometry("1120x405+0+240")

        acclbl=Label(self.root, text="DOCTOR INFORMATION",font=("Times new roman",30,"bold"),bg="sky blue",fg="white",relief=RIDGE)
        acclbl.place(x=0,y=0,width=1150,height=50)

        img4=Image.open(r"C:\Users\promoth-0101\Desktop\Python\hospital_management_db\logo2.png" )
        img5=img4.resize((180, 140))
        self.photo2=ImageTk.PhotoImage(img5)

        lbimg=Label(self.root,image=self.photo2,bd=0,relief=RIDGE)
        lbimg.place(x=1000,y=0,width=120,height=50)

        self.display_doc()

    def display_doc(self):
        


        connection = mysql.connector.connect(
            host='localhost',        # Replace with your DB host
            user='root',    # Replace with your DB username
            password='PK107119',# Replace with your DB password
            database='hospital_management', # Replace with your database name
            port=3307
        )
        
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM doctor")  # Query the doctor table

        # Fetch all rows from the database
        rows = cursor.fetchall()
        connection.close()

        # Insert data into the Treeview widget

        tree_frame = ttk.Frame(self.root)
        tree_frame.pack(fill=BOTH, expand=True, padx=0, pady=(50, 0)) 
        

        tree = ttk.Treeview(tree_frame, columns=("Doctor ID", "Doctor Name", "Education", "Position", "Fees", "Availability"), show="headings")

        tree.heading('Doctor ID', text='Doctor ID')
        tree.heading('Doctor Name', text='Name')
        tree.heading('Education', text='Qualification')
        tree.heading('Position', text='Department')
        tree.heading('Fees', text='Fees')
        tree.heading('Availability', text='Availability')
       
        tree.column('Doctor ID',width=50 )
        tree.column('Doctor Name', width=100 )
        tree.column('Education', width=150 )
        tree.column('Position',width=100 )
        tree.column('Fees', width=8 )
        tree.column('Availability', width=200 )
       
        for row in rows:
                tree.insert('', 'end', values=row)



# Pack the Treeview widget into the window
        tree.pack(fill=BOTH, expand=True)
        

    


    


if __name__=="__main__":
    root=tk.Tk()
    obj=Doc_info(root)
    root.mainloop()

