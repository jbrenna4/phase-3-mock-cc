class Restaurant:
    all = []

    # 3 READ me asks for the attribute to have a condition but explicitly states
    # that it is an _init_ so we write it in here
    def __init__(self, name):
        if type(name) == str:
            self._name = name

            Restaurant.all.append(self)
        
        else:
            print("The restaurant name must be a string!")

            raise Exception("The restaurant name must be a string!")

        # I guess this is answering 9 and 10?? function written somewhere else?
        self.reviews = []
        self.customers = []

    # 4 now README wants that name returned. this is a getter function
    # super easy to write here with a decorator
    # However, I'm unsure about "Should not be able to change after the restaurant is created"
    @property
    def name(self):
        return self._name

    # 15 Returns the average star rating for a restaurant based on its reviews
    # we create a total variables => set it to zero
    # for loop => going over each review in self.reviews
    # every loop adds the rating integer to the total
    # we create an variable for average
    # for our math we need the total number of reviews. we can use len() for that
    # then we run the math and return our average variable 
    def get_average_rating(self):
        total = 0

        for review in self.reviews:
            total += review.rating

        average = total / len(self.reviews)

        return average

    
    #16 Returns a list of all restaurants
    # all is a class attirbute, that is also a list. 
    # we append new instances to it...it's in the _init_
    @classmethod
    def get_all_restaurants(cls):
        return cls.all

    # 9 Returns a list of all reviews for that restaurant
    # Reviews must be of type Review

    # 10 Returns a unique list of all customers who have reviewed a particular restaurant.
    # Customers must be of type Customer