with

source as (
    select * from {{source('MRData', 'RaceTable')}}
),

renamed as (
    select

        raceName as race_name,
        circuitId as circuit_id,
        circuitName as circuit_name,
        locality as city

)
