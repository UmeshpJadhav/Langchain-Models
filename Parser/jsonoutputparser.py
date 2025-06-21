from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import JsonOutputParser 
from typing import  Optional

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = JsonOutputParser()

template = PromptTemplate(
    template='what is the langchain and why used it \n {format_instruction}',
    input_variables=Optional[str],
    partial_variables= {'format_instruction': parser.get_format_instructions() }
)

chain = template | model | parser

result = chain.invoke({})

print(result)



