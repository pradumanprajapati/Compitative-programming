class Ship:
    def __init__(self,customer_list):
        self.customer_list=customer_list
    def calculate_total_charge(self):
        total_charge=0.0
        for customer in self.customer_list:
            total_charge+=customer.calculate_final_charge()
        return  total_charge
class Cargo:
    cargo_charges=20000
    def __init__(self,cargo_id,cargo_weight):
        self.cargo_id=cargo_id
        self.cargo_weight=cargo_weight
    def calculate_total_amount(self):
        if self.cargo_weight>85:
            tax=Cargo.cargo_charges*0.2
        else:
            tax=Cargo.cargo_charges*0.1
            return Cargo.cargo_charges+tax
class Customer:
    def __init__(self,customer_id, customer_name):
        self.customer_id=customer_id
        self.customer_name=customer_name
        self.travel_cost =40000
    def identify_cargo_shipment_cost(self,cargo):
        cargo_charges=cargo.calculate_total_amount()
        self.travel_cost+=cargo_charges
    def calculate_final_charge(self):
        travel_tax=0.0
        if self.travel_cost>62000:
            travel_tax=self.travel_cost*0.2
        else:
            travel_tax=self.travel_cost*0.1
        return self.travel_cost+travel_tax
cargo_obj1=Cargo("C1001",90)
cargo_obj2=Cargo("C1002",78)
customer_obj1=Customer(101,"James")
customer_obj2=Customer(102,"Ronald")
customer_obj3=Customer(103,"Andrew")
customer_obj4=Customer(104,"Watson")
customer_list1=[customer_obj1,customer_obj2]
customer_list2=[customer_obj3,customer_obj4]
ship_obj1=Ship(customer_list1)
ship_obj2=Ship(customer_list2)
customer_obj1.identify_cargo_shipment_cost(cargo_obj1)
customer_obj3.identify_cargo_shipment_cost(cargo_obj2)
print(ship_obj1.calculate_total_charge())
print(ship_obj2.calculate_total_charge())
