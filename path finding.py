#A* SEARCH ALGORITHM WRITTEN BY SIMONE RUSSO, ANDREA DE RINALDIS AND OSVALDO MERLO

import csv
import math

def a_star_research(initial_state, goal, file):

    OPEN = []
    CLOSED = []
    nodes_list = []
    arcs_list = []
    path = {}
    f = {}
    successor = []

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_counter = 0    #This line helps us to understand what we are reading because the input file has its own format.
                            #In the first row, we have the node number and subsequently we have the nodes.
                            #At the end of the nodes, we have the arc number and the list of those arcs.

        #READING ALL DATA FROM CSV FILE
        for row in csv_reader:
            if(line_counter==0):
                line_counter += 1
                nodes_number=int(row[0])
                
            elif line_counter < nodes_number+1:
                line_counter +=1
                node = [row[0], row[1], row[2], row[3]]
                if node[1] == "'"+initial_state+"'":
                    OPEN.append(node)
                    initial_state_node = node
                if(node[1] == "'"+goal+"'"):
                    goal_node=node
                nodes_list.append(node)
                
            elif line_counter == nodes_number+1:
                arcs_number = int(row[0])
                line_counter +=1
                
            elif line_counter > nodes_number+1:
                line_counter +=1
                arc = [row[0], row[1], row[2]]
                arcs_list.append(arc)

    #SUCCESSOR
    while OPEN: #This while starts if there is at least 1 element in the open list 
        current_node = OPEN[0]

        if(current_node == goal_node):
            print(build_path(path, goal_node, initial_state_node))
            return

        find_successor(current_node, arcs_list, nodes_list, OPEN, CLOSED, goal_node, path, f)
        CLOSED.append(current_node)
        OPEN.remove(current_node)
        
        merge_sort(OPEN, f)

    print("Non esiste una soluzione")
        

def find_successor(parent, arcs_list, nodes_list, OPEN, CLOSED, goal, path, f):
    
    for arc in arcs_list:#We get all the arcs
        g=0 
        if arc[0] == parent[0]:                                 #We check if we're able to generate the neighbours using this arc
            for node in nodes_list:                             #We get all the nodes
                if arc[1] == node[0]:                           #Now, the question is: Can we go to this node (is this its neighbour?)
                    if node not in OPEN and node not in CLOSED: #Is it in the open list or in the closed list?
                        print("successor:" + node[1])
                        OPEN.append(node)
                        if parent[1] in path.keys():
                            g = path[parent[1]][1]
                        else:
                            g = 0
                            
                        g += int(arc[2])
                        path[node[1]] = [parent[1], g]  #in path the key is the neighbour and the value is a list which contains the parent and the cost of arc
                        f[node[0]]=g+heuristic_function(node, goal)
                        

#SORTING ALGORITHM ADAPTED TO THIS PROBLEM
def merge_sort(OPEN, f): 
    if len(OPEN) >1: 
        mid = len(OPEN)//2 #Finding the mid of the hay
        # Dividing the hay elements into 2 halves 
        L_open = OPEN[:mid]
        R_open = OPEN[mid:]
  
        merge_sort(L_open, f) # Sorting the first half 
        merge_sort(R_open, f) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp hays L[] and R[] 
        while i < len(L_open) and j < len(R_open): 
            if f[L_open[i][0]] < f[R_open[j][0]]: 
                OPEN[k] = L_open[i]
                i+= 1
            else: 
                OPEN[k] = R_open[j]
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L_open): 
            OPEN[k] = L_open[i]
            i+= 1
            k+= 1
          
        while j < len(R_open): 
            OPEN[k] = R_open[j]
            j+= 1
            k+= 1


def build_path(path, goal, initial_state_node): #this function finds the path, starting from the bottom (the goal)
                                                #As soon as I know how to reach the goal, I can go back to his parent because in variable path there is the node
                                                #I visited (as key) and his parent (as value)
                                                
                                            
    name_node = goal[1]
    p = []
    for key in reversed(path):
        if (key == name_node):
            p.append(name_node)
            name_node= path[key][0]
        
    p.append(initial_state_node[1])
    p.reverse()                                 #Now I reverse the list because I looked for the path, starting from the bottom
    return p

# HERE WE CALCULATE THE HEURISTIC FUNCTION USING THE GEOGRAPHIC COORDINATES
def heuristic_function(node, goal):         
    R = 6371.009
    conv=math.pi/180
    d_fi = float(node[2]) - float(goal[2])
    fi_m = (float(node[2]) + float(goal[2]))/2
    d_lambda = float(node[3]) - float(goal[3])
    return ((R*math.sqrt(pow(d_fi*conv,2) + pow(math.cos((fi_m)*conv)*d_lambda*conv,2))/130)*60)
    
