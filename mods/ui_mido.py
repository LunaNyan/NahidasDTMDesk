import rtmidi
import mido
from mods import storage

mido_port = ""
mido_port_actual = None
mido_rtout = False

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
            mido_port = ""
            print("Port Closed")
    if ipt1 == 2:
        if len(storage.temp_store) == 0:
            print("No Items in Temporary Storage")
        else:
            for m in storage.temp_store:
                print(m[1])
                msg = mido.Message('sysex', data=tuple(m[0][1:-1]))
                mido_port_actual.send(msg)
            print("Complete")

