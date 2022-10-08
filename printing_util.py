import pydot

def draw(parent_name, child_name, graph):
    edge = pydot.Edge(str(parent_name), str(child_name))
    graph.add_edge(edge)

def get_name(id, value):
    return "("+str(id)+") "+str(value)

def visit_forest(h_tree, graph, parent = "*"):
    id = 0
    for key in h_tree:
        h_node = h_tree[key]
        name = get_name(id, key)
        draw("*", name, graph)
        id += 1
        id = visit_h_node(h_node, name, graph, id)

def visit_h_node(h_node, parent, graph, id):
    name = get_name(id, h_node["item"])
    id += 1
    
    draw(parent, name, graph)
    for child in h_node["children"]:
        id = visit_h_node(child, name, graph, id)
    
    if h_node["leaf"] != None:
        draw(name, get_name(id, str(h_node["leaf"])), graph)
        id += 1
    return id


def generate_forest_image(h_tree, filename):
    graph = pydot.Dot(graph_type='graph')
    visit_forest(h_tree, graph)
    graph.write(path=filename, format="png")