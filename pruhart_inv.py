# D777 Task 2: Data Solutions Implementation
# Alexis Canizal-Dominguez 013361604
import order_start
import graph
import processed_reporting

# User control flow 
while True:
    print("\nInventory Management System - Pruhart")
    print("1.   Add orders")
    print("2.   Inventory Reporting")
    print("3.   Routing")
    print("4.   Exit")

    choice = input("Choose an option: ")
    # this choice takes in orders and outputs a list for the warehousing employees to physically process
    if choice == "1":
        #read in the orders_in.csv to get incoming orders
        orders = order_start.order_in_read("orders_in.csv")
        
        #print the orders as a csv file 
        order_start.order_in_write(orders, "warehouse_output.csv")

    # the previous option has to be run first before any reporting can get printed
    # the worker has to manually add the missing entries on the warehouse_output.csv
    elif choice == "2":
        # adds the updated orders to the inventory.csv for reporting
        processed_reporting.order_inventory_append("warehouse_output.csv","inventory.csv") 

        # outputs a report of all entries in the inventory.csv
        processed_reporting.report_csv("inventory.csv" ) 

    # this choice allows the user to calculate the shortest path from two warehouses    
    elif choice == "3":
        # buildss graph
        warehouse_graph = graph.build_graph('route_table.csv')

        #calculates the shortest path between two warehouses
        distance, path = graph.shortest_path(warehouse_graph, 'dallas', 'houston')
        
        print(path)

    # exits control flow
    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid option.")