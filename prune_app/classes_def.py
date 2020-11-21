'''
    The file which contains all the class definitions for use in the app
'''

# Basic prune class object definition
class pobj:
    #obj_name = ""
    #obj_type = ""
    #obj_depth = 0
    #obj_parent = ""
    
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
        # Points to itself
        self.obj_list = []
        #self.node_count = 0
        self.local_node = [ 0 ]

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

    # Print the tree from the current node
    def print_cur_tree(self):
        # Depth first search and printing will be performed
        print( "Start Tree Node : " + str(self.obj_depth) + " : " + self.obj_name + " : " + self.obj_type )
        if( len(self.obj_list) != 0 ):
            for obj in self.obj_list:
                #print( "Tree Node : " + str(obj.obj_depth) + " : " +obj.obj_name + " : " + obj.obj_type + " : " + str(len(obj.obj_list)) )
                obj.print_cur_tree()
    
    # Print the tree from the absolute root node
    def print_tree(self):
        # Depth first search and printing will be performed
        print( "Root Tree Node : " + str(self.obj_root.obj_depth) + " : " + self.obj_root.obj_name + " : " + self.obj_root.obj_type )
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
'''
