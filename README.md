
# NLPforEdu (Med)
This project purpose is to use Deep Learning and LLM models to help the education domain easier by reducing the manual work a learner has to do and help them focus only on things they need to do.

In this project, We use GPT-3 to extract diseases, symptoms, drugs, drug reaction and disease tests as entities and along with the relations between them.

# Installation
clone the directory with command:
##### git clone https://github.com/NLPforEDU/MEDNEERRE-v1.git

# Working
There are two directories 'GPT_Model' and 'Normal_Model'.
##### In Normal_Model we used model like sci-bert and biobert for entity training, we gave the data for disease and drug.
But since the data is very less for other entities, we couldn't go forward

# GPT_Model
In GPT_Model, we included the prompt for the purpose, in the api-key.txt please provide your open-ai key for usage
#### Steps to run the model
* set GPT_Model folder as main directory.
* Add the text you want to test in the test_input.txt.
* Run the file run_on_file.py
* You will get the output in test_output.txt
* To visulaize the output in graph, run plot_graph.py

# Plot output
![plot](https://github.com/NLPforEDU/MEDNEERRE-v1/blob/main/GPT_Model/images/graph_dependencies.jpg)


##### We will be also adding the link of gpt-2 models trained on medical textbook data here.
##### https://drive.google.com/drive/folders/1v8bMm5vChqTHgFO11THOeHTCjPbyRSBi?usp=sharing
