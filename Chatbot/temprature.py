from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(
    model_name="gemini-2.0-flash",
    temperature=1.5,
)

result = model.invoke("Tell me a bout rohit sharma")
print(result.content)