from models import DfaModel

class InMemoryDfaRepository:

  def __init__(self):
    self.items : list[DfaModel] = []

  def findUniqueById(self, *, id):
    dfa = next((item for item in self.items if item.id == id), None)
    if dfa is None:
      raise Exception("Dfa doesn't exist.")
    return dfa
  
  def acceptString(self, *, id, string):
    dfa = self.findUniqueById(id = id).toDfa()
    return dfa.accepts_input(input_str=string)

  def saveImage(self, *, id):
    dfa = self.findUniqueById(id = id)
    return dfa.saveImage()
  
  def create(self, *, states, inputSymbols, transitions, initialState, finalStates):
    newDfa = DfaModel(
      states = states,
      inputSymbols = inputSymbols,
      transitions = transitions,
      initialState = initialState,
      finalStates = finalStates
    )
    self.items.append(newDfa)
    return newDfa
  
  def findAll(self):
    return self.items

  def updateById(self, *, id, states, inputSymbols, transitions, initialState, finalStates):
    updatedDfa = DfaModel(
      id = id,
      states = states,
      inputSymbols = inputSymbols,
      transitions = transitions,
      initialState = initialState,
      finalStates = finalStates
    )
    self.items = list(
      map(
        (lambda item : item if item.id != id else updatedDfa),
        self.items
      )
    )
    return updatedDfa

  