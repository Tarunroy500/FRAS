import tkinter as tk
import cv2
import os
import os.path
import csv
from tkinter import filedialog, messagebox

class TakeImagesGUI:
    def __init__(self, master):
        self.master = master
        master.title("Take Images")
        master.geometry('800x600')
        master.configure(bg='#2F4F4F')

        # create labels and entry boxes for user input
        self.id_label = tk.Label(master, text="Enter Your Id: ", fg="black", font=("Helvetica", 14))
        self.id_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.id_entry = tk.Entry(master, font=("Helvetica", 14))
        self.id_entry.grid(row=0, column=1, padx=10, pady=10)

        self.name_label = tk.Label(master, text="Enter Your Name: ", fg="black", font=("Helvetica", 14))
        self.name_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.name_entry = tk.Entry(master, font=("Helvetica", 14))
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.rollno_label = tk.Label(master, text="Enter Your Roll No.: ", fg="black", font=("Helvetica", 14))
        self.rollno_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.rollno_entry = tk.Entry(master, font=("Helvetica", 14))
        self.rollno_entry.grid(row=2, column=1, padx=10, pady=10)

        self.email_label = tk.Label(master, text="Enter Your Valid Email Id: ", fg="black", font=("Helvetica", 14))
        self.email_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.email_entry = tk.Entry(master, font=("Helvetica", 14))
        self.email_entry.grid(row=3, column=1, padx=10, pady=10)

        # create a button to take images
        self.take_images_button = tk.Button(master, text="Take Images", command=self.take_images, bg="blue", fg="white",
                                            font=("Helvetica", 16))
        self.take_images_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.take_images_button.configure(width=20)

        # center the window on the screen
        master.eval('tk::PlaceWindow %s center' % master.winfo_toplevel())

    # counting the numbers
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    # function to take images
    def take_images(self):
        Id = self.id_entry.get()
        name = self.name_entry.get()
        rollno = self.rollno_entry.get()
        email = self.email_entry.get()

        if not self.is_number(Id):
            tk.messagebox.showerror("Error", "Id must be a number")
            return

        if not name.isalpha():
            tk.messagebox.showerror("Error", "Name must contain only alphabets")
            return

        if not rollno.isalnum():
            tk.messagebox.showerror("Error", "Roll no. must contain only numbers and alphabets")
            return

        if not "@" in email or not "." in email:
            tk.messagebox.showerror("Error", "Invalid email address")
            return

        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (10, 159, 255), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage" + os.sep + name + "." + Id + '.' +
                            str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('frame', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is more than 100
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name + "Roll no.: " + rollno + "Email Id: " + email
        header = ["Id", "Name", "Roll no.", "Email Id"]
        row = [Id, name, rollno, email]
        if (os.path.isfile("StudentDetails" + os.sep + "StudentDetails.csv")):
            with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(j for j in row)
            csvFile.close()
        else:
            with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(i for i in header)
                writer.writerow(j for j in row)
            csvFile.close()

root = tk.Tk()
app = TakeImagesGUI(root)
root.mainloop()






# import tkinter as tk
# import cv2
# import os
# import os.path
# import csv
# from tkinter import filedialog, messagebox
#
# class TakeImagesGUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("Take Images")
#         master.geometry('800x600')
#         master.configure(bg='#2F4F4F')
#
#         # create labels and entry boxes for user input
#         self.id_label = tk.Label(master, text="Enter Your Id: ", fg="black", font=("Helvetica", 14))
#         self.id_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
#         self.id_entry = tk.Entry(master, font=("Helvetica", 14))
#         self.id_entry.grid(row=0, column=1, padx=10, pady=10)
#
#         self.name_label = tk.Label(master, text="Enter Your Name: ", fg="black", font=("Helvetica", 14))
#         self.name_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
#         self.name_entry = tk.Entry(master, font=("Helvetica", 14))
#         self.name_entry.grid(row=1, column=1, padx=10, pady=10)
#
#         self.rollno_label = tk.Label(master, text="Enter Your Roll No.: ", fg="black", font=("Helvetica", 14))
#         self.rollno_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
#         self.rollno_entry = tk.Entry(master, font=("Helvetica", 14))
#         self.rollno_entry.grid(row=2, column=1, padx=10, pady=10)
#
#         self.email_label = tk.Label(master, text="Enter Your Valid Email Id: ", fg="black", font=("Helvetica", 14))
#         self.email_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
#         self.email_entry = tk.Entry(master, font=("Helvetica", 14))
#         self.email_entry.grid(row=3, column=1, padx=10, pady=10)
#
#         # create a button to take images
#         self.take_images_button = tk.Button(master, text="Take Images", command=self.take_images, bg="blue", fg="white",
#                                             font=("Helvetica", 16))
#         self.take_images_button.grid(row=4, column=0, columnspan=2, pady=10)
#         self.take_images_button.configure(width=20)
#
#         # center the window on the screen
#         master.eval('tk::PlaceWindow %s center' % master.winfo_toplevel())
#
#     # counting the numbers
#     def is_number(self, s):
#         try:
#             float(s)
#             return True
#         except ValueError:
#             pass
#
#         try:
#             import unicodedata
#             unicodedata.numeric(s)
#             return True
#         except (TypeError, ValueError):
#             pass
#
#         return False
#
#     # function to take images
#     def take_images(self):
#         Id = self.id_entry.get()
#         name = self.name_entry.get()
#         rollno = self.rollno_entry.get()
#         email = self.email_entry.get()
#
#         if not self.is_number(Id):
#             tk.messagebox.showerror("Error", "Id must be a number")
#             return
#
#         if not name.isalpha():
#             tk.messagebox.showerror("Error", "Name must contain only alphabets")
#             return
#
#         if not rollno.isalnum():
#             tk.messagebox.showerror("Error", "Roll no. must contain only numbers and alphabets")
#             return
#
#         if not "@" in email or not "." in email:
#             tk.messagebox.showerror("Error", "Invalid email address")
#             return
#
#         cam = cv2.VideoCapture(0)
#         harcascadePath = "haarcascade_frontalface_default.xml"
#         detector = cv2.CascadeClassifier(harcascadePath)
#         sampleNum = 0
#
#         while (True):
#             ret, img = cam.read()
#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
#             for (x, y, w, h) in faces:
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (10, 159, 255), 2)
#                 # incrementing sample number
#                 sampleNum = sampleNum + 1
#                 # saving the captured face in the dataset folder TrainingImage
#                 cv2.imwrite("TrainingImage" + os.sep + name + "." + Id + '.' +
#                             str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
#                 # display the frame
#                 cv2.imshow('frame', img)
#             # wait for 100 miliseconds
#             if cv2.waitKey(100) & 0xFF == ord('q'):
#                 break
#             # break if the sample number is more than 100
#             elif sampleNum > 100:
#                 break
#         cam.release()
#         cv2.destroyAllWindows()
#         res = "Images Saved for ID : " + Id + " Name : " + name + "Roll no.: " + rollno + "Email Id: " + email
#         header = ["Id", "Name", "Roll no.", "Email Id"]
#         row = [Id, name, rollno, email]
#         if (os.path.isfile("StudentDetails" + os.sep + "StudentDetails.csv")):
#             with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+') as csvFile:
#                 writer = csv.writer(csvFile)
#                 writer.writerow(j for j in row)
#             csvFile.close()
#         else:
#             with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+') as csvFile:
#                 writer = csv.writer(csvFile)
#                 writer.writerow(i for i in header)
#                 writer.writerow(j for j in row)
#             csvFile.close()
#
# root = tk.Tk()
# app = TakeImagesGUI(root)
# root.mainloop()



































# import csv
# import cv2
# import os
# import os.path
#
#
# # counting the numbers
#
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass
#
#     return False
#
#
# # Take image function
#
# def takeImages():
#     Id = input("Enter Your Id: ")
#     name = input("Enter Your Name: ")
#     rollno = input("Enter Your Roll No.: ")
#     email = input("Enter Your Valid Email Id: ")
#
#     if (is_number(Id) and name.isalpha() and rollno.isalnum()):
#         cam = cv2.VideoCapture(0)
#         harcascadePath = "haarcascade_frontalface_default.xml"
#         detector = cv2.CascadeClassifier(harcascadePath)
#         sampleNum = 0
#
#         while (True):
#             ret, img = cam.read()
#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
#             for (x, y, w, h) in faces:
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (10, 159, 255), 2)
#                 # incrementing sample number
#                 sampleNum = sampleNum + 1
#                 # saving the captured face in the dataset folder TrainingImage
#                 cv2.imwrite("TrainingImage" + os.sep + name + "." + Id + '.' +
#                             str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
#                 # display the frame
#                 cv2.imshow('frame', img)
#             # wait for 100 miliseconds
#             if cv2.waitKey(100) & 0xFF == ord('q'):
#                 break
#             # break if the sample number is more than 100
#             elif sampleNum > 100:
#                 break
#         cam.release()
#         cv2.destroyAllWindows()
#         res = "Images Saved for ID : " + Id + " Name : " + name + "Roll no.: " + rollno + "Email Id: " + email
#         header = ["Id", "Name", "Roll no.", "Email Id"]
#         row = [Id, name, rollno, email]
#         if (os.path.isfile("StudentDetails" + os.sep + "StudentDetails.csv")):
#             with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+') as csvFile:
#                 writer = csv.writer(csvFile)
#                 writer.writerow(j for j in row)
#             csvFile.close()
#         else:
#             with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+') as csvFile:
#                 writer = csv.writer(csvFile)
#                 writer.writerow(i for i in header)
#                 writer.writerow(j for j in row)
#             csvFile.close()
#     else:
#         if (is_number(Id)):
#             print("Enter Alphabetical Name")
#         if (name.isalpha()):
#             print("Enter Numeric ID")
#         if (rollno.isalnum()):
#             print("Enter Only Number and Alphabet")
