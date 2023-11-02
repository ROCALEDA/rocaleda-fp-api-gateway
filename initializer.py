from fastapi import FastAPI

from app.authentication.controllers import authentication_controller
from app.authentication.services.authentication_service import AuthenticationService
from app.authentication.repositories.authentication_repository import (
    AuthenticationRepository,
)
from app.candidate.controllers import candidate_controller
from app.candidate.repositories.candidate_repository import CandidateRepository
from app.candidate.services.candidate_service import CandidateService
from app.customer.controllers import customer_controller
from app.customer.repositories.customer_repository import CustomerRepository
from app.customer.services.customer_service import CustomerService
from app.health.controllers import health_controller
from app.health.services.health_service import HealthService
from app.position.controllers import position_controller
from app.position.repositories.position_repository import PositionRepository
from app.position.services.position_service import PositionService


class Initializer:
    def __init__(self, app: FastAPI):
        self.app = app

    def setup(self):
        self.init_health_module()
        self.init_authentication_module()
        self.init_candidate_module()
        self.init_customer_module()
        self.init_position_module()

    def init_health_module(self):
        print("Initializing health module")
        health_service = HealthService()
        health_controller.initialize(health_service)
        self.app.include_router(health_controller.router)

    def init_authentication_module(self):
        print("Initializing authentication module")
        authentication_repository = AuthenticationRepository()
        authentication_service = AuthenticationService(authentication_repository)
        authentication_controller.initialize(authentication_service)
        self.app.include_router(authentication_controller.router)

    def init_candidate_module(self):
        print("Initializing candidate module")
        candidate_repository = CandidateRepository()
        candidate_service = CandidateService(candidate_repository)
        candidate_controller.initialize(candidate_service)
        self.app.include_router(candidate_controller.router)

    def init_customer_module(self):
        print("Initializing customer module")
        customer_repository = CustomerRepository()
        customer_service = CustomerService(customer_repository)
        customer_controller.initialize(customer_service)
        self.app.include_router(customer_controller.router)

    def init_position_module(self):
        print("Initializing position module")
        position_repository = PositionRepository()
        position_service = PositionService(position_repository)
        position_controller.initialize(position_service)
        self.app.include_router(position_controller.router)
