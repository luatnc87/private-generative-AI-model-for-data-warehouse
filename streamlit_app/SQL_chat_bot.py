from nsql.db_connector import DuckDBConnector
from nsql.prompt_formatters import RajkumarFormatter
from manifest import Manifest
import streamlit as st

with st.sidebar:
    duckdb_database_path = st.text_input("DuckDB Database Path:", placeholder="path/to/database.db", key="duckdb_database_path")
    duckdb_schema = st.text_input("DuckDB Database Schema:", placeholder="main", key="duckdb_database_schema")
    "[Get example here](https://duckdb.org/docs/api/python/overview)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"

st.title("💬 SQL Chatbot")
st.caption("🚀 A streamlit chatbot powered by NSQL")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Please, input your database and schema!"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Load schema
@st.cache_resource(ttl="2h")
def load_db():
    db_conn = DuckDBConnector(
        database_path=duckdb_database_path
    )
    db_conn.connect()
    # Load schema
    tables = []
    tables.extend(db_conn.get_tables())

    msg_content = f"Loading tables: {tables}"
    st.session_state.messages.append({"role": "assistant", "content": msg_content})
    st.chat_message("assistant").write(msg_content)
    return db_conn, tables

# Get the connector and formatter
if st.sidebar.button("Load schema", type="primary"):
    if (not duckdb_database_path) or (not duckdb_schema):
        st.info("Please add your DuckDB database or/ and schema to continue.")
        st.stop()

    st.session_state.db_cnn, tables = load_db()
    db_schema = [st.session_state.db_cnn.get_schema(table) for table in tables]
    st.session_state.formatter = RajkumarFormatter(db_schema)

# Connect to model server
manifest_client = Manifest(client_name="huggingface", client_connection="http://127.0.0.1:5000")

def ask_bot(instruction: str, max_tokens: int = 300) -> str:
    prompt = st.session_state.formatter.format_prompt(instruction)
    res = manifest_client.run(prompt, max_tokens=max_tokens)
    return st.session_state.formatter.format_model_output(res)

if prompt := st.chat_input():
    if (not duckdb_database_path) or (not duckdb_schema):
        st.info("Please add your DuckDB database or/ and schema to continue.")
        st.stop()

    # append user's message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    # ask the assistant
    response = ask_bot(prompt)
    # append assistant's message
    df = st.session_state.db_cnn.run_sql(response)
    msg_content  = f"{response}"
    st.session_state.messages.append({"role": "assistant", "content": msg_content})
    st.chat_message("assistant").write(msg_content)
    st.dataframe(df)