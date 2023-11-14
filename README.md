<img src="https://github.com/lmangani/embedded-olap-benchmarks/assets/1423657/ba8f08fe-49db-4f77-a2b5-71181e87233e" width=350 />

# Embedded OLAP benchmarks

This project benchmarks embedded OLAP engines using Python 3.x <br>
Benchmark queries for supported databases are executed within Github Actions. <br>

:warning: _Focus on free, low-resource runners. NOT intended as a rigorous benchmark!_

### OLAP Racers 🏁

- [chdb](https://doc.chdb.io)
- [duckdb](https://duckdb.org)
- [glaredb](https://glaredb.com)
- [databend](https://databend.com)



## Results

For the latest results, check the latest Action reports.

### [Example Action Report](https://github.com/lmangani/embedded-olap-benchmarks/actions/workflows/benchmarks.yml)

> [Github Action](https://github.com/lmangani/embedded-olap-benchmarks/actions/workflows/benchmarks.yml) Free Runner _(2x vCPU, 7GB RAM)_

<!-- START-RESULTS -->
```
Testing chdb 0.16.0rc2 (23.10.1.1)
chdb:version: avg=0.012s min=0.011s max=0.014s (3 runs) | Memory used: -2.47 MB
chdb:count: avg=0.135s min=0.064s max=0.264s (3 runs) | Memory used: 3.91 MB
chdb:groupby: avg=0.435s min=0.407s max=0.478s (3 runs) | Memory used: 25.98 MB

Testing duckdb 0.9.1
duckdb:version: avg=0.001s min=0.000s max=0.001s (3 runs) | Memory used: 2.96 MB
duckdb:count: avg=0.360s min=0.083s max=0.900s (3 runs) | Memory used: 26.02 MB
duckdb:groupby: avg=0.697s min=0.685s max=0.715s (3 runs) | Memory used: 25.86 MB

Testing glaredb 0.5.1
glaredb:version: avg=0.001s min=0.000s max=0.001s (3 runs) | Memory used: 11.38 MB
glaredb:count: avg=0.157s min=0.071s max=0.307s (3 runs) | Memory used: 9.00 MB
glaredb:groupby: avg=0.489s min=0.482s max=0.496s (3 runs) | Memory used: 200.90 MB

Testing databend 1.2.207
databend:version: avg=0.013s min=0.001s max=0.038s (3 runs) | Memory used: 3.50 MB
databend:count: avg=0.237s min=0.216s max=0.277s (3 runs) | Memory used: 7.50 MB
databend:groupby: avg=1.629s min=1.580s max=1.674s (3 runs) | Memory used: 462.03 MB
```
<!-- END-RESULTS -->


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
