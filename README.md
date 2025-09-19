# Chat Locally

An interactive **Streamlit web app** that connects to a **locally installed Large Language Model (LLM)** running via **Ollama**.  
Features a **ChatGPT-like UI**, conversation history, model selection, and reset functionality.  

---

## 🚀 Features
- 📝 User-friendly Streamlit interface
- 💬 Chat-like conversation history
- 🔄 Reset conversation button
- 🎛️ Model selection (choose from installed Ollama models)
- ⚡ Connects seamlessly with **local Ollama LLM**

---

## 📂 Project Structure
```
📂 local-llm-streamlit-ollama
┣ 📂 utils
┃ ┗ 📜 ollama_api.py
┣ 📂 assets
┃ ┗ 📜 live-chat.png
┣ 📜 app.py
┣ 📜 requirements.txt
┣ 📜 README.md
┗ 📜 Local_LLM_Streamlit_Ollama_Report_v1.pdf
```

---

## 🛠 Installation & Usage
1. Clone this repo or download the files:
   ```bash
   git clone https://github.com/<your-username>/local-llm-streamlit-ollama.git
   cd local-llm-streamlit-ollama
   ```
### 👉 Install Ollama
https://ollama.com/
Please make sure you download the model based on the resources available on your machine. (I used llama3.1:8b)

### Install dependencies:

   ``` pip install -r requirements.txt
Ensure Ollama is installed and running locally:
   ```
### Run the app:
```
streamlit run app.py
```

### Open in browser:
```
http://localhost:8501
```

A detailed project report is included:
Local_LLM_Streamlit_Ollama_Report_v1.pdf


## 🧑‍💻 Author  
Abdul Basit Khan  
[LinkedIn](https://www.linkedin.com/in/imbasito/) | [GitHub](https://github.com/imbasito)


