import json
import logging


def read_json_file(json_file_name):
    with open(json_file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def shape_intents_from_file(training_questions_json_file_name):
    try:
        training_questions = read_json_file(training_questions_json_file_name)
        logging.debug('Training questions received')
        intents = []
        for intent_name, qna in training_questions.items():
            questions = qna["questions"]
            answers = [qna["answer"]]
            training_phrases = [
                {
                    "parts": [{"text": training_phrase}]
                }
                for training_phrase in questions
            ]
            messages = [
                {
                    "text": {"text": [message]}
                }
                for message in answers
            ]
            intent = {"display_name": intent_name,
                      "messages": messages,
                      "training_phrases": training_phrases
                      }
            intents.append(intent)
        logging.debug('Intents shaped')
        return intents
    except FileNotFoundError as file_not_found_error:
        logging.error(file_not_found_error)
    except TypeError as type_error:
        logging.error('Wrong training questions file content format')
        logging.error(type_error)
