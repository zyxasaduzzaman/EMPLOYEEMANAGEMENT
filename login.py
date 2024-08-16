from tkinter import messagebox
from customtkinter import *
from PIL import Image
import mysql.connector
from register import Register
from delete import Delete
from forgot import Forgot
from mainWindow import MainWindow

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+80+80")
        self.root.title("Admin Login Only")
        self.root.resizable(False, False)

        # Cover Image
        self.coverImage = CTkImage(Image.open("Image/cover.png"), size=(700, 550))
        self.coverImageLabel = CTkLabel(self.root, image=self.coverImage, text="")
        self.coverImageLabel.place(x=200, y=0)

        # Heading Labels
        self.headingLabel = CTkLabel(self.root, text="Employee Management System", font=("Goudy old style", 25, "bold"),
                                     text_color="#89BFD9")
        self.headingLabel.place(x=20, y=50)
        infoLabel = CTkLabel(self.root, text="Admin Login Only", font=("Goudy old style", 25, "bold"),
                             text_color="#89BFD9")
        infoLabel.place(x=50, y=80)

        # Entry Fields
        self.userNameEntry = CTkEntry(self.root, placeholder_text="Enter your user name",
                                      font=("Goudy old style", 20, "bold"), text_color="#89BFD9", width=200)
        self.userNameEntry.place(x=50, y=130)
        self.passwordEntry = CTkEntry(self.root, placeholder_text="Enter your password", show="*",
                                      font=("Goudy old style", 20, "bold"), text_color="#89BFD9", width=200)
        self.passwordEntry.place(x=50, y=180)

        # Buttons
        self.loginButton = CTkButton(self.root, text="LOGIN", cursor="hand2", font=("Goudy old style", 20, "bold"),
                                     command=self.loginFunction)
        self.loginButton.place(x=70, y=250)
        self.fogotButton = CTkLabel(self.root, fg_color="#242424", text="Forgot password", bg_color="#1E1F22",
                                    cursor="hand2", font=("Goudy old style", 16, "bold"))
        self.fogotButton.place(x=90, y=280)
        self.registerButton = CTkLabel(self.root, fg_color="#242424", text="Register now", cursor="hand2",
                                       font=("Goudy old style", 16, "bold"))
        self.registerButton.place(x=100, y=305)

        # Bind events
        self.fogotButton.bind("<Button-1>", self.forgotFunction)
        self.registerButton.bind("<Button-1>", self.registerFunction)

        self.deleteButton = CTkButton(self.root, command=self.deleteFunction, text="DELETE ACCOUNT", cursor="hand2",
                                      font=("Goudy old style", 20, "bold"))
        self.deleteButton.place(x=50, y=380)

    def loginFunction(self):
        if self.userNameEntry.get() == "" or self.passwordEntry.get() == "":
            messagebox.showwarning("Warning", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="employee"
                )
                cursor = conn.cursor()

                    # Query to check if the username and password are correct
                query = "SELECT * FROM user WHERE username = %s AND password = %s"
                cursor.execute(query, (self.userNameEntry.get(), self.passwordEntry.get()))
                result = cursor.fetchone()

                if result:
                    messagebox.showinfo("Success", "Login successful!", parent=self.root)
                    self.userNameEntry.delete(0, 'end')
                    self.passwordEntry.delete(0, 'end')
                    self.root.withdraw()  # Hide the login window
                    self.main_window = MainWindow(self.root)  # Corrected: Pass only the parent

                else:
                    messagebox.showerror("Error", "Invalid username or password!", parent=self.root)

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}", parent=self.root)
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()

    def forgotFunction(self, event):
        Forgot(self.root)  # Open the Forgot window

    def registerFunction(self, event):
        Register(self.root)  # Open the Register window

    def deleteFunction(self):
        Delete(self.root)  # Open the Delete window

root = CTk()  # Only one instance of CTk()
login = Login(root)
root.mainloop()
