"""
Write a Python program to generate tickets for online bus booking.

validate_source_destination(): Validate source and destination. source must always be Delhi and destination can be either Mumbai, Chennai, Pune or Kolkata. 
If both are valid, return true. Else return false

generate_ticket():
Validate source and destination
If valid, generate ticket id and assign it to attribute, ticket_id.Ticket id should be generated with the first letter of source followed by first letter of destination and an auto-generated value starting from 01 (Ex: DM01, DP02,.. ,DK10,DC11)
Else, set ticket_id as None
"""

#!/usr/bin/python3


class Ticket:
    counter = 0
    def __init__(self, passenger_name, source, destination):
        self.__passenger_name=passenger_name
        self.__source=source
        self.__destination=destination
        self.__ticket_id=None
        
    def get_passenger_name(self):
        return self.__passenger_name
    def get_ticket_id(self):
        self.__ticket_id
    def get_source(self):
        self.__source
    def get_destination(self):
        if self.__destination=="Pune":
            return self.__destination
        elif self.__destination=="Mumbai":
            return self.__destination
        elif self.__destination=="Chennai":
            return self.__destination
        elif self.__destination=="Kolkata":
            return self.__destination

        else:
            return None
        
    def set_passenger_name(self, passenger_name):
        self.__passenger_name = passenger_name
    def set_ticket_id(self, ticket_id):
        self.__ticket_id = ticket_id
    def set_source(self, source):
        self.__source = source
    def set_destination(self, destination):
        self.__destination = destination
    
    def validate_source_destination(self):
        
        if self.__source.upper()=="DELHI" and (self.__destination.upper()=="PUNE" or self.__destination.upper()=="MUMBAI" or self.__destination.upper()=="CHENNAI" or self.__destination=="KOLKATA"): 
            return True
        else:
            return False
        
        
    def generate_ticket(self):
        if self.validate_source_destination() == "True":
            self.__ticket_id = self.__source[0].upper() + self.__destination[0].upper() + str(Ticket.counter)
            Ticket.counter += 1 
            return self.__ticket_id
        
    
        
t=Ticket("abd", "Delhi", "Kolkata")
t.set_source("Delhi")
t.set_destination("Pune")
print(t.validate_source_destination())
