from src.aggregator.AggregationStrategy import AggregationStrategy


class AggregationContext:
    def __init__(self, strategy: AggregationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: AggregationStrategy) -> None:
        self._strategy = strategy

    def aggregate_data(self) -> None:
        self._strategy.aggregate()

    def return_aggregated_data(self):
        return self._strategy.return_aggregation()
