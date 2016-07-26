import community
import networkx as nx
import matplotlib.pyplot as plt

G = nx.erdos_renyi_graph(30, 0.05)
partition = community.best_partition(G)
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
print "Graph : ", G
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
                                node_color = str(count / size))

print G
nx.draw_networkx_edges(G,pos, alpha=0.5)
plt.show()