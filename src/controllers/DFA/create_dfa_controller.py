from pydantic import BaseModel
from repositories import InMemoryDfaRepository

class CreateDfaBodyRequestDto(BaseModel):
  states: list[str] 
  inputSymbols: list[str]
  transitions: dict[str, dict[str, str]]
  initialState: str
  finalStates: list[str]

class CreateDfaController:

  def __init__(self, *, repository : InMemoryDfaRepository):
    self.__repository = repository
  
  def execute(self, *, dfa : CreateDfaBodyRequestDto):
    newDfa = self.__repository.create(
      states = dfa.states,
      inputSymbols = dfa.inputSymbols,
      transitions = dfa.transitions,
      initialState = dfa.initialState,
      finalStates = dfa.finalStates
    )
    return newDfa