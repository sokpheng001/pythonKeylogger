import re
import pandas as pd
log = """
2023-11-15 00:34:14,314: Key 'a' pressed
2023-11-15 00:34:14,571: Key 'c' pressed
2023-11-15 00:34:14,690: Key 'h' pressed
2023-11-15 00:34:33,490: Key Key.space pressed
2023-11-15 00:34:14,571: Key 'c' pressed
2023-11-15 00:34:14,690: Key 'h' pressed
"""


def convert_to_readable(log):
    key_mapping = {
        'enter': '\n',
        'space': '  ',
        'esc': '',
        'shift_r': '',
        'caps_lock': '',
    }

    readable_statement = ""
    for line in log.split("\n"):
        if "Key " in line and "pressed" in line:
            key_parts = line.split("'")
            key = key_parts[1] if len(key_parts) > 1 else ''
            readable_statement += key_mapping.get(key, key) if key.isalnum() else ''
            if key == "space":
                readable_statement += "_"
            if key == 'esc':
                break
    return readable_statement

# result = convert_to_readable(log)
# print(result)import pandas as pd


def convert_log(log):
    # Split the log string into lines
    log_lines = log.split("\n");
    # Create empty lists for timestamp and message
    timestamps = []
    messages = []
    # Extract timestamp and message from each line
    for line in log_lines:
        if line.startswith("2023"):
            timestamp, message = line.split(": ", 1)
            timestamps.append(timestamp)
            messages.append(message)
    
    # Create a DataFrame from the extracted data
    df = pd.DataFrame({"timestamp": timestamps, "message": messages})
    
    # Convert timestamps to datetime format
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    
    # Sort the DataFrame by timestamp
    df = df.sort_values(by="timestamp")
    # Print the DataFrame
    return df.to_string();

