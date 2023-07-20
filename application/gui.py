from tkinter import *
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
from Test_Case import *
from Connected_Devices import *





ctk.set_appearance_mode("System")  
 
# Sets the color of the widgets in the window
ctk.set_default_color_theme("green")   
 
# Dimensions of the window
appWidth, appHeight = 600, 700




    

# class App(ctk.CTk):
   
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
 
        
#         self.title("GUI Application")  
        
#         self.geometry(f"{appWidth}x{appHeight}")   
 
        
#         self.nameLabel = ctk.CTkLabel(self,
#                                 text="select the excel file")
#         self.nameLabel.grid(row=0, column=5,
#                             padx=20, pady=20,
#                             sticky="ew")
        
    
#         self.browseButton = ctk.CTkButton(self,
#                                          text="Generate Results",
#                                          command= self.browseFiles)
#         self.browseButton.grid(row=5, column=5,columnspan=2, padx=20,pady=20, sticky="ew")

#          Age Label
#         self.fileLabel = ctk.CTkLabel(self, text="")
#         self.fileLabel.grid(row=1, column=0,
#                            padx=20, pady=20,
#                            sticky="ew")
   
#     def browseFiles(self):
#         self.filename = filedialog.askopenfilename(initialdir = "/",
#                                         title = "Select a File",
#                                         filetypes = (("Excel files",
#                                                     "*.xlsx*"),
#                                                     ))
#         fileLablel.configure(text="File Opened: "+self.filename)
    

# if __name__ == "__main__":
#     app = App()
   
#     app.mainloop() 
# 

def browseFiles():
        
        filename = filedialog.askopenfilename(initialdir = "/",
                                        title = "Select a File",
                                        filetypes = (("Excel files",
                                                    "*.xlsx*"),
                                                    ))
        return filename
        
def updateTestCaseArg():
    file = browseFiles()
    updateTestCase(file,"List of devices attached R59RA00NL7D device LMG900EMf7a2d5d5 device R58M36NV1GD device R58N91KCNYY device 215cf1f7 device",'new')
    Label1 = ctk.CTkLabel(master=root,text="file updated successfully")
    Label1.grid(row=0, column=0,padx=20, pady=20,sticky="ew")

def executionPlanArg():
    file = browseFiles()
    executionPlan(file,"List of devices attached R59RA00NL7D device LMG900EMf7a2d5d5 device R58M36NV1GD device R58N91KCNYY device 215cf1f7 device")    
    Label1 = ctk.CTkLabel(master=root,text="file updated successfully")
    Label1.grid(row=0, column=0,padx=20, pady=20,sticky="ew")

root = ctk.CTk()

root.geometry('400x400')

Label1 = ctk.CTkLabel(master=root,text="select the excel file to update")
Label1.grid(row=0, column=0,padx=20, pady=20,sticky="ew")

# browseButton = ctk.CTkButton(master=root,text="Browse Files",command=browseFiles)
# browseButton.grid(row=1, column=0,columnspan=2, padx=20,pady=20, sticky="ew")

# Label2 = ctk.CTkLabel(master=root, text="the chosen file is:")
# Label2.grid(row=2, column=0,
#                     padx=20, pady=20,
#                     sticky="ew")
# Label3 = ctk.CTkLabel(master=root, text=browseFiles)
# Label3.grid(row=3, column=0,
#                     padx=20, pady=20,
#                     sticky="ew")
    
changeButton1 = ctk.CTkButton(master=root,text="Change test case",command=updateTestCaseArg)
changeButton1.grid(row=4, column=0,columnspan=2, padx=20,pady=20, sticky="ew")

changeButton2 = ctk.CTkButton(master=root,text="Change execution plan",command=executionPlanArg)
changeButton2.grid(row=5, column=0,columnspan=2, padx=20,pady=20, sticky="ew")


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()