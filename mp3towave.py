from pydub import AudioSegment

def convert_mp3_to_wav(mp3_file, wav_file):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_file)

    # Export the audio as WAV file
    audio.export(wav_file, format='wav')

# Provide the file paths for the input MP3 file and desired output WAV file
mp3_file_path = 'C:\Users\hpZBOOK\Desktop\dsp\FurElise_Slow.mp3'
wav_file_path = 'FurElise_Slow.wav'

# Convert MP3 to WAV
convert_mp3_to_wav(mp3_file_path, wav_file_path)
