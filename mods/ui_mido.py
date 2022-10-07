import rtmidi
import mido
from mods import storage

mido_port = ""
mido_port_actual = None
mido_port_in = ""
mido_port_in_actual = None

def test_port():
    print("1 : Test Instrument (Channel 1)")
    print("2 : Test Rhythm (Channel 10)")
    ipt = input("Test Section : ")
    if ipt == "1":
        mf = "res/test_mid/pno.mid"
    elif ipt == "2":
        mf = "res/test_mid/drm.mid"
    else:
        raise ValueError("abort")
    print("Playing..")
    # Title - Hello World!
    syx = [0x41, 0x10, 0x45, 0x12, 0x10, 0x00, 0x00, 0x48, 0x65, 0x6C, 0x6C, 0x6F, 0x20, 0x57, 0x6F, 0x72, 0x6C, 0x64, 0x21, 0x33]
    msg = mido.Message('sysex', data=tuple(syx))
    mido_port_actual.send(msg)
    for msg in mido.MidiFile(mf).play():
        mido_port_actual.send(msg)

def ui_mido():
    global mido_port, mido_port_actual
    global mido_port_in, mido_port_in_actual
    if mido_port == "":
        mprt = "OFF"
    else:
        mprt = mido_port
    if mido_port_in == "":
        mprti = "OFF"
    else:
        mprti = mido_port_in
    print("1 : Set MIDI OUT (" + mprt + ")")
    print("2 : Set MIDI IN (" + mprti + ")")
    print("3 : Send Storage")
    print("4 : Test Port")
    ipt1 = int(input(">>"))
    if ipt1 == 1:
        prts = mido.get_output_names()
        cnt = 0
        for i in prts:
            print("#" + str(cnt) + " : " + i)
            cnt += 1
        print("other char : close port")
        try:
            ipt2 = int(input("Port : "))
            mido_port = prts[ipt2]
            mido_port_actual = mido.open_output(mido_port)
        except:
            mido_port_actual.close()
            mido_port_actual = None
            mido_port = ""
            print("Port Closed")
    if ipt1 == 2:
        prts = mido.get_input_names()
        cnt = 0
        for i in prts:
            print("#" + str(cnt) + " : " + i)
            cnt += 1
        print("other char : close port")
        try:
            ipt2 = int(input("Port : "))
            mido_port_in = prts[ipt2]
            mido_port_in_actual = mido.open_input(mido_port_in)
        except:
            mido_port_in_actual.close()
            mido_port_in_actual = None
            mido_port_in = ""
            print("Port Closed")
    elif ipt1 == 3:
        if len(storage.temp_store) == 0:
            print("No Items in Temporary Storage")
        else:
            for m in storage.temp_store:
                print(m[1])
                msg = mido.Message('sysex', data=tuple(m[0][1:-1]))
                mido_port_actual.send(msg)
            print("Complete")
    elif ipt1 == 4:
        if mido_port_actual == None:
            print("Open Port first")
        else:
            test_port()
    else:
        raise ValueError("abort")