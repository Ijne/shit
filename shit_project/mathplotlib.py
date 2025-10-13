import graphviz

dot = graphviz.Digraph('round-table', comment='The Round Table') 
dot.node("A", "First Node")
print(dot.source)
dot.render(directory='doctest-output', view=True) 
