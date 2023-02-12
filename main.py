# import openai library
import streamlit as st
import openai
import base64
#
# # Set up the OpenAI API client
# openai.api_key = "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"
# with st.sidebar:
#     st.header("Chat Bot")
#     st.caption("Made by Sandeep Kashyap")
# st.header("Demonstrating text-davinci-003")
# # st.caption("Made by Sandeep Kashyap")
# About = st.button('About the model')
# if About:
#     st.markdown("Text-davinci-003 is the model used to built this system. It is the most capable GPT-3 model of "
#                 "OpenAI. It can do any task the other models can do, often with higher quality, longer output and "
#                 "better instruction-following. It also supports inserting completions within text. The dataset in "
#                 "which the model got trained was up to Jun 2021.")
#
# # while True:
# query = st.text_input("Ask anything")
#
# # def main():
# #     # this loop will let us ask questions continuously and behave like ChatGPT
# #     # while True:
# #     query = st.text_input("Ask anything but remember it is not as smart as ChatGPT")
#     # while True:
#     # input = st.text_input("Enter your query")
#     # st.file_uploader()
#     # Set up the model and prompt
#     # model_engine = "text-davinci-003"
#     # if 'exit' in query or 'quit' in query:
#     #     break
#     # Generate a response
#     # completion = openai.Completion.create(
#     #     engine=model_engine,
#     #     prompt=query,
#     #     max_tokens=1024,
#     #     n=1,
#     #     stop=None,
#     #     temperature=0.5,
#     # )
#     #
#     # response = completion.choices[0].text
#     #
#     # # printing response
#     # st.markdown(response)
#
#
# # if __name__ == '__main__':
#     # main()

#
# @st.cache_data
# def get_img_as_base64(file):
#     with open(file, "rb") as f:
#         data = f.read()
#     return base64.b16encode(data).decode()
#
#
# img = get_img_as_base64("background_1.jpg")
# page_bg_img = """
# <style>
# [data-testid="stAppViewContainer"] > div:first-child {{
# background-image: url("data:image/jpg;base64, {img}");
# }}
# </style>
#
# """
#
# st.markdown(page_bg_img, unsafe_allow_html=True)
# st.title("lets check it out")

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('background_1.jpg')