from tkinter import *
import tkinter as tk
from tkinter import simpledialog
import customtkinter as ctk
from tkinter import filedialog
from Test_Case import *
from Connected_Devices import *





ctk.set_appearance_mode("System")  
 
# Sets the color of the widgets in the window
ctk.set_default_color_theme("green")   
 
# Dimensions of the window
appWidth, appHeight = 600, 700


def browseFiles():
        
        filename = filedialog.askopenfilename(initialdir = "/",
                                        title = "Select a File",
                                        filetypes = (("Excel files",
                                                    "*.xlsx*"),
                                                    ))
        return filename

def choose_directory():
    global directory
    directory = filedialog.askdirectory()
    changeButton1 = ctk.CTkButton(master=root,text="Change test case",command=updateTestCaseArg)
    changeButton1.grid(row=5, column=0,columnspan=2, padx=20,pady=20, sticky="ew")

    changeButton2 = ctk.CTkButton(master=root,text="Change execution plan",command=executionPlanArg)
    changeButton2.grid(row=6, column=0,columnspan=2, padx=20,pady=20, sticky="ew")




def message():
     global pop
     pop = Toplevel(root)
     pop.title("message")
     pop.geometry("250x150")
     pop_frame = Frame(pop)
     pop_frame.pack(pady=5)
     pop_label = ctk.CTkLabel(master=pop_frame,text="file updated successfully")
     pop_label.grid(row=1,column=0)
     ok = ctk.CTkButton(pop_frame, text="ok", command=pop.destroy)
     ok.grid(row=2,column=0)
     
# def display_text():
#    global entry
#    global string
#    string= entry.get()

# def get_user_input():
#     global user_input
#     user_input = filedialog.askdirectory()
#     return user_input
   
    
def updateTestCaseArg():
    file = browseFiles()
    updateTestCase(file,"List of devices attached R59RA00NL7D device LMG900EMf7a2d5d5 device R58M36NV1GD device R58N91KCNYY device 215cf1f7 device",'new',directory)
    message()

def executionPlanArg():
    file = browseFiles()
    executionPlan(file,"List of devices attached R59RA00NL7D device LMG900EMf7a2d5d5 device R58M36NV1GD device R58N91KCNYY device 215cf1f7 device",directory)    
    message()



root = ctk.CTk()

root.geometry('400x400')

Label1 = ctk.CTkLabel(master=root,text="select the excel file to update")
Label1.grid(row=0, column=0,padx=20, pady=20,sticky="ew")

changeButton1 = ctk.CTkButton(master=root,text="Choose directory to save updated file",command=choose_directory)
changeButton1.grid(row=4, column=0,columnspan=2, padx=20,pady=20, sticky="ew")



# entry= Entry(root, width= 300)
# entry.focus_set()
# entry.grid(row=7, column=0,columnspan=2, padx=20,pady=20, sticky="ew")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()