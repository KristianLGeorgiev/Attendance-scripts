#seperate class for generating a unique id for the pyzk UID property

import random

class UID_Generator:
    #constructor - assign max and min value
    def __init__(self, min_value = 0, max_value = 32767):
        self.min_value = min_value
        self.max_value = max_value
        self.generated_uids = set()

    #function generate the unique id and return it
    def generate_uid(self):
        if len(self.generated_uids) >= (self.max_value - self.min_value + 1):
            raise ValueError("All possible UID's generated!")
        
        while True:
            uid = random.randint(self.min_value, self.max_value)
            if uid not in self.generated_uids:
                self.generated_uids.add(uid)
                return uid
