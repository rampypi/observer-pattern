from abc import ABC, abstractmethod

# Define the FlyBehavior interface (abstract base class)
class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        """Define how the duck flies"""
        pass

# Define the QuackBehavior interface (abstract base class)
class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        """Define how the duck quacks"""
        pass

# Define the Duck base class that uses behaviors
class Duck:
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fly_behavior: FlyBehavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackBehavior):
        self.quack_behavior = quack_behavior

    def display(self):
        """Display method to be implemented by subclasses"""
        pass

# Implement specific flying behaviors
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying with wings!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly.")

# Implement specific quacking behaviors
class Quack(QuackBehavior):
    def quack(self):
        print("Quack!")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak!")

# Implement concrete Duck classes
class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print("I'm a real Mallard duck!")

class RubberDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Squeak())

    def display(self):
        print("I'm a rubber duck!")

# Using the classes
def main():
    mallard = MallardDuck()
    rubber_duck = RubberDuck()

    # Display initial behavior
    mallard.display()
    mallard.perform_fly()
    mallard.perform_quack()

    rubber_duck.display()
    rubber_duck.perform_fly()
    rubber_duck.perform_quack()

    # Change behaviors dynamically
    print("\nChanging behaviors dynamically...\n")

    mallard.set_fly_behavior(FlyNoWay())  # Mallard can no longer fly
    mallard.set_quack_behavior(Squeak())  # Mallard now squeaks
    mallard.perform_fly()
    mallard.perform_quack()

    rubber_duck.set_fly_behavior(FlyWithWings())  # Rubber duck can now fly
    rubber_duck.set_quack_behavior(Quack())  # Rubber duck now quacks
    rubber_duck.perform_fly()
    rubber_duck.perform_quack()

if __name__ == "__main__":
    main()
