from nsql.db_connector import DuckDBConnector
from nsql.prompt_formatters import RajkumarFormatter
from manifest import Manifest


DATABASE = "/data/duckdb/adventureworks_dwh.duckdb"
TABLES = []  # list of tables to load or [] to load all tables

# Get the connector and formatter
duckdb_connector = DuckDBConnector(
    database_path=DATABASE
)
duckdb_connector.connect()

# Load schema
if len(TABLES) <= 0:
    TABLES.extend(duckdb_connector.get_tables())
print(f"Loading tables: {TABLES}")

db_schema = [duckdb_connector.get_schema(table) for table in TABLES]
formatter = RajkumarFormatter(db_schema)

# Connect to model server
manifest_client = Manifest(client_name="huggingface", client_connection="http://127.0.0.1:5000")

def ask_bot(instruction: str, max_tokens: int = 300) -> str:
    prompt = formatter.format_prompt(instruction)
    res = manifest_client.run(prompt, max_tokens=max_tokens)
    return formatter.format_model_output(res)


# Chat with SQL-bot
ask = f"Number of rows in {TABLES[0]} table?"
print(f"Ask: {ask}")
response_sql = ask_bot(ask)
print(f"Answer: {response_sql}")
df = duckdb_connector.run_sql(response_sql)
print(f"{df.to_string()}")