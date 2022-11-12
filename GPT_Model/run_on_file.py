from core_code.entity_re import get_response
from nltk.tokenize import sent_tokenize
from parse_output import parse_output

accepted_relations = ['symptom','drug','test','side effect','possible cause']


def get_Entity_and_relation(data):
    sentences = sent_tokenize(data)
    all_relations = []

    sent_threshold = 50
    if len(sentences)>sent_threshold:
        for i in range(0,len(sentences),sent_threshold):
            sub_text = ' '.join(sentences[i-2:i+40]) # adding previous sentences also so that there might be some reference to it --- chnage this number based on the need
            gpt_response = get_response(sub_text)
            gpt_response = parse_output(gpt_response)
            all_relations += (gpt_response)
    
    else:
        gpt_response = get_response(data)
        all_relations = parse_output(gpt_response)


    all_relations = list(set(all_relations))
    return(all_relations)


if __name__ == '__main__':
    with open('test_input.txt','r') as f:
        data = f.read()

    result_ = get_Entity_and_relation(data)

    with open('test_output.txt','w') as f:
        for sent in result_[:-1]:
            f.write(str(sent)+'\n')
        f.write(str(result_[-1]))