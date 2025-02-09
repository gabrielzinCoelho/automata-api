from pydantic import BaseModel
from repositories import InMemoryDfaRepository

class GetDfaController:

  def __init__(self, *, repository : InMemoryDfaRepository):
    self.__repository = repository
  
  def execute(self, *, id : str):
    dfa = self.__repository.findUniqueById(id = id)
    return dfa