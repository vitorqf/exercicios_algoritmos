import re

STRING_CONFIG = {
    "min": 1,
    "max": 50, 
}

REGEX_CONFIG = {
    "pattern": r"\w+",
    "max": r"\w{50}"
}

def get_line_from_user() -> list[str]:

    line = (input('> '))

    if re.search(REGEX_CONFIG["max"], line) is not None:
        raise Exception('There is a maximum of 50 characters per word.')

    line = re.findall(REGEX_CONFIG["pattern"], line)

    if len(line) > STRING_CONFIG['max'] or len(line) < STRING_CONFIG["min"]:
        raise Exception('The amount of lines must be >= 1 and <= 50.')

    line.sort(key=len, reverse=True)

    return line


quantifier = int(input('Insert the amount of lines to input: '))

print('\nBelow, insert your lines.')

try:
    lines = [get_line_from_user() for _ in range(quantifier)]

except Exception as e:
    print(e)

print()

for line in lines:
    print(" ".join(line))





    
    

