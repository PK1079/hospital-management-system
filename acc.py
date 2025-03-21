import tkinter as tk
from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry

class Acc_info:
    def __init__(self,root):
        self.root=root
        self.root.title("Account Details")
        self.root.geometry("1120x405+0+240")

        acclbl=Label(self.root, text="ACCOUNT INFORMATION",font=("Times new roman",30,"bold"),bg="sky blue",fg="white",relief=RIDGE)
        acclbl.place(x=0,y=0,width=1150,height=50)

        img4=Image.open(r"C:\Users\promoth-0101\Desktop\Python\hospital_management_db\logo2.png" )
        img5=img4.resize((180, 140))
        self.photo2=ImageTk.PhotoImage(img5)

        lbimg=Label(self.root,image=self.photo2,bd=0,relief=RIDGE)
        lbimg.place(x=1000,y=0,width=120,height=50)

        lbl_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="INVOICE DETAILS",font=("times new roman",12,"bold"),padx=2)
        lbl_frame.place(x=5,y=50,width=425,height=349)

        pat_name= Label(lbl_frame,text="Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        pat_name.grid(row=0,column=0)

        self.entry_name=Entry(lbl_frame,width=29,font=("times new roman",12,"bold"))
        self.entry_name.grid(row=0,column=1)

        pat_dos= Label(lbl_frame,text="Date",font=("times new roman",12,"bold"),padx=2,pady=6)
        pat_dos.grid(row=1,column=0)

       # Place the DateEntry widget in lbl_frame using grid
        self.date_entry = DateEntry(lbl_frame, width=35, background='darkblue', foreground='white', borderwidth=2,date_pattern='yyyy/mm/dd')
        self.date_entry.grid(row=1, column=1,)  # Adjust row, column, padx, pady as needed


        Doc_fee= Label(lbl_frame,text="Doctor fees",font=("times new roman",12,"bold"),padx=2,pady=6)
        Doc_fee.grid(row=2,column=0)

        self.entry_fee=Entry(lbl_frame, width=29,font=("times new roman",12,"bold"))
        self.entry_fee.grid(row=2,column=1)

        med_cost= Label(lbl_frame,text="Medicine Cost",font=("times new roman",12,"bold"),padx=2,pady=6)
        med_cost.grid(row=3,column=0)

        self.entry_med=Entry(lbl_frame,width=29,font=("times new roman",12,"bold"))
        self.entry_med.grid(row=3,column=1)

       
        pay_met= Label(lbl_frame,text="Payment Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        pay_met.grid(row=4,column=0)


        self.entry_met=ttk.Combobox(lbl_frame,width=27,font=("times new roman",12,"bold"),state="readonly")
        self.entry_met['values']=("Select","Credit card","Debit card","Online Transaction","Cash")
        self.entry_met.grid(row=4,column=1)
        self.entry_met.current(0)


        pat_phn= Label(lbl_frame,text="Contact Number",font=("times new roman",12,"bold"),padx=2,pady=6)
        pat_phn.grid(row=5,column=0)

        self.entry_phn=Entry(lbl_frame,width=29,font=("times new roman",12,"bold"))
        self.entry_phn.grid(row=5,column=1)

        pay_stat= Label(lbl_frame,text="Payment Status",font=("times new roman",12,"bold"),padx=2,pady=6)
        pay_stat.grid(row=6,column=0)


        self.entry_stat=ttk.Combobox(lbl_frame,width=27,font=("times new roman",12,"bold"),state="readonly")
        self.entry_stat['values']=("Select","pending","complete")
        self.entry_stat.grid(row=6,column=1)
        self.entry_stat.current(0)


        btn_frame=LabelFrame(lbl_frame,bd=0,relief=RIDGE)
        btn_frame.place(x=0,y=290,width=380,height=37)

        btn_submit = Button(btn_frame, text="SUBMIT",command=self.save_details, font=("times new roman", 12, "bold"),bg="green",fg="white")
        btn_submit.grid(row=0, column=0,padx=1)

        btn_display = Button(btn_frame, text="DISPLAY ",command=self.display_details, font=("times new roman", 12, "bold"),bg="red",fg="white")
        btn_display.grid(row=0, column=1,padx=10)

        btn_reset = Button(btn_frame, text="RESET", command=self.reset_fields ,font=("times new roman", 12, "bold"),bg="red",fg="white")
        btn_reset.grid(row=0, column=2,padx=10)

        table_frame=LabelFrame(self.root, text="View Details",bd=2,relief=RIDGE,font=("Times new roman",12,"bold"))
        table_frame.place(x=435,y=50,width=680,height=349)

        lbl_search=Label(lbl_frame,text="Search By",font=("Times New Roman",12,"bold"),fg="black",padx=1,pady=6)
        lbl_search.grid(row=7,column=0)

        self.entry_search=ttk.Combobox(lbl_frame,width=13,font=("times new roman",12,"bold"),state="readonly")
        self.entry_search['values']=("Select","Payment Status","Payment Type")
        self.entry_search.grid(row=7,column=1,padx=1, pady=5, sticky="W")
        self.entry_search.current(0)

        self.txt_search=Entry(lbl_frame,font=("times new roman",12,"bold"),bd=1)
        self.txt_search.place(x=270, y=250, width=130)

        btn_search = Button(btn_frame, text="SEARCH",command=self.search_details, font=("times new roman", 12, "bold"),bg="red",fg="white")
        btn_search.grid(row=0, column=4,padx=10)

     
    def reset_fields(self):
    # Resetting all the Entry fields
        self.entry_name.delete(0, END)      # Clear Name field
        self.date_entry.delete(0, END)      # Clear Date field
        self.entry_fee.delete(0, END)  # Clear Doctor fees field
        self.entry_med.delete(0, END)  # Clear Medicine cost field
        self.entry_phn.delete(0, END)       # Clear Contact number field
    
    # Resetting the ComboBox fields
        self.entry_met.set('Select')  # Reset Payment type combobox
        self.entry_stat.set('Select')  # Reset Payment status combobox
    
    # Resetting the Search fields
        self.entry_search.set('Select')  # Reset Search by combobox
        self.txt_search.delete(0, END)  # Clear Search text field



    def save_details(self):
        pat_name=self.entry_name.get()
        acc_date=self.date_entry.get()
        doc_fee=self.entry_fee.get()
        medicine_cost=self.entry_med.get()
        payment_method=self.entry_met.get()
        contact_num=self.entry_phn.get()
        payment_status=self.entry_stat.get()
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
        query = "INSERT INTO Accounts (name, date, doctor_fees,medicine_cost,payment_type,contact_number,payment_status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (pat_name, acc_date, doc_fee,medicine_cost,payment_method,contact_num,payment_status))
 
        messagebox.showinfo("Success", f"Account  added successfully!",parent=self.root)
        connection.commit()  # Commit the transaction
        connection.close() 

    def display_details(self):
        try:
            # Connect to the MySQL database
            connection = mysql.connector.connect(
                host='localhost',        # Replace with your DB host
                user='root',             # Replace with your DB username
                password='PK107119',     # Replace with your DB password
                database='hospital_management',  # Replace with your database name
                port=3307
            )
            cursor = connection.cursor()

            # Execute SQL query to fetch all records from the Patient table
            query = "SELECT * FROM Accounts"
            cursor.execute(query)
            rows = cursor.fetchall()

            # If no records found, show a message
            if not rows:
                messagebox.showinfo("No Data", "No patient data available.")
                return

            # Create a new window for displaying data
            new_window = Toplevel(self.root)
            new_window.title("Accounts Data")
            new_window.geometry("670x300+440+340")

            # Create a Treeview widget to display the records in a table format
            tree = ttk.Treeview(new_window, columns=('ID', 'Name', 'Date', 'Doctor Fees', 'Medicine Cost', 'Total Cost', 'Payment Type', 'Contact Number', 'Payment Status'), show='headings')

            # Define the column headings
            tree.heading('ID', text='Account ID')
            tree.heading('Name', text='Name')
            tree.heading('Date', text='Date')
            tree.heading('Doctor Fees', text='Doctor Fees')
            tree.heading('Medicine Cost', text='Medicine Cost')
            tree.heading('Total Cost', text='Total Cost')
            tree.heading('Payment Type', text='Payment Type')
            tree.heading('Contact Number', text='Contact Number')
            tree.heading('Payment Status', text='Payment Status')

            # Define the column widths
            tree.column('ID', width=50)
            tree.column('Name', width=150)
            tree.column('Date', width=100)
            tree.column('Doctor Fees', width=100)
            tree.column('Medicine Cost', width=100)
            tree.column('Total Cost', width=100)
            tree.column('Payment Type', width=120)
            tree.column('Contact Number', width=150)
            tree.column('Payment Status', width=100)

            # Insert the retrieved rows into the Treeview
            for row in rows:
                tree.insert('', 'end', values=row)

            # Pack the Treeview to the window
            tree.pack(fill='both', expand=True)

            # Close the database connection
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")


        scrollbar = ttk.Scrollbar(new_window, orient="horizontal", command=tree.xview)
        tree.configure(xscroll=scrollbar.set)
        scrollbar.pack(side='bottom', fill='x')
        scrollbar = ttk.Scrollbar(new_window, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
    
    def search_details(self):
        search_det1=self.entry_search.get()
        search_det=self.txt_search.get()

        try:
            # Connect to the MySQL database
            connection = mysql.connector.connect(
                host='localhost',        # Replace with your DB host
                user='root',             # Replace with your DB username
                password='PK107119',     # Replace with your DB password
                database='hospital_management',  # Replace with your database name
                port=3307
            )
            cursor = connection.cursor()

            # Execute SQL query to fetch all records from the Patient table
            query = f"SELECT * FROM Accounts where {search_det1.lower().replace(' ', '_')} LIKE '%{search_det}%' "
            cursor.execute(query)
            rows = cursor.fetchall()

    
            # If no records found, show a message
            if not rows:
                messagebox.showinfo("No Data", "No patient data available.")
                return

            # Create a new window for displaying data
            new_window = Toplevel(self.root)
            new_window.title("Accounts Data")
            new_window.geometry("670x300+440+340")

            # Create a Treeview widget to display the records in a table format
            tree = ttk.Treeview(new_window, columns=('ID', 'Name', 'Date', 'Doctor Fees', 'Medicine Cost', 'Total Cost', 'Payment Type', 'Contact Number', 'Payment Status'), show='headings')

            # Define the column headings
            tree.heading('ID', text='Account ID')
            tree.heading('Name', text='Name')
            tree.heading('Date', text='Date')
            tree.heading('Doctor Fees', text='Doctor Fees')
            tree.heading('Medicine Cost', text='Medicine Cost')
            tree.heading('Total Cost', text='Total Cost')
            tree.heading('Payment Type', text='Payment Type')
            tree.heading('Contact Number', text='Contact Number')
            tree.heading('Payment Status', text='Payment Status')

            # Define the column widths
            tree.column('ID', width=50)
            tree.column('Name', width=150)
            tree.column('Date', width=100)
            tree.column('Doctor Fees', width=100)
            tree.column('Medicine Cost', width=100)
            tree.column('Total Cost', width=100)
            tree.column('Payment Type', width=120)
            tree.column('Contact Number', width=150)
            tree.column('Payment Status', width=100)

            tree.delete(*tree.get_children())

            # Insert the retrieved rows into the Treeview
            for row in rows:
                tree.insert('', 'end', values=row)

            # Pack the Treeview to the window
            tree.pack(fill='both', expand=True)

            # Close the database connection
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")


        scrollbar = ttk.Scrollbar(new_window, orient="horizontal", command=tree.xview)
        tree.configure(xscroll=scrollbar.set)
        scrollbar.pack(side='bottom', fill='x')
        scrollbar = ttk.Scrollbar(new_window, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        
        

if __name__ == "__main__":
    root=Tk()
    obj=Acc_info(root)
    root.mainloop()