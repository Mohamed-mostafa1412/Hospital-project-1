class Medical_records():
    def __init__(self):
        self.__visits = []    

    def add_visit(self, doctor_name, diagnosis, date):
        visit_data_of_patient = {
        "doctor": doctor_name,
        "diagnosis": diagnosis,
        "date": date
    }
        self.__visits.append(visit_data_of_patient)

    def get_visits(self):
        return self.__visits

