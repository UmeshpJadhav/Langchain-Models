from langchain_core.prompts import ChatPromptTemplate


chat_prompt_template = ChatPromptTemplate.from_messages([
    ('systrem', 'You are a helpful {domain} expert assistant.'),
    ('human', '{user_input}'),
    
])

prompt = chat_prompt_template.invoke(
    domain='AI',
    user_input='What is the capital of France?'
)

print(prompt)
