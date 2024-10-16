import time

from speaker import TTSSpeaker
from routine_loader import RoutineLoader, YogaRoutine
from utils import convert_number_to_countdown_string, get_random_end_of_pose_phrase, get_random_end_of_routine_phrase


SECONDS_TO_ANNOUNCE_BEFORE_END = 5


def show_and_pick_routine(available_routines: list[YogaRoutine]) -> YogaRoutine:
    print("Available Yoga Routines:")
    for idx, routine in enumerate(available_routines):
        print(f"{idx + 1}. {routine.name}")
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

    for pose in yoga_routine.poses:
        speaker.speak(pose.name)
        time.sleep(pose.time - SECONDS_TO_ANNOUNCE_BEFORE_END)
        for i in range(SECONDS_TO_ANNOUNCE_BEFORE_END, -1, -1):
            speaker.speak(f"{convert_number_to_countdown_string(i)}.")

        if pose.need_time_to_change_pose:
            speaker.speak(get_random_end_of_pose_phrase())

        time.sleep(yoga_routine.pauses_between_poses)

    speaker.speak(get_random_end_of_routine_phrase())
    print("Yoga session completed.")


if __name__ == "__main__":
    main()
