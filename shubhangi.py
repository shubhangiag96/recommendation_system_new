class Person:
    def __init__(self, id):
        self.id = id
        obama = Person(100)
        obama.__dict__['age'] = 49
        print(obama.age + len(obama.__dict__))
