import os
from dotenv import load_dotenv
import logging
import dialogflow_v2 as dialogflow
import dialogflow_v2beta1 as dialogflow_beta
from shape_intents import shape_intents_from_file
from google.api_core.exceptions import PermissionDenied, InvalidArgument


def main():
    load_dotenv()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG)
    project_id = os.environ['DIALOGFLOW_PROJECT_ID']
    training_questions_file_name = 'training_questions.json'
    try:
        intents_client = dialogflow.IntentsClient()
        intents_parent = intents_client.project_agent_path(project_id)
        intents = shape_intents_from_file(training_questions_file_name)

        agents_client = dialogflow_beta.AgentsClient()
        agents_parent = agents_client.project_path(project_id)

        for intent in intents:
            intents_client.create_intent(intents_parent, intent)
        logging.debug('Intents created')
        agents_client.train_agent(agents_parent)
        logging.info('Trained successfully')
    except PermissionDenied as permission_denied_error:
        logging.error('Permission denied')
        logging.error(permission_denied_error)
    except TypeError as type_error:
        logging.error('Can not open training questions file')
        logging.error(type_error)
    except InvalidArgument as argument_error:
        logging.error(argument_error)


if __name__ == "__main__":
    main()
