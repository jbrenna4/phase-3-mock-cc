class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []
        self.restaurants = []

    def first_name(self):
        # first_name property goes here!
        pass

    def last_name(self):
        # last_name property goes here!
        pass

    def get_full_name(self):
        pass

    def get_num_reviews(self):
        pass

    def add_review(self, restaurant, rating):
        # This prevents a circular import!
        # Don't worry about it right now, but check it out when you have the time!
        from classes.review import Review
        pass