import json
import re


def extract_json(text):
    # Utilizar una expresión regular para encontrar el contenido JSON entre las etiquetas ```
    match = re.search(r"```json\n({.*?})\n```", text, re.DOTALL)
    if match:
        json_content = match.group(1)
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
```json
{
  "sujeto": "Paul",
  "predicado": "Does love music?"
}
```
"""

print(extract_json(text_response))
