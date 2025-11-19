# 🚀 Career Booster — AI-Powered Resume Analyzer & Skill Gap Advisor

Career Booster is an AI-assisted platform that scans your resume, extracts skills/projects, identifies missing skills, and recommends courses to upskill — all with a beautiful, modern UI.

This project is perfect for job seekers, students, and professionals who want to upgrade their career visibility.

---

## ✨ Features

### **📄 Resume Upload & Parsing**
- Upload PDF or DOCX resume
- Auto-extract:
  - Skills
  - Projects
  - Experience (optional)
  - Education (optional)
- Uses **PyPDF2** and **docx2txt** for accurate extraction

---

### **🧠 AI Skill Gap Analysis**
- Compares your current skills with industry-leading skills
- Detects missing or weak skills
- Suggests **value-boosting skills** even if they are not in your resume
- Smart filtering to avoid marking existing skills as missing

---

### **🧩 Add Missing Skills Manually**
- User can type additional skills
- System re-calculates the skill gap automatically

---

### **🎯 Recommended Skills Section**
- Shows:
  - Skills you have ✔
  - Skills you should add ⭐ (industry trending ones)
  - Skills the system could not detect but are relevant

---

### **🎓 Course Recommendation Engine**
Over **350+ curated tech + non-tech skills**, mapped to:

- Coursera  
- Udemy  
- edX  
- YouTube  
- DataCamp  
- Google Garage  
- LinkedIn Learning  
- Pluralsight  
- Free Resources  

Each missing skill gets 4–8 recommended courses + Google search link.

---

### **🎨 Modern UI (Dark Mode Edition)**
- Full-screen background
- Neon blue accents
- Blurred glass cards
- Clean, centered layout
- Professional SaaS look
- Designed with TailwindCSS 4

---

### **🔗 Frontend–Backend Connected**
- Frontend: **Next.js + React**
- Backend: **Flask + Python**
- CORS enabled
- Uses REST API:
  - `/upload`
  - `/course-recommendations`

---

## 🛠️ Tech Stack

### **Frontend**
- Next.js 16
- React 19
- Tailwind CSS 4
- Fetch API

### **Backend**
- Python 3.10+
- Flask
- Flask-CORS
- PyPDF2
- docx2txt
- fuzzywuzzy

---

## 📁 Project Structure

