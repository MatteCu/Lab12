from dataclasses import dataclass


@dataclass
class SoldByRetailer:
    Retailer_ID: int
    Product_N:int
    def __hash__(self):
        return hash(self.Retailer_ID + self.Product_N)