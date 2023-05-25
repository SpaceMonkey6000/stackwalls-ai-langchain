#importing necessary modules
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Title and Question
st.title("🤖 StackWalls AI")
prompt = st.text_area("What project would you like to get done today?", height=50)

#Prompt Template
title_template = PromptTemplate(
    input_variables = ['topic'],
    template='Based on the requirements given to you, come up with tools that can do the required tasks and also get the details of the number of pages/screens required in the project. The type of project may include: App/Website/UI-UX/Design. The platforms used may be: Figma/Shopify/Wordpress/Kajabi/Canva. You are to return a list of the format: <project type>,<Name of the Business/name of the user>, <Best platform availiable to complete the task>, <Details of the pages/screens required in the project>. Here are the requirements: {topic}'
)

# Init OpenAI
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

#If prompt given then running making the API call
if prompt:
    topic=prompt
    response = title_chain.run(topic)
    st.write(response)
