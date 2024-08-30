from typing import Dict

from src.mappings.FieldMapping import FieldMapping


class FlowLogTags:
    """Handles loading and querying the lookup table for port/protocol to tag mappings."""
    def __init__(self, table_data: Dict):
        self.table = table_data

    @staticmethod
    def load_from_data(data, field_mapping: FieldMapping) -> 'FlowLogTags':
        """
        Loads the lookup table from a CSV file
        :param field_mapping: FieldMapping object for this
        :param data: The list of dict contaning the mapping
        :return: Returns LookupTable object
        """
        mapping_data = dict()

        for row in data:

            dstport_index = field_mapping.get_field_index("dstport")
            protocol_index = field_mapping.get_field_index("protocol")
            tag_index = field_mapping.get_field_index("tag")

            mapping_data[(int(row[dstport_index]), row[protocol_index].lower())] = row[tag_index]

        return FlowLogTags(mapping_data)

    def get_tag(self, dstport, protocol):
        """Returns the tag for a given port and protocol."""
        return self.table.get((dstport, protocol.lower()), "Untagged")

    def __repr__(self):
        return f"FlowLogTags({self.table})"
