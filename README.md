<img src="https://github.com/lmangani/embedded-olap-benchmarks/assets/1423657/ba8f08fe-49db-4f77-a2b5-71181e87233e" width=350 />

# Embedded OLAP benchmarks

This project benchmarks embedded OLAP engines such as [chDB](https://chdb.dev) and [DuckDB](https://duckdb.org). <br>
Benchmark queries for supported databases are executed within Github Actions. <br>

:warning: _Focus on free, low-resource runners only. not a rigorous benchmark._

## Results

**Benchmarks:**

> [Github Action](https://github.com/lmangani/embedded-olap-benchmarks/actions/workflows/benchmarks.yml) Free Runner _(2x vCPU, 7GB RAM)_

<!-- START-RESULTS -->
```
Testing chdb 23.10.1.1
chdb:version: avg=0.012s min=0.011s max=0.014s (3 runs) | Memory used: -2.47 MB
chdb:count: avg=0.135s min=0.064s max=0.264s (3 runs) | Memory used: 3.91 MB
chdb:groupby: avg=0.435s min=0.407s max=0.478s (3 runs) | Memory used: 25.98 MB
chdb:groupby-local: avg=0.351s min=0.348s max=0.355s (3 runs) | Memory used: 6.99 MB

Testing duckdb 0.9.1
duckdb:version: avg=0.001s min=0.000s max=0.001s (3 runs) | Memory used: 2.96 MB
duckdb:count: avg=0.360s min=0.083s max=0.900s (3 runs) | Memory used: 26.02 MB
duckdb:groupby: avg=0.697s min=0.685s max=0.715s (3 runs) | Memory used: 25.86 MB
duckdb:groupby-local: avg=0.527s min=0.524s max=0.529s (3 runs) | Memory used: 0.62 MB

Testing glaredb: latest
glaredb:version: avg=0.001s min=0.000s max=0.001s (3 runs) | Memory used: 11.38 MB
glaredb:count: avg=0.157s min=0.071s max=0.307s (3 runs) | Memory used: 9.00 MB
glaredb:groupby: avg=0.489s min=0.482s max=0.496s (3 runs) | Memory used: 200.90 MB
glaredb:groupby-local: avg=0.363s min=0.353s max=0.378s (3 runs) | Memory used: 156.86 MB

```
<!-- END-RESULTS -->


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
