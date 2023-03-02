from classes.customer import Customer
from classes.restaurant import Restaurant

class Review:
    
    # 5 README asks for these initial attributes
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

        # Not sure why we need these
        self.add_customer_to_restaurant()
        self.add_restaurant_to_customer()
        self.add_review_to_customer()
        self.add_review_to_restaurant()

    # 6 now it asks for a getter/setter for rating attribute. 
    # we we have a condition and an Exception. 
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if rating > 0 and rating < 6:
            self._rating = rating
        else:
            print("Rating must be between 1 and 5")
            raise Exception("Rating must be between 1 and 5")

    # 7 we're asked to make customer a property
    # it needs to be returned. so that's an easy getter
    # then comes our first bit of Object Relationship
    # our condition is seeing if this customer that we're passing in
    #is an instance/object of Customer class. if is groovy. if not Exception time.
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            print("Customer is not an instance of class Customer!")

            raise Exception("Customer is not an instance of class Customer!")

    # 8 we're doing the same thing now with restaurant for the review.
    # is it one underscore or two?
    @property
    def restaurant(self):
        return self._restaurant
    
    @restaurant.setter
    def restaurant(self, restaurant):
        if isinstance(restaurant, Restaurant):
            self._restaurant = restaurant
            
        else:
            print("Restaurant is not an instance of class Restaurant!")

            raise Exception("Restaurant is not an instance of class Restaurant!")




    def rating(self):
        def get_rating(self):
            return self._rating

        def set_rating(self, rating):
            if type(rating) == int and 1 <= (rating) <= 5:
                self._rating = rating

        rating = property(get_rating, set_rating,)


    # not sure when these functions happen
    def add_customer_to_restaurant(self):
        if self._customer not in self._restaurant.customers:
            self._restaurant.customers.append(self._customer)

    def add_review_to_restaurant(self):
        self._restaurant.reviews.append(self)

    def add_restaurant_to_customer(self):
        if self._restaurant not in self._customer.restaurants:
            self._customer.restaurants.append(self._restaurant)

    def add_review_to_customer(self):
        self._customer.reviews.append(self)


