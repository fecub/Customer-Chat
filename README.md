# Customer-Chat

# 📞 Kunden-Support-Chat mit FastAPI & Vue.js

Dieses Projekt ist ein **Echtzeit-Kunden-Support-Chat**, in dem Kunden mit Support-Mitarbeitern kommunizieren können.\
Es besteht aus:

- **Backend**: FastAPI + SQLAlchemy für die Datenbankverwaltung
- **Kunden-Frontend**: Vue 3 + Vuetify für die Benutzeroberfläche der Kunden
- **Support-Frontend**: Eigenständige Vue 3 + Vuetify App für den Support-Mitarbeiter

---

## 🚀 **Funktionen**

✅ Kunden können sich registrieren und einen Chat mit dem Support starten\
✅ Support-Mitarbeiter sehen eine Liste aller aktiven Chats und können darauf antworten\
✅ Nachrichten werden in Echtzeit synchronisiert (Polling oder WebSockets möglich)\
✅ SQLAlchemy ORM zur Verwaltung der Benutzer, Chats und Nachrichten

---

## 📦 **Projektstruktur**

```plaintext
customer-chat-backend/
│── core/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── controller.py    # API-Endpunkte für Kunden & Support
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── router.py
│   ├── chat/
│   │   ├── __init__.py
│   │   ├── router.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── session.py       # Datenbankverbindung & Session-Handling
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py          # User-Modell (Kunden & Support)
│   │   ├── chat.py          # Chat- & Nachrichten-Modelle
│   ├── schema/
│   │   ├── __init__.py
│   │   ├── chat_schema.py   # Pydantic-Schemas für API-Responses
│   │   ├── user_schema.py
│   ├── startup_main.py      # Initialisiert die Datenbank
│── app.py                   # FastAPI Haupt-App
│── requirements.txt          # Python-Abhängigkeiten
│── README.md
```

Frontend:

```plaintext
frontend/customer-frontend/      # Kunden-Frontend (Vue 3 + Vuetify)
frontend/support-frontend/       # Support-Frontend (Vue 3 + Vuetify)
```

---

## 🛠 **1️ Backend-Installation (FastAPI)**

### **📉 Voraussetzungen**

- **Python 3.10+**
- **SQLite**
- **FastAPI & SQLAlchemy**

### **📉 Installation**

```bash
git clone https://github.com/fecub/Customer-Chat.git
cd core
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### **📉 Datenbank migrieren & Server starten**

```bash
fastapi dev app.py
```

Der Server läuft jetzt unter ``\
**Swagger-Dokumentation**
"/": [**http://127.0.0.1:8000/docs**](http://127.0.0.1:8000/docs)
"/api": [**http://127.0.0.1:8000/api/docs**](http://127.0.0.1:8000/api/docs)

---

## 🖥 **2️. Kunden-Frontend (Vue 3 + Vuetify)**

### **📉 Installation**

```bash
cd frontend/customer-frontend
npm install
npm run dev
```

Die App läuft unter: ``

---

## 🖥 **3️. Support-Frontend (Vue 3 + Vuetify)**

### **📉 Installation**

```bash
cd frontend/support-frontend
npm install
npm run dev
```

---

## 📈 **4. Weiterentwicklung**

- ✅ **Echte Echtzeit-Updates mit WebSockets statt Polling**
- ✅ **Auth-System für Kunden & Support mit JWT**
- ✅ **Datenbank auf PostgreSQL umstellen**
- ✅ **Docker-Container für einfaches Deployment**
- ✅ **Intuitiveres Design**

---

## 🔍 **5. Fazit**

Dieses Projekt bietet eine **schnelle und skalierbare Chat-Lösung** für Kunden-Support. 🚀\

---

### **👨‍💻 Autor: Dein Name**

💎 **E-Mail**: [ferit.cubukcuoglu@yazcub.com](mailto:ferit.cubukcuoglu@yazcub.com)\
🔗 **GitHub**: [github.com/fecub](https://github.com/fecub)
