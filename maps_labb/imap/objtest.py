class Term:

    # At this indentation level we define the "methods" of a class
    def __init__(self, value):
        self.value = value

    # Every method of a class needs to have at least 1
    # parameter to it. This is refering to the object itself.
    # It is good style to call this parameter 'self'
    def print_me(self):
        print ("My value is:", self.value)

term1 = Term(4711)