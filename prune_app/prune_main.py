'''
    The main file of the prune app.
'''

# File Imports
from global_vars import *
from classes_def import *
from tree_view_def import *

# GUI Imports
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Prune v0.1")
root.geometry(str(win_width)+"x"+str(win_height))
root.resizable(width=False, height=False)

# Global Variables
global curFrame

# 6 Frames will be created from the time being
frame0 = tk.Frame(root, bg="white", height=win_height, width=win_width)
frame1 = tk.Frame(root, bg="white")
frame2 = tk.Frame(root, bg="white")
frame3 = tk.Frame(root, bg="white")
frame4 = tk.Frame(root, bg="white")
frame5 = tk.Frame(root, bg="white")

# Initializations
curFrame = frame0

# Frame0 ( Main Menu )
labf0 = tk.Label(frame0, text="Main Menu", padx=200, pady=10, bg="white")
btf0tof1 = tk.Button(frame0, text="Create TB", width=100, padx=0, pady=2, bg="white", command=lambda: change_frame(frame1))
btf0tofA = tk.Button(frame0, text="Options", width=100, padx=0, pady=2, bg="white") # TODO
btf0tofExit = tk.Button(frame0, text="Exit", width=100, padx=0, pady=2, bg="white", command=lambda: close_gui(root))

# Frame1 ( Create TB )
labf1 = tk.Label(frame1, text="Create TB", padx=200, pady=10, bg="white")
btf1tofX = tk.Button(frame1, text="Custom Testbench", width=100, padx=40, pady=2, bg="white") # TODO
btf1tofY = tk.Button(frame1, text="Testbench From Template", width=100, padx=40, pady=2, bg="white") # TODO
btf1tof2 = tk.Button(frame1, text="Generic Testbench", width=100, padx=40, pady=2, bg="white", command=lambda: change_frame_and_gen_tree(frame2))
btf1tof0 = tk.Button(frame1, text="Back", padx=5, pady=2, bg="white", command=lambda: change_frame(frame0))

# Frame2 ( Create TB )
labf2 = tk.Label(frame2, text="Generic Testbench Details", padx=200, pady=10, bg="white")


# Frame Packing
labf0.pack()
btf0tof1.pack()
btf0tofA.pack()
btf0tofExit.pack()

labf1.pack()
btf1tofX.pack()
btf1tofY.pack()
btf1tof2.pack()
btf1tof0.pack()

labf2.pack()

def close_gui(root):
    root.destroy()

def change_frame(Frame):
    # Clearing the root window first
    global curFrame
    curFrame.pack_forget()
    # Packing the new frame
    curFrame = Frame
    Frame.pack(fill="both", expand=True)

def change_frame_and_gen_tree(Frame):
    change_frame(Frame)
    generic_tb_populate_treeview(Frame)

# Base Frame
frame0.pack(fill="both", expand=True)



#obj_00 = pobj()
#obj_00.obj_name = "common"
#obj_00.obj_type = "dir"
#
#obj_00.print_det()

root.grid_columnconfigure(0, weight=1)
root.mainloop()
