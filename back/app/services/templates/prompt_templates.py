class PromptTemplates:
    @staticmethod
    def subject_predicate_prompt(sentence, language):
        if language == "en":
            return f"Please split the following sentence into subject and predicate: '{sentence}'"
        elif language == "es":
            return f"Por favor, separa la siguiente oración en sujeto y predicado: '{sentence}'"
        else:
            return f"Please split the following sentence into subject and predicate: '{sentence}'"
