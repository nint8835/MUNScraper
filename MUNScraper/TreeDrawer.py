from typing import List

import networkx as nx
from networkx.drawing.nx_pydot import write_dot, to_pydot
import matplotlib.pyplot as plt

from .CourseScraper import scrape_courses

def _add_node(graph, node, colours):
    if isinstance(node, str):
        content = node
    else:
        content = repr(node)
    try:
        colour = colours[content[:4]]
    except KeyError:
        colour = "#DDDDDD"
    graph.add_node(content, fillcolor=colour, style="filled")


def draw_tree(urls: List[tuple], colours: dict):
    courses = []
    for url in urls:
        courses += scrape_courses(*url)
    
    G = nx.DiGraph()

    for course in courses:
        if repr(course) not in G:
            _add_node(G, course, colours)
        for dep in course.requirements:
            if str(dep) not in G:
                _add_node(G, dep, colours)
            G.add_edge(str(dep), repr(course))
    
    for node in list(G.nodes()):
        if len(list(G.out_edges(node)) + list(G.in_edges(node))) == 0:
            G.remove_node(node)

    p = to_pydot(G)
    p.write_png('example.png')