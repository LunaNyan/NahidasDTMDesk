from mods import ui_syx
from mods import ui_efx
from mods import ui_etc
from mods import ui_userdrum
from mods import storage
from mods import common

try:
    from mods import ui_mido
    print("MIDI OUT Loaded\n")
except ImportError:
    print("WARNING!")
    print("python_rtmidi, mido Module Not Found.")
    print("MIDI OUT Disabled. but hey, other things work as well. so you can continue.")
    print("to use MIDI OUT Function, execute 'pip install -r requirements.txt'.")

def ui_main():
    try:
        print("== HOME MENU ==")
        if storage.protected:
            prt = ", Protected"
        else:
            prt = ""
        print("0 : Memory (Current : " + str(len(storage.temp_store)) + prt +")")
        try:
            if ui_mido.mido_port != None:
                print("9 : MIDI")
            else:
                print("9 : MIDI (" + ui_mido.mido_port + ")")
        except NameError:
            pass
        print("=====")
        print("1 : MIDI Reset")
        print("2 : System Effects")
        print("3 : Channel Settings")
        print("4 : Insertion Effects (EFX)")
        print("5 : Etc")
        try:
            if ui_mido.mido_port != None:
                print("=====")
                print("6 : User Drum")
                print("7 : User Instrument")
        except NameError:
            pass
        print("=====")
        print("8 : Tone Finder")
        ipt1 = int(input("> "))
        if ipt1 == 0:
            storage.store_menu()
        elif ipt1 == 9:
            try:
                ui_mido.ui_mido()
            except NameError:
                print("MIDI OUT Disabled. you may have to install definitions to use it.")
                print("Exit this application, then execute 'pip install -r requirements.txt'.")
        elif ipt1 == 1:
            res = ui_syx.reset()
            print(res[1])
            print("    " + common.tostr(res[0]))
            storage.store(res)
        elif ipt1 == 2:
            print("System Effects")
            print("1 : Reverb")
            print("2 : Chorus")
            print("3 : Delay")
            print("4 : System EQ")
            ipt2 = int(input(">> "))
            if ipt2 == 1:
                res = ui_syx.reverb()
            elif ipt2 == 2:
                res = ui_syx.chorus()
            elif ipt2 == 3:
                res = ui_syx.delay()
            elif ipt2 == 4:
                res = ui_syx.syseq()
            else:
                raise ValueError("abort")
            print(res[1])
            print("    " + common.tostr(res[0]))
            storage.store(res)
        elif ipt1 == 3:
            print("Channel Settings")
            print("1 : Rhythm Map")
            print("2 : Output Port")
            print("3 : Send to EQ")
            ipt2 = int(input(">> "))
            if ipt2 == 1:
                res = ui_syx.rhythm()
            elif ipt2 == 2:
                res = ui_syx.outport()
            elif ipt2 == 3:
                res = ui_syx.sendeq()
            else:
                raise ValueError("abort")
            print(res[1])
            print("    " + common.tostr(res[0]))
            storage.store(res)
        elif ipt1 == 4:
            res = ui_efx.ui_efx()
            print(res[1])
            print("    " + common.tostr(res[0]))
            storage.store(res)
        elif ipt1 == 5:
            res = ui_etc.ui_etc()
            print(res[1])
            print("    " + common.tostr(res[0]))
            storage.store(res)
        elif ipt1 == 5:
            ui_userdrum.ui_userdrum()
    except Exception as e:
        print(e)
    print("")