from ..src.llm_service import LLMService
from .templates.prompt_templates import PromptTemplates


class SubjectPredicateService:
    def __init__(self):
        self.llm_service = LLMService()

    def split_subject_predicate(self, sentence, language):
        # Obtener el prompt adecuado según el idioma
        prompt = PromptTemplates.subject_predicate_prompt(sentence, language)

        # Generar la respuesta utilizando el modelo LLM
        try:
            response = self.llm_service.generate_response(prompt)
            return {
                "sentence": sentence,
                "language": language,
                "response": response.text,
            }
        except Exception as e:
            return {"sentence": sentence, "language": language, "error": str(e)}
