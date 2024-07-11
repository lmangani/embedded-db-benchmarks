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
- [datafusion](https://arrow.apache.org/datafusion-python/)


## Results

For the latest results, check the latest Action reports.


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
