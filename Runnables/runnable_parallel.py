from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

prompt1 = PromptTemplate(
    template='Generate the tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Genenrate the linkedin post about the {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
  'tweet': RunnableSequence(prompt1, model, parser),
  'linkedin': RunnableSequence(prompt2, model, parser)
})

result  = parallel_chain.invoke({'topic':'Ai'})

print(result['tweet'])
print(result['linkedin'])