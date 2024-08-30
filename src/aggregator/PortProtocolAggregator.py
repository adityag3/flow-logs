from typing import List, Tuple, Dict
from collections import Counter

from src.aggregator.AggregationStrategy import AggregationStrategy
from . import FlowLog
from src.mappings.PortProtocolMapping import PortProtocolMapping


class PortProtocolAggregator(AggregationStrategy):
    def __init__(self, flow_logs: List[FlowLog], port_protocol_mapping: PortProtocolMapping):
        self._flow_logs = flow_logs
        self._tag_count = Counter()
        self._port_protocol_mapping = port_protocol_mapping

    def aggregate(self) -> None:
        for flow_log in self._flow_logs:
            port = flow_log["dstport"]
            protocol = flow_log["protocol"]
            self._tag_count[(port, protocol)] += 1

    def return_aggregation(self) -> Tuple[List[str], List[Dict]]:
        return_data = list()
        field_names = ["Port", "Protocol", "Count"]
        tags_data = [[data[0][0], self._port_protocol_mapping.get_protocol(data[0][1]), data[1]] for data in list(self._tag_count.items())]

        for data_row in tags_data:
            tmp_dict = dict()
            for index in range(len(field_names)):
                tmp_dict[field_names[index]] = data_row[index]
            return_data.append(tmp_dict)

        return field_names, return_data



