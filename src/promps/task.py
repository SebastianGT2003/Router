CLASSIFIER_TASK = """
# TAREA
Analiza el siguiente mensaje de un cliente y clasifícalo en una de las cuatro
intenciones: billing, technical, complaint u other.

# MENSAJE DEL CLIENTE
\"\"\"
{message}
\"\"\"

# PASOS
1. Lee el mensaje completo e identifica qué necesita resolver el cliente.
2. Ignora el tono emocional al decidir; úsalo solo si no hay un problema
   concreto de cobro o técnico (en ese caso puede ser complaint).
3. Si el mensaje menciona varios temas, elige el que el cliente necesita
   resolver primero.
4. Aplica las reglas para casos ambiguos que ya conoces.
5. Escribe una razón breve que justifique tu decisión.

# RESULTADO ESPERADO
- intent: exactamente uno de estos valores -> billing | technical | complaint | other
- reason: una sola frase, en español, de máximo 20 palabras, que mencione
  la parte del mensaje que determinó la clasificación.

No respondas al cliente, no agregues saludos ni texto adicional.
"""