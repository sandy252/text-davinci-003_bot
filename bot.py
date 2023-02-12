import streamlit as st
import openai
import base64

# Custom image for streamlit background
# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
#         background-size: cover
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
#     )
#
#
# add_bg_from_local('background_1.jpg')


API_KEY = "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"
openai.api_key = API_KEY

with st.sidebar:
    st.header("Chat Bot")
    st.caption("made by Sandeep Kashyap")
    if st.button("About model"):
        st.markdown("Text-davinci-003 is the model used to built this system. It is the most capable GPT-3 model of "
                "OpenAI. It can do any task the other models can do, often with higher quality, longer output and "
                "better instruction-following. It also supports inserting completions within text. The dataset in "
                "which the model got trained was up to Jun 2021.")
    st.markdown('''
            - [OpenAI](https://openai.com/)
            - [Streamlit](https://docs.streamlit.io/)
            ''')


st.header("text-davinci-003 in Action")
st.caption("Check the sidebar for model information")
query = st.text_input("Ask anything but remember it is not as smart as ChatGPT")


model_engine = "text-davinci-003"
completion = openai.Completion.create(
    engine=model_engine,
    prompt=query,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
response = completion.choices[0].text
st.markdown(response)


