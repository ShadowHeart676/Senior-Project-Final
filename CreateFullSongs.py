from midiutil import MIDIFile


def CreateMusic(song, noteDuration, recordingNum):
    if len(song) == len(noteDuration):
        x=0
        while(x<len(noteDuration)):
            degrees  = song  # MIDI note number
            track    = 0
            channel  = 0
            time     = 0    # In beats
            duration = noteDuration[x]    # In beats
            tempo    = 60  # In BPM
            volume   = 100  # 0-127, as per the MIDI standard
            x+=1
            MyMIDI = MIDIFile(1)  # One track
            MyMIDI.addTempo(track, time, tempo)

            for i, pitch in enumerate(degrees):
                MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

        with open("CreatedMusic/Recording"+ str(recordingNum) +".mid", "wb") as output_file:
            MyMIDI.writeFile(output_file)