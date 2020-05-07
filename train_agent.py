import os
import dialogflow_v2 as dialogflow
import dialogflow_v2beta1 as dialogflow_beta
from shape_intents import shape_intents_from_file

project_id = os.environ['DIALOGFLOW_PROJECT_ID']
training_questions_file_name = 'training_questions.json'


def main():
    intents_client = dialogflow.IntentsClient()
    intents_parent = intents_client.project_agent_path(project_id)
    intents = shape_intents_from_file(training_questions_file_name)

    agents_client = dialogflow_beta.AgentsClient()
    agents_parent = agents_client.project_path(project_id)

    for intent in intents:
        intents_client.create_intent(intents_parent, intent)
    agents_client.train_agent(agents_parent)


if __name__ == "__main__":
    main()