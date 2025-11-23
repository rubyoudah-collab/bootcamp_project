import json

class Module:
    """ Implements a Module entity """

    def __init__(self):
        self.id = 0
        self.module_name = ""
        self.description = ""
        self.status = ""

    def __str__(self)-> str:
        return self.to_json()
    
    def __repr__(self)-> str:
        return self.to_json()
    
    def to_json(self)-> str:
        supplier_dict = {}
        supplier_dict["id"] = self.id
        supplier_dict["module_name"] = self.module_name
        supplier_dict["description"] = self.description
        supplier_dict["status"] = self.status

        return json.dumps(supplier_dict)