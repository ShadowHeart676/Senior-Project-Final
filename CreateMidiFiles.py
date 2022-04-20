from midiutil import MIDIFile

def CreateNotes():
    FileName = ["LowC.mid","LowC#.mid","LowD.mid","LowD#.mid","LowE.mid","LowF.mid","LowF#.mid","LowG.mid","LowG#.mid","LowA.mid","LowA#.mid","LowB.mid",
                "C.mid","C#.mid","D.mid","D#.mid","E.mid","F.mid","F#.mid","G.mid","G#.mid","A.mid","A#.mid","B.mid",
                "HighC.mid","HighC#.mid","HighD.mid","HighD#.mid","HighE.mid","HighF.mid","HighF#.mid","HighG.mid","HighG#.mid","HighA.mid","HighA#.mid","HighB.mid"]

    pitchNum = 48
    for index in FileName:
        MyMIDI = MIDIFile(1)
        track = 0
        time = 0
        MyMIDI.addTrackName(track, time, index)
        MyMIDI.addTempo(track, time, 120)
        channel = 0
        pitch = pitchNum
        duration = 10
        volume = 100
        MyMIDI.addNote(track, channel, pitch, time, duration, volume)

        with open("CodeCreatedSounds/"+index, 'wb') as binfile:
            MyMIDI.writeFile(binfile)
        pitchNum += 1
