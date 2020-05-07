import json


def open_json_file(json_file_name):
    with open(json_file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def shape_intents_from_file(training_questions_json_file_name):
    training_questions = open_json_file(training_questions_json_file_name)
    intents = []
    for intent_name, qna in training_questions.items():
        questions = qna["questions"]
        answers = [qna["answer"]]
        training_phrases = list(
            {
                "parts": [{"text": training_phrase}]
            }
            for training_phrase in questions
        )
        messages = list(
            {
                "text": {"text": [message]}
            }
            for message in answers
        )
        intent = {"display_name": intent_name,
                  "messages": messages,
                  "training_phrases": training_phrases
                  }
        intents.append(intent)
    return intents
