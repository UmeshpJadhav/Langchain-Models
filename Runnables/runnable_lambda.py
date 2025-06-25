from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

def word_counter(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template = 'write a joke about {topic}',
    input_variables=['topic']
)



joke_gen_chain = RunnableSequence(prompt1, model, parser)

runnable_word_counter = RunnableParallel({
'joke': RunnablePassthrough(),
'counter': RunnableLambda(word_counter)
})

final_chain= RunnableSequence(joke_gen_chain, runnable_word_counter)

result = final_chain.invoke({'topic':'AI'})

final_result = """ {} \n word count - {} """.format(result['joke'], result['word_counter'])

print(final_result)