import os
import google.generativeai as genai
from typing import Dict, Any
from google.ai.generativelanguage_v1beta.types import content


class LLMService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LLMService, cls).__new__(cls)
            cls._instance.configure()
        return cls._instance

    def configure(self):
        # Configurar la API con la clave desde las variables de entorno
        # api_key = os.getenv("API_KEY")
        api_key = "AIzaSyD4BSGwiJWaYRWOGezpJcwSQqSBVcmxaGI"
        if not api_key:
            raise ValueError("API_KEY environment variable not set.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def generate_response(self, prompt: str, schema: Dict[str, Any] = None):
        # Método para generar la respuesta usando Gemini
        print(prompt)
        if schema:
            # Construir la configuración del esquema dinámicamente
            response_schema = content.Schema(
                type=content.Type.OBJECT,
                properties=schema.get("properties", {}),
                required=schema.get("required", []),
                enum=schema.get("enum", []),
            )

            return self.model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    temperature=0.2,
                    response_mime_type="application/json",
                    response_schema=response_schema,
                ),
            )
        else:
            return self.model.generate_content(prompt)
