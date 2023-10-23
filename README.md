# chDB vs. DuckDB benchmarks

This project benchmarks two simple queries against chDB and DuckDB. <br>
It runs the benchmarks as native queries against s3/cloud hosted parquet files. <br>
It runs all benchmark iterations in the same session and does not reset caches. <br>

_Warning: This is far from a rigorous benchmark._

## Results

**Benchmarks:**

```
chdb:version: avg=0.011s min=0.011s max=0.011s (2 runs)
chdb:count: avg=0.215s min=0.176s max=0.254s (2 runs)
chdb:groupby: avg=0.799s min=0.785s max=0.813s (2 runs)

duckdb:version: avg=0.000s min=0.000s max=0.000s (2 runs)
duckdb:count: avg=0.231s min=0.151s max=0.311s (2 runs)
duckdb:groupby: avg=0.920s min=0.811s max=1.029s (2 runs)
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
