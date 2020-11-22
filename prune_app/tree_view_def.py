from global_vars import *
from classes_def import *
import tkinter
from tkinter import ttk

'''
win_width=500
win_height=500

root = tkinter.Tk()
root.title("Prune v0.1")
root.geometry(str(win_width)+"x"+str(win_height))

# Code goes here

my_tree = ttk.Treeview(root)

# Define our columns
#my_tree['columns'] = ("Name", "Type") # Main columns + phantom column | Will only use the phantom column

# Format for columns
my_tree.column("#0", width=win_width, minwidth=int(win_width/2))
#my_tree.column("Name", anchor="w", width=120, minwidth=25)
#my_tree.column("Type", anchor="center", width=120, minwidth=25)

# Create heading
my_tree.heading("#0", text="Testbench File Layout", anchor="center")
#my_tree.heading("Name", text="F/C Name", anchor="w")
#my_tree.heading("Type", text="F/C Type", anchor="center")

# Add Data # Alternative Suggestion - Just use the test field for the primary data holder. In our case, the name of the person
my_tree.insert(parent='', index='end', iid=0, text="tb_name")
my_tree.insert(parent=0, index='end', iid=1, text="common")
my_tree.insert(parent=0, index='end', iid=2, text="components")
my_tree.insert(parent=0, index='end', iid=3, text="tests")
my_tree.insert(parent=0, index='end', iid=4, text="sequences")
my_tree.insert(parent=0, index='end', iid=5, text="runfiles")

# Adding Children
#my_tree.insert(parent='', index='end', iid=6, text="Child", values=("Cheeto", "Human"))
#my_tree.move(6, 0, 0)
#my_tree.insert(parent=6, index='end', iid=7, text="Grandchild", values=("Dune", "Human"))
#my_tree.insert(parent=6, index='end', iid=8, text="Grandchild", values=("Dima", "Human"))
#my_tree.insert(parent=6, index='end', iid=9, text="Grandchild", values=("Diane", "Human"))
#my_tree.insert(parent=9, index='end', iid=10, text="GGC", values=("Eric", "Human"))

my_tree.insert(parent=1, index='end', iid=11, text="misc")
my_tree.insert(parent=1, index='end', iid=12, text="source")
my_tree.insert(parent=2, index='end', iid=13, text="environment")
my_tree.insert(parent=2, index='end', iid=14, text="master")
my_tree.insert(parent=2, index='end', iid=15, text="slave")
my_tree.insert(parent=2, index='end', iid=16, text="monitor")
my_tree.insert(parent=2, index='end', iid=17, text="scoreboard")
my_tree.insert(parent=14, index='end', iid=18, text="driver")
my_tree.insert(parent=14, index='end', iid=19, text="sequencer")
my_tree.insert(parent=15, index='end', iid=20, text="driver")
my_tree.insert(parent=15, index='end', iid=21, text="sequencer")

# Pack to the screen
my_tree.pack(pady=20)

# App running loop
root.mainloop()
'''

def generic_tb_populate_treeview( frame ):
    my_tree = ttk.Treeview(frame)

    f = open( "tb_layout_v2.fmt", "r" )
       
    base = pobj( "top", "dir" )
    for x in f:
        #print(f.readline().rstrip('\n').replace(" ",""))
        str_list = x.rstrip('\n').replace(" ","").split(sep=':')
        print( str_list )
        #print( x.rstrip('\n').replace(" ","").splt(sep=':') )
        base = gen_arc_tree(base, str_list)

    base.generate_treeview(base, my_tree)
    my_tree.pack(fill="both")
    base.print_tree()
    #base.print_arc_readable()

    f.close()
