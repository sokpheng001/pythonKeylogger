import re


def read_log_sentence(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Use a regular expression to extract the desired information
            match = re.match(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (\w+) \[(.*?)\] (.*)$', line)
            if match:
                # Extract the information from the match object
                timestamp, log_level, process, message = match.groups()
                # Format the message into a readable statement
                readable_statement = f"{timestamp} {log_level} {process}: {message}"
                print("This is log:\n {}".format(readable_statement));