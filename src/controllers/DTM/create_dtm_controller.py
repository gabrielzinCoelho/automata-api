from pydantic import BaseModel
from repositories import InMemoryDtmRepository
from models import TransitionDtm

class CreateDtmBodyRequestDto(BaseModel):
  states: list[str] 
  inputSymbols: list[str]
  tapeSymbols: list[str]
  transitions: dict[str, dict[str, TransitionDtm]]
  initialState: str
  blankSymbol: str
  finalStates: list[str]

class CreateDtmController:

  def __init__(self, *, repository : InMemoryDtmRepository):
    self.__repository = repository
  
  def execute(self, *, dtm : CreateDtmBodyRequestDto):
    newDtm = self.__repository.create(
      states = dtm.states,
      inputSymbols = dtm.inputSymbols,
      transitions = dtm.transitions,
      initialState = dtm.initialState,
      finalStates = dtm.finalStates,  
      tapeSymbols = dtm.tapeSymbols,
      blankSymbol = dtm.blankSymbol
    )
    return newDtm