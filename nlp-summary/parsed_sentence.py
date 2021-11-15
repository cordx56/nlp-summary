from typing import Optional, List
from .calced_word import CalcedWord

class ParsedSentence:
    calced_words: List[CalcedWord]
    def weight_sum(self) -> Optional[float]:
        return 0.0
