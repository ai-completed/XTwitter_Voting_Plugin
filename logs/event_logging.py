import logging

# Set up logging
logging.basicConfig(filename='voting_system.log', level=logging.INFO)

def log_event(event):
    logging.info(f"Event logged: {event}")