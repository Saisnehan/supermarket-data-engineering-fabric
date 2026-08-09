[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "Customers csv_DataDestination", IsNewTarget = true], Settings = [Kind = "Manual", AllowCreation = true, ColumnSettings = [Mappings = {[SourceColumnName = "CustomerID", DestinationColumnName = "CustomerID"], [SourceColumnName = "FirstName", DestinationColumnName = "FirstName"], [SourceColumnName = "LastName", DestinationColumnName = "LastName"], [SourceColumnName = "City", DestinationColumnName = "City"], [SourceColumnName = "Gender", DestinationColumnName = "Gender"]}], DynamicSchema = false, UpdateMethod = [Kind = "Replace"], TypeSettings = [Kind = "Table"]]]}]
shared #"Customers csv" = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "759aa60a-f2cd-4b13-af28-a56c44ed485a"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "820fef14-d0a3-4589-90bf-9c140a159cac"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "Files", ItemKind = "Folder"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[Name = "Supermarket_sales_data"]}[Content],
  #"Navigation 4" = #"Navigation 3"{[Name = "Customers.csv"]}[Content],
  #"Imported CSV" = Csv.Document(#"Navigation 4", [Delimiter = ",", Columns = 5, Encoding = 65001, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(#"Imported CSV", [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"CustomerID", Int64.Type}, {"FirstName", type text}, {"LastName", type text}, {"City", type text}, {"Gender", type text}}),
  #"Replaced value" = Table.ReplaceValue(#"Changed column type", "", "unknown", Replacer.ReplaceValue, {"FirstName"}),
  #"Removed duplicates" = Table.Distinct(#"Replaced value", {"CustomerID"}),
  #"Replaced value 1" = Table.ReplaceValue(#"Removed duplicates", "", "unknown", Replacer.ReplaceValue, {"LastName"}),
  #"Filtered rows" = Table.SelectRows(#"Replaced value 1", each ([City] <> "") and ([Gender] <> ""))
in
  #"Filtered rows";
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "OrderDetails csv_DataDestination", IsNewTarget = true], Settings = [Kind = "Manual", AllowCreation = true, ColumnSettings = [Mappings = {[SourceColumnName = "OrderDetailID", DestinationColumnName = "OrderDetailID"], [SourceColumnName = "OrderID", DestinationColumnName = "OrderID"], [SourceColumnName = "ProductID", DestinationColumnName = "ProductID"], [SourceColumnName = "Quantity", DestinationColumnName = "Quantity"], [SourceColumnName = "Discount", DestinationColumnName = "Discount"]}], DynamicSchema = false, UpdateMethod = [Kind = "Replace"], TypeSettings = [Kind = "Table"]]]}]
shared #"OrderDetails csv" = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "759aa60a-f2cd-4b13-af28-a56c44ed485a"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "820fef14-d0a3-4589-90bf-9c140a159cac"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "Files", ItemKind = "Folder"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[Name = "Supermarket_sales_data"]}[Content],
  #"Navigation 4" = #"Navigation 3"{[Name = "OrderDetails.csv"]}[Content],
  #"Imported CSV" = Csv.Document(#"Navigation 4", [Delimiter = ",", Columns = 5, Encoding = 65001, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(#"Imported CSV", [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"OrderDetailID", Int64.Type}, {"OrderID", Int64.Type}, {"ProductID", Int64.Type}, {"Quantity", Int64.Type}, {"Discount", Int64.Type}}),
  #"Removed duplicates" = Table.Distinct(#"Changed column type", {"OrderDetailID"}),
  #"Filtered rows" = Table.SelectRows(#"Removed duplicates", each ([Quantity] <> null and [Quantity] <> -2 and [Quantity] <> 0) and ([ProductID] <> null) and ([Discount] <> null))
in
  #"Filtered rows";
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "Orders csv_DataDestination", IsNewTarget = true], Settings = [Kind = "Manual", AllowCreation = true, ColumnSettings = [Mappings = {[SourceColumnName = "OrderID", DestinationColumnName = "OrderID"], [SourceColumnName = "CustomerID", DestinationColumnName = "CustomerID"], [SourceColumnName = "StoreID", DestinationColumnName = "StoreID"], [SourceColumnName = "OrderDate", DestinationColumnName = "OrderDate"], [SourceColumnName = "PaymentMethod", DestinationColumnName = "PaymentMethod"]}], DynamicSchema = false, UpdateMethod = [Kind = "Replace"], TypeSettings = [Kind = "Table"]]]}]
shared #"Orders csv" = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "759aa60a-f2cd-4b13-af28-a56c44ed485a"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "820fef14-d0a3-4589-90bf-9c140a159cac"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "Files", ItemKind = "Folder"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[Name = "Supermarket_sales_data"]}[Content],
  #"Navigation 4" = #"Navigation 3"{[Name = "Orders.csv"]}[Content],
  #"Imported CSV" = Csv.Document(#"Navigation 4", [Delimiter = ",", Columns = 5, Encoding = 65001, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(#"Imported CSV", [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"OrderID", Int64.Type}, {"CustomerID", Int64.Type}, {"StoreID", Int64.Type}, {"OrderDate", type datetime}, {"PaymentMethod", type text}}),
  #"Removed duplicates" = Table.Distinct(#"Changed column type", {"OrderID"}),
  #"Filtered rows" = Table.SelectRows(#"Removed duplicates", each ([CustomerID] <> null) and ([OrderDate] <> null) and ([PaymentMethod] <> ""))
in
  #"Filtered rows";
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "Products csv_DataDestination", IsNewTarget = true], Settings = [Kind = "Manual", AllowCreation = true, ColumnSettings = [Mappings = {[SourceColumnName = "ProductID", DestinationColumnName = "ProductID"], [SourceColumnName = "ProductName", DestinationColumnName = "ProductName"], [SourceColumnName = "Category", DestinationColumnName = "Category"], [SourceColumnName = "Price", DestinationColumnName = "Price"], [SourceColumnName = "StockQty", DestinationColumnName = "StockQty"]}], DynamicSchema = false, UpdateMethod = [Kind = "Replace"], TypeSettings = [Kind = "Table"]]]}]
shared #"Products csv" = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "759aa60a-f2cd-4b13-af28-a56c44ed485a"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "820fef14-d0a3-4589-90bf-9c140a159cac"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "Files", ItemKind = "Folder"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[Name = "Supermarket_sales_data"]}[Content],
  #"Navigation 4" = #"Navigation 3"{[Name = "Products.csv"]}[Content],
  #"Imported CSV" = Csv.Document(#"Navigation 4", [Delimiter = ",", Columns = 5, Encoding = 65001, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(#"Imported CSV", [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"ProductID", Int64.Type}, {"ProductName", type text}, {"Category", type text}, {"Price", Int64.Type}, {"StockQty", Int64.Type}}),
  #"Removed duplicates" = Table.Distinct(#"Changed column type", {"ProductID"}),
  #"Filtered rows" = Table.SelectRows(#"Removed duplicates", each ([ProductName] <> "") and ([Category] <> "") and ([Price] <> null))
in
  #"Filtered rows";
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "Stores csv_DataDestination", IsNewTarget = true], Settings = [Kind = "Manual", AllowCreation = true, ColumnSettings = [Mappings = {[SourceColumnName = "StoreID", DestinationColumnName = "StoreID"], [SourceColumnName = "StoreName", DestinationColumnName = "StoreName"], [SourceColumnName = "City", DestinationColumnName = "City"], [SourceColumnName = "StoreType", DestinationColumnName = "StoreType"]}], DynamicSchema = false, UpdateMethod = [Kind = "Replace"], TypeSettings = [Kind = "Table"]]]}]
shared #"Stores csv" = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "759aa60a-f2cd-4b13-af28-a56c44ed485a"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "820fef14-d0a3-4589-90bf-9c140a159cac"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "Files", ItemKind = "Folder"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[Name = "Supermarket_sales_data"]}[Content],
  #"Navigation 4" = #"Navigation 3"{[Name = "Stores.csv"]}[Content],
  #"Imported CSV" = Csv.Document(#"Navigation 4", [Delimiter = ",", Columns = 4, Encoding = 65001, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(#"Imported CSV", [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"StoreID", Int64.Type}, {"StoreName", type text}, {"City", type text}, {"StoreType", type text}}),
  #"Removed duplicates" = Table.Distinct(#"Changed column type", {"StoreID"}),
  #"Filtered rows" = Table.SelectRows(#"Removed duplicates", each ([StoreName] <> "") and ([City] <> "") and ([StoreType] <> ""))
in
  #"Filtered rows";
shared #"Customers csv_DataDestination" = let
  Pattern = Fabric.Warehouse([CreateNavigationProperties = false, HierarchicalNavigation = true]),
  Navigation_1 = Pattern{[workspaceId = "759aa60a-f2cd-4b13-af28-a56c44ed485a"]}[Data],
  Navigation_2 = Navigation_1{[warehouseId = "354979ba-2d47-4507-914d-7d1f6faf0351"]}[Data],
  Navigation_3 = Navigation_2{[Schema = "dbo"]}[Data],
  TableNavigation = Navigation_3{[Name = "Customers"]}?[Data]?
in
  TableNavigation;
shared #"OrderDetails csv_DataDestination" = let
  Pattern = Fabric.Warehouse([CreateNavigationProperties = false, HierarchicalNavigation = true]),
  Navigation_1 = Pattern{[workspaceId = "759aa60a-f2cd-4b13-af28-a56c44ed485a"]}[Data],
  Navigation_2 = Navigation_1{[warehouseId = "354979ba-2d47-4507-914d-7d1f6faf0351"]}[Data],
  Navigation_3 = Navigation_2{[Schema = "dbo"]}[Data],
  TableNavigation = Navigation_3{[Name = "OrderDetails"]}?[Data]?
in
  TableNavigation;
shared #"Products csv_DataDestination" = let
  Pattern = Fabric.Warehouse([CreateNavigationProperties = false, HierarchicalNavigation = true]),
  Navigation_1 = Pattern{[workspaceId = "759aa60a-f2cd-4b13-af28-a56c44ed485a"]}[Data],
  Navigation_2 = Navigation_1{[warehouseId = "354979ba-2d47-4507-914d-7d1f6faf0351"]}[Data],
  Navigation_3 = Navigation_2{[Schema = "dbo"]}[Data],
  TableNavigation = Navigation_3{[Name = "Products"]}?[Data]?
in
  TableNavigation;
shared #"Stores csv_DataDestination" = let
  Pattern = Fabric.Warehouse([CreateNavigationProperties = false, HierarchicalNavigation = true]),
  Navigation_1 = Pattern{[workspaceId = "759aa60a-f2cd-4b13-af28-a56c44ed485a"]}[Data],
  Navigation_2 = Navigation_1{[warehouseId = "354979ba-2d47-4507-914d-7d1f6faf0351"]}[Data],
  Navigation_3 = Navigation_2{[Schema = "dbo"]}[Data],
  TableNavigation = Navigation_3{[Name = "Stores"]}?[Data]?
in
  TableNavigation;
shared #"Orders csv_DataDestination" = let
  Pattern = Fabric.Warehouse([CreateNavigationProperties = false, HierarchicalNavigation = true]),
  Navigation_1 = Pattern{[workspaceId = "759aa60a-f2cd-4b13-af28-a56c44ed485a"]}[Data],
  Navigation_2 = Navigation_1{[warehouseId = "354979ba-2d47-4507-914d-7d1f6faf0351"]}[Data],
  Navigation_3 = Navigation_2{[Schema = "dbo"]}[Data],
  TableNavigation = Navigation_3{[Name = "Orders"]}?[Data]?
in
  TableNavigation;
