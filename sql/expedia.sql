Count all live listings by customer Type and brand name with a created date in January 2015.​ 

With data as (
Select L.lisingID
	, B.brandName
	, C.customerType

From Listing L
Join Brand as B
 	On L.BrandID = B.BrandID
Join customer as C
	On L.customerID = C.customerID
Where L.LiveFlag = 1
	And L.createdDate >= ‘2015-01-01’
	And L.createDate <= ‘2015-01-31’
)

Select customerType
	, brandName
	count(*)
From data
Groupby 1,2

Count all customers without any live listings.​

With data as (
Select distinct customerID
From Listing L
Where L.LiveFlag = 1
)

Select customerID
From customer
left data
	customer.customerID = data.customerID
Where data.customerD is Null

              
Calculate Month over Month (for each month) BookingAmount performance for each PM customer in 2020

With data as (
Select L.lisingID
	
	, C.customerType
	, C.customerID
	, B.boookingAmount
	,case 
When year(boookingDate) = 2019 then 0
Else  month(bookingDate) #month of the date
End as month

From Listing L
Joni bookingFact B
	On L.listingID = B.listingID
Join customer as C
	On L.customerID = C.customerID
Where 	B.bookingDate >= ‘2019-12-01’
	And B.bookingDate <= ‘2020-12-31’
	C.cutomerType = ‘PM’
),

Bookingamount (
Select customerID
, month
	,sum(bookingAmount)

From data
Groupby customerID, month
)

Select B.cutomerID
	, B.month
	, B.amount - A.amount as diff_amount

From bookingamount A
Join bookingamount B
	On A.month +1  = B.month 


Sum all PageViews for 2015 by BrandName​
 With data as (
Select L.lisingID
	, B.brandName
	, A.PageViews

From Listing L
Join ListingActivitiyFact A
	On L.ListingID = A.ListingID
Join Brand as B
 	On L.BrandID = B.BrandID

Where 	B.dateID >= ‘2015-01-01’
	And B.dateID <= ‘2015-12-31’

),

Select brandname
, sum(pageViews)
From data
Groupby brandname

	
Count Number of Bookings by Stay Length (i.e. CheckoutDate-CheckInDate) booked in  2015 ​



Count displayed (i.e. dateID between created date and expiration date)  listings for each day in 2015


