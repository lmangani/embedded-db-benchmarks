select
    toYYYYMMDD(tpep_pickup_datetime) as day,
    uniqHLL12(PULocationID) as locations,
    count(*) as trips,
    sum(fare_amount) + sum(mta_tax) + sum(tolls_amount) + sum(tip_amount) as revenue
from url('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet')
where trip_distance > 5
group by toYYYYMMDD(tpep_pickup_datetime)
order by day
