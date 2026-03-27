class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current_floor = bottom_floor
        print(f"Elevator created. Current floor: {self.current_floor}")

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Moving up... Now at floor {self.current_floor}")
        else:
            print("Already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Moving down... Now at floor {self.current_floor}")
        else:
            print("Already at the bottom floor.")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom or target_floor > self.top:
            print("Target floor is out of range.")
            return

        print(f"Going to floor {target_floor}...")

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()
# --- Main program (test) ---
if __name__ == "__main__":
    h = Elevator(1,10)
    h.go_to_floor(5)
    h.go_to_floor(1)