import os
import smtplib
from email.message import EmailMessage
import pandas
import tkinter as tk
from tkinter import filedialog, messagebox


class EmailSenderApp:
    def __init__(self, master):
        self.master = master
        master.title("Email Sender App")
        master.configure(bg="#F5F5F5")

        # Create the main frame
        self.frame = tk.Frame(master, bg="#F5F5F5")
        self.frame.pack(expand=True, fill='both')

        # Create the label and entry for sender email
        self.sender_email_label = tk.Label(self.frame, text="Enter Your Email ID: ", bg="#F5F5F5")
        self.sender_email_label.grid(row=0, column=0, padx=10, pady=10)

        self.sender_email_entry = tk.Entry(self.frame)
        self.sender_email_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create the label and entry for sender password
        self.sender_pass_label = tk.Label(self.frame, text="Enter Your Password: ", bg="#F5F5F5")
        self.sender_pass_label.grid(row=1, column=0, padx=10, pady=10)

        self.sender_pass_entry = tk.Entry(self.frame, show="*")
        self.sender_pass_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create the label and entry for attachment file
        self.attechment_label = tk.Label(self.frame, text="Enter the Attendance file Path: ", bg="#F5F5F5")
        self.attechment_label.grid(row=2, column=0, padx=10, pady=10)

        self.attechment_entry = tk.Entry(self.frame)
        self.attechment_entry.grid(row=2, column=1, padx=10, pady=10)

        # Create the browse button
        self.browse_file_button = tk.Button(self.frame, text="Browse", command=self.browse_file, bg="#4CAF50",
                                            fg="white", activebackground="#7FFF00", activeforeground="white")
        self.browse_file_button.grid(row=2, column=2, padx=10, pady=10)

        # Create the send email button
        self.send_email_button = tk.Button(self.frame, text="Send Email", command=self.send_email, bg="#FF5722",
                                           fg="white", activebackground="#FFA07A", activeforeground="white")
        self.send_email_button.grid(row=3, column=1, padx=10, pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Select Attendance File", filetypes=[("Excel Files", "*.xlsx *.xls")])
        if file_path:
            self.attechment_entry.delete(0, tk.END)
            self.attechment_entry.insert(0, file_path)

    def send_email(self):
        sender_email = self.sender_email_entry.get()
        sender_pass = self.sender_pass_entry.get()
        attechment = self.attechment_entry.get()

        if not (sender_email and sender_pass and attechment):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            df = pandas.read_excel(attechment)
            receivers_email = df["EMAIL_ID"].values
            sub = ("Test Mail")
            attach_files = df["Files to be attached"]
            name = df["NAME"].values

            zipped = zip(receivers_email, attach_files, name)

            for (a, b, c) in zipped:
                msg = EmailMessage()
                files = [(attechment.format(b))]

                for file in files:
                    with open(file, 'rb') as f:
                        file_data = f.read()
                        file_name = f.name

                    msg['From'] = sender_email
                    msg['To'] = a
                    msg['Subject'] = sub
                    msg.set_content(f"hello {c}! I have something for you.")
                    msg.add_attachment(file_data, maintype='application', subtype='octet-stream',
                                       filename="{}.xls".format(b))

                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(sender_email, sender_pass)

                        smtp.send_message(msg)

            messagebox.showinfo("Success", "All mails sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


root = tk.Tk()
app = EmailSenderApp(root)
root.mainloop()






# import os
# import smtplib
# from email.message import EmailMessage
# import pandas
# import tkinter as tk
# from tkinter import filedialog, messagebox
#
#
# class EmailSenderApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("Email Sender App")
#
#         self.sender_email_label = tk.Label(master, text="Enter Your Email ID: ")
#         self.sender_email_label.pack()
#
#         self.sender_email_entry = tk.Entry(master)
#         self.sender_email_entry.pack()
#
#         self.sender_pass_label = tk.Label(master, text="Enter Your Password: ")
#         self.sender_pass_label.pack()
#
#         self.sender_pass_entry = tk.Entry(master, show="*")
#         self.sender_pass_entry.pack()
#
#         self.attechment_label = tk.Label(master, text="Enter the Attendance file Path: ")
#         self.attechment_label.pack()
#
#         self.attechment_entry = tk.Entry(master)
#         self.attechment_entry.pack()
#
#         self.browse_file_button = tk.Button(master, text="Browse", command=self.browse_file)
#         self.browse_file_button.pack()
#
#         self.send_email_button = tk.Button(master, text="Send Email", command=self.send_email)
#         self.send_email_button.pack()
#
#     def browse_file(self):
#         file_path = filedialog.askopenfilename(title="Select Attendance File", filetypes=[("Excel Files", "*.xlsx *.xls")])
#         if file_path:
#             self.attechment_entry.delete(0, tk.END)
#             self.attechment_entry.insert(0, file_path)
#
#     def send_email(self):
#         sender_email = self.sender_email_entry.get()
#         sender_pass = self.sender_pass_entry.get()
#         attechment = self.attechment_entry.get()
#
#         if not (sender_email and sender_pass and attechment):
#             messagebox.showerror("Error", "All fields are required!")
#             return
#
#         try:
#             df = pandas.read_excel(attechment)
#             receivers_email = df["EMAIL_ID"].values
#             sub = ("Test Mail")
#             attach_files = df["Files to be attached"]
#             name = df["NAME"].values
#
#             zipped = zip(receivers_email, attach_files, name)
#
#             for (a, b, c) in zipped:
#                 msg = EmailMessage()
#                 files = [(attechment.format(b))]
#
#                 for file in files:
#                     with open(file, 'rb') as f:
#                         file_data = f.read()
#                         file_name = f.name
#
#                     msg['From'] = sender_email
#                     msg['To'] = a
#                     msg['Subject'] = sub
#                     msg.set_content(f"hello {c}! I have something for you.")
#                     msg.add_attachment(file_data, maintype='application', subtype='octet-stream',
#                                        filename="{}.xls".format(b))
#
#                     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#                         smtp.login(sender_email, sender_pass)
#
#                         smtp.send_message(msg)
#
#             messagebox.showinfo("Success", "All mail sent!")
#         except Exception as e:
#             messagebox.showerror("Error", str(e))
#
#
# root = tk.Tk()
# app = EmailSenderApp(root)
# root.mainloop()


































# import os
# import smtplib
# from email.message import EmailMessage
# # from getpass import getpass
# import pandas
#
#
# def mail():
#     sender_email = input("Enter Your Email ID: ")
#     sender_pass = input("Enter Your Password: ")
#     attechment = input("Enter the Attendance file Path: ")
#
#     df = pandas.read_excel("E:\For email.xlsx")
#     receivers_email = df["EMAIL_ID"].values
#     sub = ("Test Mail ")
#     attach_files = df["Files to be attached"]
#     name = df["NAME"].values
#
#     zipped = zip(receivers_email, attach_files, name)
#
#     for (a, b, c) in zipped:
#
#         msg = EmailMessage()
#         files = [(attechment.format(b))]
#
#         for file in files:
#             with open(file, 'rb') as f:
#                 file_data = f.read()
#                 file_name = f.name
#
#             msg['From'] = sender_email
#             msg['To'] = a
#             msg['Subject'] = sub
#             msg.set_content(f"hello {c}! I have something for you.")
#             msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename="{}.xls".format(b))
#
#             with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#                 smtp.login(sender_email, sender_pass)
#
#                 smtp.send_message(msg)
#
#     print("All mail sent!")
#
# ‪E:\For email.xlsx
