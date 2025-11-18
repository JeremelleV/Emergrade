# Emergrade — EEG-Driven Virtual Try-On Platform

![JavaScript](https://img.shields.io/badge/Language-JavaScript-F7DF1E?logo=javascript&logoColor=black)
![HTML/CSS](https://img.shields.io/badge/UI-HTML%20%2F%20CSS-E34F26?logo=html5&logoColor=white)

![Django](https://img.shields.io/badge/Framework-Django-092E20?logo=django)
![Python](https://img.shields.io/badge/Backend-Python_/_Django-3776AB?logo=python)

![Render](https://img.shields.io/badge/Hosted_on-Render-46E3B7?logo=render&logoColor=white)

![IDM-VTON](https://img.shields.io/badge/AI_Model-IDM--VTON-FF6F61?logo=huggingface&logoColor=white)
![HuggingFace](https://img.shields.io/badge/API-HuggingFace_Space-FFD21E?logo=huggingface&logoColor=black)

---

## Overview

Emergrade is an ambitious, full-stack web application built on **Django** that seamlessly integrates **Virtual Try-On (VTON)** technology with **EEG** data processing. The core mission is to investigate how a user's real-time cognitive state, as captured via the Muse 2 (EEG), affects a virtual clothing try-on experience.

This project was developed by our multidisciplinary team for NatHacks 2025, focusing on AI, UX, sustainability, and digital well-being.

Check out the live website: **[Emergrade on Render](https://emergrade-a0wx.onrender.com)** 

Check out the project on Devpost: **[Devpost Page Here](https://devpost.com/software/emergrade)**

---

## Key Features

* **Virtual Try-On (VTON) Core:** Utilizes yisol et. al IDM-VTON model to accurately composite new garment images onto a target person's photo. A dedicated HTML page (`vton_demo.html`) serves as the primary front-end for this feature.

* **Django Web Application:** Provides a robust and scalable web framework for the entire platform, handling user interactions, data storage (`db.sqlite3`), and the presentation layer.

* **EEG Integration:** Processes physiological data by acquiring, handling, and analyzing EEG signals (specifically **Delta, Theta, Alpha, Beta, Gamma** band powers). Dependencies on `muselsl` confirm support for streaming data from devices like the Muse headset. This data is the unique layer informing the "smart shopper" experience. This feature is yet to be fully integrated.

---

## Tech Stack

### **Frontend**
- HTML, CSS, JS  

### **Backend**
- **Python 3.12**
- **Django**

### **AI / Model Hosting**
- HuggingFace Space (IDM-VTON)
- Pillow (image preprocessing)
- Requests → HF inference API

### **Bio-Signal Tools (Optional)**
- MuseLSL  
- Lab Streaming Layer (LSL)  
- Python WebSockets client  

---

## Local Setup and Development

This project requires a Python environment managed by **Pipenv** (using `Pipfile`).

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/JeremelleV/Emergrade.git
    ```
2.  **Install Dependencies:**
    ```bash
    pipenv install
    pipenv shell
    ```
3.  **Run the Django Server:**
    ```bash
    python manage.py runserver
    ```

---

## Model Credit — yisol/IDM-VTON

All virtual try-on results are generated using the excellent open-source model:

### **IDM-VTON on Hugging Face**  
🔗 https://huggingface.co/spaces/yisol/IDM-VTON  

### **GitHub Repository**  
🔗 https://github.com/yisol/IDM-VTON  

This extension does **not** modify or distribute model weights.  
All inference calls go directly through the publicly available **Hugging Face Space API** using the `@gradio/client` library.

If you use or extend this project, please credit **yisol et al.** for their work.
