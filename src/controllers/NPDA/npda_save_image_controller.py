from repositories import InMemoryNpdaRepository

class NpdaSaveImageController:

  def __init__(self, *, repository : InMemoryNpdaRepository):
    self.__repository = repository
  
  def execute(self, *, id : str):
    urlImg = self.__repository.saveImage(id = id)
    return {
      'success': f'Image saved with success in {urlImg}'
    }