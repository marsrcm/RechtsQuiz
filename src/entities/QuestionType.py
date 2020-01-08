from enum import Enum


class Type(Enum):
    MultipleChoice = 'Multiple Choice'
    OpenEnded = 'Open Ended'

    def __str__(self):
        return self.value
