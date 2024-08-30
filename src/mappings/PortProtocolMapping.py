class PortProtocolMapping:
    def __init__(self, mapping: dict):
        """
        Initializes a PortProtocolMapping object with a mapping dictionary.
        :param mapping: A dictionary mapping port to their protocol.
        """
        self.mapping = mapping
        self.reversed_mapping = {value: key for key, value in mapping.items()}

    def get_protocol(self, port: int) -> str:
        """
        Returns the index of the field in the log string.
        :param port: The numeric digit representing the port.
        :return: The index of the protocol name.
        """
        return self.mapping.get(int(port), "").lower()

    def get_port(self, protocol: str) -> int:
        """
        Returns the index of the field in the log string.
        :param protocol: The string representing the protocol.
        :return: The index of the protocol name.
        """
        return self.mapping.get(protocol.upper(), None)

    def __repr__(self):
        return f"PortProtocolMapping({self.mapping})"
