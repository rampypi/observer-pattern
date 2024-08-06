from abc import abstractmethod, ABC 



class FlyBehaviour(ABC):
    @abstractmethod
    def fly():
        raise NotImplementedError
    
class QuackBehaviour(ABC):
    @abstractmethod
    def quack():
        raise NotImplementedError

class Duck:

    def __init__(self, fly_behaviour : FlyBehaviour, quack_behaviour : QuackBehaviour):
        self.fly_behaviour = fly_behaviour
        self.quack_behaviour = quack_behaviour
    
    def set_fly_behaviour(self, fly_behaviour):
        self.fly_behaviour = fly_behaviour

        
    def set_quack_behaviour(self, quack_behaviour):
        self.fly_behaviour = quack_behaviour

    def perform_fly(self):
        return self.fly_behaviour.fly()
    
    def perform_quack(self):
        return self.quack_behaviour.quack()
   
    def display(self):
        return "I am a duck"

class Flywithwings(FlyBehaviour):
    def fly():
        return "I can fly"
class Quack(QuackBehaviour):
    def quack():
        return "I can quack"
    
class NoFly(FlyBehaviour):
    def fly():
        return "I cannot fly"

class NoQuack(QuackBehaviour):
    def quack():
        return "I cannot quack"

class MallardDuck(Duck):
    def __init__(self):
        super().__init__(Flywithwings, Quack)

    def display(self):
        return "I am a Mallard duck"
    
class RubberDuck(Duck):
    def __init__(self):
        super().__init__(NoFly, NoQuack)
    
    def display(self):
        return "I am a rubber duck"