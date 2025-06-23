from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate 5 facts about {topic} in a list format.",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a summary of the following facts: {facts}",
    input_variables=["facts"]
)

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

chain1 = prompt1 | model | parser | prompt2 | model | parser
result = chain1.invoke({"topic": "Python programming language"})
print(result)