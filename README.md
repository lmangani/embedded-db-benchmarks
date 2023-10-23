<img src="https://avatars.githubusercontent.com/u/132536224?s=200&v=4" />

# chDB vs. DuckDB benchmarks

This project benchmarks two simple queries against chDB and DuckDB. <br>
It runs the benchmarks as native queries against local/cloud hosted datasets.. <br>
It runs all benchmark iterations in the same session and does not reset caches. <br>

_Warning: This is far from a rigorous benchmark._

## Results

**Benchmarks:**

```
chdb:version: avg=0.016s min=0.015s max=0.017s (3 runs)
chdb:count: avg=0.278s min=0.154s max=0.459s (3 runs)
chdb:groupby: avg=0.705s min=0.678s max=0.746s (3 runs)
chdb:groupby-local: avg=0.376s min=0.373s max=0.380s (3 runs)

duckdb:version: avg=0.000s min=0.000s max=0.001s (3 runs)
duckdb:count: avg=0.361s min=0.113s max=0.855s (3 runs)
duckdb:groupby: avg=0.727s min=0.724s max=0.731s (3 runs)
duckdb:groupby-local: avg=0.468s min=0.464s max=0.474s (3 runs)
```

## Instructions

1. Clone this repo and `cd` into it

2. Install Requirements
```shell
pip3 install -r requirements.txt
```

3. Run the benchmark

```shell
./run.sh
```
