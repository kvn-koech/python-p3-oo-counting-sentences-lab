# lib/my_string.py
class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        """Returns True if value ends with a period, False otherwise"""
        return self.value.endswith('.')

    def is_question(self):
        """Returns True if value ends with a question mark, False otherwise"""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Returns True if value ends with an exclamation mark, False otherwise"""
        return self.value.endswith('!')

    def count_sentences(self):
        """Counts the number of sentences in the value"""
        if not self.value:
            return 0
            
        # Replace all sentence-ending punctuation with periods for consistency
        temp_value = self.value.replace('?', '.').replace('!', '.')
        
        # Split on periods
        sentences = temp_value.split('.')
        
        # Filter out empty strings and count non-empty ones
        non_empty_sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        
        return len(non_empty_sentences)