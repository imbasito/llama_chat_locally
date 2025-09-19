import streamlit as st
from utils.ollama_api import query_ollama
import uuid

# --- Page config ---
st.set_page_config(
    page_title="Chat with Local LLM",
    page_icon="assets/live-chat.png",
    layout="centered"
)

# --- Initialize session state ---
if "conversations" not in st.session_state:
    st.session_state.conversations = {}  # {chat_id: {"name": str, "history": []}}
if "current_chat" not in st.session_state:
    chat_id = str(uuid.uuid4())
    st.session_state.current_chat = chat_id
    st.session_state.conversations[chat_id] = {"name": "Chat", "history": []}
if "model" not in st.session_state:
    st.session_state.model = "llama3.1:8b"

# --- Sidebar ---
with st.sidebar:
    st.header("Conversations")
    for cid, chat in st.session_state.conversations.items():
        if st.button(chat["name"], key=cid):
            st.session_state.current_chat = cid
            st.rerun()
    
    st.markdown("---")
    if st.button("+ New Chat"):
        new_id = str(uuid.uuid4())
        st.session_state.conversations[new_id] = {"name": "New Chat", "history": []}
        st.session_state.current_chat = new_id
        st.rerun()

    if st.button("Clear Chat"):
        st.session_state.conversations[st.session_state.current_chat]["history"] = []
        st.rerun()
    
    st.markdown("---")
    st.subheader("⚙️ Settings")
    model = st.selectbox("Choose model:", ["llama3.1:8b"], index=0)
    st.session_state.model = model
# --- Show title only when chat is empty ---
if len(chat["history"]) == 0:
    st.markdown("<h1 style='text-align:center; color:#2E7D32;'>Chat Locally</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666;'>Start the chat by typing below</p>", unsafe_allow_html=True)

# --- CSS Styling ---
st.markdown("""
<style>
.stApp { background-color: #0E1117; }

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #171c26;
} 
            
/* Buttons */
.stButton>button {
    background-color: #202633;
    color: white;
    border-radius: 8px;
    border: none;
}
.stButton>button:hover {
    background-color: #283040;
    color: white;
}

/* Chat bubbles */
.chat-box {
    background-color: #0E1117;
    max-height: 70vh;
    overflow-y: auto;
    padding: 12px;
    margin-bottom: 16px;
    border-radius: 8px;
}
.user-bubble {
    background-color: #1e2430;
    color: #FFFFFF;
    padding: 10px 14px;
    border-radius: 14px;
    margin: 8px 0 8px auto;
    max-width: fit-content;
    text-align: right;
    display: block;
}
.bot-bubble {
    background-color: #161a23;
    color: #F9FAFB;
    padding: 10px 14px;
    border-radius: 14px;
    margin: 8px 0 8px 0;
    max-width: fit-content;
    text-align: left;
    display: block;
}
</style>
""", unsafe_allow_html=True)

# --- Current Chat ---
chat = st.session_state.conversations[st.session_state.current_chat]

# --- Chat UI ---
st.markdown("<div class='chat-box' id='chat-box'>", unsafe_allow_html=True)
for turn in chat["history"]:
    if turn["role"] == "user":
        st.markdown(f"<div class='user-bubble'>{turn['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-bubble'>{turn['content']}</div>", unsafe_allow_html=True)
st.markdown("<div id='end-of-chat'></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Input ---
user_prompt = st.chat_input("Type your message...")

if user_prompt:
    # Append user message
    chat["history"].append({"role": "user", "content": user_prompt})

    # Auto-name chat from first user message
    if chat["name"] == "Chat":
        chat["name"] = user_prompt[:20]

    # Get reply (pass history list, not plain text)
    with st.spinner(user_prompt):
        try:
            reply = query_ollama(st.session_state.model, chat["history"])
        except Exception as e:
            reply = f"⚠️ Request failed: {e}"

    # Append assistant reply
    chat["history"].append({"role": "assistant", "content": reply})

  

    st.rerun()

# --- Auto-scroll ---
st.markdown(
    """
    <script>
    const end = document.getElementById('end-of-chat');
    if (end) {
      setTimeout(() => { end.scrollIntoView({behavior: 'smooth', block: 'end'}); }, 30);
    }

    
    </script>
    """,
    unsafe_allow_html=True,
)
