from midiutil import MIDIFile
import numpy as np
import librosa
audio_file = 'C:\\Users\\hpZBOOK\\Desktop\\dsp\\FurElise_Slow.wav'
y, sr = librosa.load(audio_file)
window = np.hamming(len(y))
y_windowed = y * window


hop_length = 512 
D = librosa.stft(y_windowed, hop_length=hop_length)
magnitude = np.abs(D)
frequencies = librosa.fft_frequencies(sr=sr, n_fft=len(window))

note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
peaks = librosa.util.peak_pick(magnitude, 3, 3, 3, 5, 0.5, 10)
notes = np.round(12 * np.log2(frequencies[peaks] / 440)) + 69 
note_names = [note_names[int(note) % 12] for note in notes] 

print(note_names)


midi = MIDIFile(1)
track = 0
time = 0

for note in notes:
    duration = 1  
    velocity = 80  
    midi.addNote(track, 0, int(note), time, duration, velocity)
    time += duration


with open('extracted_notes.mid', 'wb') as file:
    midi.writeFile(file)
