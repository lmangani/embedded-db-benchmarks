from contextlib import contextmanager
import os
import sys
from datetime import datetime
import duckdb
import chdb
from chdb import session as chs
import glaredb

DBNAME = os.environ['DBNAME'] or '*'

# Number of times to benchmark each query
ITERATIONS = os.environ['ITERATIONS'] or 3
ITERATIONS = int(ITERATIONS)

# Names of queries to load from the "./queries/" folder
BENCHMARKS = ["version", "count", "groupby", "groupby-local"]

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

def benchmark_db(db, execute_fn):
    """ Benchmarks all queries against one datastore """
    for name in BENCHMARKS:
        # Load query
        with open(f"queries/{name}.{db}.sql") as f:
            query = f.read()
        
        # Run benchmark and track query durations
        deltas = []
        for _ in range(ITERATIONS):
            start = datetime.now()
            with suppress_stdout():
                results = execute_fn(query)
            end = datetime.now()
            deltas.append((end - start).total_seconds())

        # Print result
        avg = sum(deltas) / len(deltas)
        print("{}:{}: avg={:.3f}s min={:.3f}s max={:.3f}s ({} runs)".format(
            db,
            name,
            avg,
            min(deltas),
            max(deltas),
            ITERATIONS,
        ))

def main():
    match DBNAME:
        case "chdb":
            print("Testing chdb")
            chdbs = chs.Session()
            benchmark_db("chdb", lambda query: chdb.query(query))
        case "duckdb":
            print("Testing duckdb")
            ddb = duckdb.connect()
            benchmark_db("duckdb", lambda query: ddb.execute(query))
        case "glaredb":
            print("Testing glaredb")
            gdb = glaredb.connect()
            benchmark_db("glaredb", lambda query: gdb.sql(query).show())
        case _:
            print("Testing all databases.")
            chdbs = chs.Session()
            benchmark_db("chdb", lambda query: chdb.query(query))
            ddb = duckdb.connect()
            benchmark_db("duckdb", lambda query: ddb.execute(query))
            gdb = glaredb.connect()
            benchmark_db("glaredb", lambda query: gdb.sql(query).show())

if __name__ == "__main__":
    main()
