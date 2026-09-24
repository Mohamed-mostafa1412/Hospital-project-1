import customtkinter as ctk
from tkinter import messagebox
from models.Doctor import Doctor
from models.Patient import Patient

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class HospitalGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hospital Management System")
        self.geometry("500x500")
        self.configure(fg_color="#F4F7F6")
        self.resizable(False, False)

        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)

        self.show_role_selection_screen()

    def clear_container(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

    
    
    def show_role_selection_screen(self):
        self.clear_container()

        card = ctk.CTkFrame(self.main_container, fg_color="#FFFFFF", corner_radius=15, border_width=1, border_color="#E0E0E0")
        card.pack(fill="both", expand=True, padx=10, pady=10)

        title = ctk.CTkLabel(card, text="Hospital Portal", font=("Segoe UI", 24, "bold"), text_color="#1E3A8A")
        title.pack(pady=(30, 5))

        subtitle = ctk.CTkLabel(card, text="Welcome! Please choose your login role:", font=("Segoe UI", 12), text_color="#64748B")
        subtitle.pack(pady=(0, 30))

        btn_doctor = ctk.CTkButton(
            card, text="👨‍⚕️ Doctor Login", font=("Segoe UI", 14, "bold"),
            fg_color="#3B82F6", hover_color="#2563EB", text_color="#FFFFFF",
            corner_radius=10, height=45, width=280,
            command=lambda: self.show_login_screen("Doctor")
        )
        btn_doctor.pack(pady=10)

        btn_patient = ctk.CTkButton(
            card, text="🩺 Patient Login", font=("Segoe UI", 14, "bold"),
            fg_color="#60A5FA", hover_color="#3B82F6", text_color="#FFFFFF",
            corner_radius=10, height=45, width=280,
            command=lambda: self.show_login_screen("Patient")
        )
        btn_patient.pack(pady=10)

    def show_login_screen(self, role):
        self.clear_container()

        card = ctk.CTkFrame(self.main_container, fg_color="#FFFFFF", corner_radius=15, border_width=1, border_color="#E0E0E0")
        card.pack(fill="both", expand=True, padx=10, pady=10)

        title = ctk.CTkLabel(card, text=f"{role} Login", font=("Segoe UI", 22, "bold"), text_color="#1E3A8A")
        title.pack(pady=(25, 20))

        self.entry_name = ctk.CTkEntry(
            card, placeholder_text="Full Name", width=300, height=40,
            corner_radius=8, border_color="#CBD5E1", fg_color="#F8FAFC"
        )
        self.entry_name.pack(pady=10)

        self.entry_id = ctk.CTkEntry(
            card, placeholder_text="ID Number", width=300, height=40,
            corner_radius=8, border_color="#CBD5E1", fg_color="#F8FAFC"
        )
        self.entry_id.pack(pady=10)

        btn_login = ctk.CTkButton(
            card, text="Sign In", font=("Segoe UI", 14, "bold"),
            fg_color="#2563EB", hover_color="#1D4ED8", text_color="#FFFFFF",
            corner_radius=8, height=40, width=300,
            command=lambda: self.handle_login(role)
        )
        btn_login.pack(pady=(20, 10))

        btn_back = ctk.CTkButton(
            card, text="← Back to Roles", font=("Segoe UI", 12),
            fg_color="transparent", text_color="#64748B", hover_color="#F1F5F9",
            width=150, command=self.show_role_selection_screen
        )
        btn_back.pack()

    def handle_login(self, role):
        name = self.entry_name.get().strip()
        user_id = self.entry_id.get().strip()

        if not name or not user_id:
            messagebox.showerror("Error", "Please complete all fields!")
            return

        if role == "Doctor":
            user = Doctor(name=name, id_number=user_id, speciliazed_in="General Medicine")
        else:
            user = Patient(name=name, id_number=user_id)

        self.show_dashboard_screen(role, user)

    def show_dashboard_screen(self, role, user):
        self.clear_container()

        card = ctk.CTkFrame(self.main_container, fg_color="#FFFFFF", corner_radius=15, border_width=1, border_color="#E0E0E0")
        card.pack(fill="both", expand=True, padx=10, pady=10)

        welcome_lbl = ctk.CTkLabel(card, text=f"Welcome, {user.name}!", font=("Segoe UI", 20, "bold"), text_color="#1E3A8A")
        welcome_lbl.pack(pady=(20, 2))

        role_lbl = ctk.CTkLabel(card, text=f"Role: {role}  |  ID: {user.get_id_number()}", font=("Segoe UI", 12), text_color="#64748B")
        role_lbl.pack(pady=(0, 20))

        actions_frame = ctk.CTkFrame(card, fg_color="#F8FAFC", corner_radius=10)
        actions_frame.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        if role == "Doctor":
            ctk.CTkButton(actions_frame, text="📅 View Appointments Schedule", fg_color="#3B82F6", hover_color="#2563EB", height=38).pack(fill="x", padx=15, pady=12)
            ctk.CTkButton(actions_frame, text="🕒 Manage Working Slots", fg_color="#3B82F6", hover_color="#2563EB", height=38).pack(fill="x", padx=15, pady=5)
        else:
            ctk.CTkButton(actions_frame, text="➕ Book New Appointment", fg_color="#3B82F6", hover_color="#2563EB", height=38).pack(fill="x", padx=15, pady=12)
            ctk.CTkButton(actions_frame, text="📋 View Medical Records", fg_color="#3B82F6", hover_color="#2563EB", height=38).pack(fill="x", padx=15, pady=5)

        btn_logout = ctk.CTkButton(
            card, text="Logout", font=("Segoe UI", 12, "bold"),
            fg_color="#EF4444", hover_color="#DC2626", text_color="#FFFFFF",
            height=35, width=120, corner_radius=8, command=self.show_role_selection_screen
        )
        btn_logout.pack(pady=(0, 15))

if __name__ == "__main__":
    app = HospitalGUI()
    app.mainloop()