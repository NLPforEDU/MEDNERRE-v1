from dash import Dash, html
import dash_cytoscape as cyto
from ast import literal_eval

app = Dash(__name__)

def generate_dict(name,position):
    return {'data': {'id': name, 'label': name},
             'position': {'x': position[0], 'y': position[1]}}

def parse_output(data):
    lines = data.split('\n')
    list_nerre = [literal_eval(line) for line in lines]
    return list_nerre

def generate_elements():
    with open('test_output.txt','r') as f:
        data = f.read()
    list_ent_rels = parse_output(data)
    
    #Possible_cause-Symptom-Disease-Drug-Side_effect

    elements_list = []
    dis = symp = drug = side_eff = cause = 1
    done = []

    for (ent1,ent2,relation) in list_ent_rels:
        if relation == 'symptom':
            if ent1 not in done:
                elements_list.append(generate_dict(ent1,(150*3,dis*50)))
                dis += 1
                done.append(ent1)
            if ent2 not in done:
                elements_list.append(generate_dict(ent2,(100*3,symp*50)))
                symp += 1
                done.append(ent2)
        
        if relation == 'drug':
            if ent1 not in done:
                elements_list.append(generate_dict(ent1,(200*3,dis*50)))
                dis += 1
                done.append(ent1)
            if ent2 not in done:
                elements_list.append(generate_dict(ent2,(150*3,drug*50)))
                drug += 1
                done.append(ent2)
        
        if relation == 'side effect':
            if ent1 not in done:
                elements_list.append(generate_dict(ent1,(200*3,drug*50)))
                drug += 1
                done.append(ent1)
            if ent2 not in done:
                elements_list.append(generate_dict(ent2,(250*3,side_eff*50)))
                side_eff += 1
                done.append(ent2)
        
        if relation == 'possible cause':
            if ent1 not in done:
                elements_list.append(generate_dict(ent1,(150*3,dis*50)))
                dis += 1
                done.append(ent1)
            if ent2 not in done:
                elements_list.append(generate_dict(ent2,(50*3,cause*50)))
                cause += 1
                done.append(ent2)

    
    #edge elements
    for (ent1,ent2,relation) in list_ent_rels:
        elements_list.append({'data': {'source': ent1, 'target': ent2, 'label': relation}})

    # print(elements_list)
    return elements_list



app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape',
        layout={'name': 'preset'},
        style={'width': '100%', 'height': '1000px'},
        stylesheet = [{
            'selector': 'edge',
            'style': {
                'label': 'data(label)',
                # The default curve style does not work with certain arrows
                    },
            },
            {
                'selector': 'node',
                'style': {
                'label': 'data(label)',
                }

            }
            ],
        elements=generate_elements()
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)