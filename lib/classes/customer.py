class Customer:

    # 1 just following README. We init the first and last names
    # WE ARE FAILING THE FIRST TEST LOL - MAYBE SOMETHING WITH MY PROPERTY
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        # I guess these are 11 and 12???
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

    def get_last_name(self):
        return self._last_name
    
    def set_last_name(self, last_name):
        if type(last_name) == str and len(last_name) <= 25:
            self._last_name = last_name
    
    last_name = property(get_last_name, set_last_name,)


    # def first_name(self):
    #     # first_name property goes here!
    #     pass

    # def last_name(self):
    #     # last_name property goes here!
    #     pass

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"


    # 13 Returns the total number of reviews that a customer has authored
    def get_num_reviews(self):
        return len(self.reviews)


    # 14 given a restaurant object and a star rating (as an integer),
    #  creates a new review and associates it with that customer and restaurant.

    def add_review(self, restaurant, rating):
        # This prevents a circular import!
        # Don't worry about it right now, but check it out when you have the time!
        from classes.review import Review
        Review(self, restaurant, rating)