from repositories import InMemoryDtmRepository

class FetchDtmsController:

  def __init__(self, *, repository : InMemoryDtmRepository):
    self.__repository = repository
  
  def execute(self):
    return self.__repository.findAll()