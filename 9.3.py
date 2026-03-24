import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        # Speed cannot go below 0
        if self.current_speed < 0:
            self.current_speed = 0

        # Speed cannot exceed max_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


# Main program

# 1. Create 10 cars
cars = []
for i in range(1, 11):
    registration = "ABC-" + str(i)
    max_speed = random.randint(100, 200)
    car = Car(registration, max_speed)
    cars.append(car)


# 2. Start the race
race_finished = False

while not race_finished:
    for car in cars:

        # Change speed randomly (-10 to +15)
        change = random.randint(-10, 15)
        car.accelerate(change)

        # Drive for 1 hour
        car.drive(1)

        # Check if any car reached 10,000 km
        if car.travelled_distance >= 10000:
            race_finished = True


# 3. Print results in a table
print(f"{'License':<12}{'Max Speed':<12}{'Speed':<10}{'Distance':<12}")

for car in cars:
    print(f"{car.registration_number:<12}{car.max_speed:<12}{car.current_speed:<10}{car.travelled_distance:<12}")
