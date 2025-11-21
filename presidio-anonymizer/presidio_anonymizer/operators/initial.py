"""Converts the PII text entity to initials."""
from typing import Dict
from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Convert text to initials."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """Convert text to initials.
        
        :param text: The text to convert to initials.
        :param params: Optional parameters (not used for initial operator).
        :return: The initials of the text.
        """
        if not text:
            return ""
        
        # Split text into words and get first character of each word
        words = text.split()
        initials = []
        
        for word in words:
            if word:  # Make sure word is not empty
                # Find the first alphanumeric character
                first_alnum_index = -1
                for i, char in enumerate(word):
                    if char.isalnum():
                        first_alnum_index = i
                        break
                
                if first_alnum_index != -1:
                    # Preserve everything before the first alphanumeric character
                    prefix = word[:first_alnum_index]
                    # Get the first alphanumeric character and capitalize it
                    initial_char = word[first_alnum_index].upper()
                    # Combine: prefix + initial + period
                    initials.append(prefix + initial_char + ".")
                else:
                    # If no alphanumeric character found, skip this word
                    continue
        
        # Join initials with spaces
        return " ".join(initials)

    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize