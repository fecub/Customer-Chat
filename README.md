# Customer-Chat with FastAPI & Vue.js

This project is a **real-time customer support chat** where customers can communicate with support agents.\
It consists of:

- **Backend**: FastAPI + SQLAlchemy for database management
- **Customer Frontend**: Vue 3 + Vuetify for the customer interface
- **Support Frontend**: Separate Vue 3 + Vuetify app for support agents

---

## 🚀 **Features**

✅ Customers can register and start a chat with support\
✅ Support agents see a list of all active chats and can respond\
✅ Messages are synchronized in real-time\
✅ SQLAlchemy ORM for managing users, chats, and messages

---

## 📦 **Project Structure**

```plaintext
customer-chat-backend/
│── core/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── controller.py    # API endpoints for customers & support
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── router.py
│   ├── chat/
│   │   ├── __init__.py
│   │   ├── router.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── session.py       # Database connection & session handling
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py          # User model (customers & support)
│   │   ├── chat.py          # Chat & message models
│   ├── schema/
│   │   ├── __init__.py
│   │   ├── chat_schema.py   # Pydantic schemas for API responses
│   │   ├── user_schema.py
│── startup_main.py          # Initializes the database
│── app.py                   # FastAPI main app
│── requirements.txt         # Python dependencies
│── README.md
```

Frontend:

```plaintext
frontend/customer-frontend/      # Customer frontend (Vue 3 + Vuetify)
frontend/support-frontend/       # Support frontend (Vue 3 + Vuetify)
```

---

## 🛠 **1. Backend Installation (FastAPI)**

### **📉 Prerequisites**

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

### **📉 Migrate Database & Start Server**

```bash
fastapi dev app.py
```

The server is now running at ``\
**Swagger Documentation**
- "/": [**http://127.0.0.1:8000/docs**](http://127.0.0.1:8000/docs)
- "/api": [**http://127.0.0.1:8000/api/docs**](http://127.0.0.1:8000/api/docs)

---

## 🖥 **2. Customer Frontend (Vue 3 + Vuetify)**

### **📉 Installation**

```bash
cd frontend/customer-frontend
npm install
npm run dev
```
---

## 🖥 **3. Support Frontend (Vue 3 + Vuetify)**

### **📉 Installation**

```bash
cd frontend/support-frontend
npm install
npm run dev
```

---

## 📈 **4. Further Development**

- ✅ **Real real-time updates with WebSockets instead of polling**
- ✅ **Auth system for customers & support with JWT**
- ✅ **Switch database to PostgreSQL**
- ✅ **Docker container for easy deployment**
- ✅ **More intuitive design**

---

## 🔍 **5. Conclusion**

This project offers a **fast and scalable chat solution** for customer support. 🚀

---

### **👨‍💻 Author: Ferit Cubukcuoglu**

💎 **Email**: [ferit.cubukcuoglu@yazcub.com](mailto:ferit.cubukcuoglu@yazcub.com)\
🔗 **GitHub**: [github.com/fecub](https://github.com/fecub)
