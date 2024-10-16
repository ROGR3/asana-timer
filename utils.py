import random

END_OF_POSE_PHRASES = [
    "Well done! Transitioning to the next pose.",
    "Great job! Get ready for the next one.",
    "Take a deep breath and prepare for the next pose.",
    "You are doing amazing! Let's move on.",
    "Stay focused and ready for the next.",
    "Awesome work! Next pose coming up.",
    "Excellent! Let's move on to the next pose.",
    "Embrace the moment, next pose is coming.",
    "Breathe deeply, and get ready for the next pose.",
    "You're shining! On to the next pose now.",
    "Wonderful effort! Next pose is just ahead.",
]

END_OF_HOLD_PHRASES = ["Let go.", "Release.", "Relax.", "Unwind.", "Feel the release.", "Ease out."]
END_OF_ROUTINE_PHRASES = ["Namaste!", "Routine completed!", "Yoga session ended!", "Yoga routine ended!"]


def get_random_end_of_pose_phrase() -> str:
    return random.choice(END_OF_POSE_PHRASES)


def get_random_end_of_routine_phrase() -> str:
    return random.choice(END_OF_ROUTINE_PHRASES)


def convert_number_to_countdown_string(number: int) -> str:
    if number == 0:
        return random.choice(END_OF_HOLD_PHRASES)
    if number == 0:
        return "zero"
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
