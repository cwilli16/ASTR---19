class Tiger:
    def __init__(self, arm_length: float, leg_length: float, num_eyes: int, has_tail: bool, is_furry: bool):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe_physical_characteristics(self):
        print("--- Physical Characteristics of the Tiger ---")
        print(f"Arm Length: {self.arm_length} meters")
        print(f"Leg Length: {self.leg_length} meters")
        print(f"Number of Eyes: {self.num_eyes}")
        print(f"Has a Tail: {self.has_tail}")
        print(f"Is Furry: {self.is_furry}")

# Example values for an average tiger
my_favorite_animal = Tiger(arm_length=0.8, leg_length=1.0, num_eyes=2, has_tail=True, is_furry=True)

my_favorite_animal.describe_physical_characteristics()