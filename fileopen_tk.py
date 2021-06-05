import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
filename= os.path.basename(file_path).rsplit( ".", 1 )[ 0 ] 


print(file_path)
print(filename)

with open('%s.txt'%filename, 'w') as f:
    print('Filename:', file_path, file=f)  # Python 3.x
    