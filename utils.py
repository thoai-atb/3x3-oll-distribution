from tkinter import filedialog, Tk
import os

def get_directory():
  root = Tk()
  root.withdraw() # use to hide tkinter window
  currdir = os.getcwd()
  tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
  return tempdir


