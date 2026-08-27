from models.person import Person

class Doctor(Person):
    def __init__(self, name, id_number, speciliazed_in, working_days=None, working_hours="N/A", room_number=0, age=None, contact_info=None, available_slots=None):
        super().__init__(name, id_number, age, contact_info)
        self.speciliazed_in = speciliazed_in
        self.working_days = working_days if working_days else []
        self.working_hours = working_hours
        self.room_number = room_number
        self.available_slots = available_slots if available_slots else ["10:00 AM", "12:00 PM"]