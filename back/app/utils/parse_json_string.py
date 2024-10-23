import re
import json


def parse_json_string(json_string: str) -> dict:
    # Usar una expresión regular para extraer el contenido entre las llaves {}
    match = re.search(r"\{(.*?)\}", json_string)
    if match:
        content = match.group(1)  # Captura el contenido entre las llaves
        # Divide el contenido en líneas para procesarlo
        items = content.split(",")
        json_dict = {}

        for item in items:
            # Limpiar y dividir en clave y valor
            key_value = item.split(":")
            key = key_value[0].strip().strip('"')  # Limpiar y quitar comillas
            value = key_value[1].strip().strip('"')  # Limpiar y quitar comillas
            json_dict[key] = value

        return json_dict
    else:
        raise ValueError("No se encontró un objeto JSON válido.")


# Ejemplo de uso
json_input = """
```json
{
"subject": "he",
"predicate": "Does kiss his girlfriend?"
}
```
"""
result = parse_json_string(json_input)

# Convertir el diccionario a JSON
result_json = json.dumps(result, indent=4)
print(result_json)
