import networkx as nx
G = nx.Graph()

G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)

G.add_edge(0, 3)
G.add_edge(1, 3)
G.add_edge(2, 3)

print(G)


centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
  print("c(",n, ")=", centrality[n])