import os
from TTS.api import TTS  # type: ignore


class TTSSpeaker:
    def __init__(self) -> None:
        self.__tts = TTS(model_name="tts_models/en/ljspeech/vits")

    def speak(self, text: str) -> None:
        text_to_speak = self.__ensure_ends_with_dot(text)
        self.__create_wav_file(text_to_speak)
        self.__play_wav_file()

    def __create_wav_file(self, text: str) -> None:
        self.__tts.tts_to_file(text=text, file_path="output.wav")

    def __play_wav_file(self) -> None:
        os.system("aplay output.wav")

    def __ensure_ends_with_dot(self, text: str) -> str:
        if not text.endswith("."):
            text += "."
        return text
