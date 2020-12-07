import pdb
import networkx as nx
from networkx.algorithms import dag
import re

lines = []
with open('input', 'r') as input_file:
    for line in input_file:
        lines.append(line.strip())

parent_regex = "(.+) bags"
descendant_regex = "(\d+) (.+) bag"

def get_match_from_string(input, regex, index):
    match = re.search(regex, input)
    return  match.group(index + 1)

edges = []
for line in lines:
    splitted = line.split("contain")
    parent = get_match_from_string(splitted[0], parent_regex, 0)
    descendants = []
    if 'no other bags' not in splitted[1]:
        descendants_text = splitted[1].split(',')
        for text in descendants_text:
            descendant_name = get_match_from_string(text, descendant_regex, 1)
            descendant_count = int(get_match_from_string(text, descendant_regex, 0))
            descendants.append((descendant_name, descendant_count))
    for descendant_name, descendant_count in descendants:
        for i in range(descendant_count):
            edges.append((parent, descendant_name))

graph = nx.MultiDiGraph()
graph.add_edges_from(edges)
ancestors = dag.ancestors(graph, "shiny gold")

print(f"Part 1: {len(ancestors)}")


descendants = dag.descendants(graph, "shiny gold")

def get_descendant(nodes, parent_name):
    contain_count = 1
    for descendant in nodes:
        edge_count = graph.number_of_edges(parent_name, descendant)
        nested_descendants = list(dag.descendants(graph, descendant))

        if not nested_descendants:
            contain_count += edge_count
        else:
            contain_count += edge_count * get_descendant(nested_descendants, descendant)
        continue

    return contain_count

print(f'Part 2: {get_descendant(descendants, "shiny gold") - 1}')
