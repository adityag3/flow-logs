# Flow Logs Insights


## Description
Quick working solution for the given problem statement by Illumino. Avoiding adding more info about the problem statement as the repo is public.

### Project Structure
| Path                      | Type           | Description                                                 |
|---------------------------|----------------|-------------------------------------------------------------|
| `src/`                    | Directory      | Contains the main source code for the project.              |
| `src/main.py` | File        | Contains orchestration code for running this project.           |
| `src/data_handler/`       | Directory      | Contains modules related to data handling.                  |
| `src/aggregator/`            | Directory      | Contains modules for data aggregations.                |
| `src/flow_logs` | Directory           | Contains modules of all flow log related logic.                      |
| `src/mappings` | Directory      | Contains modules of all dynamic mappings we are loading at runtime.                 |
| `tests/`                  | Directory      | Contains unit tests for the project.                        |
| `README.md`               | File           | Provides an overview of the project and documentation.      |
| `requirements.txt`        | File           | Lists the dependencies required to run the project.         |
| `LICENSE`                 | File           | Contains the licensing information for the project.         |

### Instructions to run
- Add the concerned input files in `/data` directory
- If required, change the file names in `config.py`
- If schema change in flow log, change the `FIELDS_MAPPING` class variable in `config.py`
- Run `main.py` using the command `python3 main.py`

## Assumptions
- `Port` in 2nd aggregation requirement in problem statement refers to `dstport`
- `protocol` number is provided (which is protocol code) in flow log so using the port to protocol mapping to find the protocol name.
- Required fields would always be present in flow logs.
- There cannot be case in-consistency in the logs.
- The protocol number is always valid and thus present in mapping.

## Future Work
- Implement Interfaces and base classes to make code more extensible.
- Better Exception handling and logging. 
- Add unit & functional tests.

## Notes
- Python allows loose OOD. Example, allowed implementing Strategy pattern with different constructor parameters
- Schemas were added where ever possible to avoid hard-coding and dynamically load 

