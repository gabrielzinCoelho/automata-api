from automata.fa.dfa import DFA
from repositories import InMemoryNpdaRepository
from fastapi import APIRouter
from .create_npda_controller import CreateNpdaController, CreateNpdaBodyRequestDto
from .get_npda_controller import GetNpdaController
from .fetch_npdas_controller import FetchNpdasController
from .npda_save_image_controller import NpdaSaveImageController
from .npda_accept_strings_controller import NpdaAcceptStringsController
from .update_npda_controller import UpdateNpdaController, UpdateNpdaBodyRequestDto

class NpdaController:

  def __init__(self):
    self.repository = InMemoryNpdaRepository()

npda_controller = NpdaController()
router = APIRouter()

@router.get('/npda/{id}')
def get_npda(id):
  getNpdaController = GetNpdaController(repository = npda_controller.repository)
  return getNpdaController.execute(id = id)

@router.get('/npda/{id}/accept/{string:path}')
def accept_string(id, string = ''):
  acceptStringsController = NpdaAcceptStringsController(repository = npda_controller.repository)
  return acceptStringsController.execute(id = id, string = string)

@router.post('/npda/{id}/image')
def save_image(id):
  saveImageController = NpdaSaveImageController(repository = npda_controller.repository)
  return saveImageController.execute(id = id)

@router.get("/npda")
def fetch_npda():
  fetchNpdasController = FetchNpdasController(repository = npda_controller.repository)
  return fetchNpdasController.execute()

@router.post("/npda")
def create_npda(npda : CreateNpdaBodyRequestDto):
  createNpdaController = CreateNpdaController(repository = npda_controller.repository)
  return createNpdaController.execute(npda = npda)

@router.put("/npda/{id}")
def update_npda(npda : UpdateNpdaBodyRequestDto, id):
  updateNpdaController = UpdateNpdaController(repository = npda_controller.repository)
  return updateNpdaController.execute(npda = npda, id = id)
  