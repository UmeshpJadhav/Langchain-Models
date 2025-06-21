from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser , ResponseSchema

load_dotenv()



model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

schema = [
    ResponseSchema(name="key_themes", description="Write down all the key themes discussed in the review in a list", type="list[str]"),
    ResponseSchema(name="summary", description="A brief summary of the review", type="str"),
    ResponseSchema(name="sentiment", description="Return sentiment of the review either negative, positive or neutral", type="str", enum=["pos", "neg", "neutral"]),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="I recently used the {product_name} and I must say, it’s an absolute powerhouse! The performance is lightning fast—whether I’m gaming, multitasking, or editing photos. The battery easily lasts a full day even with heavy use, and the fast charging is a lifesaver.\n\nThe integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.\n\nHowever, the weight and size make it a bit uncomfortable for one-handed use. Also, the software still comes with bloatware—why do I need five different apps for things Google already provides? The price tag is also a hard pill to swallow.\n\nPros:\n{pros}\n\nReview by {reviewer_name} \n {format_instructions}",
    input_variables=['product_name, pros, reviewer_name'],

)

chain = template | model | parser

result = chain.invoke({
    'product_name': 'Samsung Galaxy S24 Ultra',
    'pros': 'Insanely powerful processor (great for gaming and productivity), Stunning 200MP camera with incredible zoom capabilities, Long battery life with fast charging, S-Pen support is unique and useful',
    'reviewer_name': 'Umesh Jadhav'
})

print(result)