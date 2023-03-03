class Customer:

    # 1 just following README. We init the first and last names
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        # these are 11 and 12...just like 9 and 10. empty lists for now
        # Returns a unique list of all restaurants a customer has reviewed
        # Returns a list of all reviews a customer has written
        self.reviews = []
        self.restaurants = []


    # 2 both our inits need to be returned and have conditions. so they're properties.
    # we should use the decorator to pass the test. 
    # and we need an Exception for our Else statement. 
    # It looks like a print. So that's easy. 
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if type(first_name) == str and ( len(first_name) > 0 and len(first_name) < 26 ):
            self._first_name = first_name
        else:
            print("Your first name must be a string and contain between 1 and 25 letters, inclusive!")

            raise Exception("Your first name must be a string and contain between 1 and 25 letters, inclusive!")

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        if type(last_name) == str and ( len(last_name) > 0 and len(last_name) < 26 ):
            self._last_name = last_name
        else:
            print("Your last name must be a string and contain between 1 and 25 letters, inclusive!")

            raise Exception("Your last name must be a string and contain between 1 and 25 letters, inclusive!")

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"


    # 13 Returns the total number of reviews that a customer has authored
    # pretty easy. We're just taking all of our reviews and checking the length of the list. 
    # the list will be populated by the function we write in Review
    def get_num_reviews(self):
        return len(self.reviews)


    # 14 given a restaurant object and a star rating (as an integer),
    #  creates a new review and associates it with that customer and restaurant.
    # README is asking for a restaurant instance/object. And it gives us the import from Review
    # the arguments passed to the function are exactly what we need. 
    # they basically give us the answer. 
    # we create a restaurant instance in the function code block. 
    # it has the same arugments as init in Review...but we are in Customer! 
    # so we can pass self instead of customer 

    def add_review(self, restaurant, rating):
        # This prevents a circular import!
        # Don't worry about it right now, but check it out when you have the time!
        from classes.review import Review
        Review(self, restaurant, rating)