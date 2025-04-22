from abc import ABC, abstractmethod
from typing import Any, Optional, List, Dict


class ICrud(ABC):

    @abstractmethod
    def create(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass

    @abstractmethod
    def consult(self) -> None:
        pass