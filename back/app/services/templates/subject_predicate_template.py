def _get_context(language):
    if language == "en":
        return (
            "I want you to analyze a sentence and identify its two main parts: the subject and the predicate. "
            "This task involves recognizing the main components of a sentence, providing clarity on what the sentence is about and what action it describes."
        )
    elif language == "es":
        return (
            "Quiero que analices una oración e identifiques sus dos partes principales: el sujeto y el predicado. "
            "Esta tarea implica reconocer los componentes principales de una oración, proporcionando claridad sobre de qué trata la oración y qué acción describe."
        )
    else:
        return (
            "I want you to analyze a sentence and identify its two main parts: the subject and the predicate. "
            "This task involves recognizing the main components of a sentence, providing clarity on what the sentence is about and what action it describes."
        )


def _get_instructions(language):
    if language == "en":
        return (
            "1. The **subject** should capture who or what the sentence is about. "
            "It usually contains the noun or pronoun that acts as the topic or the doer of the action.\n\n"
            "2. The **predicate** should include everything else that describes the action or provides additional information about the subject. "
            "It usually starts with the main verb and can include objects, complements, or modifiers."
        )
    elif language == "es":
        return (
            "1. El **sujeto** debe captar quién o qué es el tema de la oración. "
            "Normalmente contiene el sustantivo o pronombre que actúa como el tema o el ejecutor de la acción.\n\n"
            "2. El **predicado** debe incluir todo lo demás que describa la acción o proporcione información adicional sobre el sujeto. "
            "Normalmente comienza con el verbo principal y puede incluir objetos, complementos o modificadores."
        )
    else:
        return (
            "1. The **subject** should capture who or what the sentence is about. "
            "It usually contains the noun or pronoun that acts as the topic or the doer of the action.\n\n"
            "2. The **predicate** should include everything else that describes the action or provides additional information about the subject. "
            "It usually starts with the main verb and can include objects, complements, or modifiers."
        )


def _get_examples(language):
    if language == "en":
        return (
            "Example:\n"
            "- Sentence: 'The cat sits on the mat.'\n"
            "- Result:\n"
            "  {\n"
            '    "subject": "The cat",\n'
            '    "predicate": "sits on the mat"\n'
            "  }\n"
        )
    elif language == "es":
        return (
            "Ejemplo:\n"
            "- Oración: 'El gato se sienta en la alfombra.'\n"
            "- Resultado:\n"
            "  {\n"
            '    "sujeto": "El gato",\n'
            '    "predicado": "se sienta en la alfombra"\n'
            "  }\n"
        )
    else:
        return (
            "Example:\n"
            "- Sentence: 'The dog barks loudly.'\n"
            "- Result:\n"
            "  {\n"
            '    "subject": "The dog",\n'
            '    "predicate": "barks loudly"\n'
            "  }\n"
        )


def _get_format_instruction(language):
    if language == "en":
        # return "Please return the result in JSON format as shown in the example above."
        return """
Use this JSON schema:

Recipe = {'subject': str, 'predicate': str}
Return: Recipe"""

    elif language == "es":
        return "Por favor, devuelve el resultado en formato JSON como se muestra en el ejemplo anterior."
    else:
        return "Please return the result in JSON format as shown in the example above."


def _get_specific_request(sentence, language):
    if language == "en":
        return f"Now, please perform the task for the following sentence:\n- Sentence: '{sentence}'"
    elif language == "es":
        return f"Ahora, por favor, realiza la tarea para la siguiente oración:\n- Oración: '{sentence}'"
    else:
        return f"Now, please perform the task for the following sentence:\n- Sentence: '{sentence}'"


def subject_predicate_prompt(sentence, language):
    context = _get_context(language)
    instructions = _get_instructions(language)
    examples = _get_examples(language)
    format_instruction = _get_format_instruction(language)
    specific_request = _get_specific_request(sentence, language)

    return f"{context}\n\n{instructions}\n\n{examples}\n\n{format_instruction}\n\n{specific_request}"
