from flask import Blueprint, request, jsonify
from .services.sentence_service import SentenceService
from .services.word_service import WordService
from .services.another_service import AnotherService
from .services.subject_predicate_service import (
    SubjectPredicateService,
)  # Importar nuevo servicio

# Crear un blueprint para agrupar las rutas
api = Blueprint("api", __name__)

# Instancias de los servicios
sentence_service = SentenceService()
word_service = WordService()
another_service = AnotherService()
subject_predicate_service = SubjectPredicateService()  # Instancia del nuevo servicio


@api.route("/", methods=["GET"])
def isLife():
    return "Esta vivooooo"


@api.route("/api/split-sentence", methods=["POST"])
def split_sentence_route():
    data = request.json
    sentence = data.get("sentence", "")
    result = sentence_service.split_sentence(sentence)
    return jsonify(result)


@api.route("/api/split-words", methods=["POST"])
def split_words_route():
    data = request.json
    sentence = data.get("sentence", "")
    result = word_service.split_words(sentence)
    return jsonify(result)


@api.route("/api/categorize-words", methods=["POST"])
def categorize_words_route():
    data = request.json
    sentence = data.get("sentence", "")
    result = another_service.categorize_words(sentence)
    return jsonify(result)


@api.route("/api/split-subject-predicate", methods=["POST"])
def split_subject_predicate_route():
    data = request.json
    print(data)
    sentence = data.get("sentence", "")
    language = data.get("language", "en")  # Idioma por defecto es inglés
    print(sentence)
    print(language)
    result = subject_predicate_service.split_subject_predicate(sentence, language)
    return jsonify(result)


def register_routes(app):

    app.register_blueprint(api)
