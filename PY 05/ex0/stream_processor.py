from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    """Abstract base class for all processors."""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if the data is suitable for the processor."""
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return a result string."""
        pass

    def format_output(self, result: str) -> str:
        """Default output formatter."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor for numeric lists."""

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data")

            if isinstance(data, (int, float)):
                numbers: List[Union[int, float]] = [data]
            else:
                numbers = data
            count: int = len(numbers)
            total: float = sum(numbers)
            avg: float = total / count if count > 0 else 0

            result: str = (
                f"Processed {count} numeric values, sum={total}, avg={avg}"
            )
            return result

        except Exception as e:
            return f"Error processing numeric data: {e}"


class TextProcessor(DataProcessor):
    """Processor for text strings."""

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")

            text: str = data
            characters: int = len(text)
            words: int = len(text.split())

            result: str = (
                f"Processed text: {characters} characters, {words} words"
            )
            return result

        except Exception as e:
            return f"Error processing text data: {e}"


class LogProcessor(DataProcessor):
    """Processor for log messages."""

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid log entry")

            log: str = data

            levels: Dict[str, str] = {
                "ERROR": "ALERT",
                "INFO": "INFO"
            }

            for level, tag in levels.items():
                if level in log:
                    message: Optional[str] = log.split(f"{level}:")[-1].strip()
                    return f"[{tag}] {level} level detected: {message}"

            return "Unknown log level"

        except Exception as error:
            return f"Error processing log data: {error}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    numeric = NumericProcessor()
    numeric_data: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    if numeric.validate(numeric_data):
        print("Validation: Numeric data verified")
    print(numeric.format_output(numeric.process(numeric_data)))

    print("\nInitializing Text Processor...")
    text = TextProcessor()
    text_data: str = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    if text.validate(text_data):
        print("Validation: Text data verified")
    print(text.format_output(text.process(text_data)))

    print("\nInitializing Log Processor...")
    log = LogProcessor()
    log_data: str = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')
    if log.validate(log_data):
        print("Validation: Log entry verified")
    print(log.format_output(log.process(log_data)))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    data_stream: List[Any] = [
        [1, 2, 3],
        "Hello World!",
        "INFO: System ready",
    ]

    for i, (processor, data) in enumerate(zip(processors, data_stream)):
        result: str = processor.process(data)
        print(f"Result {i+1}: {result}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
