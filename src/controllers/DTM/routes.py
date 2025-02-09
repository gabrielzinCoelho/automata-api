from automata.fa.dfa import DFA
from repositories import InMemoryDtmRepository
from fastapi import APIRouter
from .create_dtm_controller import CreateDtmController, CreateDtmBodyRequestDto
from .update_dtm_controller import UpdateDtmBodyRequestDto, UpdateDtmController
from .fetch_dtms_controller import FetchDtmsController
from .get_dtm_controller import GetDtmController
from .dtm_accept_strings_controller import DtmAcceptStringsController

class DtmController:

  def __init__(self):
    self.repository = InMemoryDtmRepository()

dtm_controller = DtmController()
router = APIRouter()

@router.get('/dtm/{id}')
def get_dfa(id):
  getDtmController = GetDtmController(repository = dtm_controller.repository)
  return getDtmController.execute(id = id)

@router.get('/dtm/{id}/accept/{string:path}')
def accept_string(id, string = ''):
  acceptStringsController = DtmAcceptStringsController(repository = dtm_controller.repository)
  return acceptStringsController.execute(id = id, string = string)

@router.get("/dtm")
def fetch_dtm():
  fetchDtmsController = FetchDtmsController(repository = dtm_controller.repository)
  return fetchDtmsController.execute()

@router.post("/dtm")
def create_dtm(dtm : CreateDtmBodyRequestDto):
  createDtmController = CreateDtmController(repository = dtm_controller.repository)
  return createDtmController.execute(dtm = dtm)

@router.put("/dtm/{id}")
def update_dtm(dtm : UpdateDtmBodyRequestDto, id):
  updateDtmController = UpdateDtmController(repository = dtm_controller.repository)
  return updateDtmController.execute(dtm = dtm, id = id)
  