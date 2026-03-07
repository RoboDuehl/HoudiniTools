from tkinter import * 
import zipfile 
import os 
import sys 
import glob 
import pandas as pd 

THEME_COLOR = "#444953"

class FolderInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("test")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.opened_dir = None 
        self.zip_files = None

        
        self.folder_name_label = Label(text="Select Folder: ", bg=THEME_COLOR, fg="#FFFFFF") 
        self.folder_name_label.grid(row=0, column=1)

        #Open button
        self.open_btn_image = PhotoImage(file=r"buttons\open.png")
        self.openDir_btn = Button(bg=THEME_COLOR, image=self.open_btn_image, bd=0, highlightbackground=THEME_COLOR, highlightthickness=0, command=self.openDirectory)
        self.openDir_btn.grid(row=1, column=1)
        self.window.mainloop()


        #open dir function 
    def openDirectory(self):
        print("BUTTON working") 


if __name__ =="__main__":
    ui = FolderInterface()
        
