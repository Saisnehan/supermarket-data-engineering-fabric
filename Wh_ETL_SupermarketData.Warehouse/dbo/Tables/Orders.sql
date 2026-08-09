CREATE TABLE [dbo].[Orders] (

	[OrderID] bigint NULL, 
	[CustomerID] bigint NULL, 
	[StoreID] bigint NULL, 
	[OrderDate] datetime2(6) NULL, 
	[PaymentMethod] varchar(8000) NULL
);