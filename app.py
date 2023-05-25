import os
from key import apikey
os.environ["OPENAI_API_KEY"] = apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain


st.title("🤖 StackWalls AI")
prompt = st.text_area("How may we help you today?", height=40)#, max_chars=100)

title_template = PromptTemplate(
    input_variables = ['req'],
    template='Based on the requirements given to you, come up with tools that can do the required tasks and also get the details of the number of pages/screens required in the project. The type of project may include: App/Website/UI-UX/Design. The platforms used may be: Figma/Shopify/Wordpress/Kajabi/Canva. You are to return a list of the format: <project type>,<Name of the Business/name of the user>, <Best platform availiable to complete the task>, <Details of the pages/screens required in the project>. Here are the requirements: {req}'
)

llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

if prompt:
    response = title_chain.run(req=prompt)
    st.write(response)