# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:02:13 2022

@author: shane
"""
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

g=nx.Graph()
g.add_node(1)
g.nodes()
g.add_nodes_from([2, 3, 4])
g.nodes()
g.add_edge(1, 2)
g.edges()
g.add_edges_from([(3, 4), (5, 6)])
g.edges()
g.add_weighted_edges_from([(7, 8, 1.5),(9, 10, 3.5)])
g.edges(data=True)
e=(2,7)
g.add_edge(*e)
#nx.draw_networkx(g,node_color='green',node_size=250)

G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 5)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)

# explicitly set positions
pos = {1: (0, 0), 2: (-1, 0.3), 3: (2, 0.17), 4: (4, 0.255), 5: (5, 0.03)}

options = {
    "font_size": 36,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G, pos, **options)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()