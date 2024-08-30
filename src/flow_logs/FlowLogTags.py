from typing import List, Dict


class FlowLogTags:
    """Handles loading and querying the lookup table for port/protocol to tag mappings."""
    def __init__(self, table_data: Dict):
        self.table = table_data

    @staticmethod
    def load_from_data(data: List[Dict]) -> 'FlowLogTags':
        """
        Loads the lookup table from a CSV file
        :param data: The list of dict contaning the mapping
        :return: Returns LookupTable object
        """
        mapping_data = dict()
        for row in data:
            mapping_data[(int(row['dstport']), row['protocol'].lower())] = row['tag']

        return FlowLogTags(mapping_data)

    def get_tag(self, dstport, protocol):
        """Returns the tag for a given port and protocol."""
        return self.table.get((dstport, protocol.lower()), "Untagged")

    def __repr__(self):
        return f"FlowLogTags({self.table})"
