
# billing_service.py
class BillingService:
    def __init__(self):
        self.billing_records = []

    def add_billing(self, amount, description):
        self.billing_records.append({"amount": amount, "description": description})

    def remove_billing(self, index):
        if index < 0 or index >= len(self.billing_records):
            raise IndexError("Invalid index")
        del self.billing_records[index]

    def update_billing(self, index, new_amount=None, new_description=None):
        if index < 0 or index >= len(self.billing_records):
            raise IndexError("Invalid index")
        if new_amount:
            self.billing_records[index]["amount"] = new_amount
        if new_description:
            self.billing_records[index]["description"] = new_description
