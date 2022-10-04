from mods import syx
from mods import storage

def ui_main():
    try:
        print("0 : Temporary Storage")
        print("=====")
        print("1 : MIDI Reset")
        print("2 : System Effects")
        print("3 : Channel Settings")
        print("4 : Insertion Effects (EFX)")
        print("5 : Etc")
        ipt1 = int(input("> "))
        if ipt1 == 0:
            storage.store_menu()
        elif ipt1 == 1:
            storage.store(syx.reset())
        elif ipt1 == 2:
            print("System Effects")
            print("1 : Reverb")
            print("2 : Chorus")
            print("3 : Delay")
            print("4 : System EQ")
            ipt2 = int(input(">> "))
            if ipt2 == 1:
                storage.store(syx.reverb())
            elif ipt2 == 2:
                storage.store(syx.chorus())
            elif ipt2 == 3:
                storage.store(syx.delay())
            elif ipt2 == 4:
                storage.store(syx.syseq())
        elif ipt1 == 3:
            print("Channel Settings")
            print("1 : Rhythm Map")
            print("2 : Output Port")
            print("3 : Send to EQ")
            ipt2 = int(input(">> "))
            if ipt2 == 1:
                storage.store(syx.rhythm())
            elif ipt2 == 2:
                storage.store(syx.outport())
            elif ipt2 == 3:
                storage.store(syx.sendeq())
    except Exception as e:
        print(e)
