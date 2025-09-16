import time

from speaker import TTSSpeaker
from routine_loader import RoutineLoader, YogaRoutine
from utils import convert_number_to_countdown_string, get_random_end_of_pose_phrase, get_random_end_of_routine_phrase


SECONDS_TO_ANNOUNCE_BEFORE_END = 5


def round_to_nearest_tens(value: int) -> int:
    return round(value / 10) * 10


def calculate_total_time(yoga_routine: YogaRoutine) -> int:
    total_pose_time = sum(pose.time for pose in yoga_routine.poses)
    total_pause_time = yoga_routine.pauses_between_poses * (len(yoga_routine.poses) - 1)
    total_time = total_pose_time + total_pause_time
    return round_to_nearest_tens(total_time)


def show_and_pick_routine(available_routines: list[YogaRoutine]) -> YogaRoutine:
    print("Available Yoga Routines:")
    for idx, routine in enumerate(available_routines):
        print(f"{idx + 1}. {routine.name} ({calculate_total_time(routine)} seconds)")
    print("Choose a routine by entering the corresponding number:")

    choice = int(input()) - 1
    return available_routines[choice]


def main() -> None:
    available_routines = RoutineLoader.load_routine_list()

    yoga_routine = show_and_pick_routine(available_routines)

    print(f"Selected routine: {yoga_routine.name}")

    speaker = TTSSpeaker()

    speaker.speak(f"You have selected the {yoga_routine.name}. {yoga_routine.description}")
    speaker.speak("Let's begin the session.")

    for idx, pose in enumerate(yoga_routine.poses):
        if yoga_routine.pauses_between_poses != 0 and pose.time > SECONDS_TO_ANNOUNCE_BEFORE_END:
            speaker.speak(f"{pose.name} - {pose.sanskrit}")
            time.sleep(pose.time - SECONDS_TO_ANNOUNCE_BEFORE_END)
            for i in range(SECONDS_TO_ANNOUNCE_BEFORE_END, 0, -1):
                speaker.speak(f"{convert_number_to_countdown_string(i)}.")

            if idx < len(yoga_routine.poses) - 1:
                speaker.speak(get_random_end_of_pose_phrase(yoga_routine.poses[idx + 1].name))
                time.sleep(yoga_routine.pauses_between_poses)
        else:
            speaker.speak(f"{pose.name}")
            if pose.time - SECONDS_TO_ANNOUNCE_BEFORE_END > 0:
                time.sleep(pose.time - SECONDS_TO_ANNOUNCE_BEFORE_END)
            for i in range(min(SECONDS_TO_ANNOUNCE_BEFORE_END, pose.time), 0, -1):
                speaker.speak(f"{convert_number_to_countdown_string(i)}.")

    speaker.speak(get_random_end_of_routine_phrase())
    print("Yoga session completed.")


if __name__ == "__main__":
    main()
