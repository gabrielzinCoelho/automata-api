from repositories import InMemoryDfaRepository

class FetchDfasController:

  def __init__(self, *, repository : InMemoryDfaRepository):
    self.__repository = repository
  
  def execute(self):
    return self.__repository.findAll()