import rtmidi
import mido
from mods import storage

mido_port = ""
mido_port_actual = None
mido_rtout = False

def test_port():
    print("1 : Test Instrument (Channel 1)")
    print("2 : Test Rhythm (Channel 10)")
    ipt = input("Test Section : ")
    if ipt == "1":
        mf = "res/pno.mid"
    elif ipt == "2":
        mf = "res/drm.mid"
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
    global mido_rtout, mido_port, mido_port_actual
    if mido_port == "":
        mprt = "OFF"
    else:
        mprt = mido_port
    if mido_rtout:
        mout = "OFF"
    else:
        mout = "ON"
    print("1 : Set Port (" + mprt + ")")
    print("2 : Send Storage")
    print("3 : Test Port")
    print("4 : Set Channel Instrument")
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
    elif ipt1 == 2:
        if len(storage.temp_store) == 0:
            print("No Items in Temporary Storage")
        else:
            for m in storage.temp_store:
                print(m[1])
                msg = mido.Message('sysex', data=tuple(m[0][1:-1]))
                mido_port_actual.send(msg)
            print("Complete")
    elif ipt1 == 3:
        if mido_port_actual == None:
            print("Open Port first")
        else:
            test_port()
    elif ipt1 == 4:
        if mido_port_actual == None:
            print("Open Port first")
        else:
            iptc = int(input("Channel : "))
            iptp = int(input("PC : "))
            iptm = int(input("MSB : "))
            iptl = int(input("LSB : "))
            msgs = []
            msgs.append(mido.Message('program_change', channel=iptc - 1, program=iptp))
            msgs.append(mido.Message('control_change', channel=iptc - 1, control=0, value=iptm))
            msgs.append(mido.Message('control_change', channel=iptc - 1, control=32, value=iptl))
            for m in msgs:
                mido_port_actual.send(m)
    else:
        raise ValueError("abort")