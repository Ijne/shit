import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import BytesIO
import graphviz


def render_with_kroki(dot_code, format='png'):
    """Визуализация через Kroki API"""
    url = f"https://kroki.io/graphviz/{format}"
    response = requests.post(url, data=dot_code)
    
    if response.status_code == 200:
        # Отображаем через matplotlib
        img = mpimg.imread(BytesIO(response.content))
        plt.figure(figsize=(10, 8))
        plt.imshow(img)
        plt.axis('off')
        plt.show()
        return True
    else:
        print("Ошибка:", response.status_code)
        return False
    
def getCode():
    dot = graphviz.Digraph('round-table', comment='The Round Table') 
    dot.node("Name", "matplotlib")
    dot.node("Version", "3.10.7")
    dot.node("Summary", "Python plotting package")
    dot.node("Home-page", "First Node")
    dot.node("Author", "John D. Hunter, Michael Droettboom")
    dot.node("Author-email", "Unknown <matplotlib-users@python.org>")
    dot.node("License", "License agreement for matplotlib versions 1.3.0 and later")
    dot.node("Packeges", "Packeges")

    dot.node("Package 1", "contourpy")
    dot.node("Package 2", "cycler")
    dot.node("Package 3", "fonttools")
    dot.node("Package 4", "kiwisolver")
    dot.node("Package 5", "numpy")
    dot.node("Package 6", "packaging")
    dot.node("Package 7", "pillow")
    dot.node("Package 8", "pyparsing")
    dot.node("Package 9", "python-dateutil")

    dot.edge("Name", "Version")
    dot.edge("Name", "Summary")
    dot.edge("Name", "Home-page")
    dot.edge("Name", "Author")
    dot.edge("Author", "Author-email")
    dot.edge("Name", "License")
    dot.edge("Name", "Packeges")

    dot.edge("Packeges", "Package 1")
    dot.edge("Packeges", "Package 2")
    dot.edge("Packeges", "Package 3")
    dot.edge("Packeges", "Package 4")
    dot.edge("Packeges", "Package 5")
    dot.edge("Packeges", "Package 6")
    dot.edge("Packeges", "Package 7")
    dot.edge("Packeges", "Package 8")
    dot.edge("Packeges", "Package 9")
 
    try:
        dot.render(directory='doctest-output')
    except Exception:
        pass
    render_with_kroki(dot.source)

getCode()
