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
                # Get first character, capitalize it, and add a period
                initials.append(word[0].upper() + ".")
        
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