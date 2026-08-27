class Person:
    def __init__(self, name="Unknown", id_number=0, age=None, contact_info=None):
        self.name = name
        self.__id_number = id_number
        self.age = age
        self.contact_info = contact_info

    def get_id_number(self):
        return self.__id_number