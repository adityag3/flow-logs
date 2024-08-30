from typing import List, Optional
from src.mappings.FieldMapping import FieldMapping
from src.flow_logs.FlowLog import FlowLog


class FlowLogParser:
    def __init__(self, field_mapping: FieldMapping):
        """
        Initializes the FlowLogParser with a field mapping.
        :param field_mapping: A FieldMapping object defining which fields to extract.
        """
        self.field_mapping = field_mapping
        self.flow_logs = []

    def parse_logs(self, log_data_list: List[List[str]]) -> None:
        """
        Parses a list of log strings and generates FlowLog objects.
        :param log_data_list: A list of log data.
        """
        self.flow_logs = [FlowLog.from_list(log_data, self.field_mapping) for log_data in log_data_list]

    def get_flow_logs(self) -> List[FlowLog]:
        """
        Returns the list of FlowLog objects.
        :return: A list of FlowLog objects.
        """
        return self.flow_logs

    def find_log_by_field(self, field_name: str, value: str) -> Optional[FlowLog]:
        """
        Finds a FlowLog object where the specified field matches the given value.
        :param field_name: The field name to search by.
        :param value: The value to match.
        :return: A FlowLog object if found, otherwise None.
        """
        for log in self.flow_logs:
            if log[field_name] == value:
                return log
        return None

    def __repr__(self):
        return f"FlowLogParser(field_mapping={self.field_mapping}, flow_logs={self.flow_logs})"
