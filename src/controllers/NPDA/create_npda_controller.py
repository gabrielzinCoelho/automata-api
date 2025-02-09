from pydantic import BaseModel
from enum import Enum 
from repositories import InMemoryNpdaRepository
from models import Transition

class AcceptanceModeEnum(str, Enum):
    final_state = 'final_state'
    empty_stack = 'empty_stack'
    both = 'both'

class CreateNpdaBodyRequestDto(BaseModel):
  states: list[str] 
  inputSymbols: list[str]
  transitions: dict[str, dict[str, dict[str, list[Transition]]]]
  initialState: str
  finalStates: list[str]
  stackSymbols: list[str]
  initialStackSymbol: str
  acceptanceMode: AcceptanceModeEnum

class CreateNpdaController:

  def __init__(self, *, repository : InMemoryNpdaRepository):
    self.__repository = repository
  
  def execute(self, *, npda : CreateNpdaBodyRequestDto):
    newNpda = self.__repository.create(
      states = npda.states,
      inputSymbols = npda.inputSymbols,
      stackSymbols= npda.stackSymbols,
      initialStackSymbol = npda.initialStackSymbol,
      transitions = npda.transitions,
      initialState = npda.initialState,
      finalStates = npda.finalStates,
      acceptanceMode = npda.acceptanceMode
    )
    return newNpda