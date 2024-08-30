from src.aggregator.PortProtocolAggregator import PortProtocolAggregator
from src.mappings.FieldMapping import FieldMapping
from src.data_handler.FileHandler import FileHandler
from src.data_handler.CSVHandler import CSVHandler
from src.flow_logs.FlowLogParser import FlowLogParser
from src.flow_logs.FlowLogTags import FlowLogTags
from src.aggregator.TagAggregator import TagAggregator
from src.mappings.PortProtocolMapping import PortProtocolMapping
from src.aggregator.AggregationContext import AggregationContext
from config import Config


def main():
    print("Execution Started!")

    fields_mapping = Config.FIELDS_MAPPING

    logs = FileHandler.read_file(Config.FLOW_LOG_TEXT_FILE)

    flow_log_parser = FlowLogParser(FieldMapping(fields_mapping))
    flow_log_parser.parse_logs(logs)

    lookup_table = CSVHandler.read_file(Config.LOOKUP_TABLE_FILE)
    flow_log_tags = FlowLogTags.load_from_data(lookup_table)

    port_protocol_mapping = PortProtocolMapping(Config.PORT_PROTOCOL_MAPPING)

    # Strategy pattern implemented
    tag_aggregator = TagAggregator(flow_log_parser.get_flow_logs(), flow_log_tags, port_protocol_mapping)
    port_protocol_aggregator = PortProtocolAggregator(flow_log_parser.get_flow_logs(), port_protocol_mapping)
    aggregation_context = AggregationContext(tag_aggregator)

    # Tag data aggregation
    aggregation_context.aggregate_data()
    tag_data = aggregation_context.return_aggregated_data()
    # Writing output to file
    CSVHandler.write_file(Config.TAG_AGGREGATION_FILE, tag_data[1], tag_data[0])

    # Port Protocol data aggregation
    aggregation_context.set_strategy(port_protocol_aggregator)
    aggregation_context.aggregate_data()
    port_protocol_data = aggregation_context.return_aggregated_data()
    # Writing output to file
    CSVHandler.write_file(Config.PORT_PROTOCOL_AGGREGATION_FILE, port_protocol_data[1], port_protocol_data[0])

    print("Execution Completed!")


if __name__ == "__main__":
    main()








