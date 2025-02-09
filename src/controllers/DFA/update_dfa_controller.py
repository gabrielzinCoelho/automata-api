from pydantic import BaseModel
from repositories import InMemoryDfaRepository

class UpdateDfaBodyRequestDto(BaseModel):
  states: list[str] 
  inputSymbols: list[str]
  transitions: dict[str, dict[str, str]]
  initialState: str
  finalStates: list[str]

class UpdateDfaController:

  def __init__(self, *, repository : InMemoryDfaRepository):
    self.__repository = repository
  
  def execute(self, *, dfa : UpdateDfaBodyRequestDto, id : str):
    updatedFda = self.__repository.updateById(
      id = id,
      states = dfa.states,
      inputSymbols = dfa.inputSymbols,
      transitions = dfa.transitions,
      initialState = dfa.initialState,
      finalStates = dfa.finalStates
    )
    return updatedFda