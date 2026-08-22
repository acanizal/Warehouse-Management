import csv
from pprint import pformat
from collections import deque 
from pathlib import Path

inventory_queue = deque()
inventory = {}
headers = [ "inventory_id",
                "order_id",
                "order_date",
                "status",
                "total_amt",
                "from_warehouse",
                "to_warehouse"        ]


#reads warehouse_output.csv and adds to inventory csv
def order_inventory_append(source_file, dest_file):

    source = Path(source_file)
    dest = Path(dest_file)
    try:
    # opens source file and appends contents to inventory.csv
        with source.open("r", encoding="utf-8-sig", newline="") as src:

            reader = csv.reader(src)
            next(reader,None)
            # checks if there is a inventory.csv
            if not dest.exists():

                # creates inventory.csv - if not
                with dest.open("w", encoding="utf-8", newline="") as destination:
                    writer = csv.writer(destination)
                    writer.writerow(headers)

            # 
            with dest.open("a", encoding="utf-8", newline="") as destination:
                writer = csv.writer(destination)


            for row in reader:
                    writer.writerow(row)
    except Exception as e:
        print(f"Unexpected error: {e}")  
   
# reporting function - all entries

def report_csv(filename, columns=None):
    
    try:
        # open inventory.csv
        with open(filename, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            # Print all columns if none are specified
            if columns is None:
                columns = reader.fieldnames

            # Print header
            print(" | ".join(columns))
            print("-" * (len(" | ".join(columns))))

            # Print selected columns
            for row in reader:
                values = [str(row.get(col, "") or "") for col in columns]
                print(" | ".join(values))

    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

