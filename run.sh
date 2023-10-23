#!/bin/bash

if ! test -f ./yellow_tripdata_2023-01.parquet; then
  wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet

fi

poetry run python3 benchmark.py
