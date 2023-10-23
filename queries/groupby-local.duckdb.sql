select
    cast(tpep_pickup_datetime as date) as day,
    approx_count_distinct(PULocationID) as locations,
    count(*) as trips,
    sum(fare_amount) + sum(mta_tax) + sum(tolls_amount) + sum(tip_amount) as revenue
from read_parquet('yellow_tripdata_2023-01.parquet') 
where trip_distance > 5
group by cast(tpep_pickup_datetime as date)
order by day
