from tkinter import*
from tkinter import Tk,ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
from add_staff import add_staff

class staff_det:
    def __init__(self,root):
        self.root=root
        self.root.title("STAFF DATA")
        self.root.geometry("1120x405+0+240")

        acclbl=Label(self.root, text="STAFF INFORMATION",font=("Times new roman",30,"bold"),bg="sky blue",fg="white",relief=RIDGE)
        acclbl.place(x=0,y=0,width=1150,height=50)

        img4=Image.open(r"C:\Users\promoth-0101\Desktop\Python\hospital_management_db\logo2.png" )
        img5=img4.resize((180, 140))
        self.photo2=ImageTk.PhotoImage(img5)

        lbimg=Label(self.root,image=self.photo2,bd=0,relief=RIDGE)
        lbimg.place(x=1000,y=0,width=120,height=50)



        search_frame=LabelFrame(self.root,bd=2,relief=RIDGE,)
        search_frame.place(x=0,y=50,width=1150,height=50)        

        search_lbl=Label(search_frame,text="Search",font=("Times new roman",15,"bold"),fg="black",padx=1,pady=3)
        search_lbl.grid(row=0,column=0)

        self.entry_search_box=ttk.Combobox(search_frame,width=22,font=("times new roman",12,"bold"),state="readonly")
        self.entry_search_box['values']=("Select","department_id","status","gender","role")
        self.entry_search_box.grid(row=0,column=1,padx=10)
        self.entry_search_box.current(0)

        self.txt_search=Entry(search_frame,font=("times new roman",12,"bold"),bd=1,width=23)
        self.txt_search.grid(row=0,column=2, padx=10)

        btn_search = Button(search_frame, text="SEARCH",command=self.search_staff, font=("times new roman", 12, "bold"),bg="red",fg="white")
        btn_search.grid(row=0, column=3,padx=10)

        btn_display =Button(search_frame, text="DISPLAY ALL",command=self.display_staff,font=("times new roman", 12, "bold"),bg="red",fg="white")
        btn_display.grid(row=0, column=4,padx=10)

        add_btn= Button(search_frame,text="ADD STAFF",command=self.add_staff,font=("times new roman",12,"bold"),fg="white",bg="black")
        add_btn.grid(row=0,column=5,padx=10)

        



    def add_staff(self):
        self.new_window=Toplevel(self.root)
        self.app=add_staff(self.new_window)
        


    def search_staff(self):
        search_box=self.entry_search_box.get()
        entry_box=self.txt_search.get()

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
           
        
            if search_box.lower() == 'gender':
                query = "SELECT * FROM Staff WHERE gender = %s"
                cursor.execute(query, (entry_box,))
            else:
                query = f"SELECT * FROM Staff WHERE {search_box.lower().replace(' ', '_')} LIKE %s"
                cursor.execute(query, (f"%{entry_box}%",))

            rows = cursor.fetchall()
                        



    
            # If no records found, show a message
            if not rows:
                messagebox.showinfo("No Data", "No patient data available.")
                return

            # Create a new window for displaying data
            new_window = Toplevel(self.root)
            new_window.title("Staff  Data")
            new_window.geometry("1120x280+0+365")
            tree = ttk.Treeview(new_window, columns=("staff_id", "name", "role", "department_id", "contact_number","email", "address", "date_of_birth", "gender", "salary","emergency_contact_number", "status"),show='headings')


    # Define the column headings and widths
            tree.heading("staff_id", text="ID")
            tree.heading("name", text="Name")
            tree.heading("role", text="Role")
            tree.heading("department_id", text="Department ID")
            tree.heading("contact_number", text="Contact Number")
            tree.heading("email", text="Email")
            tree.heading("address", text="Address")
            tree.heading("date_of_birth", text="Date of Birth")
            tree.heading("gender", text="Gender")
            tree.heading("salary", text="Salary")
            tree.heading("emergency_contact_number", text="Emergency Contact")
            tree.heading("status", text="Status")

            # Set column widths (optional)
            tree.column("staff_id", width=50)
            tree.column("name", width=150)
            tree.column("role", width=100)
            tree.column("department_id", width=100)
            tree.column("contact_number", width=120)
            tree.column("email", width=150)
            tree.column("address", width=200)
            tree.column("date_of_birth", width=100)
            tree.column("gender", width=80)
            tree.column("salary", width=100)
            tree.column("emergency_contact_number", width=120)
            tree.column("status", width=100)

           

            # Insert the retrieved rows into the Treeview
            for row in rows:
                tree.insert('', 'end', values=row)

            # Pack the Treeview into the window and add scrollbars
            tree.pack(fill=BOTH, expand=True)



        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

            # Scrollbars for the Treeview
            
        scrollbar = ttk.Scrollbar(new_window, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        scrollbar = ttk.Scrollbar(new_window, orient="horizontal", command=tree.xview)
        tree.configure(xscroll=scrollbar.set)
        scrollbar.pack(side='bottom', fill='x')
    

    def display_staff(self):
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
            query = f"SELECT * FROM Staff "
            cursor.execute(query)
            rows = cursor.fetchall()

    
            # If no records found, show a message
            if not rows:
                messagebox.showinfo("No Data", "No patient data available.")
                return

            # Create a new window for displaying data
            new_window = Toplevel(self.root)
            new_window.title("Staff Data")
            new_window.geometry("1120x280+0+365")

            tree = ttk.Treeview(new_window, columns=("staff_id", "name", "role", "department_id", "contact_number","email", "address", "date_of_birth", "gender", "salary","emergency_contact_number", "status"),show='headings')


    # Define the column headings and widths
            tree.heading("staff_id", text="ID")
            tree.heading("name", text="Name")
            tree.heading("role", text="Role")
            tree.heading("department_id", text="Department ID")
            tree.heading("contact_number", text="Contact Number")
            tree.heading("email", text="Email")
            tree.heading("address", text="Address")
            tree.heading("date_of_birth", text="Date of Birth")
            tree.heading("gender", text="Gender")
            tree.heading("salary", text="Salary")
            tree.heading("emergency_contact_number", text="Emergency Contact")
            tree.heading("status", text="Status")

            # Set column widths (optional)
            tree.column("staff_id", width=50)
            tree.column("name", width=150)
            tree.column("role", width=100)
            tree.column("department_id", width=100)
            tree.column("contact_number", width=120)
            tree.column("email", width=150)
            tree.column("address", width=200)
            tree.column("date_of_birth", width=100)
            tree.column("gender", width=80)
            tree.column("salary", width=100)
            tree.column("emergency_contact_number", width=120)
            tree.column("status", width=100)


            
    # Pack the Treeview into the window
            tree.pack(fill=BOTH, expand=True)

            

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

        scrollbar = ttk.Scrollbar(new_window, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        scrollbar = ttk.Scrollbar(new_window, orient="horizontal", command=tree.xview)
        tree.configure(xscroll=scrollbar.set)
        scrollbar.pack(side='bottom', fill='x')
    
    
               
        
if __name__=="__main__":
    root=Tk()
    obj=staff_det(root)
    root.mainloop()

