def get_boolean_input(prompt):
    """
    Gets user input for yes/no questions and converts it to a boolean.

    :param prompt: The question to ask the user
    :return: True if user inputs 'y', False otherwise
    """
    return input(prompt).strip().lower() == 'y'
