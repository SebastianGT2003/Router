from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from utils.state import BillingInfo
from promps import PROMPTS

load_dotenv()  # Carga las variables de entorno desde el archivo .env
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def BillsAgent():
    """
    Responde a un mensaje de soporte clasificado en bills.

    """
    #Traer el prompt de clasificación

    message_billing_prompt= PromptTemplate(
        template=PROMPTS["MESSAGE_BILLING"],
        input_variables=["message"]
    )
    return message_billing_prompt | llm.with_structured_output(BillingInfo)


