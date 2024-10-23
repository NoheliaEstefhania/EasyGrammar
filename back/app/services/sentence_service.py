class SentenceService:
    def split_sentence(self, sentence):
        # Ejemplo simple de separación
        parts = sentence.split(",")
        if len(parts) >= 2:
            return {
                "subject": parts[0].strip(),
                "predicate": ",".join(parts[1:]).strip(),
            }
        else:
            return {"error": "No se pudo dividir en sujeto y predicado."}
