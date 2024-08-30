class FieldMapping:
    def __init__(self, mapping: dict):
        """
        Initializes a FieldMapping object with a mapping dictionary.
        :param mapping: A dictionary mapping field names to their positions in the log string.
        """
        self.mapping = mapping

    def get_field_index(self, field_name: str) -> int:
        """
        Returns the index of the field in the log string.
        :param field_name: The name of the field.
        :return: The index of the field.
        """
        return self.mapping.get(field_name, None)

    def __repr__(self):
        return f"FieldMapping({self.mapping})"
