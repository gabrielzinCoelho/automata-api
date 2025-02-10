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


@router.get(
    "/dfa/{id}",
    summary="Obter DFA por ID",
    description="Recupera um DFA a partir do seu ID.",
    response_model=None,
    tags=["Deterministic Finite Automaton"],
    status_code=200,
    responses={
        200: {
            "description": "DFA listado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "id": "435dd07d-2374-4e47-814f-de1b1d2abc33",
                        "inputParameters": {
                            "states": ["q2", "q0", "q1"],
                            "input_symbols": ["1", "0"],
                            "transitions": {
                                "q0": {"0": "q1", "1": "q2"},
                                "q1": {"0": "q2", "1": "q1"},
                                "q2": {"0": "q1", "1": "q2"},
                            },
                            "initial_state": "q0",
                            "final_states": ["q2"],
                            "allow_partial": False,
                        },
                    }
                }
            },
        }
    },
)
def get_dfa(id):
    getDfaController = GetDfaController(repository=dfa_controller.repository)
    return getDfaController.execute(id=id)


@router.get(
    "/dfa/{id}/accept/{string:path}",
    summary="Verificar se o DFA aceita a string",
    description="Verifica se o DFA identificado pelo ID aceita a string fornecida.",
    response_model=None,
    tags=["Deterministic Finite Automaton"],
    status_code=200,
    responses={
        200: {
            "description": "Aceitação da palavra verificada com sucesso.",
            "content": {
                "application/json": {
                    "example": {"string": "0000001111111", "isValid": False}
                }
            },
        }
    },
)
def accept_string(id, string=""):
    acceptStringsController = DfaAcceptStringsController(
        repository=dfa_controller.repository
    )
    return acceptStringsController.execute(id=id, string=string)


@router.post(
    "/dfa/{id}/image",
    summary="Salvar imagem do DFA",
    description="Gera e salva uma imagem do DFA identificado pelo ID.",
    response_model=None,
    tags=["Deterministic Finite Automaton"],
    status_code=200,
    responses={
        200: {
            "description": "Imagem DFA salva com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "success": "Image saved with success in images/2754c2ce-fead-4f65-b9b3-8b983a80d660.png"
                    }
                }
            },
        }
    },
)
def save_image(id):
    saveImageController = DfaSaveImageController(repository=dfa_controller.repository)
    return saveImageController.execute(id=id)


@router.get(
    "/dfa",
    summary="Listar todos os DFAs",
    description="Recupera todos os DFAs armazenados.",
    response_model=None,
    tags=["Deterministic Finite Automaton"],
    status_code=200,
    responses={
        200: {
            "description": "DFA's listado com sucesso",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": "435dd07d-2374-4e47-814f-de1b1d2abc33",
                            "inputParameters": {
                                "states": ["q2", "q0", "q1"],
                                "input_symbols": ["1", "0"],
                                "transitions": {
                                    "q0": {"0": "q1", "1": "q2"},
                                    "q1": {"0": "q2", "1": "q1"},
                                    "q2": {"0": "q1", "1": "q2"},
                                },
                                "initial_state": "q0",
                                "final_states": ["q2"],
                                "allow_partial": False,
                            },
                        }
                    ]
                }
            },
        }
    },
)
def fetch_dfa():
    fetchDfasController = FetchDfasController(repository=dfa_controller.repository)
    return fetchDfasController.execute()


@router.post(
    "/dfa",
    summary="Criar um novo DFA",
    description="Cria um novo DFA a partir do corpo da solicitação.",
    response_model=None,
    tags=["Deterministic Finite Automaton"],
    status_code=201,
    responses={
        201: {
            "description": "DFA criado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "id": "435dd07d-2374-4e47-814f-de1b1d2abc33",
                        "inputParameters": {
                            "states": ["q2", "q0", "q1"],
                            "input_symbols": ["1", "0"],
                            "transitions": {
                                "q0": {"0": "q1", "1": "q2"},
                                "q1": {"0": "q2", "1": "q1"},
                                "q2": {"0": "q1", "1": "q2"},
                            },
                            "initial_state": "q0",
                            "final_states": ["q2"],
                            "allow_partial": False,
                        },
                    }
                }
            },
        }
    },
)
def create_dfa(dfa: CreateDfaBodyRequestDto):
    createDfaController = CreateDfaController(repository=dfa_controller.repository)
    return createDfaController.execute(dfa=dfa)


@router.put(
    "/dfa/{id}",
    summary="Atualizar um DFA existente",
    description="Atualiza um DFA existente com base no ID e nas informações fornecidas.",
    response_model=None,
    tags=["Deterministic Finite Automaton"],
    status_code=200,
    responses={
        200: {
            "description": "DFA atualizado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "id": "435dd07d-2374-4e47-814f-de1b1d2abc33",
                        "inputParameters": {
                            "states": ["q2", "q0", "q1"],
                            "input_symbols": ["1", "0"],
                            "transitions": {
                                "q0": {"0": "q1", "1": "q2"},
                                "q1": {"0": "q2", "1": "q1"},
                                "q2": {"0": "q1", "1": "q2"},
                            },
                            "initial_state": "q0",
                            "final_states": ["q2"],
                            "allow_partial": False,
                        },
                    }
                }
            },
        }
    },
)
def update_dfa(dfa: UpdateDfaBodyRequestDto, id):
    updateDfaController = UpdateDfaController(repository=dfa_controller.repository)
    return updateDfaController.execute(dfa=dfa, id=id)
