from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import (
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()

memory = ConversationBufferMemory(
    # chat_memory=FileChatMessageHistory("messages.json"),
    memory_key="messages",
    return_messages=True,
)

prompt = ChatPromptTemplate(
    input_variables=[
        "content",
        #  "messages"
    ],
    messages=[
        # MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}"),
    ],
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    # memory=memory,
)

while True:
    print("")
    content = input("You: ")
    result = chain({"content": content})
    print("BOT:", result["text"])
    print("")