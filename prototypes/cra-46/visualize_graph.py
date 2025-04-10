#!/usr/bin/env python3
import pydot
from workflow import builder

def create_graph_visualization():
    """Create a visualization of the workflow graph using pydot."""
    # Create a new directed graph
    graph = pydot.Dot(graph_type='digraph')
    
    # Add nodes
    for node in builder.nodes:
        graph.add_node(pydot.Node(node, shape="box"))
    
    # Add start node
    graph.add_node(pydot.Node("__start__", shape="circle"))
    
    # Add edges
    for edge in builder.edges:
        graph.add_edge(pydot.Edge(edge[0], edge[1]))
    
    # Save the graph
    graph.write_png("workflow_graph.png")
    print("Graph visualization saved as workflow_graph.png")

if __name__ == "__main__":
    create_graph_visualization()
