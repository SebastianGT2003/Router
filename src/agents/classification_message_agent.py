from utils.state import MessageState
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.types import Command, interrupt
from langgraph.graph import END, START, StateGraph
from promps import PROMPTS
from langchain_core.prompts import PromptTemplate
from utils.state import MessageClassification

load_dotenv()  # Carga las variables de entorno desde el archivo .env
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
def ClassificationMessageAgent():
    """
    Classifies the intent of a message and provides a reason for the classification.

    Args:
        state (MessageState): The current state containing the message to classify.
    """
    #Traer el prompt de clasificación

    message_categorizer_prompt= PromptTemplate(
        template=PROMPTS["MESSAGE_CATEGORIZER"],
        input_variables=["message"]
    )
    return message_categorizer_prompt | llm.with_structured_output(MessageClassification)


