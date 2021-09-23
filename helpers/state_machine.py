class Automata:
    def __init__(self, states, init_state):
        self.states=states
        self.init_state=init_state
        self.current_state=self.init_state
    def move_to(self, state):
        if(state not in self.states):
            return "No existe el estado:"+str(state)
        print("Moving from "+self.current_state.name+" to "+state.name+"...")
        #TODO implement change of state
        print("Moved from "+self.current_state.name+" to "+state.name+".")
        
class State:
    def __init__(self, name, pre_state_change_function):
        self.name=name
        self.pre_state_change_function=pre_state_change_function
    def run(self, previous):
        pass

    