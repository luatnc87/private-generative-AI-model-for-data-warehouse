import duckdb
from contextlib import contextmanager
from dataclasses import dataclass
from nsql.prompt_formatters import TableColumn, Table
from typing import Generator, List


@dataclass
class DuckDBConnector:
    """DuckDB connection."""
    database_path: str

    @contextmanager
    def connect(self) -> Generator[duckdb.DuckDBPyConnection, None, None]:
        """Yield a connection to a DuckDB db."""

        conn = None
        try:
            conn = duckdb.connect(database=self.database_path, read_only=True)
            yield conn
        finally:
            if conn != None: conn.close()

    def get_tables(self) -> List[str]:
        """Get all tables in the database."""

        with self.connect() as conn:
            sql_get_tables = f"SELECT DISTINCT table_name FROM duckdb_tables()"
            table_list = conn.sql(sql_get_tables).fetchall()
            table_names = []
            for table in table_list:
                table_names.append(table[0])

            return table_names

    def get_schema(self, table: str) -> Table:
        """Return Table."""

        with self.connect() as conn:
            columns = []
            sql_get_columns = f"SELECT DISTINCT column_name, data_type FROM duckdb_columns() WHERE table_name = '{table}'"
            column_list = conn.sql(sql_get_columns).fetchall()
            for col in column_list:
                columns.append(TableColumn(name=col[0], dtype=col[1]))

            return Table(name=table, columns=columns)
