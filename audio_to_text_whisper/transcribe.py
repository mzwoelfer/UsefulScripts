import argparse
import openai
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

def transcribe_audio(input_audio_path, output_json_path):
    try:
        # Set the OpenAI API key
        openai.api_key = api_key

        # Read the audio file
        with open(input_audio_path, "rb") as audio_file:
            # Transcribe the audio
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
        
        # Create a dictionary with the transcript
        transcript_data = {
            "transcript": transcript
        }

        # Write the transcript to a JSON file
        with open(output_json_path, "w") as json_file:
            json.dump(transcript_data, json_file, indent=4)

        print(f"Transcription saved to {output_json_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe audio and save as JSON")
    parser.add_argument("input_audio", help="Path to the input audio file")
    args = parser.parse_args()

    input_audio_path = args.input_audio
    output_json_path = f"{input_audio_path}.json"

    transcribe_audio(input_audio_path, output_json_path)

