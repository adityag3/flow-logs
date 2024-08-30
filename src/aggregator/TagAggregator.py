from typing import List, Tuple, Dict
from collections import Counter

from src.aggregator.AggregationStrategy import AggregationStrategy
from . import FlowLogTags
from . import FlowLog
from src.mappings.PortProtocolMapping import PortProtocolMapping


class TagAggregator(AggregationStrategy):
    def __init__(self, flow_logs: List[FlowLog], flow_log_tags: FlowLogTags, port_protocol_mapping: PortProtocolMapping):
        self._flow_logs = flow_logs
        self._flow_log_tags = flow_log_tags
        self._tag_count = Counter()
        self._port_protocol_mapping = port_protocol_mapping

    def aggregate(self) -> None:
        for flow_log in self._flow_logs:
            # print(flow_log["dstport"], flow_log["protocol"])
            dstport = flow_log["dstport"]
            protocol_name = self._port_protocol_mapping.get_protocol(flow_log["protocol"])
            tag = self._flow_log_tags.get_tag(dstport, protocol_name)
            self._tag_count[tag] += 1

    def return_aggregation(self) -> Tuple[List[str], List[Dict]]:
        return_data = list()
        field_names = ["Tag", "Count"]
        tags_data = [list(data) for data in list(self._tag_count.items())]

        for data_row in tags_data:
            tmp_dict = dict()
            for index in range(len(field_names)):
                tmp_dict[field_names[index]] = data_row[index]
            return_data.append(tmp_dict)
        return field_names, return_data

    def __repr__(self):
        return f"TagAggregator({self._tag_count})"



