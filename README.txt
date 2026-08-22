README

Alexis Canizal-Dominguez
013361604
Python version - 3.14.6

Functions
Order_in_read(“orders_in.csv”)
	- Takes in a csv of a list of orders and adds to a queue. Then adds it to 
	a Dict, which is pythons hash table equivalent, that dict is used in the 	order_in_write() function. That function takes in the dict from the first function 
	and outputs a csv of orders that gets updated by the warehouse workers. 
Report_csv(“inventory.csv”) 
	- Reads in content from the inventory.csv and outputs it to the console. 
Order_inventory_append(“warehouse_output.csv”, “inventory.csv”)
	- Updates the inventory.csv by appending updated new orders from 	warehouse_output.csv.
Shortest_path(warehouse_graph, ‘dallas’, ‘houston’)
	-  Calculates the shortest path between two cities specified. It also takes in a 	graph that is created by build_graph() function, it reads in the route_table.csv 	and creates a graph. 

Running
There is a user control flow that is run from pruhart_inv.py. They can be run in any order only after going through the flow 1-3 for the first time. When running the following options are printed to the console: 
1.   Add orders		- runs order_in_read() and order_in_write
2.   Inventory Reporting 	-runs order_inventory_append() and report_csv()
3.   Routing	- runs build_graph() and shortest_path()
4.   Exit	- exits the flow
They have to run in order the first time because 2 depends on the warehouse_output.csv being written in 1. 

Error handling
Order_in_read(“orders_in.csv”)
	- Uses a try block with excepts to gracefully handle errors.
Report_csv(“inventory.csv”) 
	- Uses a try block with excepts to gracefully handle errors.
Order_inventory_append(“warehouse_output.csv”, “inventory.csv”)
	- Uses a try block with excepts to gracefully handle errors.
	- In the case of the file needed not existing, then creates one.
Shortest_path(warehouse_graph, ‘dallas’, ‘houston’)
	-  build_graph() uses a try block with excepts to gracefully handle errors when 	reading the route_table.csv. Making sure the graph used by shortest_path() error 	free. 
