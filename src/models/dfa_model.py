from automata.fa.dfa import DFA
import uuid

class DfaModel:

  def __init__(self, *, id = str(uuid.uuid4()), states, inputSymbols, transitions, initialState, finalStates):
    self.id = id
    dfa = DFA(
      states = set(states),
      input_symbols = set(inputSymbols),
      transitions = transitions,
      initial_state = initialState,
      final_states = set(finalStates)
    )
    self.inputParameters = dfa.input_parameters
  
  def toDfa(self):
    dfa = DFA(**self.inputParameters)
    return dfa

  def saveImage(self):
    urlImage = f'images/{self.id}.png'
    self.toDfa().show_diagram(path = urlImage)
    return urlImage