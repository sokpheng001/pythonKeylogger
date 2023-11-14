import re
import re

log = """
2023-11-15 00:34:14,314: Key 'a' pressed
2023-11-15 00:34:14,571: Key 'c' pressed
2023-11-15 00:34:14,690: Key 'h' pressed
2023-11-15 00:34:33,490: Key Key.space pressed
2023-11-15 00:34:14,571: Key 'c' pressed
2023-11-15 00:34:14,690: Key 'h' pressed
"""

def convert_to_readable_statement(log):
    lines = log.split('\n')
    keys = [re.findall(r"Key\s'(.+?)'\spressed", line) for line in lines]
    readable_statement = " ".join([key[0] for key in keys if key])
    return readable_statement

readable_log = convert_to_readable_statement(log)
print(readable_log)


def convert_to_readable(log):
    key_mapping = {
        'enter': '\n',
        'space': ' ',
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
                readable_statement += "\t"
            if key == 'esc':
                break
    return readable_statement

# result = convert_to_readable(log)
# print(result)


