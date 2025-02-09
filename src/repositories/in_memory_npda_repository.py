from models import NpdaModel

class InMemoryNpdaRepository:

  def __init__(self):
    self.items : list[NpdaModel] = []

  def findUniqueById(self, *, id):
    npda = next((item for item in self.items if item.id == id), None)
    if npda is None:
      raise Exception("Npda doesn't exist.")
    return npda
  
  def acceptString(self, *, id, string):
    npda = self.findUniqueById(id = id).toNPDA()
    return npda.accepts_input(input_str=string)

  def saveImage(self, *, id):
    npda = self.findUniqueById(id = id)
    return npda.saveImage()
  
  def create(self, *, states, inputSymbols, stackSymbols, initialStackSymbol, transitions, initialState, finalStates, acceptanceMode):
    newNpda = NpdaModel(
      states = states,
      inputSymbols = inputSymbols,
      stackSymbols= stackSymbols,
      initialStackSymbol = initialStackSymbol,
      transitions = transitions,
      initialState = initialState,
      finalStates = finalStates,
      acceptanceMode = acceptanceMode
    )
    self.items.append(newNpda)
    return newNpda
  
  def findAll(self):
    return self.items

  def updateById(self, *, id, states, inputSymbols, stackSymbols, initialStackSymbol, transitions, initialState, finalStates, acceptanceMode):
    updatedNpda = NpdaModel(
      states = states,
      inputSymbols = inputSymbols,
      stackSymbols= stackSymbols,
      initialStackSymbol = initialStackSymbol,
      transitions = transitions,
      initialState = initialState,
      finalStates = finalStates,
      acceptanceMode = acceptanceMode
    )
    self.items = list(
      map(
        (lambda item : item if item.id != id else updatedNpda),
        self.items
      )
    )
    return updatedNpda

  