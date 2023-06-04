import openai
import ast
import os
from serpapi import GoogleSearch

#from dotenv import load_dotenv, find_dotenv
#_ = load_dotenv(find_dotenv())

def go
openai.api_key  = "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"

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
Can you provide me with a list of products I will need to build a gazebo. \
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
      "api_key": "4a53e845f3349710680efe6c0bdd6a9dc23dcc2666c12c6ba84756041387173f"
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

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

def determine_response(context, prompt):


    respond_check = f"""
      You will be provided with a prompt delimited by triple quotes. \
      If the prompt asks how to build or create something then just return the number "0" \
      If it asks for anything else just return the number "1" \

      \"\"\"{prompt}\"\"\"
      """


    # response3 = get_completion(respond_check)

    # response = ""


    # if response3 == "0":

    #   prompt = prompt + "and give me a list of materials"
      

    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context)

    first = response.find("[")

    second = response.find("]")

    third = response.find("{")

    if first != -1 and second != -1 and third != -1:

      # # # Convert the string to a list of dictionaries
      list_of_dictionaries = ast.literal_eval(response[first:second + 1])

      # print(type(res))
      # print(res)
      # print(list_of_dictionaries)

      queried = []
      urls = []

      for product in list_of_dictionaries:
          # print(product)
          query_name = product['product_name']

          params = {
              "engine": "home_depot",
              "q": f"""{query_name}""",
              "api_key": "bce29c7f1145935059018a8e7b6f99357fe2977f84e5d34fc62ba4160b711357"
          }

          search = GoogleSearch(params)
          results = search.get_dict()
          products = results["products"]

          
          for i in range(2):
              queried.append(products[i]['title'])
              urls.append(products[i]['link'])

      respond_with_products_prompt = f"""
      You will be provided with three arrays delimited by triple quotes. \
      The first array contains Home Depot product names. \
      The second array contains the corresponding URLs for each product. \
      The third array contains the product the user wants to create in a prompt \

      \"\"\"{queried}\"\"\"
      \"\"\"{urls}\"\"\"
      \"\"\"{prompt}\"\"\"

      To begin with:
      Provide a list of instructions on how to build the product listed in the prompt. \
      After the list of instructions create a new seperate list:
      provide a the list of products with their corresponding urls that match\ 
       the URLs for each product mentioned in that step. \
      Keep on doing this until all the products and urls have been listed. \
      Example format:
      "
      1. Instruction 1
      ------
      1. Product 1 used in instruction 1,
      - URL for product 1
      - URL 2 for product 1
      "
      """

      response2 = get_completion(respond_with_products_prompt)
      return response2

    else:


      return response

context = [ {'role':'system', 'content':"""
You are a customer service chatbot for Home Depot. \
You first greet the customer, then answer the question they ask. \
Follow the instructions below only if the customer asks for a list of products or materials OR the customer asks about how to build or construct a product or project or some sort: \
For each product generate its name, a short description, and how it can be useful towards building the user project
Provide them only in JSON format with the following keys: 
product_name, description, usefulness.//
Make sure to place brackets "[]" if the products are generated.



"""} ]  # accumulate messages

def go(query):
    prompt = query
    response = determine_response(context, prompt)
    context.append({'role':'assistant', 'content':f"{response}"})
    return response

respond_with_products_prompt = f"""
You will be provided with two arrays delimited by triple quotes. \
The first array contains Home Depot product names. \
The second array contains the corresponding URLs for each product. \

Provide directions on how to build a gazebo using these products, \ 
After each step, provide the URLs for each product mentioned in that step. \
\"\"\"{queried} {urls}\"\"\"
"""
response2 = get_completion(respond_with_products_prompt)
print(response2)