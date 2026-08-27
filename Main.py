from models.Doctor import Doctor
from models.Patient import Patient
from models.appointment import Appointment

dr_ahmed = Doctor(
    name="Dr Ahmed",
    id_number=1,
    speciliazed_in="Cardiology",
    working_days=["Sunday", "Tuesday"],
    working_hours="10:00 AM - 04:00 PM",
    room_number=2,
    available_slots=["10:00 AM", "12:00 PM"],
    contact_info="01021094002"
)

patient_mohamed = Patient(
    name="Mohamed",
    id_number=2,
    age=23,
    gender="Male",
    blood_type="A+",
    contact_info="01550453738"
)

patient_mohamed.add_new_visit(
    doctor_name=dr_ahmed.name,
    diagnosis="Checkup",
    date="16/8/2026"
)

app1 = Appointment(
    doctor=dr_ahmed,
    patient=patient_mohamed,
    date="16/8/2026",
    time_slot="10:00 AM"
)

print("="*90)

print("Doctor Info")
print(f"Name: {dr_ahmed.name} , ID: {dr_ahmed.get_id_number()} , Specialization: {dr_ahmed.speciliazed_in}")
print(f"Room: {dr_ahmed.room_number} , Contact: {dr_ahmed.contact_info}")
print(f"Working Days: {dr_ahmed.working_days} , Hours: {dr_ahmed.working_hours}")
print(f"Available Slots: {dr_ahmed.available_slots}")


print("=" * 90)
print("Patient Info")
print(f"Name: {patient_mohamed.name} , Gender: {patient_mohamed.gender} , Age: {patient_mohamed.age} , ID: {patient_mohamed.get_id_number()}")
print(f"Blood Type: {patient_mohamed.blood_type} , Contact: {patient_mohamed.contact_info}")


print("="*90)
print("Appointment Details (Composition)")
print(app1.get_details())


print("=" * 90)
print("Medical Records")
for visit in patient_mohamed.medical_records.get_visits():
    print(f"Date: {visit['date']} , Doctor: {visit['doctor']} , Diagnosis: {visit['diagnosis']}")


print("=" * 90)
print("Appointment Details")
print(app1.get_details())

####################################################################################################
# with unknown values 

dr_test = Doctor(
    name="Dr Sarah",
    id_number=3,
    speciliazed_in="Eyes"
)

patient_test = Patient(
    name="Ali",
    id_number=4
)

app_test = Appointment(
    doctor=dr_test,
    patient=patient_test,
    date="19/8/2026",
    time_slot="11:00 AM"
)


print("=" * 90)

print("Testing absence of value")
print(f"Doctor: {dr_test.name} , ID: {dr_test.get_id_number()} , Spec: {dr_test.speciliazed_in} , Room: {dr_test.room_number} , Contact: {dr_test.contact_info}")
print(f"Days: {dr_test.working_days} , Hours: {dr_test.working_hours} , Slots: {dr_test.available_slots}")

print("-" * 90)
print(f"Patient: {patient_test.name} , Gender: {patient_test.gender} , Age: {patient_test.age} , ID: {patient_test.get_id_number()}")
print(f"Blood Type: {patient_test.blood_type} , Contact: {patient_test.contact_info}")

print("-" * 90)
print(f"Appointment: {app_test.get_details()}")
print("=" * 90)