import mysql.connector
from tkinter import messagebox
from customtkinter import *
from PIL import Image

class Register(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("900x500+80+80")
        self.title("Create An Account Here")
        self.attributes("-topmost", True)

        # Setup UI elements for the Register window
        self.coverImage = CTkImage(Image.open("Image/cover.png"), size=(700, 550))
        self.coverImageLabel = CTkLabel(self, image=self.coverImage, text="")
        self.coverImageLabel.place(x=200, y=0)

        self.headingLabel = CTkLabel(self, text="Employee Management System", font=("Goudy old style", 25, "bold"),
                                     text_color="#89BFD9")
        self.headingLabel.place(x=20, y=30)

        infoLabel = CTkLabel(self, text="Create an account", font=("Goudy old style", 25, "bold"),
                             text_color="#89BFD9")
        infoLabel.place(x=60, y=70)

        self.nameEntry = CTkEntry(self, placeholder_text="Enter your fullname", font=("Goudy old style", 20, "bold"),
                                  text_color="#89BFD9", width=200)
        self.nameEntry.place(x=50, y=150)

        self.userNameEntry = CTkEntry(self, placeholder_text="Enter your username", font=("Goudy old style", 20, "bold"),
                                      text_color="#89BFD9", width=200)
        self.userNameEntry.place(x=50, y=200)

        self.passwordEntry = CTkEntry(self, placeholder_text="Enter your password", font=("Goudy old style", 20, "bold"),
                                      text_color="#89BFD9", width=200, show="*")
        self.passwordEntry.place(x=50, y=250)

        self.hintEntry = CTkEntry(self, placeholder_text="Enter password hint", font=("Goudy old style", 20, "bold"),
                                  text_color="#89BFD9", width=200)
        self.hintEntry.place(x=50, y=300)

        self.submitButton = CTkButton(self, text="REGISTER", cursor="hand2", command=self.registerFunction,
                                      font=("Goudy old style", 20, "bold"))
        self.submitButton.place(x=70, y=350)

    def registerFunction(self):
        if self.nameEntry.get() == "" or self.userNameEntry.get() == "" or self.passwordEntry.get() == "" or self.hintEntry.get() == "":
            messagebox.showwarning("Warning", "All fields are required",parent=self)
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
                INSERT INTO user (name, username, password, hint) VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insert_query, (self.nameEntry.get(), self.userNameEntry.get(), self.passwordEntry.get(), self.hintEntry.get()))
                conn.commit()

                messagebox.showinfo("Success", "Account created successfully!",parent=self)
                self.destroy()  # Close the Register window after success

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}",parent=self)
            finally:
                cursor.close()
                conn.close()
