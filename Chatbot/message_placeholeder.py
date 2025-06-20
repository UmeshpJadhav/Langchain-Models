from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

 
chat_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful customer support agent.'),
     MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}'),
   
])


chat_history = []

with open('Chatbot/chat_history.txt', 'r') as file:
    chat_history.extend(file.readlines())

print(chat_history)


prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'where is my refund?'})
print(prompt)