from datetime import datetime
import duckdb
import chdb
from chdb import session as chs

# Number of times to benchmark each query
ITERATIONS = 2

# Names of queries to load from the "./queries/" folder
BENCHMARKS = ["version", "count", "groupby"]


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
            execute_fn(query)
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
    chdbs = chs.Session()
    benchmark_db("chdb", lambda query: chdb.query(query))

    ddb = duckdb.connect()
    benchmark_db("duckdb", lambda query: ddb.execute(query))

if __name__ == "__main__":
    main()
