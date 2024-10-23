class AnotherService:
    def categorize_words(self, sentence):
        # Lógica de ejemplo para categorizar palabras
        words = sentence.split()
        categorized = {
            "nouns": [word for word in words if len(word) > 3],  # Ejemplo simplista
            "others": [word for word in words if len(word) <= 3],
        }
        return categorized
