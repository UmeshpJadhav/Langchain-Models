from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

# prompt = PromptTemplate(
#     template='Answer the following question \n {question}  from the following text - \n {text}',
#     input_variables=['question','text']
# )


url = 'https://www.reddit.com/user/kojied/'
loader = WebBaseLoader(url)

# docs = loader.load()

# chain = prompt | model | parser

# result  = chain.invoke({'question':'what is the price of the asus rog strix g16 13th Gen?' , 'text':docs[0].page_content})

# print(result)

# print(docs[0].page_content)

docs = loader.load()


print(docs[0].page_content)






