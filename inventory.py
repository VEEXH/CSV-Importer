import csv

class Inventory:
    def __init__(self, file_name):
        self.items = []
        self.file_name = file_name
        self.load_items_from_file()

    def load_items_from_file(self):
        # Open the CSV file for reading
        with open(self.file_name, 'r') as csv_file:
            reader = csv.reader(csv_file)

            # Load items from CSV file
            for row in reader:
                self.items.append({'name': row[0], 'quantity': int(row[1])})

    def update_item_quantity(self, item_name, new_quantity):
        # Find the item in the list
        for item in self.items:
            if item['name'] == item_name:
                item['quantity'] = new_quantity
                break

        # Write all items back to the CSV file
        with open(self.file_name, 'w') as csv_file:
            writer = csv.writer(csv_file)
            for item in self.items:
                writer.writerow([item['name'], item['quantity']])

    def restock_items(self, restock_threshold, target_quantity):
        for item in self.items:
            if item['quantity'] < restock_threshold:
                self.update_item_quantity(item['name'], target_quantity)

    def check_stock_levels(self, restock_threshold):
        out_of_stock_items = []
        for item in self.items:
            if item['quantity'] == 0:
                out_of_stock_items.append(item)
            elif item['quantity'] < restock_threshold:
                out_of_stock_items.append(item)
        return out_of_stock_items

def main():
    # Create an inventory instance
    inventory = Inventory('items.csv')

    # Set restock threshold and target quantity
    restock_threshold = 10
    target_quantity = 20

    # Check stock levels and restock items if necessary
    out_of_stock_items = inventory.check_stock_levels(restock_threshold)
    if out_of_stock_items:
        print('Out of stock items:')
        for item in out_of_stock_items:
            print(f' - {item["name"]}')
        print('Restocking items...')
        inventory.restock_items(restock_threshold, target_quantity)
        print('Done!')
    else:
        print('All items are in stock.')

if __name__ == '__main__':
    main()
