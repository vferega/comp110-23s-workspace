"""Define Pizza Class."""

class Pizza:

    #attributes
    size:str# "small" or "large"
    toppings: int
    gluten_free: bool 

    def_init_(self, size_input:str):
    self.size = size_input