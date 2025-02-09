from pydantic import BaseModel
from enum import Enum 
from repositories import InMemoryNpdaRepository
from automata.pda.npda import NPDATransitionsT
from models import Transition

class AcceptanceModeEnum(str, Enum):
    final_state = 'final_state'
    empty_stack = 'empty_stack'
    both = 'both'

class UpdateNpdaBodyRequestDto(BaseModel):
  states: list[str] 
  inputSymbols: list[str]
  transitions: dict[str, dict[str, dict[str, list[Transition]]]]
  initialState: str
  finalStates: list[str]
  stackSymbols: list[str]
  initialStackSymbol: str
  acceptanceMode: AcceptanceModeEnum

class UpdateNpdaController:

  def __init__(self, *, repository : InMemoryNpdaRepository):
    self.__repository = repository
  
  def execute(self, *, npda : UpdateNpdaBodyRequestDto, id : str):
    updatedNpda = self.__repository.updateById(
      id = id,
      states = npda.states,
      inputSymbols = npda.inputSymbols,
      stackSymbols= npda.stackSymbols,
      initialStackSymbol = npda.initialStackSymbol,
      transitions = npda.transitions,
      initialState = npda.initialState,
      finalStates = npda.finalStates,
      acceptanceMode = npda.acceptanceMode
    )
    return updatedNpda