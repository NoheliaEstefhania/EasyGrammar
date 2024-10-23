import json
import re


def extract_json(text):
    # Utilizar una expresión regular que busque contenido JSON entre ```json ... ```
    # o simplemente contenido JSON independiente.
    match = re.search(r"```json\n({.*?})\n```|({.*?})", text, re.DOTALL)
    if match:
        # Selecciona el grupo que tenga contenido
        json_content = match.group(1) or match.group(2)
        try:
            # Parsear el contenido JSON
            return json.loads(json_content)
        except json.JSONDecodeError:
            print("Error: No se pudo decodificar el JSON.")
            return None
    else:
        print("Error: No se encontró contenido JSON en el texto.")
        return None


# Ejemplo de uso
text_response = """
{
  "sujeto": "Paul",
  "predicado": "Does love music?"
}
"""

# text_response = """
# ```json
# {
#   "sujeto": "Paul",
#   "predicado": "Does love music"
# }
# ```
# """


print(extract_json(text_response))
