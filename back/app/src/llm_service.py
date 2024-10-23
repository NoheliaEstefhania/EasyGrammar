import os
import google.generativeai as genai
from typing import TypedDict
from google.ai.generativelanguage_v1beta.types import content


class SentenceSchema(TypedDict):
    subject: str
    predicate: str


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

    def generate_response(self, prompt, schema=None):
        # schema = SentenceSchema()
        # Método para generar la respuesta usando Gemini
        print(prompt)
        if schema:
            return self.model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    temperature=0.2,
                    response_mime_type="application/json",
                    response_schema=content.Schema(
                        type=content.Type.OBJECT,
                        enum="[]",
                        required="['subject', 'predicate']",
                        properties={
                            "subject": content.Schema(
                                type=content.Type.STRING,
                            ),
                            "predicate": content.Schema(
                                type=content.Type.STRING,
                            ),
                        },
                    ),
                ),
            )
        else:
            return self.model.generate_content(prompt)
