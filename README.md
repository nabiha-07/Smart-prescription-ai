# Smart Prescription Assistant BD

An academic/demo Android application that helps patients and their families store prescriptions
digitally, extract text from prescription photos with OCR, **correct or manually enter medicines when
OCR cannot read handwriting**, keep a prescription history, and receive medicine reminders — in
**Bangla and English**.

> ⚕️ **Medical disclaimer**
> This application does **not** diagnose diseases, prescribe medicine, recommend dosage, or replace a
> doctor or pharmacist. OCR output is **not** assumed to be medically correct and must always be
> reviewed by the user. *Always follow your doctor's or pharmacist's instructions.*

---

## Technology stack (fixed — no substitutions)

| Layer | Technology |
|---|---|
| Application logic | **Java** (no Kotlin) |
| User interface | **XML layouts / Android Views** (no Jetpack Compose) |
| IDE | Android Studio |
| Authentication | Firebase Authentication (Email + Password) |
| OCR | Google ML Kit Text Recognition |
| Local storage | Room Database |
| Reminders | AlarmManager + Android Notifications |

Package name: `com.example.smartprescriptionassistantbd`

---

## Build status

🚧 **Under construction — built step by step.**

This repository is developed in 24 sequential steps. Each step has its own guide under `docs/`, and a
step is only started after the previous one has been confirmed working on a real machine.

| Step | Topic | Guide | Status |
|---:|---|---|---|
| 1 | Create Android Studio Java/XML project | [`docs/STEP_01_CREATE_PROJECT.md`](docs/STEP_01_CREATE_PROJECT.md) | 📄 Instructions ready — awaiting your confirmation |
| 2 | Configure Gradle and dependencies | — | ⏳ Blocked: needs your SDK versions |
| 3 | MainActivity / Splash screen | — | ⏳ |
| 4 | Login UI + Java logic | — | ⏳ |
| 5 | Register UI + Firebase Authentication | — | ⏳ |
| 6 | Dashboard | — | ⏳ |
| 7 | Camera / Gallery prescription selection | — | ⏳ |
| 8 | Google ML Kit OCR integration | — | ⏳ |
| 9 | Room Database | — | ⏳ |
| 10 | Prescription and Medicine models | — | ⏳ |
| 11 | Prescription History | — | ⏳ |
| 12 | Prescription Details | — | ⏳ |
| 13 | Manual Medicine Entry | — | ⏳ |
| 14 | Edit Prescription | — | ⏳ |
| 15 | Medicine Search | — | ⏳ |
| 16 | Medicine Reminder | — | ⏳ |
| 17 | Android Notifications | — | ⏳ |
| 18 | Emergency Contact | — | ⏳ |
| 19 | Bangla localization | — | ⏳ |
| 20 | UI polish | — | ⏳ |
| 21 | Full application testing | — | ⏳ |
| 22 | Bug fixes | — | ⏳ |
| 23 | Final project documentation | — | ⏳ |
| 24 | Viva questions and answers | — | ⏳ |

Nothing above is claimed as implemented until its row says so. No source code has been committed yet.

---

## Planned features

1. User Registration
2. User Login
3. Firebase Email/Password Authentication
4. Dashboard
5. Prescription scan using Camera
6. Prescription image selection from Gallery
7. Google ML Kit OCR
8. Display OCR extracted text
9. Edit / correct OCR text
10. Manual Medicine Entry
11. Add multiple medicines per prescription
12. Save Prescription
13. Prescription History
14. Prescription Details
15. Edit Prescription
16. Delete Prescription
17. Medicine Search (local demo dataset)
18. Medicine Reminder
19. Android Notification
20. Emergency Contact
21. Bangla and English support
22. Logout

## Future scope (NOT implemented — listed for the project report only)

- Doctor Appointment Reminder
- Drug Interaction Warning
- Hospital / Pharmacy Integration
- AI-based Prescription Analysis

---

## Setup notes

- `google-services.json` is **not** committed to this repository and never will be. You generate your
  own from the Firebase Console — full click-by-click instructions arrive in **Step 5**.
- `local.properties` is machine specific and is git-ignored.
- No API keys, secrets or real patient data appear anywhere in this repository. All demo data is
  fictional.
