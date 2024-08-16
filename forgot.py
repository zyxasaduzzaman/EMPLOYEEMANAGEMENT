import mysql.connector
from tkinter import messagebox
from customtkinter import *
from PIL import Image

class Forgot(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("900x500+80+80")
        self.title("Recover your password")
        self.attributes("-topmost", True)

        # Setup UI elements for the Forgot window
        self.coverImage = CTkImage(Image.open("Image/cover.png"), size=(700, 550))
        self.coverImageLabel = CTkLabel(self, image=self.coverImage, text="")
        self.coverImageLabel.place(x=200, y=0)

        self.headingLabel = CTkLabel(self, text="Employee Management System", font=("Goudy old style", 25, "bold"),
                                     text_color="#89BFD9")
        self.headingLabel.place(x=20, y=30)

        infoLabel = CTkLabel(self, text="Recover your password", font=("Goudy old style", 25, "bold"),
                             text_color="#89BFD9")
        infoLabel.place(x=60, y=70)

        self.userNameEntry = CTkEntry(self, placeholder_text="Enter your username", font=("Goudy old style", 20, "bold"),
                                      text_color="#89BFD9", width=200)
        self.userNameEntry.place(x=50, y=150)

        self.hintEntry = CTkEntry(self, placeholder_text="Enter password hint", font=("Goudy old style", 20, "bold"),
                                  text_color="#89BFD9", width=200)
        self.hintEntry.place(x=50, y=200)

        self.passwordEntry = CTkEntry(self, placeholder_text="Enter new password", font=("Goudy old style", 20, "bold"),
                                      text_color="#89BFD9", width=200, show="*")
        self.passwordEntry.place(x=50, y=250)

        self.submitButton = CTkButton(self, text="SUBMIT", cursor="hand2", command=self.forgotFunction,
                                      font=("Goudy old style", 20, "bold"))
        self.submitButton.place(x=70, y=350)

    def forgotFunction(self):
        if self.userNameEntry.get() == "" or self.passwordEntry.get() == "" or self.hintEntry.get() == "":
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

                select_query = """
                SELECT * FROM user WHERE username = %s AND hint = %s
                """
                cursor.execute(select_query, (self.userNameEntry.get(), self.hintEntry.get()))
                result = cursor.fetchone()

                if result:
                    update_query = """
                    UPDATE user SET password = %s WHERE username = %s
                    """
                    cursor.execute(update_query, (self.passwordEntry.get(), self.userNameEntry.get()))
                    conn.commit()

                    messagebox.showinfo("Success", "Password updated successfully!",parent=self)
                    self.destroy()
                else:
                    messagebox.showerror("Error", "Username or hint is incorrect",parent=self)

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}",parent=self)
            finally:
                cursor.close()
                conn.close()
