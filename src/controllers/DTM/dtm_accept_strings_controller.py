from repositories import InMemoryDtmRepository

class DtmAcceptStringsController:

  def __init__(self, *, repository : InMemoryDtmRepository):
    self.__repository = repository
  
  def execute(self, *, id : str, string : str):
    strIsValid = self.__repository.acceptString(id = id, string = string)
    return {
      'string': string,
      'isValid': strIsValid
    }