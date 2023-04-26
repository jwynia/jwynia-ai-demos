# To run: streamlit run SimpleResearchWebBot.py
from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
import streamlit as st

# This is extra work to deal with my dev environment. To simplify, you can delete these 3 lines and just set the keys directly.
load_dotenv('.env')
openApiKey = os.getenv('OPEN_API_KEY')
serpApiKey = os.getenv('SERPAPI_API_KEY')
# You could just use these 2 lines and set the keys directly
os.environ["OPENAI_API_KEY"] = openApiKey;
os.environ["SERPAPI_API_KEY"] = serpApiKey

llm = OpenAI(temperature=0.9,max_tokens=-1)
tools = load_tools(["serpapi"],llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description",verbose=True)

st.header("Research Bot")
query = st.text_input("Your Query: ")

if st.button("Search"):
    st.markdown(agent.run(query))

st.write("Source: https://github.com/jwynia/jwynia-ai-demos")