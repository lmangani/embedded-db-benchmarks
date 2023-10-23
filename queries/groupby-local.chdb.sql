select
    toYYYYMMDD(tpep_pickup_datetime) as day,
    uniqHLL12(PULocationID) as locations,
    count(*) as trips,
    sum(fare_amount) + sum(mta_tax) + sum(tolls_amount) + sum(tip_amount) as revenue
from file('yellow_tripdata_2023-01.parquet', Parquet)
where trip_distance > 5
group by toYYYYMMDD(tpep_pickup_datetime)
order by day
