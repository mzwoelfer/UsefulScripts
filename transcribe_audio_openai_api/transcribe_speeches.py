import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


def transcribe_file(file_path):
    """
    Transcribe an audio file to text.

    Args:
        file_path (str): Path to the audio file.

    Returns:
        Text of transcription
    """


    print(f"Transcribing: {file_path}")

    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language=f"{language}",
            response_format="text",
            prompt=("Transcribe the audio"),
        )

    return transcription


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe_audio_openai_api.py <mp3-file-name>")
        sys.exit(1)

    audio_file = sys.argv[1]
    language = "en"

    filename, extension = os.path.splitext(audio_file)
    output_file = f"{filename}.txt"

    if extension != ".mp3":
        print(f"Skipping unsupported file type: {audio_file}")

    print(audio_file)
    print(output_file)
    print(filename)
    # transcription = transcribe_file(audio_file)
    # with open(output_file, "w") as output:
    #     output.write(transcription)
