Let's say these three questions came to you from the same coworker.
How would you design a dashboard that you could point them to?
How would you construct the underlying dataset?
How would you design your dashboard so that it can also be responsive to additional questions that were not explicitly asked by that coworker?

To refresh, the questions (dash does not necessarily need to cover all of them!) were
- Find the destinations that had the most number of guests 
- The % of total guests by state.
- Find the number of guests whose first booking was for Texas


CREATE TABLE bookings (
      id_booking     INT
    , id_listing     INT
    , id_host        INT
    , id_guest       INT
    , num_guests     INT
    , ds_checkin     STRING     # check-in date e.g. ‘2020-08-07’
    , ds_checkout    STRING     # check-out date e.g. ‘2020-08-10’
)
PARTITIONED BY (
    ds               STRING     # date booking was made, e.g. ‘2020-07-01’
)

CREATE TABLE dim_listings (
      id_listing            INT 
    , location_state        STRING # e.g. ‘Texas’
    , is_studio             INT 
    , is_private            INT 
)

-- 3. Find the number of guests whose first booking was for Texas.
with data as (
select b.id_listing
    , id_guests
    , b.num_guests
    , b.ds
    , dim.location_state
    , ROW_NUMBER() OVER (PARTITION BY id_guests ORDER BY b.ds) as book_order
from bookings b
join dim_listings dim
    on b.id_listing = dim.id_listing
),

select sum(num_guests)
from (
select *
from data
where book_order = 1
    and location_state = 'TX'
)



-- 2. Given the tables above. Write a query that gives the % of total guests by state.
with data as (
select b.id_listing
    , b.num_guests
    , dim.location_state
from bookings b
join dim_listings dim
    on b.id_listing = dim.id_listing
),

stat as (
select location_state
    , sum(num_guests) as total_guests
from data
group by location_state
),

overall as (
select sum(num_guests) as overall_guests
from data
)

select location_state
    , total_guests
    , total_guests/overall.overall_guest as percentage
from stat
cross join overall

-- 1. Given the tables above. Write a query that gives the top 5 states by number of guests
with data as (
select b.id_listing
    , b.num_guests
    , dim.location_state
from bookings b
join dim_listings dim
    on b.id_listing = dim.id_listing
),

stat as (
select location_state
    , sum(num_guests) as total_guests
from data
group by location_state
)

select *
from stat
order by total_guests desc
limit 5

