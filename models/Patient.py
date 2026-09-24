from .person import Person
from .Medical_records import Medical_records

class Patient(Person):
    def __init__(self, name, id_number, age=None, gender="Not Specified", blood_type=None, contact_info=None):
        super().__init__(name, id_number, age, contact_info)
        self.gender = gender
        self.blood_type = blood_type
        self.medical_records = Medical_records()

    def add_new_visit(self, doctor_name, diagnosis, date):
        self.medical_records.add_visit(doctor_name, diagnosis, date)