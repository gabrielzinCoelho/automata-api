from pydantic import BaseModel
from repositories import InMemoryNpdaRepository

class NpdaAcceptStringsController:

  def __init__(self, *, repository : InMemoryNpdaRepository):
    self.__repository = repository
  
  def execute(self, *, id : str, string : str):
    strIsValid = self.__repository.acceptString(id = id, string = string)
    return {
      'string': string,
      'isValid': strIsValid
    }