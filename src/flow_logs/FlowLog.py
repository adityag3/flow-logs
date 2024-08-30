from typing import List

from ..mappings import FieldMapping


class FlowLog:
    """Represents a flexible flow log entry."""

    def __init__(self, attributes):
        self.attributes = attributes

    @staticmethod
    def from_list(flow_log_list: List[str], field_mapping: FieldMapping) -> 'FlowLog':
        """
        Parses a flow log string based on a field mapping and returns a FlowLog object.
        :param flow_log_list: The log data list to parse.
        :param field_mapping: A FieldMapping object defining which fields to extract.
        :return: A FlowLog object with dynamically assigned attributes.
        """
        attributes = {}

        for key in field_mapping.mapping.keys():
            index = field_mapping.get_field_index(key)
            if index is not None and index < len(flow_log_list):

                # TODO: Better logic/strategy to do this type casting
                if flow_log_list[index].isdigit():
                    attributes[key] = int(flow_log_list[index])
                else:
                    attributes[key] = flow_log_list[index]

        return FlowLog(attributes)

    def __getitem__(self, key):
        """Allows for dynamic attribute access."""
        return self.attributes.get(key, None)

    def __repr__(self):
        return f"FlowLog({self.attributes})"
