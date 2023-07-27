from tkinter import *
import tkinter as tk
from tkinter import simpledialog,filedialog,Toplevel, Frame, Canvas, Scrollbar
import customtkinter as ctk
from Test_Case import *
from Connected_Devices import *





ctk.set_appearance_mode("System")  
 
# Sets the color of the widgets in the window
ctk.set_default_color_theme("green")   
 
# Dimensions of the window
appWidth, appHeight = 800, 900

# allows user to select a file
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Excel files","*.xlsx*"),))
    return filename

# asks a user to choose where to save the file
def choose_directory():
    global directory
    directory = filedialog.askdirectory()
    changeButton1 = ctk.CTkButton(master=root,text="Select test case",command=updateTestCaseArg)
    changeButton1.grid(row=5, column=0,columnspan=2, padx=20,pady=20, sticky="ew")

    changeButton2 = ctk.CTkButton(master=root,text="Select execution plan",command=executionPlanArg)
    changeButton2.grid(row=6, column=0,columnspan=2, padx=20,pady=20, sticky="ew")





#####  test case #####

# displays message after the changes are made
def messageUpdated1():
     global pop
     pop = Toplevel(root)
     pop.title("message")
     pop.geometry("250x150")
     pop_frame = Frame(pop)
     pop_frame.pack(pady=5)
     pop_label = ctk.CTkLabel(master=pop_frame,text="file updated successfully")
     pop_label.grid(row=1,column=0)
     ok = ctk.CTkButton(pop_frame, text="see changes", command=getNewAndOld1)
     ok.grid(row=2,column=0)

# displays the changes made
def getNewAndOld1():
    global pop
    pop = Toplevel(root)
    pop.title("message")
    pop.geometry("500x350")
    pop_frame = Frame(pop)
    pop_frame.pack(pady=5)
    changes = getChangesTestCase()
     
    for i, change in enumerate(changes):
        pop_label = ctk.CTkLabel(master=pop_frame, text=change)
        pop_label.grid(row=i, column=0, padx=5, pady=5)
    
    ok = ctk.CTkButton(pop_frame, text="ok", command=pop.destroy)
    ok.grid(row=6,column=0)
     
def updateTestCaseArg():
    user_input = simpledialog.askstring("Input", "Enter the name of the updated file")
    file = browseFiles()
    updateTestCase(file,"List of devices attached R59RA00NL7D device LMG900EMf7a2d5d5 device R58M36NV1GD device R58N91KCNYY device 215cf1f7 device",user_input,directory)
    messageUpdated1()


#####   execution plan   #####

# asks user where the test case files are saved
def messagePath():
    global pop
    pop = Toplevel(root)
    pop.title("choose path")
    pop.geometry("750x150")
    pop_frame = Frame(pop)
    pop_frame.pack(pady=5)
    pop_label = ctk.CTkLabel(master=pop_frame,text="select the folder in which the test case files are saved")
    pop_label.grid(row=1,column=0)
    ok = ctk.CTkButton(pop_frame, text="browse", command=choose_directory2)
    ok.grid(row=2,column=0)
    

# allows user to chose the path in which test case files are saved
def choose_directory2():
    global directory2
    pop.destroy()
    directory2 = filedialog.askdirectory()
    if directory2:
        executionPlan(file,directory2,"List of devices attached R59RA00NL7D device LMG900EMf7a2d5d5 device R58M36NV1GD device R58N91KCNYY device 215cf1f7 device",directory)    
        messageUpdated2()

# displays message after the changes are made
def messageUpdated2():
     global pop
     pop = Toplevel(root)
     pop.title("message")
     pop.geometry("250x150")
     pop_frame = Frame(pop)
     pop_frame.pack(pady=5)
     pop_label = ctk.CTkLabel(master=pop_frame,text="file updated successfully")
     pop_label.grid(row=1,column=0)
     ok = ctk.CTkButton(pop_frame, text="see changes", command=getNewAndOld2)
     ok.grid(row=20,column=0)


# displays the changes made
def getNewAndOld2():
    global pop
    pop = Toplevel(root)
    pop.title("Message")
    pop.geometry("500x350")

    # Create a canvas inside the pop-up window
    canvas = Canvas(pop)
    canvas.pack(side="left", fill="both", expand=True)
    
    # Add a frame inside the canvas to hold the content
    pop_frame = Frame(canvas)
    canvas.create_window((0, 0), window=pop_frame, anchor="nw")

    # Create a vertical scrollbar
    scrollbar = Scrollbar(pop, command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas to work with the scrollbar
    canvas.config(yscrollcommand=scrollbar.set)

    # Add the content to the frame (your existing code)
    changes = getChangesExecutionPlan()
    for i, change in enumerate(changes):
        pop_label = ctk.CTkLabel(master=pop_frame, text=change)
        pop_label.grid(row=i, column=0, padx=5, pady=5)

    # Update the canvas scrolling region when the frame changes size
    pop_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Add "OK" button to close the pop-up
    ok = ctk.CTkButton(master=pop_frame, text="OK", command=pop.destroy)
    ok.grid(row=len(changes), column=0, padx=5, pady=5)   

def executionPlanArg():
    global file
    file = browseFiles()
    messagePath()
    


##### main window #####


root = ctk.CTk()

root.geometry('400x400')

Label1 = ctk.CTkLabel(master=root,text="select the excel file to update")
Label1.grid(row=0, column=0,padx=20, pady=20,sticky="ew")

changeButton1 = ctk.CTkButton(master=root,text="Choose directory to save updated file",command=choose_directory)
changeButton1.grid(row=4, column=0,columnspan=2, padx=20,pady=20, sticky="ew")



root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()