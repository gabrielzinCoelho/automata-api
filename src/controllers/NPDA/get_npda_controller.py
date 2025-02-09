from pydantic import BaseModel
from repositories import InMemoryNpdaRepository

class GetNpdaController:

  def __init__(self, *, repository : InMemoryNpdaRepository):
    self.__repository = repository
  
  def execute(self, *, id : str):
    npda = self.__repository.findUniqueById(id = id)
    return npda