import random
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance += self.speed * hours
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print("-" * 45)
        print(f"{'Car':<10}{'Speed':<10}{'Distance':<10}")
        print("-" * 45)
        for car in self.cars:
            print(f"{car.registration_number:<10}{car.speed:<10}{car.distance:<10.1f}")

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False

cars = []
for i in range(10):
    cars.append(Car(f"ABC-{i+1}", random.randint(100, 200)))

# Create race
race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        race.print_status()
# Final status
race.print_status()
print(f"\nRace finished in {hours} hours!")