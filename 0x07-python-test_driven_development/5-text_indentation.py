def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """


    if not isinstance(text, str):
        raise TypeError("text must be a string")

    formatted_text = ""

    for char in text:
        formatted_text += char

        if char in ['.', '?', ':']:
            formatted_text += '\n\n'

    lines = formatted_text.split('\n')
    for line in lines:
        print(line.strip())
