from mods import ui_mido
from mods import common
from mods import storage
import time
import mido

def get_ex():
    print("1 : ALL")
    print("2 : PC#65")
    print("3 : PC#66")
    ipt = input(">> ")
    if ipt == "1":
        sx = [0x41, 0x10, 0x42, 0x11, 0x0C, 0x00, 0x00, 0x00, 0x02, 0x00, 0x72]
    elif ipt == "2":
        sx = [0x41, 0x10, 0x42, 0x11, 0x0C, 0x00, 0x00, 0x00, 0x02, 0x40, 0x32]
    elif ipt == "3":
        sx = [0x41, 0x10, 0x42, 0x11, 0x0C, 0x00, 0x00, 0x00, 0x02, 0x41, 0x31]
    else:
        return
    msg = mido.Message('sysex', data=tuple(sx))
    ui_mido.mido_port_actual.send(msg)
    print("Wait 3 sec..")
    time.sleep(3)
    mbx = ui_mido.mido_port_in_actual.iter_pending()
    for i in mbx:
        t = [0xF0]
        for i2 in i:
            t.append(i2)
        t.append(0xF7)
        print("User Drum")
        print("    " + common.tostr(t))
        storage.store(t)
    print("Complete")

def translate_key(ipt):
    try:
        ipt2 = int(ipt)
        return ipt2
    except:
        kscale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        if ipt[-2:] == "10":
            koct = 10
            ipt_scale = kscale.index(ipt[:-2])
        else:
            koct = int(ipt[-1])
            ipt_scale = kscale.index(ipt[:-1])
        res = (koct * 12) + ipt_scale
        if res > 127 or res < 0:
            raise ValueError("Key No# must between 0 and 127")
        return res

def ui_userdrum():
    try:
        if ui_mido.mido_port == "" or ui_mido.mido_port_in == "":
            print("both MIDI OUT and MIDI IN is required.")
            return
    except:
        print("mido, python_rtmidi is required")
        print("Windows : pip install -r requirements.txt")
        print("Linux : pip3 install -r requirements.txt")
        return
    print("Welcome to User Drum Zone")
    drmpc = 0x00
    while True:
        if drmpc == 0x00:
            print("0 : Go to PC#66 (Current : 65)")
        else:
            print("0 : Go to PC#65 (Current : 66)")
        print("1 : Assign Sound to Key")
        print("2 : Set Key Parameter")
        print("3 : Download!")
        print("8 : Find Sounds")
        print("9 : Exit")
        ipt1 = input(">>")
        if ipt1 == "0":
            if drmpc == 0x00:
                drmpc = 0x10
            else:
                drmpc = 0x00
        elif ipt1 == "1":
            ipt2 = input("Target Key (0 ~ 127 or C0 ~ G10) : ")
            try:
                tk = translate_key(ipt2)
            except Exception as e:
                print(e)
                continue
            ipt2 = input("BankSel LSB : ")
            try:
                lsb = int(ipt2)
                if lsb > 4 or lsb < 0:
                    print("Invalid LSB")
                    continue
            except Exception as e:
                print(e)
                continue
            ipt2 = input("PC# : ")
            try:
                pc = int(ipt2) -1
                if pc > 127 or pc < 0:
                    print("Invalid PC")
                    continue
            except Exception as e:
                print(e)
                continue
            ipt2 = input("Source Key (0 ~ 127 or C0 ~ G10) : ")
            try:
                sk = translate_key(ipt2)
            except Exception as e:
                print(e)
                continue
            syx = [
                [0x41, 0x10, 0x42, 0x12, 0x21, drmpc + 0x0A, tk, lsb, common.checksum([0x21, drmpc + 0x0A, tk, lsb])],
                [0x41, 0x10, 0x42, 0x12, 0x21, drmpc + 0x0B, tk, pc, common.checksum([0x21, drmpc + 0x0B, tk, pc])],
                [0x41, 0x10, 0x42, 0x12, 0x21, drmpc + 0x0C, tk, sk, common.checksum([0x21, drmpc + 0x0C, tk, sk])]
            ]
            for i in syx:
                ui_mido.mido_port_actual.send(mido.Message('sysex', data=tuple(i)))
        elif ipt1 == "2":
            mnu = ["Assign Group", "Panpot", "Reverb Send Level", "Chorus Send Level", "Delay Send Level"]
            mnu_address = [0x03, 0x04, 0x05, 0x06, 0x09]
            cnt = 1
            for i in mnu:
                print(str(cnt) + " : " + i)
            ipt2 = int(input(">> "))
            try:
                ipt3 = int(input(mnu[ipt2 - 1] + " : "))
            except Exception as e:
                print(e)
                continue
            if ipt3 > 127 or ipt3 < 0:
                print("Invalid Value")
                continue
            sx = [0x41, 0x10, 0x42, 0x12, 0x21, drmpc + mnu_address[ipt2 - 1], ipt3, common.checksum([0x21, drmpc + mnu_address[ipt2 - 1], ipt3])]
            ui_mido.mido_port_actual.send(mido.Message('sysex', data=tuple(sx)))
        elif ipt1 == "3":
            get_ex()
        elif ipt1 == "9":
            print("Return to Main Menu, Good Bye!")
            return
        else:
            continue
