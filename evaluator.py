# evaluator.py
import yaml
import re
from typing import List, Dict, Tuple

class Evaluator:
    def __init__(self, test_file_path):
        self.test_file_path = test_file_path
        self.tests = self.load_tests()
    
    def load_tests(self):
        with open(self.test_file_path, 'r') as f:
            data = yaml.safe_load(f)
        return data
    
    def evaluate_response(self, response: str, must_have: List[str], must_not_have: List[str]) -> Tuple[float, Dict]:
        score = 10.0
        results = {
            'found_required': [],
            'missing_required': [],
            'found_forbidden': [],
            'passed_forbidden': []
        }
        
        # Check must_have items
        for item in must_have:
            if self._contains_phrase(response, item):
                results['found_required'].append(item)
            else:
                results['missing_required'].append(item)
                score -= (10.0 / len(must_have)) if must_have else 0
        
        # Check must_not_have items
        for item in must_not_have:
            if self._contains_phrase(response, item):
                results['found_forbidden'].append(item)
                score -= (5.0 / len(must_not_have)) if must_not_have else 0
            else:
                results['passed_forbidden'].append(item)
        
        return max(0.0, score), results
    
    def _contains_phrase(self, text: str, phrase: str) -> bool:
        # Case-insensitive search
        return phrase.lower() in text.lower()
