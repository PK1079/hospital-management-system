from tkinter import*
from tkinter import Tk,ttk,messagebox
import mysql.connector
from tkcalendar import DateEntry
class add_staff:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1120x273+0+370")

        lbl_frame=LabelFrame(self.root,bd=0,relief=RIDGE,text="STAFF DETAILS",font=("times new roman",12,"bold"),padx=2)
        lbl_frame.place(x=5,y=0,width=425,height=449)

        pat_name= Label(lbl_frame,text="Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        pat_name.grid(row=0,column=0)

        self.entry_name=Entry(lbl_frame,width=29,font=("times new roman",12,"bold"))
        self.entry_name.grid(row=0,column=1)

        pat_role= Label(lbl_frame,text="Role",font=("times new roman",12,"bold"),padx=2,pady=6)
        pat_role.grid(row=2,column=0)

        self.entry_role=Entry(lbl_frame,width=29,font=("times new roman",12,"bold"))
        self.entry_role.grid(row=2,column=1)

        pat_gen= Label(lbl_frame,text="Department Id",font=("times new roman",12,"bold"),padx=2,pady=6)
        pat_gen.grid(row=5,column=0)

        self.entry_dept=Entry(lbl_frame,width=29,font=("times new roman",12,"bold"))
        self.entry_dept.grid(row=5,column=1)

        pat_phn= Label(lbl_frame,text="Contact Number",font=("times new roman",12,"bold"),padx=2,pady=6)
        pat_phn.grid(row=3,column=0)

        self.entry_phn=Entry(lbl_frame,width=29,font=("times new roman",12,"bold"))
        self.entry_phn.grid(row=3,column=1)

        pat_email= Label(lbl_frame,text="Email Id",font=("times new roman",12,"bold"),padx=2,pady=6)
        pat_email.grid(row=4,column=0)

        self.entry_emil=Entry(lbl_frame,width=29,font=("times new roman",12,"bold"))
        self.entry_emil.grid(row=4,column=1)

        pat_add= Label(lbl_frame,text="Address",font=("times new roman",12,"bold"),padx=2,pady=6)
        pat_add.grid(row=6,column=0)


        self.entry_add=Entry(lbl_frame,width=29,font=("times new roman",12,"bold"))
        self.entry_add.grid(row=6,column=1)


        pat_dob= Label(lbl_frame,text="Date of Birth",font=("times new roman",12,"bold"),padx=2,pady=6)
        pat_dob.grid(row=1,column=0)

        self.entry_dob=DateEntry(lbl_frame,width=35,background='black', foreground='white', borderwidth=2,date_pattern='yyyy/mm/dd')
        self.entry_dob.grid(row=1,column=1)

        table_frame=LabelFrame(self.root,bd=0,relief=RIDGE,font=("Times new roman",12,"bold"))
        table_frame.place(x=435,y=17,width=680,height=349)

        
        pat_gen= Label(table_frame,text="Gender",font=("times new roman",12,"bold"),padx=2,pady=6)
        pat_gen.grid(row=0,column=0)

        self.entry_gen=ttk.Combobox(table_frame,width=27,font=("times new roman",12,"bold"),state="readonly")
        self.entry_gen['values']=("Select","Male","Female","Other")
        self.entry_gen.grid(row=0,column=1)
        self.entry_gen.current(0)

        
        pat_salary= Label(table_frame,text="Salary",font=("times new roman",12,"bold"),padx=2,pady=6)
        pat_salary.grid(row=1,column=0)

        self.entry_sal=Entry(table_frame,width=29,font=("times new roman",12,"bold"))
        self.entry_sal.grid(row=1,column=1)

        pat_ephn= Label(table_frame,text="Emergency Number",font=("times new roman",12,"bold"),padx=2,pady=6)
        pat_ephn.grid(row=2,column=0)

        self.entry_ephn=Entry(table_frame,width=29,font=("times new roman",12,"bold"))
        self.entry_ephn.grid(row=2,column=1)

        pat_stat= Label(table_frame,text="Status",font=("times new roman",12,"bold"),padx=2,pady=6)
        pat_stat.grid(row=3,column=0)

        self.entry_stat=ttk.Combobox(table_frame,width=27,font=("times new roman",12,"bold"),state="readonly")
        self.entry_stat['values']=("Select","Active","On Leave")
        self.entry_stat.grid(row=3,column=1)
        self.entry_stat.current(0)

        btn_submit = Button(table_frame, text="SUBMIT",command=self.insert_staff, font=("times new roman", 12, "bold"),bg="green",fg="white")
        btn_submit.grid(row=4, column=0,pady=10,)

        btn_reset = Button(table_frame, text="RESET",command=self.reset_staff, font=("times new roman", 12, "bold"),bg="red",fg="white")
        btn_reset.grid(row=4, column=1,pady=10,)

    def insert_staff(self):
        
        staff_name= self.entry_name.get()
        staff_role= self.entry_role.get()
        staff_dept= self.entry_dept.get()
        staff_phone=self.entry_phn.get()
        staff_email= self.entry_emil.get()
        staff_address= self.entry_add.get()
        staff_dateob=self.entry_dob.get()
        staff_gender=self.entry_gen.get()
        staff_salary=self.entry_sal.get()
        staff_emergency=self.entry_ephn.get()
        staff_stat=self.entry_stat.get()

         # Ensure fields are not empty
            # Connect to the MySQL database
        connection = mysql.connector.connect(
                host='localhost',        # Replace with your DB host
                user='root',    # Replace with your DB username
                password='PK107119',# Replace with your DB password
                database='hospital_management', # Replace with your database name
                port=3307
            )
        cursor=connection.cursor()  

        query = "INSERT INTO Staff (name,role,department_id,contact_number,email,address,date_of_birth,gender,salary,emergency_contact_number,status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (staff_name,staff_role,staff_dept,staff_phone,staff_email,staff_address,staff_dateob,staff_gender,staff_salary,staff_emergency,staff_stat))
 
        messagebox.showinfo("Success", f"Staff  added successfully!")
        connection.commit()  # Commit the transaction
        connection.close() 

    def reset_staff(self):
        self.entry_name.delete(0, END)      # Clear Name field
        self.entry_role.delete(0, END)      # Clear Date field
        self.entry_add.delete(0, END)  # Clear Doctor fees field
        self.entry_emil.delete(0, END)  # Clear Medicine cost field
        self.entry_phn.delete(0, END)       # Clear Contact number field
        self.entry_sal.delete(0, END)      # Clear Name field
        self.entry_dept.delete(0, END)      # Clear Date field
        self.entry_ephn.delete(0, END)  
        self.entry_dob.delete(0,END)
    
    # Resetting the ComboBox fields
        self.entry_gen.set('Select')  # Reset Payment type combobox
        self.entry_stat.set('Select')  # Reset Payment status combobox
    

if __name__=="__main__":
    root=Tk()
    obj=add_staff(root)
    root.mainloop()