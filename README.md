<img src="https://github.com/lmangani/embedded-olap-benchmarks/assets/1423657/ba8f08fe-49db-4f77-a2b5-71181e87233e" width=350 />

# Embedded OLAP benchmarks

This project benchmarks embedded OLAP engines such as chDB and DuckDB. <br>
It runs the benchmarks as native queries against local/cloud hosted datasets.. <br>
It runs all benchmark iterations in the same session and does not reset caches. <br>

_Warning: This is far from a rigorous benchmark._

## Results

**Benchmarks:**

> [Github Action](https://github.com/lmangani/embedded-olap-benchmarks/actions/workflows/benchmarks.yml) Free Runner _(2x vCPU, 7GB RAM)_
```
chdb:version: avg=0.018s min=0.017s max=0.020s (3 runs)
chdb:count: avg=0.312s min=0.210s max=0.502s (3 runs)
chdb:groupby: avg=0.772s min=0.742s max=0.824s (3 runs)
chdb:groupby-local: avg=0.436s min=0.432s max=0.441s (3 runs)

duckdb:version: avg=0.000s min=0.000s max=0.001s (3 runs)
duckdb:count: avg=0.358s min=0.120s max=0.823s (3 runs)
duckdb:groupby: avg=0.778s min=0.769s max=0.793s (3 runs)
duckdb:groupby-local: avg=0.498s min=0.494s max=0.505s (3 runs)

glaredb:version: avg=0.000s min=0.000s max=0.001s (3 runs)
glaredb:count: avg=0.166s min=0.152s max=0.178s (3 runs)
glaredb:groupby: avg=0.138s min=0.134s max=0.144s (3 runs)
glaredb:groupby-local: avg=0.002s min=0.001s max=0.003s (3 runs) 🔥
```

## Instructions

1. Clone this repo and `cd` into it

2. Install Test Requirements with `poetry`
```shell
poetry install
```

3. Run the benchmark
```shell
./run.sh
```
