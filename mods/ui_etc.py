from mods import common

def ui_etc():
    print("Etc Functions")
    print("1 : Title")
    print("2 : Dot-Matrix Display")
    print("3 : Master Volume")
    print("4 : Master Key-Shift")
    print("5 : Master Pan")
    ipt1 = int(input(">>"))
    if ipt1 == 1:
        print("~ 16 Chars : Fixed, 17 ~ 32 Chars : Scrolled")
        print("ASCII 32 - 127 Characters only")
        ipt2 = input("Title : ")
        if len(ipt2) > 32:
            raise ValueError("Too much text (32 Chars Max)")
        elif len(ipt2) < 1:
            raise ValueError("You must input title text, not blank")
        tc = []
        for ic in ipt2:
            tco = ord(ic)
            if tco > 127 or tco < 32:
                raise ValueError("Invalid Character (ASCII 32 ~ 127 Only)")
            else:
                tc.append(tco)
        print("Received " + str(len(tc)) + " Characters")
        trk = [0xF0, 0x41, 0x10, 0x45, 0x12]
        trk2 = [0x10, 0x00, 0x00] + tc
        resx = trk + trk2 + [common.checksum(trk2), 0xF7]
        cmnt = "Title - " + ipt2
    elif ipt1 == 2:
        print("not implemented yet")
    elif ipt1 == 3:
        ipt2 = int(input("Master Volume (0 ~ 127) : "))
        if ipt2 > 127 or ipt2 < 0:
            raise ValueError("Invalid Input")
        resx = common.gs_syx([0x40, 0x00, 0x04, ipt2])
        cmnt = "Set Master Volume to " + str(ipt2)
    elif ipt1 == 4:
        ipt2 = int(input("Master Key-Shift (-24 ~ 0 ~ 24) : "))
        if ipt2 > 24 or ipt2 < -24:
            raise ValueError("Invalid Input")
        resx = common.gs_syx([0x40, 0x00, 0x05, 0x40 + ipt2])
        cmnt = "Set Master Key-Shift to " + str(ipt2)
    elif ipt1 == 5:
        ipt2 = int(input("Master Pan (-63 ~ 0 ~ 63) : "))
        if ipt2 > 63 or ipt2 < -63:
            raise ValueError("Invalid Input")
        resx = common.gs_syx([0x40, 0x00, 0x06, 0x40 + ipt2])
        cmnt = "Set Master Pan to " + str(ipt2)
    else:
        raise
    return resx, cmnt
