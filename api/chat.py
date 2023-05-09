import openai
import os
from serpapi import GoogleSearch
import ast


from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]


# messages =  [  
# {'role':'system', 'content':'You are a customer service chatbot./'},    
# {'role':'user', 'content':'Hi, my name is Isa'}  ]
# response = get_completion_from_messages(messages, temperature=0)

# print(response)



text_1 = f"""
Can you provide me with a list of products I will need to build a Gazebo. \
"""


prompt = f"""
You will be provided with text delimited by triple quotes. 
If it asks for materials or products needed for a project, \ 
give materials that the user will eventually need to accomplish their project \
give any neccesary materials that also fit within any constraints defined by the user \
be as specific as possible in listing a material\
do not generalize a material\
make it specific enough for a person to know what to buy \
If the text does not ask for any materials or products, \ 
then simply write \"No project provided.\
For each product generate its name, a short description, and how it can be useful towards user project
Provide them only in JSON format with the following keys: 
product_name, description, usefulness."

\"\"\"{text_1}\"\"\"
"""
response = get_completion(prompt)
print("Completion for Text 1:")

res = response.split('\n\n')[1]

string_of_dictionaries = f"[{res}]"

# Convert the string to a list of dictionaries
list_of_dictionaries = ast.literal_eval(string_of_dictionaries)


queried = []
urls = []

for product in list_of_dictionaries:
    print(product)
    query_name = product['product_name']

    params = {
      "engine": "home_depot",
      "q": f"""{query_name}""",
      "api_key": "06fb4f4032ed1164e073f96d5dc2964c04a03e07f2f6ede876b6a2fe35af526f"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    products = results["products"]

    
    for i in range(2):
        queried.append(products[i]['title'])
        urls.append(products[i]['link'])

print("Results after searching company api:")

for i in range(len(queried)):
    print("Product:")
    print(queried[i])
    print("url:")
    print(urls[i])