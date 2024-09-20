import google.generativeai as genai
import os
import promt as ut
import gradio as gr
import config as cfg
from inventory import read_csv


# Configure api_key
genai.configure(api_key=cfg.main())

#Define Model Instance
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Function to get a response from the AI model based on the provided prompt
def get_response(prompt):
    response = chat.send_message(prompt)
    return response.text

##Reading the inventory data
car_data=read_csv()
context =  ut.content()
context.append(car_data)
context.append("")
response = get_response(context)

# Function for creating the chat
def chatbot(message, history):
  prompt = message
  context.append(prompt)
  response = get_response(context)
  context.append(response)
  return response

## Code for displaying the content 
gr.ChatInterface(fn=chatbot, title='Used Car Marketplace').launch(debug=True, share=True)