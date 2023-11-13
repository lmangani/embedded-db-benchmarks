<img src="https://github.com/lmangani/embedded-olap-benchmarks/assets/1423657/ba8f08fe-49db-4f77-a2b5-71181e87233e" width=350 />

# Embedded OLAP benchmarks

This project benchmarks embedded OLAP engines such as [chDB](https://chdb.dev) and [DuckDB](https://duckdb.org). <br>
Benchmark queries for supported databases are executed within Github Actions. <br>

:warning: _Focus on free, low-resource runners only. not a rigorous benchmark._

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

glaredb:version: avg=0.001s min=0.000s max=0.002s (3 runs)
glaredb:count: avg=0.182s min=0.073s max=0.384s (3 runs)
glaredb:groupby: avg=0.783s min=0.772s max=0.799s (3 runs)
glaredb:groupby-local: avg=0.625s min=0.612s max=0.641s (3 runs)
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
