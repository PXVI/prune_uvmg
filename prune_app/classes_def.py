'''
    The file which contains all the class definitions for use in the app
'''

from global_vars import *

# Basic prune class object definition
class pobj:
    #obj_name = ""
    #obj_type = ""
    #obj_depth = 0
    #obj_parent = ""
    
    # General Count Local Variable
    count = 0

    # Unique Node Id Vaulue
    #node_id
    master_node = [ '' ]

    # Component/Arc Files Lists & Counts ( Using Dictionary )
    comp_file_list = []
    comp_file_name_dict = {}
    comp_file_count_dict = {}

    # Depth wise traversal node accounting
    local_node = [ 0 ]

    # Array/List of recursive objects
    #obj_list = []

    def create_child4(self, obj_name, obj_type, obj_depth, obj_parent, obj_root, local_node):
        self.obj_name = obj_name
        self.obj_type = obj_type
        self.obj_depth = obj_depth
        self.obj_parent = obj_parent
        self.obj_list = []
        self.obj_root = obj_root
        self.local_node = local_node
        self.count = 0
        #self.node_count = 0

    #def create_child3(self, obj_name, obj_type, obj_depth):
    #    self.obj_name = obj_name
    #    self.obj_type = obj_type
    #    self.obj_depth = obj_depth
    #    self.obj_parent = ""
    #    self.obj_list = []
    #    self.obj_root = obj_root
    #    #self.node_count = 0
    
    def __init__(self, obj_name, obj_type):
        self.obj_name = obj_name
        self.obj_type = obj_type
        self.obj_depth = 0
        self.obj_parent = self
        # Points to the absolute root
        self.obj_root = self
        self.last_created_child = self
        self.count = 0
        self.node_id = 0
        if( self.master_node[0] == '' ):
            # Do nothing
            self.master_node[0] = 0
            self.node_id = -1;
        else:
            self.master_node[0] += 1
            self.node_id = self.master_node[0]
        # Points to itself
        self.obj_list = []
        #self.node_count = 0
        self.local_node = [ 0 ]
        self.update_dict_and_list()

    def print_det(self):
        print( self.obj_depth + " - " + self.obj_name + " : " + self.obj_type )

    def create_child(self, obj_name, obj_type):
        x = pobj(obj_name, obj_type)
        self.last_created_child = x
        x.create_child4(obj_name, obj_type, self.obj_depth+1, self, self.obj_root, self.local_node)
        if( ( len( self.local_node ) - 1 ) < x.obj_depth ):
            # First node of the new depth
            print( "----------------------------------------------------------" )
            print( "Old Local Node : " + str(len( self.local_node )-1) + " : x.depth : " + str(x.obj_depth) )
            self.local_node.append( 0 )
            print( "New Local Node : " + str(len( self.local_node )-1) + " : x.depth : " + str(x.obj_depth) )
            print( "----------------------------------------------------------" )
        #x.obj_name = obj_name
        #x.obj_type = obj_type
        #x.obj_depth = self.obj_depth+1
        #x.obj_parent = self
        #self.node_count = self.node_count + 1
        #x.node_count = self.node_count
        self.obj_list.append( x )
        print( "Node Created : " + str(x.obj_depth) + " : " + x.obj_name + " : (p) " + x.obj_parent.obj_name + " : " + x.obj_type + " : " + str(len(self.obj_list)) + " : " + str(len(x.obj_list)) + " : " + str(len(self.local_node)) )

    # Update the dictionary & list
    def update_dict_and_list(self):
        if( len(self.comp_file_list) == 0 ):
            self.comp_file_list.append( self.obj_type )
            self.comp_file_name_dict[self.comp_file_list[0]] = []
            self.comp_file_name_dict[self.comp_file_list[0]].append( self.obj_name)
            self.comp_file_count_dict[self.comp_file_list[0]] = 1
        else:
            exists = 0
            m = 0
            while( m < len(self.comp_file_list )):
                if( self.comp_file_list[m] == self.obj_type ):
                    exists = 1
                    self.comp_file_name_dict[self.comp_file_list[m]].append(self.obj_name)
                    self.comp_file_count_dict[self.comp_file_list[m]] += 1

                m += 1

            if( exists == 0 ):
                self.comp_file_list.append( self.obj_type )   
                self.comp_file_name_dict[self.comp_file_list[len(self.comp_file_list)-1]] = []
                self.comp_file_name_dict[self.comp_file_list[len(self.comp_file_list)-1]].append(self.obj_name)
                self.comp_file_count_dict[self.comp_file_list[len(self.comp_file_list)-1]] = 1

    # Print the architecture details in a readable format
    def print_arc_readable(self):
        if( len(self.comp_file_list) != 0 ):
            n = 0
            while( n < len(self.comp_file_list) ):
                print( self.comp_file_list[n] + " : " + str(self.comp_file_count_dict[self.comp_file_list[n]]) )
                #print( self.comp_file_name_dict[self.comp_file_list[n]] )
                for k in self.comp_file_name_dict[self.comp_file_list[n]]:
                    print( "    " + k )
                n += 1
        else:
            print( "[E] Nothing to print" )

    # Print the tree from the current node
    def print_cur_tree(self):
        # Depth first search and printing will be performed
        print( "Start Tree Node : " + str(self.obj_depth) + " : " + self.obj_name + " : " + self.obj_type + " : Node_ID ( " + str(self.node_id) + " ) : Parent Node_ID ( " + str(self.obj_parent.node_id) + " )" )
        if( len(self.obj_list) != 0 ):
            for obj in self.obj_list:
                #print( "Tree Node : " + str(obj.obj_depth) + " : " +obj.obj_name + " : " + obj.obj_type + " : " + str(len(obj.obj_list)) )
                obj.print_cur_tree()
    
    # Print the tree from the absolute root node
    def print_tree(self):
        # Depth first search and printing will be performed
        print( "Root Tree Node : " + str(self.obj_root.obj_depth) + " : " + self.obj_root.obj_name + " : " + self.obj_root.obj_type + " : Node_ID ( " + str(self.node_id) + " ) : Parent Node_ID ( " + str(self.obj_parent.node_id) + " )" )
        if( len(self.obj_root.obj_list) != 0 ):
            for obj in self.obj_root.obj_list:
                #print( "Tree Node : " + str(obj.obj_depth) + " : " +obj.obj_name + " : " + obj.obj_type + " : " + str(len(obj.obj_list)) )
                obj.print_cur_tree()

    # Get the parent node's pointer
    # - Done -
    def get_parent(self):
        return self.obj_parent

    # Get the root node's pointer
    # - Done -
    def get_root(self):
        return self.obj_root

    # Check if the current obj instance is the absolute root node
    def isParent(self):
        if( self == self.obj_root ):
            return 1
        else:
            return 0

    # Move one depth layer down
    # - Done -
    def tree_depth_down(self):
        if( len( self.obj_list ) ):
            print( "---------------------------------------------- Dive" )
            return self.obj_list[self.local_node[self.obj_depth+1]]
        else:
            print( "[E] No lower nodes have been created. Try again" )
            return self
    
    # Move one depth layer down into the child node that was most recently created
    # - Done -
    def tree_depth_down_last_created(self):
        if( len( self.obj_list ) ):
            print( "---------------------------------------------- Dive" )
            return self.obj_list[len(self.obj_list)-1]
        else:
            print( "[E] No lower nodes have been created. Try again" )
            return self

    # Go to the next node in the current depth
    # - Done -
    def next_node(self):
        print( "********* Next Node : " + str(len( self.obj_parent.obj_list )) + " : " + str( self.local_node[self.obj_parent.obj_depth] ) )
        if( len( self.obj_parent.obj_list ) > self.local_node[self.obj_parent.obj_depth]+1 ):
            self.local_node[self.obj_parent.obj_depth] += 1
            print( "+++++++++ Next Node : " + str( self.local_node[self.obj_parent.obj_depth] ) + " : " + self.obj_parent.obj_list[self.local_node[self.obj_parent.obj_depth]].obj_name )
            return self.obj_parent.obj_list[self.local_node[self.obj_parent.obj_depth]]
        else:
            # Return the current last node of the depth
            return self.obj_parent.obj_list[self.local_node[self.obj_parent.obj_depth]]
    
    # Go to the next node in the current depth
    # - Done -
    def prev_node(self):
        print( "^^^^^^^^^^^^^^^^ Prev Node : " + str(len( self.obj_parent.obj_list )) + " : " + str(self.local_node[self.obj_parent.obj_depth]) )
        if( len( self.obj_parent.obj_list ) > 0 and self.local_node[self.obj_parent.obj_depth] > 0 ):
            self.local_node[self.obj_parent.obj_depth] -= 1
            return self.obj_parent.obj_list[self.local_node[self.obj_parent.obj_depth]]
        else:
            # Return the zeroth node of the depth
            return self.obj_parent.obj_list[self.local_node[self.obj_parent.obj_depth]]

    # Reset all the local node values
    def reset_local_node(self):
        for val in self.local_node:
            val = 0

    # Move one depth layer up
    # - Done -
    def tree_depth_up(self):
        if( self == self.obj_parent ):
            print( "Self : " + self.obj_name + " : " + self.obj_parent.obj_name )
            print( "[E] Already at the highest possible node." )
            return self
        else:
            i = self.obj_depth
            print( str( self.obj_depth ) + " : " + str( len( self.local_node ) ) + " : " + self.obj_parent.obj_name )
            while( i < len( self.local_node ) ):
                self.local_node[i] = 0
                i += 1
            print( "---------------------------------------------- Surface" )
            return self.obj_parent

    # Search obj_name TODO

    # Search obj_type TODO

    # Generic Method
    def gen_arc_tree(self, root, str_list):
        print( str_list )
    
        print( "Root : " + root.obj_name + " : " + str(root.obj_depth) )
    
        if( len(str_list) == 3 and str_list[0] == "begin" ):
            root.create_child( str_list[1], str_list[2] )
            root = root.tree_depth_down_last_created()
            print( "Root : " + root.obj_name + " : " + str(root.obj_depth) )
        elif( len(str_list) == 1 and str_list[0] == "end" ):
            root = root.tree_depth_up()
        else:
            print( "[E] <keylen> Syntax error in the arc format file" )

    # Search type & return count staring the earch from root
    def search_type_return_count_from_root(self, typ_name, initial_count):

        if( len(self.obj_root.obj_list) != 0 ):
            for obj in self.obj_root.obj_list:
                if( obj.obj_type == typ_name ):
                    initial_count += 1
                initial_count = obj.search_type_return_count(typ_name, initial_count)
        return initial_count
    
    # Search type & return count staring the earch from current node
    def search_type_return_count(self, typ_name, initial_count):

        if( len(self.obj_list) != 0 ):
            for obj in self.obj_list:
                if( obj.obj_type == typ_name ):
                    initial_count += 1
                initial_count = obj.search_type_return_count(typ_name, initial_count)
        return initial_count

    # Generate Treeview for the frame
    def generate_treeview(self, obj, my_tree):
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
        #my_tree.insert(parent='', index='end', iid=0, text="tb_name")
        self.treeview_insert(my_tree)

    # Insert Data Fields From Root Node
    def treeview_insert(self, my_tree):
        if( len(self.obj_root.obj_list) ):
            if( self.obj_parent.node_id == -1 ):
                my_tree.insert(parent='', index='end', iid=self.node_id, text=str(self.obj_name + "(" +self.obj_type + ")"))
            else:
                my_tree.insert(parent=self.obj_parent.node_id, index='end', iid=self.node_id, text=str(self.obj_name + "(" +self.obj_type + ")"))
            
            if( len(self.obj_root.obj_list) != 0 ):
                for obj in self.obj_list:
                    obj.treeview_insert_from_cur(my_tree)
        else:
            print( "[E] The arc file is empty. Layout cannot be loaded." )

    # Insert Data Fields From Current Node
    def treeview_insert_from_cur(self, my_tree):
        my_tree.insert(parent=self.obj_parent.node_id, index='end', iid=self.node_id, text=str(self.obj_name + "(" +self.obj_type + ")"))
        
        if( len(self.obj_list) != 0 ):
            for obj in self.obj_list:
                obj.treeview_insert(my_tree)
        

# ----------------------------------------------
# --------------- Testing ----------------------
# ----------------------------------------------

#parent = pobj( "parent", "dir" )
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent.create_child( "ch0", "dir" )
#parent.create_child( "ch1", "dir" )
#parent = parent.tree_depth_down()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent.create_child( "ch2", "dir" )
#parent.create_child( "ch3", "dir" )
#parent = parent.tree_depth_down()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent = parent.tree_depth_down()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent = parent.tree_depth_down()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent = parent.tree_depth_down()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent = parent.tree_depth_down()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent.create_child( "ch4", "dir" )
#parent.create_child( "ch5", "dir" )
#parent.create_child( "ch6", "dir" )
#parent = parent.tree_depth_down()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent.create_child( "ch7", "dir" )
#parent.create_child( "ch8", "dir" )
#parent.create_child( "ch9", "svfile" )
#parent = parent.tree_depth_up()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent = parent.next_node()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent = parent.next_node()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent = parent.next_node()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent.create_child( "ch14", "dir" )
#parent.create_child( "ch15", "dir" )
#parent = parent.prev_node()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent = parent.prev_node()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent = parent.prev_node()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent = parent.prev_node()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent.create_child( "ch10", "svfile" )
#parent.create_child( "ch11", "svfile" )
#parent.create_child( "ch12", "svfile" )
#parent = parent.tree_depth_up()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent = parent.tree_depth_up()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent = parent.tree_depth_up()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent = parent.tree_depth_up()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent = parent.tree_depth_up()
#print( "============== " + str( parent.obj_depth ) + " : " + parent.obj_name + " =============" )
#parent.create_child( "ch13", "svfile" )
#print( "-----------------------" )
#parent.print_tree()

# ----------------------------------------------------------------------
# Experimental Code To Generate A Architecture Tree From The Format File
# ----------------------------------------------------------------------

# Generic funtion to be called in order to build the architecture file
def gen_arc_tree(root, str_list):
    print( str_list )

    print( "Root : " + root.obj_name + " : " + str(root.obj_depth) )

    if( len(str_list) == 3 and str_list[0] == "begin" ):
        root.create_child( str_list[1], str_list[2] )
        root = root.tree_depth_down_last_created()
    elif( len(str_list) == 1 and str_list[0] == "end" ):
        root = root.tree_depth_up()
    else:
        print( "[E] <keylen> Syntax error in the arc format file" )
    return root

# Open a file and load the lines in a list
def open_file_r(fname):
    f = open( fname, "r" )
    return fname

# Close an open file
def close_file(f):
    f.close()

'''
root = pobj( "top", "dir" )


f = open( "tb_layout_v2.fmt", "r" )

for x in f:
    #print(f.readline().rstrip('\n').replace(" ",""))
    str_list = x.rstrip('\n').replace(" ","").split(sep=':')
    print( str_list )
    #print( x.rstrip('\n').replace(" ","").splt(sep=':') )
    root = gen_arc_tree(root, str_list)

f.close()

print( "----------------------------------------------------------------------" )

root.print_tree()
print( "----------------------------------------------------------------------" )
root.print_arc_readable()
'''
