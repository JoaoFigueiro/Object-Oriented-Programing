"""
## Objectives
    - creating classes, methods, and variables;
    - calling methods;
    - getting simple access to instance variables;


## Scenario
    create a class representing a mobile phone;
    
    - your class should implement the following methods:
    __init__ expects a number to be passed as an argument; this 
    method stores the number in an instance variable self.number
    
    - turn_on() should return the message 'mobile phone {number} 
    is turned on'. Curly brackets are used to mark the place to 
    insert the object's number variable;

    - turn_off() should return the message 'mobile phone is turned off';
    call(number) should return the message 'calling {number}'. Curly 
    brackets are used to mark the place to insert the object's number 
    variable;

    - create two objects representing two different mobile phones; 
    assign any random phone numbers to them; 
    
    - implement a sequence of method calls on the objects to turn them 
    on, call any number. 
    
    - Print the methods' outcomes;
    - turn off both mobiles.

"""

class MobilePhone(): 
    def __init__(self, number):
        self.number = number

    def turn_on(self): 
        print(f"Mobile phone {self.number} is turned on.") 

    def turn_off(self): 
        print(f"Mobile phone {self.number} is turned off.") 

    def call(self, number): 
        print(f"Calling {number}")

phone1 = MobilePhone('01632-960004')
phone2 = MobilePhone('01632-960012')

phone1.turn_on()
phone2.turn_on()

phone1.call('555-34343')

phone1.turn_off()
phone2.turn_off()
