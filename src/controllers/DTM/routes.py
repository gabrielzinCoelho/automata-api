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


@router.get(
    "/dtm/{id}",
    summary="Obter DTM por ID",
    description="Recupera um DTM (Deterministic Turing Machine) a partir do seu ID.",
    response_model=None,
    tags=["Determinist Turing Machine"],
    status_code=200,
    responses={
        200: {
            "description": "DTM listado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "id": "75390917-679b-4235-a5be-3d120dc38229",
                        "inputParameters": {
                            "states": ["q3", "q2", "q0", "q4", "q1"],
                            "input_symbols": ["0", "1"],
                            "tape_symbols": ["0", ".", "y", "x", "1"],
                            "transitions": {
                                "q0": {"0": ["q1", "x", "R"], "y": ["q3", "y", "R"]},
                                "q1": {
                                    "0": ["q1", "0", "R"],
                                    "1": ["q2", "y", "L"],
                                    "y": ["q1", "y", "R"],
                                },
                                "q2": {
                                    "0": ["q2", "0", "L"],
                                    "x": ["q0", "x", "R"],
                                    "y": ["q2", "y", "L"],
                                },
                                "q3": {"y": ["q3", "y", "R"], ".": ["q4", ".", "R"]},
                            },
                            "initial_state": "q0",
                            "blank_symbol": ".",
                            "final_states": ["q4"],
                        },
                    }
                }
            },
        }
    },
)
def get_dtm(id):
    getDtmController = GetDtmController(repository=dtm_controller.repository)
    return getDtmController.execute(id=id)


@router.get(
    "/dtm/{id}/accept/{string:path}",
    summary="Verificar se o DTM aceita a string",
    description="Verifica se o DTM identificado pelo ID aceita a string fornecida.",
    response_model=None,
    tags=["Determinist Turing Machine"],
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
    acceptStringsController = DtmAcceptStringsController(
        repository=dtm_controller.repository
    )
    return acceptStringsController.execute(id=id, string=string)


@router.get(
    "/dtm",
    summary="Listar todos os DTMs",
    description="Recupera todos os DTMs armazenados.",
    response_model=None,
    tags=["Determinist Turing Machine"],
    status_code=200,
    responses={
        200: {
            "description": "DTM's listado com sucesso",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": "75390917-679b-4235-a5be-3d120dc38229",
                            "inputParameters": {
                                "states": ["q3", "q2", "q0", "q4", "q1"],
                                "input_symbols": ["0", "1"],
                                "tape_symbols": ["0", ".", "y", "x", "1"],
                                "transitions": {
                                    "q0": {
                                        "0": ["q1", "x", "R"],
                                        "y": ["q3", "y", "R"],
                                    },
                                    "q1": {
                                        "0": ["q1", "0", "R"],
                                        "1": ["q2", "y", "L"],
                                        "y": ["q1", "y", "R"],
                                    },
                                    "q2": {
                                        "0": ["q2", "0", "L"],
                                        "x": ["q0", "x", "R"],
                                        "y": ["q2", "y", "L"],
                                    },
                                    "q3": {
                                        "y": ["q3", "y", "R"],
                                        ".": ["q4", ".", "R"],
                                    },
                                },
                                "initial_state": "q0",
                                "blank_symbol": ".",
                                "final_states": ["q4"],
                            },
                        }
                    ]
                }
            },
        }
    },
)
def fetch_dtm():
    fetchDtmsController = FetchDtmsController(repository=dtm_controller.repository)
    return fetchDtmsController.execute()


@router.post(
    "/dtm",
    summary="Criar um novo DTM",
    description="Cria um novo DTM a partir do corpo da solicitação.",
    response_model=None,
    tags=["Determinist Turing Machine"],
    status_code=201,
    responses={
        201: {
            "description": "DTM criado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "id": "75390917-679b-4235-a5be-3d120dc38229",
                        "inputParameters": {
                            "states": ["q3", "q2", "q0", "q4", "q1"],
                            "input_symbols": ["0", "1"],
                            "tape_symbols": ["0", ".", "y", "x", "1"],
                            "transitions": {
                                "q0": {"0": ["q1", "x", "R"], "y": ["q3", "y", "R"]},
                                "q1": {
                                    "0": ["q1", "0", "R"],
                                    "1": ["q2", "y", "L"],
                                    "y": ["q1", "y", "R"],
                                },
                                "q2": {
                                    "0": ["q2", "0", "L"],
                                    "x": ["q0", "x", "R"],
                                    "y": ["q2", "y", "L"],
                                },
                                "q3": {"y": ["q3", "y", "R"], ".": ["q4", ".", "R"]},
                            },
                            "initial_state": "q0",
                            "blank_symbol": ".",
                            "final_states": ["q4"],
                        },
                    }
                }
            },
        }
    },
)
def create_dtm(dtm: CreateDtmBodyRequestDto):
    createDtmController = CreateDtmController(repository=dtm_controller.repository)
    return createDtmController.execute(dtm=dtm)


@router.put(
    "/dtm/{id}",
    summary="Atualizar um DTM existente",
    description="Atualiza um DTM existente com base no ID e nas informações fornecidas.",
    response_model=None,
    tags=["Determinist Turing Machine"],
    status_code=200,
    responses={
        200: {
            "description": "DTM atualizado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "id": "75390917-679b-4235-a5be-3d120dc38229",
                        "inputParameters": {
                            "states": ["q3", "q2", "q0", "q4", "q1"],
                            "input_symbols": ["0", "1"],
                            "tape_symbols": ["0", ".", "y", "x", "1"],
                            "transitions": {
                                "q0": {"0": ["q1", "x", "R"], "y": ["q3", "y", "R"]},
                                "q1": {
                                    "0": ["q1", "0", "R"],
                                    "1": ["q2", "y", "L"],
                                    "y": ["q1", "y", "R"],
                                },
                                "q2": {
                                    "0": ["q2", "0", "L"],
                                    "x": ["q0", "x", "R"],
                                    "y": ["q2", "y", "L"],
                                },
                                "q3": {"y": ["q3", "y", "R"], ".": ["q4", ".", "R"]},
                            },
                            "initial_state": "q0",
                            "blank_symbol": ".",
                            "final_states": ["q4"],
                        },
                    }
                }
            },
        }
    },
)
def update_dtm(dtm: UpdateDtmBodyRequestDto, id):
    updateDtmController = UpdateDtmController(repository=dtm_controller.repository)
    return updateDtmController.execute(dtm=dtm, id=id)
