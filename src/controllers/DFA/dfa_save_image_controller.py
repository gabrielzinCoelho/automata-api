from pydantic import BaseModel
from repositories import InMemoryDfaRepository

class DfaSaveImageController:

  def __init__(self, *, repository : InMemoryDfaRepository):
    self.__repository = repository
  
  def execute(self, *, id : str):
    urlImg = self.__repository.saveImage(id = id)
    return {
      'success': f'Image saved with success in {urlImg}'
    }