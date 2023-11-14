<<<<<<< HEAD
SELECT arrow_typeof(tpep_pickup_datetime::date) as day, 
       "PULocationID" as location, 
       count(*) as trips, 
       sum(fare_amount) + sum(mta_tax) + sum(tolls_amount) + sum(tip_amount) as revenue 
FROM 'yellow_tripdata_2023-01.parquet' 
=======
SELECT TO_DATE(tpep_pickup_datetime::date) as day, 
       PULocationID as location, 
       count(*) as trips, 
       sum(fare_amount) + sum(mta_tax) + sum(tolls_amount) + sum(tip_amount) as revenue 
FROM 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet' 
>>>>>>> 669ad86a96dfcc208bb27d08e44dfe51ee4c7fb9
WHERE trip_distance > 5 
GROUP BY tpep_pickup_datetime, location
ORDER BY day
