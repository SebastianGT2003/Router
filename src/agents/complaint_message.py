from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from utils.state import MessageState
from promps import PROMPTS

load_dotenv()  # Carga las variables de entorno desde el archivo .env
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def ComplaintAgent():
    """
    Responde a un mensaje de soporte clasificado en complaint.

    """
    #Traer el prompt de clasificación

    message_complain_prompt= PromptTemplate(
        template=PROMPTS["MESSAGE_COMPLAINT"],
        input_variables=["message", "case_id"]
    )
    return message_complain_prompt | llm.with_structured_output(MessageState)


