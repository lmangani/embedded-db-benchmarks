import os
import sys
import psutil
from datetime import datetime
from contextlib import contextmanager

# Import Everything for equal memory conditions
import duckdb
import chdb
from chdb import session as chs
import glaredb
from databend import SessionContext

DBNAME = os.getenv('DBNAME', '*')
ITERATIONS = int(os.getenv('ITERATIONS', 3))
BENCHMARKS = ["version", "count", "groupby"]

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

def get_memory_usage():
    """ Returns the current memory usage of the Python process. """
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # Convert bytes to megabytes

def load_query(db: str, name: str) -> str:
    """ Load SQL query from file. """
    try:
        with open(f"queries/{name}.{db}.sql") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Query file for {name} not found.")
        sys.exit(1)

def benchmark_db(db: str, execute_fn):
    """ Benchmarks all queries against one datastore """
    for name in BENCHMARKS:
        query = load_query(db, name)
        deltas = []
        mem_usage_before = get_memory_usage()
        for _ in range(ITERATIONS):
            start = datetime.now()
            with suppress_stdout():
                try:
                    results = execute_fn(query)
                except Exception as e:
                    print(f"Error executing query on {db}: {e}")
                    continue
            end = datetime.now()
            deltas.append((end - start).total_seconds())
        mem_usage_after = get_memory_usage()

        if deltas:
            avg = sum(deltas) / len(deltas)
            mem_used = mem_usage_after - mem_usage_before
            print(f"{db}:{name}: avg={avg:.3f}s min={min(deltas):.3f}s max={max(deltas):.3f}s ({ITERATIONS} runs) | Memory used: {mem_used:.2f} MB")

def main():
    match DBNAME:
        case "chdb":
            print("Testing chdb " + str(chdb.engine_version))
            chdbs = chs.Session()
            benchmark_db("chdb", lambda query: chdb.query(query))
        case "duckdb":
            print("Testing duckdb " + str(duckdb.__version__))
            ddb = duckdb.connect()
            benchmark_db("duckdb", lambda query: ddb.execute(query))
        case "glaredb":
            print("Testing glaredb")
            gdb = glaredb.connect()
            benchmark_db("glaredb", lambda query: gdb.sql(query).show())
        case "databend":
            print("Testing databend")
            databendx = SessionContext()
            benchmark_db("databend", lambda query: databendx.sql(query).collect())
        case "datafusion":
            print("Testing datafusion")
            databendx = SessionContext()
            benchmark_db("datafusion", lambda query: databendx.sql(query).collect())

if __name__ == "__main__":
    main()
