from automata.pda.npda import NPDA
import uuid
from pydantic import BaseModel

class TransitionInfo(BaseModel):
  symbol: str
  over: str

class Transition(BaseModel):
  state: str
  stack: str | TransitionInfo

class NpdaModel:

  def __init__(self, *, id = str(uuid.uuid4()), states, inputSymbols, stackSymbols, initialStackSymbol, transitions, initialState, finalStates, acceptanceMode):
    self.id = id

    for estadoDict in transitions.values():
      for simboloPalavraDict in estadoDict.values():
        for topoPilhaDictKey, topoPilhaDict in simboloPalavraDict.items():
            simboloPalavraDict[topoPilhaDictKey] = set([
                (transicao.state, transicao.stack) if not isinstance(transicao.stack, TransitionInfo) else
                (transicao.state, (transicao.stack.symbol, transicao.stack.over))
                for transicao in topoPilhaDict
            ])

    npda = NPDA(
      states = set(states),
      input_symbols = set(inputSymbols),
      stack_symbols= set(stackSymbols),
      transitions = transitions,
      initial_state = initialState,
      initial_stack_symbol= initialStackSymbol,
      final_states = set(finalStates),
      acceptance_mode = acceptanceMode
    )
    self.inputParameters = npda.input_parameters
  
  def toNPDA(self):
    npda = NPDA(**self.inputParameters)
    return npda

  def saveImage(self):
    urlImage = f'images/{self.id}.png'
    self.toNPDA().show_diagram(path = urlImage)
    return urlImage