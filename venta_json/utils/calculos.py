from abc import ABC, abstractmethod
from typing import Any, Optional, Union


class Icalculo(ABC):
    @abstractmethod
    def cal_iva(self, iva: float = 0.12, valor: float = 0) -> float:
        pass

    @abstractmethod
    def cal_discount(self, valor: float = 0, discount: float = 0) -> float:
        pass

# ical = Icalculo()