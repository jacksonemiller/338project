from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import ast
from serpapi import GoogleSearch

def go(userQuery):
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



  def collect_messages(prompt_input):
      prompt = prompt_input
      
      response = determine_response(context, prompt)
      context.append({'role':'assistant', 'content':f"{response}"})
      
      return response



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
                "api_key": "25c5c0cd662e1c50684ac8c330e55a093b198ba102d5439b998966f5f3044b55"
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
        Provide a list of instructions that is about two sentances or more on how to build the product listed in the prompt. \
        Under each instruction:
        Go more in depth to the above instruction title with some tasks you should handle.\
        Also provide a the list of products with their corresponding urls that match\ 
        the URLs for each product mentioned in that step. \
        Keep on doing this until all the products and urls have been listed. \
        Example format(Disclaimer: asterik stars around a text means it should be bolded):
        "
        *1. Instruction 1*
        ------
        1. Product 1 used in instruction 1,
        - URL for product 1
        - URL 2 for product 1
        *2. Instruction 2*
      ...
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


  #input prompt and get the response
  return collect_messages(userQuery)

@csrf_exempt
def index(request):
    if request.method == 'PUT':
        data = request.body.decode('utf-8')
        return HttpResponse(go(data))
    return HttpResponse("Hello, world. You're at the polls index.")
