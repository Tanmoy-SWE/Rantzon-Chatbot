from django.shortcuts import render
from django.http import JsonResponse
import openai


openai.api_key = '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'


# Function to get the chatbot's response using OpenAI API
def get_chatbot_response(user_message, conversation):
    # Append user message to the conversation
    conversation.append({"role": "user", "content": user_message})
    return "Resp"
    # # Get the chatbot's response from the API
    # response = openai.ChatCompletion.create(
    #     engine="text-davinci-002", 
    #     messages=conversation
    # )

    # # Extract and return the chatbot's response
    # chatbot_response = response['choices'][0]['message']['content']
    # conversation[-1]['content'] = chatbot_response  # Update conversation with the chatbot response
    # return chatbot_response
# Function to read the text content from a file
def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# View to handle user input and chatbot response
def chatbot_view(request):
    if request.method == 'POST':
        # user_input = request.POST.get('user_input', '').strip()

        # if user_input.lower() in ['exit', 'quit', 'bye']:
        #     return JsonResponse({'response': "Chatbot: Goodbye!"})
        

        # # Step 1: Read the text content from the file
        # filename = "media/rantzon.txt"  # Replace with the actual filename
        # preprocessed_text = read_text_from_file(filename)

        # # Initial conversation message with the system's introduction and the context from the file
        # conversation = [
        #     {"role": "system", "content": f"You are a helpful assistant for Health related suggestion who predicts diseases. You can ask more information if needed."},
        #     {"role": "user", "content": preprocessed_text},
        # ]

        # # Get the chatbot's response using the OpenAI API
        # chatbot_output = get_chatbot_response(user_input, conversation)

        return JsonResponse({'response': "Chatbot: " + "chatbot_output"})

    return render(request, 'chatbot.html')

def intro(request):
    return render(request, 'into.html')