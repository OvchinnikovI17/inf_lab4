import json 
import yaml
import xml
import xmlplain
from time import time


x1 = time()
# Read the YAML file
with open("lirica.yml") as inf:
    root = xmlplain.obj_from_yaml(inf)
        
# Output back XML
with open("result.xml", "w") as outf:
    xmlplain.xml_from_obj(root, outf, pretty=True)
    
print(f'Время выполнения:\t{time() - x1}')