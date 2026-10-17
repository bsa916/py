MainDot = {
    "name": "Корень",
    "value": "45",
    "children": [
        {
            "name": "Ветка А",
            "value": "34",
            "children": [
                {
                    "name": "Лист 1",
                    "value": "34",
                    "children": []
                },
                {
                    "name": "Лист 2", 
                    "value": "34",
                    "children": []
                }
            ]
        },
        {
            "name": "Ветка Б",
            "value": "64",
            "children": [
                {
                    "name": "Лист 3", 
                    "value": "77",
                    "children": []
                }
            ]
        }
    ]
}

def node(usel, children):
    print(f"{usel['name']}: {usel['value']}")
    if (not children):
        return
    for localUsel in children:
        node(localUsel, localUsel["children"])

node(MainDot, MainDot["children"])