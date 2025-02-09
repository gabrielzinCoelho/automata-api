from automata.fa.dfa import DFA
from repositories import InMemoryDfaRepository
from fastapi import APIRouter
from .create_dfa_controller import CreateDfaController, CreateDfaBodyRequestDto
from .fetch_dfas_controller import FetchDfasController
from .get_dfa_controller import GetDfaController
from .update_dfa_controller import UpdateDfaController, UpdateDfaBodyRequestDto
from .dfa_accept_strings_controller import DfaAcceptStringsController
from .dfa_save_image_controller import DfaSaveImageController

class DfaController:

  def __init__(self):
    self.repository = InMemoryDfaRepository()

dfa_controller = DfaController()
router = APIRouter()

@router.get('/dfa/{id}')
def get_dfa(id):
  getDfaController = GetDfaController(repository = dfa_controller.repository)
  return getDfaController.execute(id = id)

@router.get('/dfa/{id}/accept/{string:path}')
def accept_string(id, string = ''):
  acceptStringsController = DfaAcceptStringsController(repository = dfa_controller.repository)
  return acceptStringsController.execute(id = id, string = string)

@router.post('/dfa/{id}/image')
def save_image(id):
  saveImageController = DfaSaveImageController(repository = dfa_controller.repository)
  return saveImageController.execute(id = id)

@router.get("/dfa")
def fetch_dfa():
  fetchDfasController = FetchDfasController(repository = dfa_controller.repository)
  return fetchDfasController.execute()

@router.post("/dfa")
def create_dfa(dfa : CreateDfaBodyRequestDto):
  createDfaController = CreateDfaController(repository = dfa_controller.repository)
  return createDfaController.execute(dfa = dfa)

@router.put("/dfa/{id}")
def update_dfa(dfa : UpdateDfaBodyRequestDto, id):
  updateDfaController = UpdateDfaController(repository = dfa_controller.repository)
  return updateDfaController.execute(dfa = dfa, id = id)
  