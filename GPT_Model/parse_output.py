#To parse the gpt output to list of tuples with strings
import re

accepted_relations = ['symptom','drug','test','side effect','possible cause']

def parse_line(text):
    text = text[1:-1] #removes '(' and ')'
    text = text.strip()
    words = text.split(',')
    try:
        if words[2] not in accepted_relations:
            return []
        else:
            return [word.strip() for word in words]
    except Exception as e:
        print(words,e)
        return []

def parse_output(gpt_response):
    lines = gpt_response.split('\n')
    output_list = []
    for line in lines:
        parse_line_output = parse_line(line)
        if len(parse_line_output) != 0:
            output_list.append(tuple(parse_line_output))
    
    return output_list
    