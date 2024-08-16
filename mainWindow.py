from tkinter import *
from tkinter import ttk,messagebox
from customtkinter import *
from PIL import Image
import mysql.connector


class MainWindow(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.login_window = parent
        self.geometry("1000x580+0+0")
        self.title("Employee Management System")
        self.config(bg="#FFFFFF")
        self.attributes("-topmost", True)

        # Frames for layout and logo
        self.beColor = CTkFrame(self, width=400, height=150, fg_color="#FFFFFF")
        self.beColor.grid(row=0, column=0)
        self.afColor = CTkFrame(self, width=400, height=150, fg_color="#FFFFFF")
        self.afColor.place(x=600, y=0)

        self.logoImage = CTkImage(Image.open("Image/logo.png"), size=(800, 150))
        self.logoImageLabel = CTkLabel(self, image=self.logoImage, text="", fg_color="white")
        self.logoImageLabel.place(x=100, y=0)

        self.Frame = CTkFrame(self, width=1000, height=460, fg_color="#1E1F22")
        self.Frame.place(x=0, y=140)

        # Left Frame for form inputs
        self.leftFrame = CTkFrame(self.Frame, width=350, height=340, fg_color="#1E1F22")
        self.leftFrame.place(x=10, y=20)

        self.idLabel = CTkLabel(self.leftFrame, text="Id", text_color="#FFFFFF", font=("Goudy old style", 26, "bold"))
        self.idLabel.place(x=10, y=0)
        self.idEntry = CTkEntry(self.leftFrame, placeholder_text="Employee id",
                                font=("Goudy old style", 26, "bold"), text_color="#9E9E9E", fg_color="#1E1F22",
                                width=230)
        self.idEntry.place(x=110, y=0)

        self.nameLabel = CTkLabel(self.leftFrame, text="Name", text_color="#FFFFFF",
                                  font=("Goudy old style", 26, "bold"))
        self.nameLabel.place(x=10, y=50)
        self.nameEntry = CTkEntry(self.leftFrame, placeholder_text="Employee Name",
                                  font=("Goudy old style", 26, "bold"), text_color="#9E9E9E", fg_color="#1E1F22",
                                  width=230)
        self.nameEntry.place(x=110, y=50)

        self.numberLabel = CTkLabel(self.leftFrame, text="Number", text_color="#FFFFFF",
                                    font=("Goudy old style", 26, "bold"))
        self.numberLabel.place(x=10, y=100)
        self.numberEntry = CTkEntry(self.leftFrame, placeholder_text="Employee mobile",
                                    font=("Goudy old style", 26, "bold"), text_color="#9E9E9E", fg_color="#1E1F22",
                                    width=230)
        self.numberEntry.place(x=110, y=100)

        self.roleLabel = CTkLabel(self.leftFrame, text="Role", text_color="#FFFFFF",
                                  font=("Goudy old style", 26, "bold"))
        self.roleLabel.place(x=10, y=150)

        self.roleEntry = CTkComboBox(self.leftFrame,
                                     values=["Software Architect", "Software Engineer", "Junior Software Developer",
                                             "Backend Developer", "Data Scientist", "Software Developer", "UI Designer",
                                             "Full stack developer",
                                             "Frontend Developer", "Web Developer", "Database Developer",
                                             "Network Engineer"],
                                     font=("Goudy old style", 20, "bold"),
                                     width=230,
                                     text_color="#9E9E9E",
                                     fg_color="#1E1F22", state="readonly")
        self.roleEntry.place(x=110, y=150)
        self.roleEntry.set("Software Engineer")

        self.genderLabel = CTkLabel(self.leftFrame, text="Gender", text_color="#FFFFFF",
                                    font=("Goudy old style", 26, "bold"))
        self.genderLabel.place(x=10, y=200)

        self.genderEntry = CTkComboBox(self.leftFrame, values=["Male", "Female", "Others"],
                                       font=("Goudy old style", 20, "bold"),
                                       width=230, text_color="#9E9E9E", fg_color="#1E1F22", state="readonly")
        self.genderEntry.place(x=110, y=200)
        self.genderEntry.set("Male")

        self.salaryLabel = CTkLabel(self.leftFrame, text="Salary", text_color="#FFFFFF",
                                    font=("Goudy old style", 26, "bold"))
        self.salaryLabel.place(x=10, y=250)
        self.salaryEntry = CTkEntry(self.leftFrame, placeholder_text="Employee salary",
                                    font=("Goudy old style", 26, "bold"), text_color="#9E9E9E", fg_color="#1E1F22",
                                    width=230)
        self.salaryEntry.place(x=110, y=250)

        self.addressLabel = CTkLabel(self.leftFrame, text="Address", text_color="#FFFFFF",
                                     font=("Goudy old style", 26, "bold"))
        self.addressLabel.place(x=10, y=300)
        self.addressEntry = CTkEntry(self.leftFrame, placeholder_text="Employee address",
                                     font=("Goudy old style", 26, "bold"), text_color="#9E9E9E", fg_color="#1E1F22",
                                     width=230)
        self.addressEntry.place(x=110, y=300)

        # Right Down Frame for Treeview and Scrollbars
        self.rightDownFrame = CTkFrame(self.Frame, width=610, height=300, fg_color="#FFFFFF")
        self.rightDownFrame.place(x=380, y=60)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Goudy old style", 16, "bold"),foreground="#0C98BF")
        # Treeview with Scrollbars
        self.tree = ttk.Treeview(self.rightDownFrame,
                                 columns=("Id", "Name", "Number", "Role", "Gender", "Salary", "Address"))

        # Scrollbars
        self.x_scroll = ttk.Scrollbar(self.rightDownFrame, orient=HORIZONTAL, command=self.tree.xview)
        self.y_scroll = ttk.Scrollbar(self.rightDownFrame, orient=VERTICAL, command=self.tree.yview)

        # Configure the Treeview with scrollbars
        self.tree.configure(xscrollcommand=self.x_scroll.set, yscrollcommand=self.y_scroll.set)

        # Place the Treeview and Scrollbars within the rightDownFrame
        self.tree.place(x=0, y=0, width=590, height=280)
        self.y_scroll.place(x=590, y=0, height=280)
        self.x_scroll.place(x=0, y=280, width=590)

        # Treeview Headings
        self.tree.heading("Id", text="ID")
        self.tree.heading("Name", text="NAME")
        self.tree.heading("Number", text="NUMBER")
        self.tree.heading("Role", text="ROLE")
        self.tree.heading("Gender", text="GENDER")
        self.tree.heading("Salary", text="SALARY")
        self.tree.heading("Address", text="ADDRESS")

        self.tree["show"] = "headings"

        # Set column width
        self.tree.column("Id", width=50)
        self.tree.column("Name", width=100)
        self.tree.column("Number", width=100)
        self.tree.column("Role", width=150)
        self.tree.column("Gender", width=50)
        self.tree.column("Salary", width=100)
        self.tree.column("Address", width=150)

        # Right upper frame for search functionality
        self.rightUpFrame = CTkFrame(self.Frame, width=610, height=50, fg_color="silver")
        self.rightUpFrame.place(x=380, y=10)
        self.searchBy = CTkComboBox(self.rightUpFrame,
                                    values=["Id", "Name", "Number", "Role", "Gender", "Salary", "Address"],
                                    font=("Goudy old style", 20, "bold"), text_color="black", fg_color="silver",
                                    state="readonly")
        self.searchBy.place(x=10, y=10)
        self.searchBy.set("Search By")

        self.searchEntry = CTkEntry(self.rightUpFrame, placeholder_text="Search here", placeholder_text_color="black",
                                    font=("Goudy old style", 20, "bold"), text_color="black", fg_color="silver")
        self.searchEntry.place(x=170, y=10)

        self.searchButton = CTkButton(self.rightUpFrame, text="SEARCH", cursor="hand2",
                                      font=("Goudy old style", 20, "bold"), width=100,command=self.search)
        self.searchButton.place(x=340, y=10)

        self.showAllButton = CTkButton(self.rightUpFrame, text="SHOW ALL", cursor="hand2",
                                      font=("Goudy old style", 20, "bold"), width=100,command=self.load_data)
        self.showAllButton.place(x=460, y=10)



        self.buttonFrame=  CTkFrame(self.Frame, width=980, height=80, fg_color="silver")
        self.buttonFrame.place(x=10,y=370)

        self.addEmployeeButton =  CTkButton(self.buttonFrame, text="ADD EMPLOYEE", cursor="hand2",
                                      font=("Goudy old style", 20, "bold"), width=100,command=self.add)
        self.addEmployeeButton.grid(row =0,column=0,pady=15,padx=17)
        self.updateEmployeeButton = CTkButton(self.buttonFrame, text="UPDATE EMPLOYEE", cursor="hand2",
                                           font=("Goudy old style", 20, "bold"), width=100,command=self.update)
        self.updateEmployeeButton.grid(row=0, column=1, pady=15, padx=17)
        self.deleteEmployeeButton = CTkButton(self.buttonFrame, text="DELETE EMPLOYEE", cursor="hand2",
                                           font=("Goudy old style", 20, "bold"), width=100,command=self.delete)
        self.deleteEmployeeButton.grid(row=0, column=2, pady=15, padx=17)

        self.deleteAllEmployeeButton = CTkButton(self.buttonFrame, text="DELETE ALL", cursor="hand2",
                                           font=("Goudy old style", 20, "bold"), width=100,command=self.delete_all)
        self.deleteAllEmployeeButton.grid(row=0, column=3, pady=15, padx=17)
        self.logoutEmployeeButton = CTkButton(self.buttonFrame, text="LOG OUT", cursor="hand2",
                                           font=("Goudy old style", 20, "bold"), width=100,command=self.logout)
        self.logoutEmployeeButton.grid(row=0, column=4, pady=15, padx=19)


        # Close event handling

        self.load_data()
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_tree_select(self, event):
        selected_items = self.tree.selection()
        if selected_items:
            selected_item = selected_items[0]  # Get the selected item
            values = self.tree.item(selected_item, "values")  # Get the values for the selected item

            # Update the entry fields with the selected values
            self.idEntry.delete(0, END)
            self.idEntry.insert(0, values[0])

            self.nameEntry.delete(0, END)
            self.nameEntry.insert(0, values[1])

            self.numberEntry.delete(0, END)
            self.numberEntry.insert(0, values[2])

            self.roleEntry.set(values[3])  # For ComboBox

            self.genderEntry.set(values[4])  # For ComboBox

            self.salaryEntry.delete(0, END)
            self.salaryEntry.insert(0, values[5])

            self.addressEntry.delete(0, END)
            self.addressEntry.insert(0, values[6])
    def load_data(self):
        """Fetch data from the database and insert it into the Treeview."""
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="employee"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM employee_data")
            rows = cursor.fetchall()

            # Clear the Treeview
            self.tree.delete(*self.tree.get_children())

            # Insert each row into the Treeview
            for row in rows:
                self.tree.insert("", "end", values=row)

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}", parent=self)
        finally:
            cursor.close()
            conn.close()

    def add(self):
        if self.idEntry.get()=="" or self.nameEntry.get()=="" or self.numberEntry.get()=="" or self.salaryEntry.get()=="" or self.addressEntry.get()=="":
            messagebox.showwarning("Warning","All fields are required",parent=self)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="employee"
                )
                cursor = conn.cursor()

                insert_query = """
                INSERT INTO employee_data (Id, Name, Number, Role,Gender,Salary,Address) VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (
                self.idEntry.get(), self.nameEntry.get(), self.numberEntry.get(), self.roleEntry.get(),self.genderEntry.get(),
                self.salaryEntry.get(),self.addressEntry.get()))
                conn.commit()

                messagebox.showinfo("Success", "Employee added successfully!", parent=self)

                self.idEntry.delete(0, END)
                self.nameEntry.delete(0, END)
                self.numberEntry.delete(0, END)
                self.roleEntry.set("Software Engineer")
                self.genderEntry.set("Male")
                self.salaryEntry.delete(0, END)
                self.addressEntry.delete(0, END)
                self.load_data()



            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}", parent=self)
            finally:
                cursor.close()
                conn.close()

    def update(self):
        if self.idEntry.get() == "" or self.nameEntry.get() == "" or self.numberEntry.get() == "" or self.salaryEntry.get() == "" or self.addressEntry.get() == "":
            messagebox.showwarning("Warning", "All fields are required", parent=self)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="employee"
                )
                cursor = conn.cursor()

                # Corrected select_query with tuple
                select_query = "SELECT * FROM employee_data WHERE Id = %s"
                cursor.execute(select_query, (self.idEntry.get(),))
                result = cursor.fetchone()

                if result:
                    if messagebox.askyesno("Confirm Deletion", "Are you sure you want update data?",
                                           parent=self):
                        # Corrected update_query
                        update_query = """
                        UPDATE employee_data
                        SET Name = %s, Number = %s, Role = %s, Gender = %s, Salary = %s, Address = %s
                        WHERE Id = %s
                        """
                        cursor.execute(update_query, (
                            self.nameEntry.get(), self.numberEntry.get(), self.roleEntry.get(), self.genderEntry.get(),
                            self.salaryEntry.get(), self.addressEntry.get(), self.idEntry.get()
                        ))

                        conn.commit()

                        messagebox.showinfo("Success", "Data updated successfully!", parent=self)
                        self.idEntry.delete(0, END)
                        self.nameEntry.delete(0, END)
                        self.numberEntry.delete(0, END)
                        self.roleEntry.set("Software Engineer")
                        self.genderEntry.set("Male")
                        self.salaryEntry.delete(0, END)
                        self.addressEntry.delete(0, END)
                        self.load_data()

                else:
                    messagebox.showerror("Error", "Id is incorrect", parent=self)

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}", parent=self)
            finally:
                cursor.close()
                conn.close()

    def delete(self):
        if self.idEntry.get() == "":
            messagebox.showwarning("Warning", "Id is required", parent=self)
        else:
            if messagebox.askyesno("Confirm Deletion", "Are you sure you want delete data?",
                                   parent=self):
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="employee"
                    )
                    cursor = conn.cursor()

                    # Corrected delete_query with tuple
                    delete_query = "DELETE FROM employee_data WHERE Id = %s"
                    cursor.execute(delete_query, (self.idEntry.get(),))
                    conn.commit()

                    # Check if any rows were deleted

                    if cursor.rowcount > 0:
                        messagebox.showinfo("Success", "Data deleted successfully!", parent=self)
                        self.idEntry.delete(0, END)
                        self.nameEntry.delete(0, END)
                        self.numberEntry.delete(0, END)
                        self.roleEntry.set("Software Engineer")
                        self.genderEntry.set("Male")
                        self.salaryEntry.delete(0, END)
                        self.addressEntry.delete(0, END)
                        self.load_data()
                    else:
                        messagebox.showerror("Error", "Id not found", parent=self)

                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Error: {err}", parent=self)
                finally:
                    cursor.close()
                    conn.close()

    def delete_all(self):
        # Ask for confirmation before proceeding
        if messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete all data?", parent=self):
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="employee"
                )
                cursor = conn.cursor()

                # SQL query to delete all rows from the table
                delete_all_query = "DELETE FROM employee_data"
                cursor.execute(delete_all_query)
                conn.commit()

                messagebox.showinfo("Success", "All data deleted successfully!", parent=self)
                self.load_data()  # Reload data to reflect changes

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}", parent=self)
            finally:
                cursor.close()
                conn.close()

    def search(self):
        search_by = self.searchBy.get()
        search_term = self.searchEntry.get()

        if search_by == "Search By":
            messagebox.showwarning("Warning", "Please select a search criterion", parent=self)
            return

        if not search_term:
            messagebox.showwarning("Warning", "Search term cannot be empty", parent=self)
            return

        # Construct SQL query based on search criterion
        query = f"SELECT * FROM employee_data WHERE {search_by} LIKE %s"

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="employee"
            )
            cursor = conn.cursor()

            cursor.execute(query, (f"%{search_term}%",))
            rows = cursor.fetchall()

            # Clear the Treeview


            if rows:
                self.tree.delete(*self.tree.get_children())
                # Insert each row into the Treeview
                for row in rows:
                    self.tree.insert("", "end", values=row)
            else:
                messagebox.showinfo("Info", "No results found", parent=self)

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}", parent=self)
        finally:
            cursor.close()
            conn.close()



    def on_closing(self):
        """Handle the close event of the MainWindow."""
        self.login_window.deiconify()  # Show the Login window again
        self.destroy()  # Close the MainWindow

    def logout(self):
        if messagebox.askyesno("Confirm Deletion", "Are you sure you want to log out?", parent=self):
            self.destroy()
            self.login_window.deiconify()

