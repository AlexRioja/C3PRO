from state_machine import Automata, State
import moves
class State_Idle(State):
    def run(self, previous, speed):
        moves.initial_position(speed=speed)