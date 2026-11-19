from langgraph.graph import END, START, StateGraph
from Nodes import NODES
from utils.state import MessageState

class MessageGraph():
    def __init__(self):
        self.builder = StateGraph(MessageState)
        self._build_graph()


    def _build_graph(self):
        # Agregar nodos al grafo
        for node_name, node_function in NODES.items():
            self.builder.add_node(node_name, node_function)

        # Agregar aristas al grafo
        self.builder.add_edge(START, "classification_message")
        self.builder.add_edge("bills_message", END)
        self.builder.add_edge("technical_message", END)
        self.builder.add_edge("complaint_message", END)
        self.builder.add_edge("other_message", END)

    def get_graph(self):
        return self.builder.compile()

graph = MessageGraph().get_graph()
