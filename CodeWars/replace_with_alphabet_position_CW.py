def alphabet_position(text):
    return ' '.join([str(ord(i.lower())-96) for i in text if i.isalpha()])