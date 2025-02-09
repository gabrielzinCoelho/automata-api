from pydantic import BaseModel
from repositories import InMemoryDfaRepository

class DfaAcceptStringsController:

  def __init__(self, *, repository : InMemoryDfaRepository):
    self.__repository = repository
  
  def execute(self, *, id : str, string : str):
    strIsValid = self.__repository.acceptString(id = id, string = string)
    return {
      'string': string,
      'isValid': strIsValid
    }