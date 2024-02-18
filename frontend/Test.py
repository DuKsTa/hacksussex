import streamlit as st
import os
from backend.vector_database import Vector_Database
vc = Vector_Database()

type_of_insurance = ""

button_colors = {
    'car' : 'white',
    'house': 'white',
    'bike': 'white',
    'van': 'white'
}
# App title
st.set_page_config(page_title="Help centre")

# Replicate Credentials
with st.sidebar:
    st.title('Hastings Direct support')
    st.subheader("Select the type of insurances:")

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

def trigger(type):
    if type == 'car':
        vc.change_vc(type)
    elif type == 'house':
        vc.change_vc(type)
    elif type == 'bike':
        vc.change_vc(type)
    elif type == 'van':
        vc.change_vc(type)
    for i in button_colors.keys():
        if i == type:
            continue
        button_colors[i] = 'white'
    st.write(f'You are now querying for the {type} insurance')
    type_of_insurance = type

st.sidebar.button(f":{button_colors['car']}[Car Insurance]", on_click=trigger, args=('car',))
st.sidebar.button(f":{button_colors['house']}[House Insurance]", on_click=trigger, args=('house',))
st.sidebar.button(f":{button_colors['bike']}[Bike Insurance]", on_click=trigger, args=('bike',))
st.sidebar.button(f":{button_colors['van']}[Van Insurance]", on_click=trigger, args=('van',))
st.sidebar.button(':red[Clear Chat History]', on_click=clear_chat_history, type='primary')

# Function for generating LLaMA2 response
# Refactored from https://github.com/a16z-infra/llama2-chatbot
def generate_llama2_response(prompt_input):
    string_dialogue = f'''You are a helpful assistant from Hasting Direct Company. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'.
                            You are helping for querying from the insurance company https://www.hastingsdirect.com/
                            Only answer questions relevant to the
                            insurances. If Other questions are asked, say you can only help with insurance related questions
                            The user is asking about {type_of_insurance} insurance'''
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"]  + "\n\n"
    output = vc.search(string_dialogue)
    if output.lower() == "I don't know the answer.":
        # Use a different agent
        _ = 0
    return output

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            full_response = generate_llama2_response(prompt)
            placeholder = st.empty()
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)