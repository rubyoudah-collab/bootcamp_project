import json

class Cohort:
    """ Implements a Cohort entity """

    def __init__(self):
        self.id = 0
        self.cohort_name = ""
        self.start_date = ""
        self.end_date = ""

    def __str__(self) -> str:
        return self.to_json()
    
    def __repr__(self) -> str:
        return self.to_json()
    
    def to_json(self) -> str:
        part_dict = {}
        part_dict["id"] = self.id
        part_dict["cohort_name"] = self.cohort_name
        part_dict["start_date"] = self.start_date
        part_dict["end_date"] = self.end_date
        
        return json.dumps(part_dict)