# MainDot = {
#     "name": "Корень",
#     "value": "45",
#     "children": [
#         {
#             "name": "Ветка А",
#             "value": "34",
#             "children": [
#                 {
#                     "name": "Лист 1",
#                     "value": "34",
#                     "children": []
#                 },
#                 {
#                     "name": "Лист 2", 
#                     "value": "34",
#                     "children": []
#                 }
#             ]
#         },
#         {
#             "name": "Ветка Б",
#             "value": "64",
#             "children": [
#                 {
#                     "name": "Лист 3", 
#                     "value": "77",
#                     "children": []
#                 }
#             ]
#         }
#     ]
# }

import json
from pathlib import Path

DEBUG_FILE = Path("ef.json")

def clear_element(element):
    return {
        'Childs': element.get('Childs'),
        'GeneratedPower': element.get('GeneratedPower'),
        'ID': element.get('ID'),
        'IsON': element.get('IsON'),
        'ObjectType': element.get('ObjectType'),
        'Power': element.get('Power'),
        'RequiredPower': element.get('RequiredPower'),
    }

def read_from_file():
    if not DEBUG_FILE.exists():
        raise FileNotFoundError(f"Файл для отладки не найден: {DEBUG_FILE}")
    with open(DEBUG_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        return json.loads(content)

# def node(uzel, children, array):
#     print(uzel['ID'])
#     if (not children):
#         array.append(clear_element(uzel))
#         return
#     for localUzel in children:
#         node(localUzel, localUzel.get('Childs'), array)

def rd(json, key):
    print()
    print(f"{key}: {str(json[key])}")
    print()
    return json[key]

def nrd(json, key):
    return json[key]

def srd(array):
    new_array = []

    for i in range(len(array)):
        if array[i] is None:
            continue
        new_array.append(clear_element(array[i]))

    # print(new_array)
    return new_array

def node(uzel, children, array):
    has_children = False
    
    if children:
        if isinstance(children, list) and len(children) > 0:
            has_children = True
        elif isinstance(children, dict): 
            has_children = True
            
    if not has_children:
        array.append(clear_element(uzel))
        return

    for local_uzel in children:
        if local_uzel is None:
            continue
        next_children = local_uzel.get('Childs')
        node(local_uzel, next_children, array)

def array_for_lines(lines_data):
    new_lines = []
    
    if isinstance(lines_data, list):
        for item in lines_data:
            if item is None:
                continue
            children = item.get('Childs')
            node(item, children, new_lines)
            
    elif isinstance(lines_data, dict):
        children = lines_data.get('Childs')
        node(lines_data, children, new_lines)

    print(new_lines)
    return new_lines

# Читает файл

m = read_from_file()

# Параметры

ElementsOK = rd(m, 'ElementsOK')
Lamp1val = rd(m, 'Lamp1val')
Lamp2val = rd(m, 'Lamp2val')
Windval = rd(m, 'Windval')
TreeOK = rd(m, 'TreeOK')

RootNode = {
    "GeneratedPower": rd(nrd(m, 'RootNode'), 'GeneratedPower'),
    "RequiredPower": rd(nrd(m, 'RootNode'), 'RequiredPower'),
    "Stations": rd(nrd(m, 'RootNode'), 'Stations'),
    "Lines": nrd(nrd(m, 'RootNode'), 'Lines'),
}

Stations = srd(RootNode['Stations'])

Lines = array_for_lines(RootNode['Lines'])
