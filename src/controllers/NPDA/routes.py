from automata.fa.dfa import DFA
from repositories import InMemoryNpdaRepository
from fastapi import APIRouter
from .create_npda_controller import CreateNpdaController, CreateNpdaBodyRequestDto
from .get_npda_controller import GetNpdaController
from .fetch_npdas_controller import FetchNpdasController
from .npda_save_image_controller import NpdaSaveImageController
from .npda_accept_strings_controller import NpdaAcceptStringsController
from .update_npda_controller import UpdateNpdaController, UpdateNpdaBodyRequestDto


class NpdaController:

    def __init__(self):
        self.repository = InMemoryNpdaRepository()


npda_controller = NpdaController()
router = APIRouter()


@router.get(
    "/npda/{id}",
    summary="Obter NPDA por ID",
    description="Recupera um NPDA a partir do seu ID.",
    response_model=None,
    tags=["Non-deterministic Pushdown Automaton"],
    status_code=200,
    responses={
        200: {
            "description": "NPDA listado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "id": "3af1cda7-75f4-4c83-9d6c-d07c6c28c90d",
                        "inputParameters": {
                            "states": ["q1", "q2", "q0"],
                            "input_symbols": ["b", "a"],
                            "stack_symbols": ["A", "#", "B"],
                            "transitions": {},
                            "initial_state": "q0",
                            "initial_stack_symbol": "#",
                            "final_states": ["q2"],
                            "acceptance_mode": "final_state",
                        },
                    }
                }
            },
        }
    },
)
def get_npda(id):
    getNpdaController = GetNpdaController(repository=npda_controller.repository)
    return getNpdaController.execute(id=id)


@router.get(
    "/npda/{id}/accept/{string:path}",
    summary="Verificar se o NPDA aceita a string",
    description="Verifica se o NPDA identificado pelo ID aceita a string fornecida.",
    response_model=None,
    tags=["Non-deterministic Pushdown Automaton"],
    status_code=200,
    responses={
        200: {
            "description": "Aceitação da palavra verificada com sucesso.",
            "content": {
                "application/json": {
                    "example": {"string": "ababaabaabaababa", "isValid": True}
                }
            },
        }
    },
)
def accept_string(id, string=""):
    acceptStringsController = NpdaAcceptStringsController(
        repository=npda_controller.repository
    )
    return acceptStringsController.execute(id=id, string=string)


@router.post(
    "/npda/{id}/image",
    summary="Salvar imagem do NPDA",
    description="Gera e salva uma imagem do NPDA identificado pelo ID.",
    response_model=None,
    tags=["Non-deterministic Pushdown Automaton"],
    status_code=200,
    responses={
        200: {
            "description": "Imagem NPDA salva com sucesso",
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
    saveImageController = NpdaSaveImageController(repository=npda_controller.repository)
    return saveImageController.execute(id=id)


@router.get(
    "/npda",
    summary="Listar todos os NPDAs",
    description="Recupera todos os NPDAs armazenados.",
    response_model=None,
    tags=["Non-deterministic Pushdown Automaton"],
    status_code=200,
    responses={
        200: {
            "description": "NPDA's listados com sucesso",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": "3af1cda7-75f4-4c83-9d6c-d07c6c28c90d",
                            "inputParameters": {
                                "states": ["q1", "q2", "q0"],
                                "input_symbols": ["b", "a"],
                                "stack_symbols": ["A", "#", "B"],
                                "transitions": {},
                                "initial_state": "q0",
                                "initial_stack_symbol": "#",
                                "final_states": ["q2"],
                                "acceptance_mode": "final_state",
                            },
                        }
                    ]
                }
            },
        }
    },
)
def fetch_npda():
    fetchNpdasController = FetchNpdasController(repository=npda_controller.repository)
    return fetchNpdasController.execute()


@router.post(
    "/npda",
    summary="Criar um novo NPDA",
    description="Cria um novo NPDA a partir do corpo da solicitação.",
    response_model=None,
    tags=["Non-deterministic Pushdown Automaton"],
    status_code=201,
    responses={
        201: {
            "description": "NPDA criado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "id": "3af1cda7-75f4-4c83-9d6c-d07c6c28c90d",
                        "inputParameters": {
                            "states": ["q1", "q2", "q0"],
                            "input_symbols": ["b", "a"],
                            "stack_symbols": ["A", "#", "B"],
                            "transitions": {},
                            "initial_state": "q0",
                            "initial_stack_symbol": "#",
                            "final_states": ["q2"],
                            "acceptance_mode": "final_state",
                        },
                    }
                }
            },
        }
    },
)
def create_npda(npda: CreateNpdaBodyRequestDto):
    createNpdaController = CreateNpdaController(repository=npda_controller.repository)
    return createNpdaController.execute(npda=npda)


@router.put(
    "/npda/{id}",
    summary="Atualizar um NPDA existente",
    description="Atualiza um NPDA existente com base no ID e nas informações fornecidas.",
    response_model=None,
    tags=["Non-deterministic Pushdown Automaton"],
    status_code=200,
    responses={
        200: {
            "description": "NPDA atualizado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "id": "3af1cda7-75f4-4c83-9d6c-d07c6c28c90d",
                        "inputParameters": {
                            "states": ["q1", "q2", "q0"],
                            "input_symbols": ["b", "a"],
                            "stack_symbols": ["A", "#", "B"],
                            "transitions": {},
                            "initial_state": "q0",
                            "initial_stack_symbol": "#",
                            "final_states": ["q2"],
                            "acceptance_mode": "final_state",
                        },
                    }
                }
            },
        }
    },
)
def update_npda(npda: UpdateNpdaBodyRequestDto, id):
    updateNpdaController = UpdateNpdaController(repository=npda_controller.repository)
    return updateNpdaController.execute(npda=npda, id=id)
