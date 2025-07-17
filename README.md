# 🧠 Ask Siren – FAQ Chatbot Interface

A simple Streamlit-based chatbot interface that allows users to ask questions based on Siren Craft Brew's FAQs. The frontend interacts with a backend API that handles retrieval and response generation.

---

## 🚀 Features

- Streamlit-powered chatbot interface
- Maintains conversation history during the session
- Sends user queries to a REST API (`/ask`) and displays intelligent answers
- Environment-variable-based configuration for secure API access

---

## 📦 Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io)
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 🛠️ Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ask-siren.git
   cd ask-siren
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root and add your backend API URL:

   ```
   SIREN_BOT_URL=https://your-api-endpoint.com
   ```

5. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

---

## 💬 How It Works

- The app starts with a chatbot-like interface using `st.chat_input` and `st.chat_message`.
- When a user enters a query, it:
  - Adds the message to the session state
  - Sends it as a POST request to the backend at `/ask`
  - Displays the assistant’s response in the interface

---

## 🔐 Security

- API URLs are managed via environment variables to keep sensitive data out of the codebase.
- Error handling ensures the UI doesn’t break if the API call fails.

---

## 📁 File Structure

```
.
├── app.py              # Main Streamlit app
├── .env                # Stores the SIREN_BOT_URL
├── requirements.txt    # Required dependencies
└── README.md           # Project documentation
```

---

## ✨ Example Usage

> **User:** _"What are your delivery hours?"_  
> **Siren:** _"We deliver between 10 AM to 6 PM from Monday to Saturday."_

---

## 📜 License

MIT License
