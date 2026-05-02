from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        has_leader = any(
            member.rank in (Rank.commander, Rank.captain)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        if self.duration_days > 365:
            experienced = [
                m for m in self.crew if m.years_experience >= 5
            ]
            if len(experienced) < len(self.crew) / 2:
                raise ValueError(
                    "Long missions need at least 50% experienced crew"
                )
        if any(not m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def display_mission(mission: SpaceMission) -> None:
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - "
            f"{member.specialization}"
        )


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)

    valid_data = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": "2026-05-01T10:00:00",
        "duration_days": 900,
        "budget_millions": 2500.0,
        "crew": [
            {
                "member_id": "001",
                "name": "Sarah Connor",
                "rank": "commander",
                "age": 45,
                "specialization": "Mission Command",
                "years_experience": 20,
            },
            {
                "member_id": "002",
                "name": "John Smith",
                "rank": "lieutenant",
                "age": 35,
                "specialization": "Navigation",
                "years_experience": 10,
            },
            {
                "member_id": "003",
                "name": "Alice Johnson",
                "rank": "officer",
                "age": 30,
                "specialization": "Engineering",
                "years_experience": 6,
            },
        ],
    }

    try:
        mission = SpaceMission(**valid_data)
        display_mission(mission)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))
    print("")
    print("=" * 41)

    invalid_data = {
        "mission_id": "M2024_FAIL",
        "mission_name": "Test Mission",
        "destination": "Moon",
        "launch_date": "2026-05-01T10:00:00",
        "duration_days": 100,
        "budget_millions": 500.0,
        "crew": [
            {
                "member_id": "004",
                "name": "Bob",
                "rank": "officer",
                "age": 28,
                "specialization": "Science",
                "years_experience": 2,
            }
        ],
    }

    try:
        SpaceMission(**invalid_data)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
