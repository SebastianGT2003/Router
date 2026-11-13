from .agent import CLASSIFIER_PROMPT
from .task import CLASSIFIER_TASK

MESSAGE_CATEGORIZER = f"{CLASSIFIER_PROMPT}\n{CLASSIFIER_TASK}"

def main() -> None:
    print("Hello from router-soporte!")