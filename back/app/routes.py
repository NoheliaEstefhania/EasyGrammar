from flask import Blueprint, request, jsonify
from .services.sentence_service import SentenceService
from .services.word_service import WordService
from .services.another_service import AnotherService

# Crear un blueprint para agrupar las rutas
api = Blueprint("api", __name__)

# Instancias de los servicios
sentence_service = SentenceService()
word_service = WordService()
another_service = AnotherService()


@api.route("/", methods=["GET"])
def isLife():
    return "live"


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


def register_routes(app):
    app.register_blueprint(api)
