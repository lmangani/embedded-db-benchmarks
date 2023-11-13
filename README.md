<img src="https://github.com/lmangani/embedded-olap-benchmarks/assets/1423657/ba8f08fe-49db-4f77-a2b5-71181e87233e" width=350 />

# Embedded OLAP benchmarks

This project benchmarks embedded OLAP engines such as [chDB](https://chdb.dev) and [DuckDB](https://duckdb.org). <br>
Benchmark queries for supported databases are executed within Github Actions. <br>

:warning: _Focus on free, low-resource runners only. not a rigorous benchmark._

## Results

**Benchmarks:**

> [Github Action](https://github.com/lmangani/embedded-olap-benchmarks/actions/workflows/benchmarks.yml) Free Runner _(2x vCPU, 7GB RAM)_
```
chdb:version: avg=0.015s min=0.015s max=0.016s (3 runs)
chdb:count: avg=0.195s min=0.099s max=0.354s (3 runs)
chdb:groupby: avg=0.487s min=0.482s max=0.497s (3 runs)
chdb:groupby-local: avg=0.362s min=0.359s max=0.364s (3 runs)

duckdb:version: avg=0.000s min=0.000s max=0.000s (3 runs)
duckdb:count: avg=0.361s min=0.101s max=0.875s (3 runs)
duckdb:groupby: avg=0.619s min=0.560s max=0.722s (3 runs)
duckdb:groupby-local: avg=0.352s min=0.340s max=0.372s (3 runs)

glaredb:version: avg=0.001s min=0.000s max=0.002s (3 runs)
glaredb:count: avg=0.176s min=0.113s max=0.300s (3 runs)
glaredb:groupby: avg=0.905s min=0.866s max=0.949s (3 runs)
glaredb:groupby-local: avg=0.666s min=0.623s max=0.689s (3 runs)

```

## [Example Action Report](https://github.com/lmangani/embedded-olap-benchmarks/actions/workflows/benchmarks.yml)
![image](https://github.com/lmangani/embedded-db-benchmarks/assets/1423657/e5961b6e-9775-4f18-adde-edbb52b672f2)


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
