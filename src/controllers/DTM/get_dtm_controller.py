from repositories import InMemoryDtmRepository

class GetDtmController:

  def __init__(self, *, repository : InMemoryDtmRepository):
    self.__repository = repository
  
  def execute(self, *, id : str):
    dtm = self.__repository.findUniqueById(id = id)
    return dtm