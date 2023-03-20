from midiutil.MidiFile import MIDIFile

# create MIDI file
midi_file = MIDIFile(1)

# set tempo and time signature
midi_file.addTempo(0, 0, 120)
midi_file.addTimeSignature(0, 0, 4, 2, 24)

# define notes and durations
notes = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76]
durations = [0.25, 0.5, 0.75, 1.0]

# add notes to MIDI file
for i in range(10):
    note = notes[i]
    duration = durations[random.randint(0, 3)]
    midi_file.addNote(0, 0, note, i, duration, 100)

# write MIDI file to disk
with open("output.mid", "wb") as output_file:
    midi_file.writeFile(output_file)
