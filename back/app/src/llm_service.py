import os
import google.generativeai as genai
from typing import TypedDict


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
        api_key = "AIzaSyDjSg7A-NO-p5BCy9yQj_Bb-X50Na6iL50"
        if not api_key:
            raise ValueError("API_KEY environment variable not set.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def generate_response(self, prompt, schema=None):
        schema = SentenceSchema()
        # Método para generar la respuesta usando Gemini
        print(prompt)
        if schema:
            return self.model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    temperature=0.2,
                    response_mime_type="application/json",
                    # response_schema=schema,
                ),
            )
        else:
            return self.model.generate_content(prompt)
