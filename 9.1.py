class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

# Main program
Audi = Car("ABC-123", 148)

# Print all properties
print("Registration number:", Audi.registration_number)
print("Maximum speed:", Audi.max_speed, "km/h")
print("Current speed:", Audi.current_speed, "km/h")
print("Travelled distance:", Audi.travelled_distance, "km")