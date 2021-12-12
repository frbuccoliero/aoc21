class Node:
	def __init__(self,name,links):
		self.name = name
		self.isStart = (True if name == "start" else False)
		self.isEnd = (True if name == "end" else False)
		self.links = links
		self.big = name[0].isupper()
	def addNext(self,l):
		if self not in l.links:
			l.links.append(self)
		if l not in self.links:
			self.links.append(l)

def loadNodes():
	links = [line.rstrip() for line in open('input')]

	nodenames = []
	nodes = []
	
	linksdic = {}

	for link in links:
		frm = link.split("-")[0]
		to = link.split("-")[1]

		if frm not in linksdic:
			linksdic[frm] = []
		linksdic[frm].append(to)

		if to not in linksdic:
			linksdic[to] = []
		linksdic[to].append(frm)

		if frm not in nodenames:
			nodenames.append(frm)
		if to not in nodenames:
			nodenames.append(to)

	for name in nodenames:
		n = Node(name,[])
		nodes.append(n)

	for l,lto in linksdic.items():
		n = [x for x in nodes if x.name == l][0]
		for lt in lto:
			ltn = [x for x in nodes if x.name == lt][0]
			n.addNext(ltn)
	return nodes

globalPaths = []

def exploreNode(node,visited,comesFrom):
	#cfn = comesFrom.name if comesFrom is not None else 'nobody' 
	#print("--")
	#print(f"I'm {node.name} from {cfn},visited:{[x.name for x in visited]}, nexts:{[x.name for x in node.links]}")
	if node.isEnd:
		globalPaths.append(visited)
	else:
		for nx in node.links:
			if (not nx.big and nx not in visited) or nx.big:
				visited.append(nx)
				exploreNode(nx,visited,node)
				visited.pop()

nodes = loadNodes()

start = [x for x in nodes if x.isStart][0]

visited = [start]

exploreNode(start,visited,None)

print(len(globalPaths))

# thanks to @mattteochen for the help with this one
