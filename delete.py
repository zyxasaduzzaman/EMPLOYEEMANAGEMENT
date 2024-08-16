import mysql.connector
from tkinter import messagebox
from customtkinter import *
from PIL import Image

class Delete(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("900x500+80+80")
        self.title("Delete Your Account")
        self.attributes("-topmost", True)

        # Setup UI elements for the Delete window
        self.coverImage = CTkImage(Image.open("Image/cover.png"), size=(700, 550))
        self.coverImageLabel = CTkLabel(self, image=self.coverImage, text="")
        self.coverImageLabel.place(x=200, y=0)

        self.headingLabel = CTkLabel(self, text="Employee Management System", font=("Goudy old style", 25, "bold"),
                                     text_color="#89BFD9")
        self.headingLabel.place(x=20, y=30)

        infoLabel = CTkLabel(self, text="Delete your account", font=("Goudy old style", 25, "bold"),
                             text_color="#89BFD9")
        infoLabel.place(x=60, y=70)

        self.userNameEntry = CTkEntry(self, placeholder_text="Enter your username", font=("Goudy old style", 20, "bold"),
                                      text_color="#89BFD9", width=200)
        self.userNameEntry.place(x=50, y=150)

        self.passwordEntry = CTkEntry(self, placeholder_text="Enter your password", font=("Goudy old style", 20, "bold"),
                                      text_color="#89BFD9", width=200, show="*")
        self.passwordEntry.place(x=50, y=200)

        self.submitButton = CTkButton(self, text="DELETE", cursor="hand2", command=self.deleteFunction,
                                      font=("Goudy old style", 20, "bold"))
        self.submitButton.place(x=70, y=350)


    def deleteFunction(self):
        if self.userNameEntry.get() == "" or self.passwordEntry.get() == "":
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

                delete_query = """
                DELETE FROM user WHERE username = %s AND password = %s
                """
                cursor.execute(delete_query, (self.userNameEntry.get(), self.passwordEntry.get()))
                conn.commit()

                if cursor.rowcount > 0:
                    messagebox.showinfo("Success", "Account deleted successfully!",parent=self)
                    self.destroy()  # Close the Delete window after success
                else:
                    messagebox.showerror("Error", "Username or password is incorrect",parent=self)

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}",parent=self)
            finally:
                cursor.close()
                conn.close()
