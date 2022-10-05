from mods import ui_syx
from mods import ui_efx
from mods import ui_etc
from mods import storage

def ui_main():
    try:
        if storage.protected:
            prt = ", Protected"
        else:
            prt = ""
        print("0 : Temporary Storage (Current : " + str(len(storage.temp_store)) + prt +")")
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
            storage.store(ui_syx.reset())
        elif ipt1 == 2:
            print("System Effects")
            print("1 : Reverb")
            print("2 : Chorus")
            print("3 : Delay")
            print("4 : System EQ")
            ipt2 = int(input(">> "))
            if ipt2 == 1:
                storage.store(ui_syx.reverb())
            elif ipt2 == 2:
                storage.store(ui_syx.chorus())
            elif ipt2 == 3:
                storage.store(ui_syx.delay())
            elif ipt2 == 4:
                storage.store(ui_syx.syseq())
        elif ipt1 == 3:
            print("Channel Settings")
            print("1 : Rhythm Map")
            print("2 : Output Port")
            print("3 : Send to EQ")
            ipt2 = int(input(">> "))
            if ipt2 == 1:
                storage.store(ui_syx.rhythm())
            elif ipt2 == 2:
                storage.store(ui_syx.outport())
            elif ipt2 == 3:
                storage.store(ui_syx.sendeq())
        elif ipt1 == 4:
            storage.store(ui_efx.ui_efx())
        elif ipt1 == 5:
            storage.store(ui_etc.ui_etc())
    except Exception as e:
        print(e)
    print("")