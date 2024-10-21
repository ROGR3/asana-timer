from dataclasses import dataclass
from enum import Enum
import json
import os
from typing import Optional


class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


@dataclass(frozen=True)
class YogaRoutine:
    name: str
    description: str
    pauses_between_poses: int
    difficulty: Difficulty
    poses: list["YogaPose"]

    @property
    def estimated_time(self) -> int:
        total_pose_time = sum(pose.time for pose in self.poses)
        total_pause_time = self.pauses_between_poses * (len(self.poses) - 1)
        return total_pose_time + total_pause_time


@dataclass(frozen=True)
class YogaPose:
    name: str
    sanskrit: str
    time: int
    time_to_prepare_next_pose: Optional[int] = None


class RoutineLoader:
    __ROUTINES_BASE_FOLDER = "./routines/"

    @staticmethod
    def load_routine_list() -> list[YogaRoutine]:

        yoga_routines = []
        for file in os.listdir(RoutineLoader.__ROUTINES_BASE_FOLDER):
            if not file.endswith(".json"):
                continue

            file_path = RoutineLoader.__ROUTINES_BASE_FOLDER + file
            print(file_path)
            with open(file_path, "r", encoding="utf-8") as json_file:
                json_data = json.load(json_file)
                yoga_routines.append(
                    YogaRoutine(
                        name=json_data["name"],
                        description=json_data["description"],
                        pauses_between_poses=json_data["pauses_between_poses"],
                        poses=[YogaPose(**pose) for pose in json_data["poses"]],
                        difficulty=Difficulty(json_data["difficulty"]),
                    )
                )

        return yoga_routines
