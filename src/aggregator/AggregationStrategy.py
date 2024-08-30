from abc import ABC, abstractmethod
from typing import List, Tuple


class AggregationStrategy(ABC):
    @abstractmethod
    def aggregate(self) -> None:
        pass

    @abstractmethod
    def return_aggregation(self) -> Tuple[List[str], List[List]]:
        pass
