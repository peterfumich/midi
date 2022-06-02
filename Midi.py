from midiutil import MIDIFile
import numpy as np
import os
base_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
base_pitches = [60, 62, 64, 65, 67, 69, 71]
Intervals = [
    "Perfect Unison",
    "Minor Second",
    "Major Second",
    "Minor Third",
    "Major Third",
    "Perfect Fourth",
    "Diminished Fifth, Augmented Fourth",
    "Perfect Fifth",
    "Minor Sixth",
    "Major Sixth",
    "Minor Seventh",
    "Major Seventh",
    "Perfect Octave"
]
Scales = [
    [["Acoustic"],[2,2,2,1,2,1,2]],
    [["Aeolian"],[2,1,2,2,1,2,2]],
    [["Algerian"],[2,1,3,1,1,3,1,2,1,2]],
    [["Altered"],[1,2,1,2,2,2,2]],
    [["Augmented"],[3,1,3,1,3,1]],
    [["Bebop"],[2,2,1,2,2,1,1,1]],
    [["Blues"],[3,2,1,1,3,2]],
    [["Chromatic"],[1,1,1,1,1,1,1,1,1,1,1,1]],
    [["Dorian"],[2,1,2,2,2,1,2]],
    [["Double Harmonic"],[1,3,1,2,1,3,1]],
    [["Enigmatic"],[1,3,2,2,2,1,1]],
    [["Flamenco"],[1,3,1,2,1,3,1]],
    [["Romani"],[2,1,3,1,1,2,2]],
    [["Half Diminished"],[2,1,2,1,2,2,2]],
    [["Harmonic Major"],[2,2,1,2,1,3,1]],
    [["Harmonic Minor"],[2,1,2,2,1,3,1]],
    [["Hirajoshi"],[4,2,1,4,1]],
    [["Hungarian minor"],[2,1,3,1,1,3,1]],
    [["Hungarian Major"],[3,1,2,1,2,1,2]],
    [["In Scale"],[1,4,2,4,2]],
    [["Ionian"],[2,2,1,2,2,2,1]],
    [["Istrian"],[1,2,1,2]],
    [["Iwato"],[1,4,1,4,2]],
    [["Locrian"],[1,2,2,1,2,2,2]],
    [["Lydian Augmented"],[2,2,2,2,1,2,1]],
    [["Lydian"],[2,2,2,1,2,2,1]],
    [["Major Bebop"],[2,2,1,2,1,1,2,1]],
    [["Major Locrian"],[2,2,1,1,2,2,2]],
    [["Major Pentatonic"],[2,2,3,2,3]],
    [["Melodic Minor Ascending"],[2,1,2,2,2,2,1]],
    [["Melodic Minor Descendng"],[2,2,1,2,2,1,2]],
    [["Minor Pentatonic"],[3,2,2,3,2]],
    [["Mixolydian"],[2,2,1,2,2,1,2]],
    [["Neapolitan Major"],[1,2,2,2,2,2,1]],
    [["Neopolitan Minor"],[1,2,2,2,1,3,1]],
    [["Octatonic 1"],[1,2,1,2,1,2,1]],
    [["Octatonic 2"],[2,1,2,1,2,1,2,1]],
    [["Persian"],[1,3,1,1,2,3,1]],
    [["Phrygian dominant"],[1,3,1,2,1,2,2]],
    [["Phrygian"],[1,2,2,2,1,2,2]],
    [["Prometheus"],[2,2,2,3,1,2]],
    [["Scale of Harmonics"],[3,1,1,2,2,3]],
    [["Tritone"],[1,3,2,1,3,2]],
    [["Two-Semitone Triton"],[1,1,4,1,1]],
    [["Ukrainian Dorian"],[2,1,3,1,2,1,2]],
    [["Vietnamese"],[2.5,.5,1,1,2]],
    [["Whole Tone"],[2,2,2,2,2,2]],
    [["Yo"],[3,2,2,3,2]]
]
Chord_Sizes = [
    ["Monad"],
    ["Dyad"],
    ["Triad"],
    ["Tetrad"],
    ["Pentad"],
    ["Hexad"],
    ["Heptad"],
    ["Octad"],
    ["Ennead"],
    ["Decad"],
]
Chord_Types = [
    [["Major"],[4,7]],
    [["Minor"],[3,7]],
    [["Augmented"],[4,8]],
    [["Diminished"],[3,6]],
    [["Power1"],[7]],
    [["Power2"],[7,12]],
    [["Power3"],[7,14]],
    [["Power4"],[7,12,14]],
    [["Suspended m"],[2,7]],
    [["Suspended M"],[5,7]],
    [["Suspended Aug m"],[2,8]],
    [["Suspended Aug M"],[5,8]],
    [["Suspended Dim m"],[2,6]],
    [["Suspended Dim M"],[5,6]]
]
    # [["Predominant"],[]],
    # [["Bitonal"], []],
    # [["Atonal"], []],
    # [["Major Third"],[]]
## MEAN OCTAVE CHANGE OVER PARTITION. have I been assumming mean of 0? ohh boy. That is DEFINE DISTRIBUTION OF INTERVALS
#  mean interval changes over partitions and variances of these
#Can have multiple of the same type of chord on a scale. A chord can be built by straddling 2 octaves.
Auto = 1

def What_Chords_are_Possible(Scale,Notes):
    Notes = sorted(set(Notes))
    possible_chords = []
    for chord  in Chord_Types:
        kord = chord[1]
        for note in Notes:
            for c in kord:
                try:
                    Notes.index(note+c)
                except:
                    break
                possible_chords.append(chord)
    return(possible_chords)
def Find_Broken_Chords(Notes,possible_chords):
    #This is going to simply sort through the list of notes and find broken chords already formed and highlight them.
    print("Working")
def Find_Arpeggios(Notes,possible_chords):
    #This is going to simply sort through the list of notes and find Arpgeggios already formed.
    print("Working")
def Build_Chords(Notes,possible_chords,arpeggios,broken):
    #This will be the hardest part, where we will attempt to INSERT/fill in chords. Part of the process will use any
    #Chords already found and then repeat them.
    #Question: Does the beat structure affect how we build chords?
    print("Working")

def Build_Scales(Manual_or_Auto,Auto_Scale_Settings):
    if Manual_or_Auto == 0 or Manual_or_Auto == "Manual":
        for i in range(len(Scales)):
            print(i, ":", Scales[i][0])
        set_of_scales = []
        print("Choose an initial Scale")
        scale = Scales[int(input())]
        print(scale)
        set_of_scales.append(scale)
        print("how many scales?")
        number_of_scales = int(input())
        num_scales_left = number_of_scales
        while num_scales_left >1:
            print("Choose",(num_scales_left - 1),"more scales")
            print("Choose another Scale")
            try:
                set_of_scales.append(Scales[int(input())])
                num_scales_left -= 1
            except:
                print("Oops a cat must have stepped on the keyboard!")
        print(set_of_scales)
    elif Manual_or_Auto == 1 or Manual_or_Auto == "Auto":
        number_of_scales = Auto_Scale_Settings[0]
        set_of_scales = []
        for r in range(number_of_scales):
            set_of_scales.append(Scales[Auto_Scale_Settings[r+1]])

            # index = np.random.randint(0, 48)
            # try:#Add each scale once!
            #     set_of_scales.index(Scales[index])#search in set of scales for a specific SCALE
            # except:
            #     set_of_scales.append(Scales[index])#If there is no such scale in Set then add it to the set
    else:
        print("Danger, Mr. Robinson")
        set_of_scales = []
    print("Scales", set_of_scales)


    return(set_of_scales)
def Build_initial_notes(Manual_or_Auto,Settings):
    set_of_notes_initial = []
    print("Building initial set of notes on which the scales will be built.")
    print("Value should be a positive integer. 60 is fairly standard, it is C")
    if Manual_or_Auto == 0:
        choose_another_note = ""
        while choose_another_note == "":
            print("Choose a note to add to the set of notes.")
            set_of_notes_initial.append(int(input()))
            print("For another note press enter, else stop by typing anything")
            choose_another_note = input()
        set_of_notes_initial = list(set(set_of_notes_initial))
    elif Manual_or_Auto == 1:
        for i in range(Settings[0]):#So Settings[0] tells us how many notes, and each entry after is the note. Hence, Random Gen can be written elsewhere!
            set_of_notes_initial.append(Settings[i+1])
    else:
        print("Danger :D ")
    return(set_of_notes_initial)
def Build_Set_of_Intervals(Manual_or_Auto,Settings):
    if Manual_or_Auto == 0:
        print("Building sets of Intervals. This will be a sequence of note spacings on an arbitrary scale,")
        print("i.e 0 will correspond to the same note, while 1 is the next note on the scale(ascending).")
        print("There are three components to each interval. [interval, number of steps of same interval, octave range]")
        print("How Many Sets of Intervals? Type an integer")
        number_of_sets = int(input())
        set_of_intervals = []
        for n in range(number_of_sets):
            intervals = []
            choose_another_interval = ""
            while choose_another_interval == "":
                interval = []
                print("Choose an interval to add to the set of notes.")
                interval.append(int(input()))
                print("How many repetitions?")
                interval.append(int(input()))
                print("Octave Range?")
                interval.append(int(input()))
                print("For another interval press enter, else stop by typing anything")
                choose_another_interval = input()
                intervals.append(interval)
            set_of_intervals.append(intervals)
    if Manual_or_Auto == 1:
        set_of_intervals = []
        number_of_sets = Settings[0]
        for n in range(number_of_sets):
            intervals = []
            number_of_intervals = Settings[n+1]
            for i in range(number_of_intervals):#Build Random Intervals?#Change distributions!
                # if i%5 ==0: #change from ascending, descending, or random
                #     movement = np.random.randint(0,2)
                #         if movement == 0:


                interval = []
                # randoms = [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]
                # random_interval = np.random.choice(randoms,1,
                #                 p=[.0,0,.05,.05,.05,.05,.3,0,.3,.05,.05,.05,.05,0,0])
                #One may want to change randoms to a function of n,i
                # interval.append(random_interval[0])
                interval.append(np.random.randint(-5,5))
                interval.append(np.random.randint(1,2))#Number of repetitions
                interval.append(3)
                #interval.append(np.random.randint(1,2))#Number of Octaves
                intervals.append(interval)
            set_of_intervals.append(intervals)
    else:
        set_of_intervals =[ [ [1,1,1],[2,2,2]  ]  ,  [   [ 1, 1, 1], [2,2,2]    ]    ]
    return(set_of_intervals)
def Build_Sets_of_Beats(Manual_or_Auto,Settings):
    set_of_beats = []
    if Manual_or_Auto == 0:
        print("Building sets of Beats. This will be a sequence of durations of notes")
        number_of_sets = int(input())
        for n in range(number_of_sets):
            beats = []
            choose_another_beat = ""
            while choose_another_beat == "":
                print("Choose a duration")
                beats.append(float(input()))
                print("For another Beat press enter, else stop by typing anything else.")
                choose_another_beat = input()
            set_of_beats.append(beats)
    elif Manual_or_Auto == 1:
        number_of_sets = Settings[0]
        for n in range(number_of_sets):
            beats = []
            number_of_beats = Settings[n + 1]
            for i in range(number_of_beats):  # Build Random Intervals?
                beats.append(np.random.randint(1,4)/4)
            set_of_beats.append(beats)
    return(set_of_beats)
def Build_Sets_of_Notes(Manual_or_Auto,set_of_scales,set_of_initial_notes,set_of_intervals,Settings):
    values = [set_of_scales,set_of_initial_notes,set_of_intervals]
    sets_of_notes = []
    if Manual_or_Auto == 0:
        print("Songs will be built in sets of notes, with a transition between each set composed of switching between ")
        print("Either the scale, the note, the interval set")
        print("To start, choose an initial scale:",set_of_scales,"Type an integer to select the index.")
        scale = set_of_scales[int(input())][1]
        print("Scale",scale)
        print("Initial note",set_of_initial_notes,"Type an integer to select the index")
        note = set_of_initial_notes[int(input())]
        print("Initial intervals,",set_of_intervals,"Type an integer to select an index")
        intervals = set_of_intervals[int(input())]
        sets_of_notes = []
        parameters = [scale, note, intervals]
        notes = [parameters[1]]
        note_scale = []
        note_scale.append(note)
        new_note = note
        for j in range(2*len(scale)):
            new_note += scale[j%len(scale)]
            note_scale.append(new_note)
        index = 0
        for i in range(len(intervals)):
            for j in range(intervals[i][1]):
                notes.append(note_scale[index])
                index = (index+intervals[i][0])%(len(note_scale))#/(3-intervals[i][2]))


        # for interval in intervals:
        #     for j in range(interval[1]):
        #         step = 0
        #         for n in range(abs(interval[0])):
        #             try:
        #
        #                 sign = interval[0]/abs(interval[0])
        #
        #                 step += sign * scale[int(sign)*n]
        #
        #             except:
        #
        #                 step = 0
        #         notes.append((notes[0]-interval[2]*12) + (notes[-1] + step-(notes[0] - interval[2] * 12)) %(interval[2]*24))
        sets_of_notes.append(notes)
        # set_of_initial_notes.append(notes[-1])
        print("To add another section press enter, otherwise type anything else")
        add_another_section = input()
        while add_another_section == "":
            print("What do you want to change, scale, initial note, or set of intervals? ",
                  "Type an integer [0,1,2]:[scale,note,intervals]")
            change = int(input())
            print("What do you want to change it to?",values[change])
            parameters[change] = values[change][int(input())]
            notes = [parameters[1]]
            intervals = parameters[2]
            scale = parameters[0][1]

            note_scale = []
            note_scale.append(note)
            new_note = note
            for j in range(2 * len(scale)):#The two gives the octave!
                new_note += scale[j % len(scale)]
                note_scale.append(new_note)
            index = 0
            for i in range(len(intervals)):
                for j in range(intervals[i][1]):
                    notes.append(note_scale[index])
                    index = (index + intervals[i][0]) % (len(note_scale))
                    #/ (3 - intervals[i][2]))
            # for i, interval in intervals:
            #     for j in range(interval[1]):
            #         step = 0
            #         for n in range(abs(interval[0])):
            #             try:
            #                 sign = interval[0] / abs(interval[0])
            #                 step += sign * scale[int(sign) * n]
            #             except:
            #                 step = 0
            #         notes.append((notes[0] - interval[2] * 12) + (notes[-1] + step - ((notes[0] - interval[2] * 12))) % (interval[2] * 24))#I know the problem, not modding correctly
            #

            sets_of_notes.append(notes)
            print("To add another section press enter, otherwise type anything else")
            add_another_section = input()
    elif Manual_or_Auto == 1:
        sets_of_notes = []
        for i in range(Settings[0]):#set how many transitions
            scale = set_of_scales[Settings[i+1][0]][1]
            note = set_of_initial_notes[Settings[i+1][1]]
            intervals = set_of_intervals[Settings[i+1][2]]


            parameters = [scale, note, intervals]
            print(parameters)
            notes = [parameters[1]]
            note_scale = []
            note_scale.append(note)
            new_note = note
            for j in range(2 * len(scale)):
                new_note += scale[j % len(scale)]
                note_scale.append(new_note)
            index = 0
            for i in range(len(intervals)):
                for j in range(intervals[i][1]):
                    notes.append(note_scale[index])
                    index = (index + intervals[i][0]) % (len(note_scale))

                    #/ (3 - intervals[i][2]))
            # for interval in intervals:
            #     for j in range(interval[1]):
            #         step = 0
            #         for n in range(abs(interval[0])):
            #             try:
            #                 sign = interval[0] / abs(interval[0])
            #                 if sign >= 0:
            #                     step += scale[n]
            #                 else:
            #                     step += int(sign)*scale[int(sign)*(n+1)]
            #             except:
            #                 step = 0
            #         print("here",step)
            #         notes.append((notes[0] - interval[2] * 12) + (notes[-1] + step - (notes[0] - interval[2] * 12)) % (interval[2] * 24))
            sets_of_notes.append(notes)
            #set_of_initial_notes.append(notes[-1])
    return(sets_of_notes)
# def Build_Chords(Manual_or_Auto,Sets_of_Notes,Sets_of_Beasts):
#     #First we need to sort through a set of notes and see if there are enough notes to build a chord. i.e if C,
#     if Manual_or_Auto == 0:
#
#     elif Manual_or_Auto == 1:
#
#     else:
#         print("Danger Mr. Robinson")

#What if we simply combine every set of notes with every beat, and then just output these each as a different midi file and combine them?
def Initialize_Song_Properties():

     #Defines each instrument as a separate channel


    # Sets_of_Scales = Build_Scales(Auto,[6,np.random.randint(0,47),np.random.randint(0,47)])
    skale = np.random.randint(0,47)
    print("SCALE NUMBER = "+str(skale))
    Sets_of_Scales = Build_Scales(Auto,[1,skale])
    scale_label = str(Sets_of_Scales[0][0][0])
    # Initial_notes = Build_initial_notes(Auto,[2,50,57])
    Initial_notes = Build_initial_notes(Auto,[1,48])
    #Sets_of_Intervals = Build_Set_of_Intervals(Auto,[2,64,64])

    #Sets_of_Intervals = Build_Set_of_Intervals(Auto,[1,1200])

    interval_file = open('intervals/pi.txt',"r")
    intervals = interval_file.read()
    interval_array = []
    for x,interval in enumerate(intervals):
        try:
            interval_array.append([int(intervals[2*x]),int(intervals[2*x+1])%4,1])
        except:
            pass
    Sets_of_Intervals = [interval_array[0:1000]]
    Sets_of_Beats = Build_Sets_of_Beats(Auto,[1,24])
    #Sets_of_Notes = Build_Sets_of_Notes(1,Sets_of_Scales,Initial_notes,Sets_of_Intervals,[2,[0,0,0],[1,1,1]])
    Sets_of_Notes = Build_Sets_of_Notes(1,Sets_of_Scales,Initial_notes,Sets_of_Intervals,[1,[0,0,0]])
    # The way the last element i Sets_of_Notes works is [a,[x1],[x2],...,[xa]], where a is the number of transitions.
    # Each X_i represents a tune, and we can select a [scale, note, interval]. The Program will routinely FAIL if the
    #Dimensions of Settings doesn't work.

    number_of_transitions = max(len(Sets_of_Scales),len(Sets_of_Intervals),len(Sets_of_Beats),len(Initial_notes))


    print(Sets_of_Notes)
    #Write to .csv here.
    print(Sets_of_Beats)
    #print(Sets_of_Intervals)

    for note_set in Sets_of_Notes:
        ordered_notes = np.unique(note_set)

    return(Sets_of_Notes,Sets_of_Intervals,Sets_of_Beats,scale_label)
def Build_Song(notes,beats,scale_label, directory):
    track = 0
    Channel_List = ["Steinway", "Epic Cloud Formation(SYNTH)",
                    "Finger Style Base(Guitar)", "Classic Clean(Guitar)",
                    "String Ensemble", "String Ensemble",
                    "Full Brass", "Trumpets",
                    "Boutique Drum Kit", "So Cal Drum Kit",
                    ]
    time     = 0    # In beats
    duration = 1    # In beats
    tempo    =  90   # In BPM
    volume   = 100
    MyMIDI = MIDIFile(2)
    MyMIDI.addTempo(track, time, tempo)
    channel = 7
    primary_channel  = channel
    secondary_channel  = 2
    third_channel = 8
    key = notes[0]
    MyMIDI = MIDIFile(5)
    MyMIDI.addTempo(0, time, tempo)
    uin = np.random.randint(10000, 99999)
    np.savetxt(os.path.join(directory,"notes" + str(uin) + ".csv"), notes, delimiter=",")
    np.savetxt(os.path.join(directory,"beats" + str(uin) + ".csv"), beats, delimiter=",")
    for i, str_note in enumerate(notes):
        note = int(str_note)
        # 0 = piano, 1 = synth piano, 2 = base guitar, 3 = electric guitar

        # "CONTINUOUS PLAY" - ORGAN
        MyMIDI.addNote(0, 10, int(note), time, beats[i % len(beats)], 20)
        # if note < 0 and (i%len(beats))%4==1:
        #     MyMIDI.addNote(0, 10, int(note), time-beats[(i-1)%len(beats)], beats[(i-1) % len(beats)], 20)
        #     if (notes[i]+notes[i-1])%2 == 0:
        #         MyMIDI.addNote(0, 10, int((notes[i]+notes[i-1])/2), time - beats[(i - 1) % len(beats)], beats[(i - 1) % len(beats)], 20)
        #     MyMIDI.addNote(0, 10, int(note)-12, time, beats[i % len(beats)], 20)
        # else:
        #     MyMIDI.addNote(0, 10, int(note), time, beats[i % len(beats)], 20)
        # BASE GUITAR
        if time % 10 < i % 14:
            note = notes[i % 8]
            if note > 60:  # Restrict max note, if it is greater reduce by one harmonic.
                note -= 12
            MyMIDI.addNote(1, 2, note, time, beats[i % len(beats)], 100)
            # if beats[i % len(beats)] > .5:
            #     MyMIDI.addNote(1,2, note, time, 2*beats[i % len(beats)], 100)
            # else:
            #     MyMIDI.addNote(1, 2, note, time, beats[i % len(beats)], 100)
        else:
            try:
                note = notes[i % 8 - 5]
            except:
                note = notes[i%8]
            if note > 60:  # Restrict max note, if it is greater reduce by one harmonic.
                note -= 12
            MyMIDI.addNote(1, 2, note, time, beats[i % len(beats)], 100)
            # if beats[i % len(beats)] > .5:
            #     MyMIDI.addNote(1, 2, note, time, 2 * beats[i % len(beats)], 100)
            # else:
            #     MyMIDI.addNote(1, 2, note, time, beats[i % len(beats)], 100)
        # PIANO

        if time % 8 < i % 12:
            if note == key:  # Build Chord?
                chord_step = 1
                chord_size = np.random.choice([2, 3])
                for c in range(chord_size):
                    MyMIDI.addNote(2, 0, notes[(i + c * chord_step) % 12], time, beats[i % len(beats)], 50)
            else:
                MyMIDI.addNote(2, 0, notes[i % 12], time, beats[i % len(beats)], 50)

        # PERCUSSION
        MyMIDI.addNote(3, 9, notes[i % 8] % 12 + 40, time, beats[i % len(beats)], 20)

        time += beats[i % len(beats)]

    with open(os.path.join(directory, str(scale_label + str(np.random.randint(10000, 99999))) + ".midi"), "wb") as output_file:
        MyMIDI.writeFile(output_file)
    return (uin) #uin will assist with looking up csv file to remix.



# def Build_Base(Notes, Beats, Intervals)
def remix(note_file,beat_file,start_sample,number_of_notes):
    notes = np.genfromtxt(note_file,delimiter= ',')
    beats = np.genfromtxt(beat_file,delimiter=',')
    remixed_notes = notes[start_sample:start_sample+number_of_notes]

    Build_Song(remixed_notes,beats,'')



def Create_New_Project():
    project_id = 'pi_test_0'#np.random.randint(10000,99999)
    root_directory = os.getcwd()
    directory = os.path.join(root_directory, str(project_id))
    if not os.path.exists(directory):
        os.makedirs(directory)

    notes,Sets_of_Intervals,beats,scale_label = Initialize_Song_Properties()
    uin = Build_Song(notes[0],beats[0],scale_label, directory)
    #start = input()
    #remix('notes'+str(uin)+'.csv','beats'+str(uin)+'.csv',int(start),len(notes)-int(start))

Create_New_Project()
#remix('notes'+'14930.csv','beats'+'14930.csv',60,1200)
#Idea: Streamline the multiple sets, and make sure x,y,z work even if x!=y!=z.
#A set of durations and times. i.e [[[1,0],[.5,1],[.5,1]],[[.5,0],[1,.5],[.5,1]] has two sets of beats
#Build Code to Auto Build These Groups


#
# def Build_Scales(Manual_or_Auto,Auto_Scale_Settings):
#     if Manual_or_Auto == 0 or Manual_or_Auto == "Manual":
#         for i in range(len(Scales)):
#             print(i, ":", Scales[i][0])
#         set_of_scales = []
#         print("Choose an initial Scale")
#         scale = Scales[int(input())]
#         print(scale)
#         set_of_scales.append(scale)
#         print("how many scales?")
#         number_of_scales = int(input())
#         num_scales_left = number_of_scales
#         while num_scales_left >1:
#             print("Choose",(num_scales_left - 1),"more scales")
#             print("Choose another Scale")
#             try:
#                 set_of_scales.append(Scales[int(input())])
#                 num_scales_left -= 1
#             except:
#                 print("Oops a cat must have stepped on the keyboard!")
#         print(set_of_scales)
#     elif Manual_or_Auto == 1 or Manual_or_Auto == "Auto":
#         set_of_scales = Scales[Auto_Scale_Settings]
#     else:
#         print("Danger, Mr. Robinson")
#         set_of_scales = []
#     return(set_of_scales)
# def Build_Initial_notes_and_Octaves(Manual_or_Auto, set_of_scales,Auto_Note_and_Octave_Settings):
#     if Manual_or_Auto == 0 or Manual_or_Auto == "Manual":
#         octaves = []
#         initial_notes = []
#         for scale in set_of_scales:
#             print("For", scale,",what initial note and octave range would you like?")
#             print("Initial note as a midi integer)")
#             initial_notes.append(int(input()))
#             print("Octave range as an integer.")
#             octaves.append(int(input()))
#     elif Manual_or_Auto == 1 or Manual_or_Auto == "Auto":
#         initial_notes =Auto_Note_and_Octave_Settings[0]
#         octaves = Auto_Note_and_Octave_Settings[1]
#     else:
#         print("Danger, Mr. Robinson")
#         initial_notes = []
#         octaves = []
#     return(initial_notes,octaves)
# def Chords_on_Scales(Manual_or_Auto,scale,Auto_Chord_Settings):
#     print(scale)
#     if Manual_or_Auto == 0 or Manual_or_Auto == "Manual":
#         scale_intervals = []
#         for n,note in enumerate(scale):#Treat scale as just the intervals of the scale so we just have to add these
#             intervals = []
#             intervals.append(note)
#             for m in range(n,len(scale)-1):
#                 note += scale[1+m]
#                 intervals.append(note)
#             scale_intervals.append(intervals)
#     else:
#         print("Seriously fuck off")
#     print(scale_intervals)
#     return(scale_intervals)
# def Build_Intervals(Manual_or_Auto, set_of_scales, Auto_Interval_Settings,Randomness,octaves):
#     if Manual_or_Auto == 0 or Manual_or_Auto == "Manual":
#         intervals = []
#         lengths_of_intervals = []
#         for scale in set_of_scales:
#             print("Choose some intervals for this Scale",scale)
#             print(Intervals)
#             print("interval as an int =?")
#             interval = int(input())
#             print("repetition as an int =?")
#             scale_intervals = []
#             repetition = int(input())
#             scale_intervals.append([interval, repetition])
#             while interval != 0 or repetition != 0:
#                 print("interval as an int =?")
#                 interval = int(input())
#                 print("repetition as an int =?")
#                 repetition = int(input())
#                 scale_intervals.append([interval, repetition])
#                 print("You can end this by making both entries 0, or fuck it all up and enter a letter like a dingus.")
#             intervals.append(scale_intervals)
#     elif Manual_or_Auto == 1 or Manual_or_Auto == "Auto":
#         intervals = []
#         lengths_of_intervals = []
#         for s in range(Auto_Interval_Settings):
#             interval_count = 0
#             interval = np.random.randint(-7*octaves[s],7*octaves[s])
#             repetition = np.random.randint(1,7)
#             scale_intervals = []
#             scale_intervals.append([interval, repetition])
#             #while interval != 0 or repetition != 0:
#             while interval_count <= 8:
#                 interval = np.random.randint(-7*octaves[s], 7*octaves[s])
#                 if interval == 0:
#                     repetition = np.random.randint(0,3)
#                 else:
#                     repetition = np.random.randint(0, 7)
#                 interval_count += repetition
#                 scale_intervals.append([interval, repetition])
#             intervals.append(scale_intervals)
#             lengths_of_intervals.append(len(scale_intervals))
#         print(intervals,lengths_of_intervals)
#     else:
#         print("Danger, Mr. Robinson")
#         intervals = []
#     return(intervals,lengths_of_intervals)
# def Build_Notes_on_Scales(initial_notes,scales,octaves,intervals):
#     notes = []
#     for s,scale in enumerate(scales):
#         note = initial_notes[s]
#         print(note)
#         note_scale = []
#         note_scale.append(note)
#         new_note = note
#         for j in range(octaves[s]*len(scale[1])):
#             new_note += scale[1][j%len(scale[1])]
#             note_scale.append(new_note)
#         index = 0
#         for i in range(len(intervals[s])):
#             for j in range(intervals[s][i][1]):
#                 notes.append(note_scale[index])
#                 index = (index+intervals[s][i][0])%(len(note_scale))
#         print(scale,note_scale)
#     return (notes)
# def Build_Beats(Auto_or_Manual, Notes,Randomness,track_and_scale):
#     durations = []
#     times = [0]
#     all_durations = []
#     all_times = []
#     #Build all Durations
#
#     set_of_durations = [1, .5, .5 , 1, .5, .5, 1, .5,.5, 1.5]
#     set_of_times = set_of_durations
#     if Auto_or_Manual == 1:
#         set_of_durations = []
#         random_length_of_melody = np.random.randint(4,24)
#         for r in range(random_length_of_melody):
#             set_of_durations.append(np.random.randint(1,4)/4)
#         set_of_times = set_of_durations
#         # set_of_times[np.random.randint(0,random_length_of_melody)] = .25
#     print(Notes)
#     for n,note in enumerate(Notes):
#
#          durations.append(set_of_durations[n%len(set_of_durations)])
#          times.append(times[-1]+set_of_times[n%len(set_of_times)])
#     return(durations,times)
# def Generator(Auto_or_Manual,Number_of_Notes, Randomness, Tracks, Channels):
#     for t,track in enumerate(Tracks):
#         #Tracks&Channels are Arrays of the same size, i.e, tracks = [1,2,3,1,2,3], Channels = [1,1,1,2,2,2]
#         #Tells us to write on channel 1 tracks 1,2,&3 and then channel 2, tracks 1,2,and 3
#         working = 1
#         track_notes = []
#         track_durations = []
#         track_times = []
#         auto_notes_octaves = []
#         if Randomness != 0:  # User defined
#             number_of_scales = np.random.randint(1, 1 + Randomness)
#             track_scales = []
#             initial_notes = []
#             octaves = []
#             for r in range(number_of_scales):
#                 track_scales.append(Build_Scales(Auto_or_Manual, np.random.randint(0, 48)))
#                 initial_notes.append(np.random.randint(30, 60))
#                 octaves.append(np.random.randint(1, 2))
#                 auto_notes_octaves = [initial_notes, octaves]
#         else:
#             track_scales = Build_Scales(0, 0)
#         # track_scales = [Build_Scales(1, 6), Build_Scales(1, 6)]
#
#         track_initial_notes_and_octaves = Build_Initial_notes_and_Octaves(Auto_or_Manual, track_scales,
#                                                                           auto_notes_octaves)
#         track_intervals = Build_Intervals(Auto_or_Manual, track_scales, len(track_scales), Randomness,
#                                           track_initial_notes_and_octaves[1])[0]
#         track_notes = Build_Notes_on_Scales(track_initial_notes_and_octaves[0], track_scales,
#                                             track_initial_notes_and_octaves[1], track_intervals)
#         Limit = Number_of_Notes
#         while len(track_notes) <= Limit:
#             # track_intervals = Build_Intervals(Auto_or_Manual, track_scales, len(track_scales), Randomness, track_initial_notes_and_octaves[1])[0]
#             new_track_notes = Build_Notes_on_Scales(track_initial_notes_and_octaves[0], track_scales,
#                                                     track_initial_notes_and_octaves[1], track_intervals)
#             for note in new_track_notes:
#                 track_notes.append(note)
#         Beat_stuff = Build_Beats(Auto_or_Manual, track_notes, Randomness, [track, track_scales])
#         track_durations = Beat_stuff[0]
#         track_times = Beat_stuff[1]
#
#         channel = Channels[t]  # Defines each instrument as a separate channel
#         time = 0  # In beats
#         tempo = 90  # In BPM
#         volume = 100
#         MyMIDI = MIDIFile(2)
#         MyMIDI.addTempo(track, time, tempo)
#         for i, pitch in enumerate(track_notes):
#             MyMIDI.addNote(track, channel, pitch, track_times[i], track_durations[i], volume)
#     with open("test.mid", "wb") as output_file:
#         MyMIDI.writeFile(output_file)
#
#     #return(track_notes,track_durations,track_times)
# auto = 1
# Generator(auto, 100,auto*8,[0],[27])
# #  MANUAL SHIT
# #
# #
# # track    = 0
# # channel  = 0 #Defines each instrument as a separate channel
# # time     = 0    # In beats
# # duration = 1    # In beats
# # tempo    = 90   # In BPM
# # volume   = 100
# #
# # MyMIDI = MIDIFile(1)
# # MyMIDI.addTempo(track, time, tempo)
# #
# #
# # for i, pitch in enumerate(track_notes):
# #     MyMIDI.addNote(track, channel, pitch, track_times[i], track_durations[i], volume)
# #
# #
# # with open("test.mid", "wb") as output_file:
# #     MyMIDI.writeFile(output_file)
# # #By taking an initial note we can take this sequence to create different scales.
# # #initial_pitch = base_pitches[base_notes.index(input())]
# # # def Diatonic_Scale(initial_notes):
# # #     notes = []
# # #     for note in initial_notes:
# # #         notes.append(note)
# # #         new_note = note
# # #         for step in diatonic_interval:
# # #             new_note += step
# # #             notes.append(new_note)
# # #     return(notes)
# # # #
# # # # def Song():
# # # #     print('initial note')
# # # #     note = base_pitches[base_notes.index(str(input()))]
# # # #     print('how many cycles')
# # # #     notes = [note]
# # # #     for i in range(int(input())):
# # # #         note -= ((-1)**i*(diatonic_interval[i%7])+(diatonic_interval[(i-1)%7]))
# # # #         note = (note)%30+55
# # # #         notes.append(note)
# # # #         # for step in diatonic_scale:
# # # #         #     note += step
# # # #         #     notes.append(note)
# # # #     return(notes)
# # # #
# # #for i, pitch in enumerate(Diatonic_Scale(base_pitches)):
# #
# #
# # # #So we will first need an array for our sequence
# # # #Second we need to scale or correspond each sequence element to a note
# # # #Need an array for durations
