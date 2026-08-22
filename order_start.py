
from collections import deque     
from pprint import pformat
from pathlib import Path
import csv

order_queue = deque()
orders = {} 
headers = [ "inventory_id",
                "order_id",
                "order_date",
                "status",
                "total_amt",
                "from_warehouse",
                "to_warehouse"        ]

# take in orders via csv read 
def order_in_read(orders_csv):
    try:
        with open(orders_csv, newline="", encoding="utf-8") as file: 
            reader = csv.DictReader(file)

            for row in reader:
                if not row["order_id"]:
                    continue
                order_queue.append(row)

    except FileNotFoundError:
        print(f"File '{orders_csv}' not found.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error: {e}")  

    # process orders via queue
    while order_queue:
        order = order_queue.popleft()

        order_id = int(order["order_id"])


        # save to a hash table(dict)
        orders[order_id] = {
            "customer_id": int(order["customer_id"]),
            "order_date": order["order_date"],
            "status": order["status"],
            "total_amount": float(order["total_amount"])
        }
    return orders
  
# function that outputs dict to csv 

def order_in_write(orders, output):
    headers = ["inventory_id"] + list(next(iter(orders.values())).keys()) + ["from_warehouse"] + ["to_warehouse"]

    # path for warehouse_output
    warehouse_ticket = Path(output)

    # if the path doesn't exist
    if not warehouse_ticket.exists():
        # create csv file                              
        with warehouse_ticket.open("w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
    
    # if it does - write to the file 
    with open(output, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(headers)

        for key, values in orders.items():
            writer.writerow([key] + list(values.values()))


def order_print(orders):
    with open("orders_in.txt", "w", encoding="utf-8") as file: 
        file.write(pformat(orders))


