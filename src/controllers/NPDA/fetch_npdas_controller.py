from repositories import InMemoryNpdaRepository

class FetchNpdasController:

  def __init__(self, *, repository : InMemoryNpdaRepository):
    self.__repository = repository
  
  def execute(self):
    return self.__repository.findAll()