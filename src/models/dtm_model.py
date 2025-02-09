from automata.tm.dtm import DTM
import uuid
from pydantic import BaseModel

class Transition(BaseModel):
  state: str
  symbolToReplace: str
  move: str

class DtmModel:

  def __init__(self, *, id = str(uuid.uuid4()), states, inputSymbols, transitions, initialState, finalStates, tapeSymbols, blankSymbol):
    self.id = id

    for estadoDict in transitions.values():
      for transitionKey, transitionData in estadoDict.items():
          estadoDict[transitionKey] = (transitionData.state, transitionData.symbolToReplace, transitionData.move)

    print(transitions)

    dtm = DTM(
      states = set(states),
      input_symbols = set(inputSymbols),
      transitions = transitions,
      initial_state = initialState,
      final_states = set(finalStates),
      blank_symbol = blankSymbol,
      tape_symbols = set(tapeSymbols),
    )
    self.inputParameters = dtm.input_parameters
  
  def toDTM(self):
    dtm = DTM(**self.inputParameters)
    return dtm