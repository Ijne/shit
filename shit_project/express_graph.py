import urllib.request
import json
from datetime import datetime

def get_express_info():
    try:
        url = "https://registry.npmjs.org/express"
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        latest_version = data['dist-tags']['latest']
        package_data = data['versions'][latest_version]
        
        return {
            'name': package_data['name'],
            'version': latest_version,
            'dependencies': package_data.get('dependencies', {})
        }
    except Exception as e:
        print(f"Error: {e}")
        return None

def create_graphviz_code(package_info, author_name="Вячеслав"):
    if not package_info:
        return None
    
    graphviz_code = [
        "digraph express {",
        "    rankdir=TB;",
        "    size=\"8,8\";",
        "    info [label=<<TABLE BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">",
        "        <TR><TD BGCOLOR=\"lightblue\"><B>EXPRESS</B></TD></TR>",
        f"        <TR><TD>Version: {package_info['version']}</TD></TR>",
        f"        <TR><TD>Author: {author_name}</TD></TR>",
        f"        <TR><TD>Date: {datetime.now().strftime('%d.%m.%Y')}</TD></TR>",
        "    </TABLE>>, shape=none];",
        "    node [shape=box, style=filled, fillcolor=lightgreen];"
    ]
    
    for dep_name in package_info['dependencies'].keys():
        dep_clean = dep_name.replace('-', '_')
        graphviz_code.append(f'    {dep_clean} [label=\"{dep_name}\"];')
        graphviz_code.append(f'    info -> {dep_clean};')
    
    graphviz_code.append("}")
    
    return "\n".join(graphviz_code)

def main():
    author = "Вячеслав"
    
    print("Getting Express package info from npm registry...")
    package_info = get_express_info()
    
    if not package_info:
        print("Failed to get package info")
        return
    
    print(f"Package: {package_info['name']} v{package_info['version']}")
    print(f"Dependencies: {len(package_info['dependencies'])}")
    print(f"Program author: {author}")
    
    graphviz_code = create_graphviz_code(package_info, author)
    
    if graphviz_code:
        filename = "express_graph.dot"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(graphviz_code)
        print(f"Graphviz code saved to: {filename}")
        print("Run: dot -Tpng express_graph.dot -o express_graph.png")
    else:
        print("Failed to create Graphviz code")

if __name__ == "__main__":
    main()