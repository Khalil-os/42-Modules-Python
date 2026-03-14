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
                return f"Sensor data: {count} readings processed"

            avg_temp: float = sum(temps) / len(temps)

            return (
                f"Sensor analysis: {count} readings processed, "
                f"avg temp: {avg_temp}°C"
            )

        except Exception as error:
            return f"Sensor processing error: {error}"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None
                    ) -> List[Any]:
        if criteria == "critical":
            return [x for x in data_batch
                    if "temp" in x and float(x.split(":")[1]) >= 30]
        return super().filter_data(data_batch, criteria)


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

            if flow == 0:
                return f"Transaction data: {count} operations processed"

            return (
                f"Transaction analysis: {count} operations, "
                f"net flow: {flow:+} units"
            )

        except Exception as error:
            return f"Transaction processing error: {error}"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None
                    ) -> List[Any]:
        if criteria == "large":
            return [x for x in data_batch
                    if int(x.split(":")[1]) > 40]
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            errors = [e for e in data_batch if "error" in e.lower()]

            count: int = len(data_batch)
            error_count: int = len(errors)

            self.processed += count

            if error_count == 0:
                return f"Event data: {count} events processed"

            return (
                f"Event analysis: {count} events, "
                f"{error_count} error detected"
            )

        except Exception as error:
            return f"Event processing error: {error}"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None
                    ) -> List[Any]:
        if criteria == "error":
            return [
                e for e in data_batch
                if "error" in e.lower()
            ]

        return super().filter_data(data_batch, criteria)


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

    processor_sensor_batch = ["humidity:30", "pressure:1000"]
    processor_trans_batch = ["buy:10", "sell:10", "buy:5", "sell:5"]
    processor_event_batch = ["login", "start", "logout"]

    batches = [
        processor_sensor_batch,
        processor_trans_batch,
        processor_event_batch
    ]

    print("\nBatch 1 Results:")
    processor.process_streams(batches)

    sensor_data = ["temp:30", "temp:35"]
    trans_data = ["buy:50", "sell:10", "buy:40", "sell:5"]

    print("\nStream filtering active: High-priority data only")

    critical_sensors = sensor.filter_data(sensor_data, "critical")
    large_transactions = trans.filter_data(trans_data, "large")

    print(f"Filtered results: {len(critical_sensors)} critical sensor alerts, "
          f"{len(large_transactions)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
