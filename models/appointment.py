class Appointment:
    def __init__(self, doctor, patient, date, time_slot):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time_slot = time_slot

    def get_details(self):
        return f"Date: {self.date} , Time: {self.time_slot} , Doctor: {self.doctor.name} , Patient: {self.patient.name}"