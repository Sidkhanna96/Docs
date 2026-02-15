"""
Use python3 for the tests to pass (random seed doesn't work the same across python version).

When a Lyft ride is completed, a rider leaves a rating for their driver and the driver does the same. This is known as rides rating. This rating can be out of 1 to 5 stars.
Given a database of rides and ratings implement simple APIs method that could be used to build a dashboard for our users.

Tasks:
1) design basics class to represent the ride and rating object.
2) transform the raw response from the helper to the ride and rating objects you designed.
3) build 2 API:
 - return the rating a user received on a ride.
 - return the average ratings received by a user.

The database has two models:
```
Ride(ride_id, driver_id, rider_id, timestamp)
Rating(ride_id, rating_from_user_id, rating)
```
For any ride there are two ratings:
- rider rate driver
- driver rate rider

The table are accessible through an API returning a json blob:
```
{
  "rides": [
     {"ride_id": 1, "rider_id": 1234, "driver_id": 5678, "timestamp": 1577836800}, -> {ride_id: {rider_id: driver_id, driver_id: rider_id, timestamp}}
     {"ride_id": 2, "rider_id": 6543, "driver_id": 5678, "timestamp": 1577927200},
     {"ride_id": 3, "rider_id": 6543, "driver_id": 9012, "timestamp": 1578548400}
   ],
  "ratings": [
    {"ride_id": 1, "rating_from_user_id":  1234, "rating": 4}, -> {ride_id: {rating_from_user_id: x, rating_from_user_id: y}}
    {"ride_id": 1, "rating_from_user_id":  5678, "rating": 3},
    {"ride_id": 2, "rating_from_user_id":  6543, "rating": 2},
    {"ride_id": 2, "rating_from_user_id":  5678, "rating": 5},
    {"ride_id": 3, "rating_from_user_id":  6543, "rating": 1},
    {"ride_id": 3, "rating_from_user_id":  9012, "rating": 2}
  ]
}
```

The APIs to build are:
```
RatingService.get_rating_for_ride_and_user(ride_id, user_id) -> int
RatingService.get_average_rating_of_user(user_id) -> float
```

`RatingService.get_rating_for_ride_and_user` take a user_id and a ride_id and returns the rating that the user received for this ride.
Given the json above:
`RatingService.get_rating_for_ride_and_user(3, 9012) == 1`

`get_average_rating_of_user` take a user_id and returns the average of the rating that the user received.
Given the json above:
`RatingService.get_average_rating_of_user(5678) == (4 + 2) / 2 == 3.0`
"""

def _generate_rides_ratings():
    """
    This method is an helper to generate data. You shouldn't modify this.
    """
    from random import randrange, shuffle, seed

    seed(
        12345
    )  # initialize the random seed so that we always get the same random values
    start_timestamp = 1577836800
    end_timestamp = 1583020800
    seed_driver_id = 100000
    seed_rider_id = 200000
    drivers_count = 3
    riders_count = 10
    drivers_id = [seed_driver_id + i for i in range(drivers_count)]
    riders_id = [seed_rider_id + i for i in range(riders_count)]
    minutes_count = int((end_timestamp - start_timestamp) / 60)
    rides_count = int(minutes_count / 15)  # 1 rides every 15 min on average
    rides = []
    ratings = []
    for i in range(rides_count):
        rand_min = (
            randrange(minutes_count) * 60
        )  # pick a random minute offset and convert to second
        driver_id = drivers_id[randrange(len(drivers_id))]  # pick a random driver
        rider_id = riders_id[randrange(len(riders_id))]  # pick a random rider
        driver_rating = randrange(5) + 1  # pick a random driver rating
        rider_rating = randrange(5) + 1  # pick a random rider rating
        timestamp = start_timestamp + rand_min  # compute the timestamp of the ride

        # Build the ride and rating objects and add to the lists
        rides.append(
            {
                "ride_id": i,
                "rider_id": rider_id,
                "driver_id": driver_id,
                "timestamp": timestamp,
            }
        )
        ratings.append(
            {"ride_id": i, "rating_from_user_id": driver_id, "rating": driver_rating}
        )
        ratings.append(
            {"ride_id": i, "rating_from_user_id": rider_id, "rating": rider_rating}
        )
    shuffle(ratings)
    shuffle(rides)
    return {"rides": rides, "ratings": ratings}  # Return a dict
        

class Ride:
    def __init__(self, ride_id, rider_id, driver_id, timestamp):
        self.ride_id = ride_id
        self.rider_id = rider_id
        self.driver_id = driver_id
        self.timestamp = timestamp

    def associated_user(self, user_id):
        if user_id == self.rider_id:
            return self.driver_id
        if user_id == self.driver_id:
            return self.rider_id
        
        raise ValueError("UserId does not exist {user_id}")
        
class Rating:
    def __init__(self, ride_id, rating_from_user_id, rating):
        self.ride_id = ride_id
        self.rating_from_user_id = rating_from_user_id
        self.rating = rating

    def get_associated_user_id(self, ride: Ride):
        return ride.associated_user(self.rating_from_user_id)

class RatingService:
    def __init__(self) -> None:
        ride_ratings = _generate_rides_ratings()
        # ride_ratings is a dictionary with 2 keys: ride_ratings["ratings"] = [{...rating dict}, ...] and ride_ratings["rides"] = [{...ride dict}, ...]

        # TODO: Design a Rating class and a Ride class and use them to transform the raw data in `ride_ratings` into 2 lists of Ride and Rating objects.
        self.rides = [Ride(**ride) for ride in ride_ratings["rides"]]
        self.ratings = [Rating(**rating) for rating in ride_ratings["ratings"]]

        self.rides_by_id = {}
        self.ratings_by_id = {}

        for ride_data in self.rides:
            self.rides_by_id[ride_data.ride_id] = ride_data

        for rating_data in self.ratings:
            if rating_data.ride_id not in self.ratings_by_id:
                self.ratings_by_id[rating_data.ride_id] = {}

            self.ratings_by_id[rating_data.ride_id][rating_data.rating_from_user_id] = rating_data


    def get_rating_for_ride_and_user(self, ride_id, user_id):
        # TODO: return the rating that this user received for this ride.
        #  eg: for ride_id=3 and user_id=9012 on the data above, the return value should be 1
        user_giving_rating = self.rides_by_id[ride_id].associated_user(user_id) # {"ride_id": 3, "rating_from_user_id":  9012, "rating": 2}
        
        return self.ratings_by_id[ride_id][user_giving_rating].rating

    def get_user_average_ratings(self, user_id):
        # Return the average rating that this user received.
        total = 0
        count = 0
        for ride_id, ratings_dict in self.ratings_by_id.items():
            for rater_id, rating_obj in ratings_dict.items():
                # The recipient is the user who did NOT give the rating
                ride = self.rides_by_id[ride_id]
                recipient_id = ride.associated_user(rater_id)
                if recipient_id == user_id:
                    total += rating_obj.rating
                    count += 1
        if count == 0:
            return 0.0
        return total / count
        



if __name__ == "__main__":
    service = RatingService()

    def check_rating(ride_id, user_id, expected):
        rating = service.get_rating_for_ride_and_user(ride_id, user_id)
        print(
            f"[OK] check_rating for {user_id}"
            if rating == expected
            else f"[KO] check_rating for user {user_id}, ride: {ride_id}. Expected {expected} got {rating}"
        )

    def check_average(user_id, expected):
        average = service.get_user_average_ratings(user_id)
        equal = abs(average - expected) < 1e-10 * max(abs(average), abs(expected))
        print(
            f"[OK] check_average for {user_id}"
            if equal
            else f"[KO] check_average for {user_id} expected {expected} got {average}"
        )

    check_rating(807, 100000, 2)
    check_rating(807, 200008, 1)
    check_rating(2654, 100001, 3)
    check_rating(2654, 200009, 2)
    check_rating(4034, 100000, 1)
    check_rating(4034, 200009, 3)

    check_average(100000, 2.9974120082815734)
    check_average(100001, 3.019172552976791)
    check_average(100002, 2.9593716143011917)
    check_average(200000, 3.083032490974729)
    check_average(200001, 3.0403508771929824)
    check_average(200005, 3.0784641068447414)
    check_average(200009, 2.9479166666666665)