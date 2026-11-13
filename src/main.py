from graph.message_graph import MessageGraph

def main():
    print("Starting Langraph Email Support Workflow!")
    # El nodo "load_emails" se encarga de traer el correo desde Gmail.
    initial_state = {
        "message": "Hoala, tengo un problema con mi factura de este mes. Me cobraron dos veces y necesito una solución.",
        "intent": "",
        "reason": "",
        "response":""
        
    }
    workflow = MessageGraph()
    graph = workflow.get_graph()      # esto llama a builder.compile()

    result = graph.invoke(initial_state)
    print(result["classification"])

if __name__ == "__main__":
    main()
    """ app = MessageGraph().get_graph()

    with open("grafo.png", "wb") as f:
        f.write(app.get_graph().draw_mermaid_png()) """
