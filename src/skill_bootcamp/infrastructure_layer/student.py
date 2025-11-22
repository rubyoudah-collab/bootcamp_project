import json
from skill_bootcamp.infrastructure_layer.cohort import Cohort
from skill_bootcamp.infrastructure_layer.module import Module
from typing import List

class Student:
    """ Implements a Student entity """

    def __init__(self):
        self.id = 0
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.cohort:Cohort = Cohort()
        self.modules:List[Module] = []

    def __str__(self)-> str:
        return self.to_json()
    
    def __repr__(self)-> str:
        return self.to_json()
    
    def to_json(self)-> str:
        supplier_dict = {}
        supplier_dict["id"] = self.id
        supplier_dict["first_name"] = self.first_name
        supplier_dict["last_name"] = self.last_name
        supplier_dict["email"] = self.email
        supplier_dict["corhort"] = self.cohort.__dict__
        supplier_dict["modules"] = []

        for module in self.modules:
            supplier_dict["modules"].append(module.__dict__)
        
        return json.dumps(supplier_dict)