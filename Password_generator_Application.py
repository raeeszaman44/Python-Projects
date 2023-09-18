import random
import tkinter as tk

class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator")

        # Create labels for user name and password length
        self.user_name_label = tk.Label(self.window, text="Enter user name:")
        self.password_length_label = tk.Label(self.window, text="Enter password length:")

        # Create entry fields for user name and password length
        self.user_name_entry = tk.Entry(self.window)
        self.password_length_entry = tk.Entry(self.window)

        # Create a button to generate the password
        self.generate_password_button = tk.Button(self.window, text="GENERATE PASSWORD", command=self.generate_password)

        # Create a text box to display the generated password
        self.generated_password_text = tk.Text(self.window, height=1, width=20)

        # Create an accept button to accept the generated password
        self.accept_button = tk.Button(self.window, text="ACCEPT", command=self.accept_password)

        # Create a reset button to reset the password generator
        self.reset_button = tk.Button(self.window, text="RESET", command=self.reset_password)

        # Place the widgets on the window
        self.user_name_label.grid(row=0, column=0)
        self.password_length_label.grid(row=1, column=0)
        self.user_name_entry.grid(row=0, column=1)
        self.password_length_entry.grid(row=1, column=1)
        self.generate_password_button.grid(row=2, column=0)
        self.generated_password_text.grid(row=3, column=0)
        self.accept_button.grid(row=3, column=1)
        self.reset_button.grid(row=4, column=1)

        # Start the mainloop
        self.window.mainloop()

    def generate_password(self):
        # Get the user name and password length from the entry fields
        user_name = self.user_name_entry.get()
        password_length = int(self.password_length_entry.get())

        # Generate a random password
        password = ""
        for i in range(password_length):
            password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")

        # Display the generated password in the text box
        self.generated_password_text.delete("1.0", "end")
        self.generated_password_text.insert("end", password)

    def accept_password(self):
        # Accept the generated password
        print("The following password has been accepted:", self.generated_password_text.get("1.0", "end"))

    def reset_password(self):
        # Reset the password generator
        self.user_name_entry.delete(0, "end")
        self.password_length_entry.delete(0, "end")
        self.generated_password_text.delete("1.0", "end")

# Create an instance of the PasswordGenerator class and start it
password_generator = PasswordGenerator()
password_generator.start()
