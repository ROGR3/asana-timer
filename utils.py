import random

END_OF_POSE_PHRASES = [
    "Let go.",
    "Release.",
    "Relax.",
    "Unwind.",
    "Ease out.",
]

POSE_ANNOUNCEMENT_PHRASES = [
    "{new_pose} is coming up.",
    "{new_pose} is just ahead.",
    "{new_pose} is about to arrive.",
    "{new_pose} is on the way.",
    "Next pose is {new_pose}.",
    "Prepare for {new_pose}.",
    "Get ready for {new_pose}.",
]


END_OF_ROUTINE_PHRASES = [
    "Namaste!",
    "Namaste! Routine completed!",
    "Namaste! Session completed!",
]


def get_random_end_of_pose_phrase(next_pose: str) -> str:
    return f"{random.choice(END_OF_POSE_PHRASES)} {random.choice(POSE_ANNOUNCEMENT_PHRASES).format(new_pose=next_pose)}"


def get_random_end_of_routine_phrase() -> str:
    return random.choice(END_OF_ROUTINE_PHRASES)


def convert_number_to_countdown_string(number: int) -> str:
    if number == 1:
        return "one"
    if number == 2:
        return "two"
    if number == 3:
        return "three"
    if number == 4:
        return "four"
    if number == 5:
        return "five"
    if number == 6:
        return "six"
    if number == 7:
        return "seven"
    if number == 8:
        return "eight"
    if number == 9:
        return "nine"
    if number == 10:
        return "ten"

    raise Exception("Could not translate number to countdown string")
