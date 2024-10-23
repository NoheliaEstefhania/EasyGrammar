from ..src.llm_service import LLMService
from .templates.subject_predicate_template import subject_predicate_prompt
import json


class SubjectPredicateService:
    def __init__(self):
        self.llm_service = LLMService()

    def split_subject_predicate(self, sentence, language):
        # primero obtiene los datos del la consulta
        print("----------service-------------")
        print("sentence: ", sentence)
        print("language: ", language)
        print("------------------------------")

        # Obtener el prompt adecuado según el idioma
        prompt = subject_predicate_prompt(sentence, language)
        print("----------prompt-------------")
        print(prompt)
        # print("language: ", language)
        print("------------------------------")

        # Generar la respuesta utilizando el modelo LLM
        try:
            response = self.llm_service.generate_response(prompt)
            print("------------RESPONSE------------------")

            print(response.text)
            print("------------------------------")

            # Extraer el contenido JSON del primer candidato

            # json_text = response.result.candidates[0].content.parts[0].text

            # Intenta analizar el contenido como JSON
            response_data = json.loads(response.text)
            return {
                "sentence": sentence,
                "language": language,
                "response": response_data,
            }
        except Exception as e:
            print(e)
            return {"sentence": sentence, "language": language, "error": str(e)}
