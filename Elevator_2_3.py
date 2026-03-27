
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()



class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []

        for _ in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, destination_floor):
        print(f"\nRunning elevator {elevator_number} to floor {destination_floor}")
        self.elevators[elevator_number].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("\n🔥 FIRE ALARM! Moving all elevators to bottom floor...")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)


# --- Test Building ---
building = Building(1, 10, 3)

building.run_elevator(0, 5)
building.run_elevator(1, 8)
building.run_elevator(2, 3)

building.fire_alarm()