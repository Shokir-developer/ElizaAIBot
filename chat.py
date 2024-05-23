import re
import random

class Chat:
    def __init__(self, pairs):
        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x,y) in pairs]

    def respond(self, user_input):
        for (pattern, responses) in self._pairs:
            match = pattern.match(user_input)

            if match:
                response = random.choice(responses)
                response = self._subsitute(response, match)
                return response
        return "Buni tushunmadim"
    
    def _subsitute(self,response, match):
        for index, group in enumerate(match.groups(), 1):
            placeholder = "%" + str(index)
            response = response.replace(placeholder, group)

        return response