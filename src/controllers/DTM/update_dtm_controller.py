from pydantic import BaseModel
from repositories import InMemoryDtmRepository
from models import TransitionDtm

class UpdateDtmBodyRequestDto(BaseModel):
  states: list[str] 
  inputSymbols: list[str]
  tapeSymbols: list[str]
  transitions: dict[str, dict[str, TransitionDtm]]
  initialState: str
  blankSymbol: str
  finalStates: list[str]

class UpdateDtmController:

  def __init__(self, *, repository : InMemoryDtmRepository):
    self.__repository = repository
  
  def execute(self, *, dtm : UpdateDtmBodyRequestDto, id : str):
    updatedDtm = self.__repository.updateById(
      id = id,
      states = dtm.states,
      inputSymbols = dtm.inputSymbols,
      transitions = dtm.transitions,
      initialState = dtm.initialState,
      finalStates = dtm.finalStates,
      blankSymbol = dtm.blankSymbol,
      tapeSymbols = dtm.tapeSymbols
    )
    return updatedDtm