import linecache
class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

    # print the output
	def printSolution(self, src , dest ,dist):
		print("Path cost from  source node" , src , "to the destination node " , dest , 'is : ' , dist[dest])

    # check for the minimum of heuristic values and it should be not visited
	def minDistance(self, dist, sptSet):

		min = 1e7

		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

    # update the heuristic values using relaxation function
	def astar(self, src , dest , dist):
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):
			u = self.minDistance(dist, sptSet)
			sptSet[u] = True


			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]
        
		self.printSolution(src , dest , dist)


##############---- input from file using file handling ----- ##############

# (47-51) read the first line and split it in to a list . These are our heuristic values
with open('data.txt') as f:
    s = f.readline()
heu = s.split(',')
heu = [ int(x) for x in heu ]
# print(heu)

#using linecache we can able to access any line in the file
# (55 - 57) Accesing second line and filtering(extracting digits in string) , also making it as source
line = linecache.getline(r"data.txt", 2)
src = list(filter(str.isdigit, line))
src = int(''.join(src))

# (61 - 64) Accesing thrid line and filtering(extracting digits in string) , also making it as source
line = linecache.getline(r"data.txt", 3)
dest = list(filter(str.isdigit, line))
dest = int(''.join(dest))

# (66 - 67) Caluculating the length of data file
with open(r"data.txt", 'r') as fs:
	length = len(fs.readlines())

#(69-71) read from line 4 to end of file and append every ine to list
with open('data.txt') as fp:
	nodes = [line.strip() for line in fp.readlines()[4:length]]


# 74 - Intialise matrix with dimension len(heu) X len(heu) to 0
g = Graph(len(heu))


#(79 - 82) Assinging path cost to the nodes from file  
for i in range(len(nodes)):
	# 81 - split every line into three values like [source , destination , cost]
	split_nodes = nodes[i].split(',')
	g.graph[int(split_nodes[0])][int(split_nodes[1])] = int(split_nodes[2])
	g.graph[int(split_nodes[1])][int(split_nodes[0])] = int(split_nodes[2])



##############---- Finding cost from source to desitination using A* ----- ##############
if src in range(0,len(heu)-1) and dest in range(0,len(heu)-1):
	g.astar(src , dest, heu)
else:
	print("There is no path")
