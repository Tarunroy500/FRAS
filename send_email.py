
import os  # accessing the os functions
import pyfiglet

import Capture_Image
import check_camera


# creating the title bar function

root = tk.Tk()

root.title("Face Recognition Attendance System")
root.geometry('800x600')
root.configure(bg='#2F4F4F')


# creating the user main menu function

def mainMenu():
    # Create the title bar
    ascii_banner = pyfiglet.figlet_format("Face   Recognition   Attendance   System", font="digital", width=100)
    root.title_label = tk.Label(text=ascii_banner, fg="#DAA520", bg="#2F4F4F", font=("Helvetica", 22, "bold"))
    root.title_label.pack(pady=20)

    # Create the main menu
    root.menu_frame = tk.Frame(bg='#2F4F4F')
    root.menu_frame.pack(pady=30)

    button_color = '#DAA520'
    button_font = ("Helvetica", 14, "bold")

    root.check_camera_button = tk.Button(root.menu_frame, text="Check Camera", command=checkCamera,
                                         font=button_font, bg=button_color, fg='#2F4F4F', padx=20, pady=10)
    root.check_camera_button.pack(pady=10)

    root.capture_faces_button = tk.Button(root.menu_frame, text="Capture Faces", command=CaptureFaces,
                                          font=button_font, bg=button_color, fg='#2F4F4F', padx=20, pady=10)
    root.capture_faces_button.pack(pady=10)

    root.train_images_button = tk.Button(root.menu_frame, text="Train Images",
                                         font=button_font, bg=button_color, fg='#2F4F4F', padx=20, pady=10)
    root.train_images_button.pack(pady=10)

    root.recognize_attendance_button = tk.Button(root.menu_frame, text="Recognize & Attendance", font=button_font,
                                                 bg=button_color, fg='#2F4F4F', padx=20, pady=10)
    root.recognize_attendance_button.pack(pady=10)

    root.auto_mail_button = tk.Button(root.menu_frame, text="Auto Mail",
                                      font=button_font, bg=button_color, fg='#2F4F4F', padx=20, pady=10)
    root.auto_mail_button.pack(pady=10)

    root.quit_button = tk.Button(root.menu_frame, text="Quit",
                                 font=button_font, bg=button_color, fg='#2F4F4F', padx=20, pady=10)
    root.quit_button.pack(pady=10)

    # print()
    # print(10 * "*", "WELCOME MENU", 10 * "*")
    # print(" [1] Check Camera")
    # print(" [2] Capture Faces")
    # print(" [3] Train Images")
    # print(" [4] Recognize & Attendance")
    # print(" [5] Auto Mail")
    # print(" [6] Quit")

    # while True:
    #     try:
    #         choice = int(input("Enter Choice: "))
    #
    #         if choice == 1:
    #             checkCamera()
    #             break
    #         elif choice == 2:
    #             CaptureFaces()
    #             break
    #         elif choice == 3:
    #             Trainimages()
    #             break
    #         elif choice == 4:
    #             RecognizeFaces()
    #             break
    #         elif choice == 5:
    #             automail.mail()
    #             # os.system("py automail.py")
    #             break
    #             mainMenu()
    #         elif choice == 6:
    #             print("Thank You")
    #             break
    #         else:
    #             print("Invalid Choice. Enter 1-4")
    #             mainMenu()
    #     except ValueError:
    #         print("Invalid Choice. Enter 1-4\n Try Again")
    # exit


# ---------------------------------------------------------
# calling the camera test function from check camera.py file

def checkCamera():
    check_camera.camer()
    # key = input("Enter any key to return main menu")
    # mainMenu()

#
# # --------------------------------------------------------------
# # calling the take image function form capture image.py file
#
def CaptureFaces():
    Capture_Image.kunal()
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


# ---------------main driver ------------------
mainMenu()
root.mainloop()