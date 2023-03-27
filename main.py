import os
import check_camera
import Capture_Image
import Train_Image
import Recognize
import automail
# from automail import EmailSenderApp
import pyfiglet
import tkinter as tk


class FaceRecognitionApp:
    def __init__(self, master):
        self.master = master
        master.title("Face Recognition Attendance System")
        master.geometry('800x600')
        master.configure(bg='#2F4F4F')

        # Create the title bar
        ascii_banner = pyfiglet.figlet_format("Face   Recognition   Attendance   System", font="digital", width=100)
        self.title_label = tk.Label(master, text=ascii_banner, fg="#DAA520", bg="#2F4F4F", font=("Helvetica", 22, "bold"))
        self.title_label.pack(pady=20)

        # Create the main menu
        self.menu_frame = tk.Frame(master, bg='#2F4F4F')
        self.menu_frame.pack(pady=30)

        button_color = '#DAA520'
        button_font = ("Helvetica", 14, "bold")

        self.check_camera_button = tk.Button(self.menu_frame, text="Check Camera", command=self.check_camera,
                                             font=button_font, bg=button_color, fg='#2F4F4F', padx=20, pady=10)
        self.check_camera_button.pack(pady=10)

        self.capture_faces_button = tk.Button(self.menu_frame, text="Capture Faces", command=self.capture_faces,
                                              font=button_font, bg=button_color, fg='#2F4F4F', padx=20, pady=10)
        self.capture_faces_button.pack(pady=10)

        self.train_images_button = tk.Button(self.menu_frame, text="Train Images", command=self.train_images,
                                             font=button_font, bg=button_color, fg='#2F4F4F', padx=20, pady=10)
        self.train_images_button.pack(pady=10)

        self.recognize_attendance_button = tk.Button(self.menu_frame, text="Recognize & Attendance",
                                                     command=self.recognize_attendance, font=button_font,
                                                     bg=button_color, fg='#2F4F4F', padx=20, pady=10)
        self.recognize_attendance_button.pack(pady=10)

        self.auto_mail_button = tk.Button(self.menu_frame, text="Auto Mail", command=self.auto_mail,
                                           font=button_font, bg=button_color, fg='#2F4F4F', padx=20, pady=10)
        self.auto_mail_button.pack(pady=10)

        self.quit_button = tk.Button(self.menu_frame, text="Quit", command=master.quit,
                                     font=button_font, bg=button_color, fg='#2F4F4F', padx=20, pady=10)
        self.quit_button.pack(pady=10)

    def check_camera(self):
        check_camera.camer()

    def capture_faces(self):
        Capture_Image.takeImages()

    def train_images(self):
        Train_Image.TrainImages()

    def recognize_attendance(self):
        Recognize.recognize_attendence()

    def auto_mail(self):
        automail.EmailSenderApp()


if __name__ == '__main__':
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()












































# import os  # accessing the os functions
# import check_camera
# import Capture_Image
# import Train_Image
# import Recognize
# import automail
# import pyfiglet
# from tkinter import *
#
# # creating the title bar function
#
# def title_bar():
#     os.system('cls')  # for windows
#
#     # title of the program
#
#     ascii_banner = pyfiglet.figlet_format("Face   Recognition   Attendance   System", font="digital", width=100)
#     print(ascii_banner)
#
# # creating the user main menu function
#
# def mainMenu():
#     title_bar()
#     print()
#     print(10 * "*", "WELCOME MENU", 10 * "*")
#     print(" [1] Check Camera")
#     print(" [2] Capture Faces")
#     print(" [3] Train Images")
#     print(" [4] Recognize & Attendance")
#     print(" [5] Auto Mail")
#     print(" [6] Quit")
#
#     while True:
#         try:
#             choice = int(input("Enter Choice: "))
#
#             if choice == 1:
#                 checkCamera()
#                 break
#             elif choice == 2:
#                 CaptureFaces()
#                 break
#             elif choice == 3:
#                 Trainimages()
#                 break
#             elif choice == 4:
#                 RecognizeFaces()
#                 break
#             elif choice == 5:
#                 automail.mail()
#                 # os.system("py automail.py")
#                 break
#                 mainMenu()
#             elif choice == 6:
#                 print("Thank You")
#                 break
#             else:
#                 print("Invalid Choice. Enter 1-4")
#                 mainMenu()
#         except ValueError:
#             print("Invalid Choice. Enter 1-4\n Try Again")
#     exit
#
#
# # ---------------------------------------------------------
# # calling the camera test function from check camera.py file
#
# def checkCamera():
#     check_camera.camer()
#     key = input("Enter any key to return main menu")
#     mainMenu()
#
#
# # --------------------------------------------------------------
# # calling the take image function form capture image.py file
#
# def CaptureFaces():
#     Capture_Image.takeImages()
#     key = input("Enter any key to return main menu")
#     mainMenu()
#
#
# # -----------------------------------------------------------------
# # calling the train images from train_images.py file
#
# def Trainimages():
#     Train_Image.TrainImages()
#     key = input("Enter any key to return main menu")
#     mainMenu()
#
#
# # --------------------------------------------------------------------
# # calling the recognize_attendance from recognize.py file
#
# def RecognizeFaces():
#     Recognize.recognize_attendence()
#     key = input("Enter any key to return main menu")
#     mainMenu()
#
#
# # ---------------main driver ------------------
# mainMenu()