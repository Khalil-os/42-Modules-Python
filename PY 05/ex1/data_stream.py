from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Base abstract class for all streams."""

    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self.processed: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None
                    ) -> List[Any]:
        """Default filter implementation."""
        if criteria is None:
            return data_batch
        return [d for d in data_batch if criteria in str(d)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "processed": self.processed
        }


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temps = [
                float(x.split(":")[1])
                for x in data_batch
                if "temp" in x
            ]

            count: int = len(data_batch)
            self.processed += count

            if not temps:
                return f"Sensor analysis: {count} readings processed"

            avg_temp: float = sum(temps) / len(temps)

            return (
                f"Sensor analysis: {count} readings processed, "
                f"avg temp: {avg_temp}°C"
            )

        except Exception as error:
            return f"Sensor processing error: {error}"


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            flow: int = 0

            for item in data_batch:
                action, value = item.split(":")
                amount: int = int(value)

                if action == "buy":
                    flow += amount
                elif action == "sell":
                    flow -= amount

            count: int = len(data_batch)
            self.processed += count

            return (f"Transaction analysis: {count} operations, "
                    f"net flow: {flow:+} units")

        except Exception as error:
            return f"Transaction processing error: {error}"


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            errors = [e for e in data_batch if "error" in e.lower()]

            count: int = len(data_batch)
            error_count: int = len(errors)

            self.processed += count

            return (
                f"Event analysis: {count} events, "
                f"{error_count} error detected"
            )

        except Exception as error:
            return f"Event processing error: {error}"


class StreamProcessor:
    """Handles multiple streams polymorphically."""

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_streams(self, batches: List[List[Any]]) -> None:
        for stream, batch in zip(self.streams, batches):
            result = stream.process_batch(batch)
            print(f"- {result}")


def main() -> None:

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    print(f"Processing sensor batch: {sensor_batch}")
    print(sensor.process_batch(sensor_batch))

    print("\nInitializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    trans_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    print(f"Processing transaction batch: {trans_batch}")
    print(trans.process_batch(trans_batch))

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    event_batch = ["login", "error", "logout"]
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    print(f"Processing event batch: {event_batch}")
    print(event.process_batch(event_batch))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    sensor_data = ["ssss:30", "sss:35"]
    trans_data = ["buy:50", "sell:10", "buy:40", "sell:5"]
    event_data = ["login", "error", "logout"]

    batches = [sensor_data, trans_data, event_data]

    print("Batch 1 Results:")
    processor.process_streams(batches)

    print("\nStream filtering active: High-priority data only")

    critical_sensors = [x for x in sensor_data if float(x.split(":")[1]) >= 30]
    large_transactions = [x for x in trans_data if int(x.split(":")[1]) > 40]

    print(f"Filtered results: {len(critical_sensors)} critical sensor alerts, "
          f"{len(large_transactions)} large transactions")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
