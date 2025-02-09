from models import DtmModel

class InMemoryDtmRepository:

  def __init__(self):
    self.items : list[DtmModel] = []

  def findUniqueById(self, *, id):
    dtm = next((item for item in self.items if item.id == id), None)
    if dtm is None:
      raise Exception("Dtm doesn't exist.")
    return dtm
  
  def acceptString(self, *, id, string):
    dtm = self.findUniqueById(id = id).toDTM()
    return dtm.accepts_input(input_str=string)
  
  def create(self, *, states, inputSymbols, transitions, initialState, finalStates, tapeSymbols, blankSymbol):
    newDtm = DtmModel(
      states = states,
      inputSymbols = inputSymbols,
      transitions = transitions,
      initialState = initialState,
      finalStates = finalStates,
      tapeSymbols = tapeSymbols,
      blankSymbol = blankSymbol
    )
    self.items.append(newDtm)
    return newDtm
  
  def findAll(self):
    return self.items

  def updateById(self, *, id, states, inputSymbols, transitions, initialState, finalStates, tapeSymbols, blankSymbol):
    updatedDtm = DtmModel(
      id = id,
      states = states,
      inputSymbols = inputSymbols,
      transitions = transitions,
      initialState = initialState,
      finalStates = finalStates,
      tapeSymbols = tapeSymbols,
      blankSymbol = blankSymbol
    )
    self.items = list(
      map(
        (lambda item : item if item.id != id else updatedDtm),
        self.items
      )
    )
    return updatedDtm

  