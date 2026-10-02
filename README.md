# SnapClass – Multimodal AI Attendance Management Platform

SnapClass is a multimodal attendance management platform that automates classroom attendance using Face Recognition and Voice Recognition pipelines. The system enables teachers to create subjects, enroll students, share class invitations, and generate attendance records through AI-powered verification.

---

## 🌐 Landing Page
![Landing Page](assets/snap-landing.png)

## 👨‍🏫 Teacher Dashboard
![Teacher Dashboard](assets/snap-teacher-flow-2-dashboard.png)

## 📚 Subject Management
![Subject Management](assets/snap-teacher-flow-3-create-course.png)

## 🔗 QR-Based Enrollment
![QR Enrollment](assets/snap-teacher-flow-4-share-qr-or-link.png)

## 🎤 Voice Attendance Verification
![Voice Attendance](assets/snap-teacher-flow-5.1-voice-attendance.png)

## 👤 Face Recognition Attendance
![Face Attendance](assets/snap-teacher-flow-5.2-photo-attendance.png)

## 📊 Attendance Analytics & Reports
![Attendance Reports](assets/snap-teacher-flow-5-see-stored-record.png)

## 🚀 Features

- Face Recognition Attendance
- Voice Recognition Attendance
- Subject & Classroom Management
- Student Enrollment System
- QR-Based Class Joining
- Attendance Reports & Analytics
- Teacher & Student Dashboards
- Secure Attendance Verification
- Streamlit Deployment
- Responsive Web Interface

---

## 🛠 Tech Stack

### AI & Machine Learning
- Face Recognition
- Voice Recognition
- OpenCV
- NumPy
- Scikit-Learn

### Backend & Application
- Python
- Streamlit

### Database
- Supabase
- PostgreSQL

### Deployment
- Streamlit Cloud
- Vercel

---

## 📂 Project Structure

```text
app.py

src/
├── components/
│   ├── dialog_add_photo.py
│   ├── dialog_attendance_result.py
│   ├── dialog_auto_enroll.py
│   ├── dialog_create_subject.py
│   ├── dialog_enroll.py
│   ├── dialog_share_subject.py
│   ├── dialog_voice_attendance.py
│   ├── footer.py
│   ├── header.py
│   └── subject_card.py
│
├── database/
│   ├── config.py
│   └── db.py
│
├── pipelines/
│   ├── face_pipeline.py
│   └── voice_pipeline.py
│
├── screens/
│   ├── home_screen.py
│   ├── student_screen.py
│   └── teacher_screen.py
│
└── ui/
    └── base_layout.py
```

---

## 🏗 Architecture

```text
Teacher Dashboard
        │
        ▼
Subject Management
        │
        ▼
Student Enrollment
        │
        ▼
Attendance Collection
      /         \
     /           \
 Face AI      Voice AI
     \           /
      \         /
        ▼      ▼
Attendance Verification
        │
        ▼
Attendance Reports
```

---

## 💡 Engineering Highlights

- Developed independent Face Recognition and Voice Recognition pipelines for multimodal attendance verification.
- Designed a modular architecture using reusable UI components, screens, pipelines, and database layers.
- Integrated Supabase PostgreSQL backend for subject management, enrollment workflows, and attendance storage.
- Implemented QR-based classroom onboarding with shareable enrollment links.
- Built teacher and student dashboards for attendance management and reporting.
- Engineered end-to-end deployment pipeline using Streamlit Cloud and Vercel.
- Developed reusable dialog-driven interfaces for enrollment, attendance review, reporting, and subject management workflows.
- Followed production-style software architecture with separation of concerns and scalable component organization.

---

## 🔗 Project Links

### Live Demo
https://snap-class-landing-page-delta.vercel.app/

## 🔮 Future Improvements

- DeepFace Integration
- Speaker Embedding Models
- Real-Time Classroom Attendance
- Attendance Analytics Dashboard
- Mobile Application
- AI Teaching Assistant

---

## 👨‍💻 Author

**Mayank Patidar**

B.Tech Artificial Intelligence & Data Science  
LNCT Bhopal

GitHub: https://github.com/mayankptdr

---
