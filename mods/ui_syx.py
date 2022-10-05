from mods import common as common
import math

def delay_time_center(val):
    if val < 1000 or val > 0.1:
        # Delay Time Center Negotiation
        if val >= 0.1 and val <= 2:
            # 0.1 ~ 2.0 (0.1)
            res = math.trunc(val / 0.1)
            rest = math.trunc(val / 0.1) * 0.1
        elif val > 2 and val <= 5:
            # 2.2 ~ 5.0 (0.2)
            res = 0x14 + int(math.trunc((val - 2) / 0.2))
            rest = math.trunc(val / 0.2) * 0.2
        elif val > 5 and val <= 10:
            # 5.5 ~ 10.0 (0.5)
            res = 0x23 + int(math.trunc((val - 5) / 0.5))
            rest = math.trunc(val / 0.5) * 0.5
        elif val > 10 and val <= 20:
            # 11 ~ 20(1)
            res = 0x2d + int(math.trunc((val - 10) / 1))
            rest = math.trunc(val / 1)
        elif val > 20 and val <= 50:
            # 20 ~ 50 (2)
            res = 0x37 + int(math.trunc((val - 20) / 2))
            rest = math.trunc((val) / 2) * 2
        elif val > 50 and val <= 100:
            # 50 ~ 100 (5)
            res = 0x46 + int(math.trunc((val - 50) / 5))
            rest = math.trunc((val) / 5) * 5
        elif val > 100 and val <= 200:
            # 100 ~ 200 (10)
            res = 0x50 + int(math.trunc((val - 100) / 10))
            rest = math.trunc(val / 10) * 10
        elif val > 200 and val <= 500:
            # 200 ~ 500 (20)
            res = 0x5A + int(math.trunc((val - 200) / 20))
            rest = math.trunc(val / 20) * 20
        elif val > 500 and val <= 1000:
            # 500 ~ 1000 (50)
            res = 0x69 + int(math.trunc((val - 500) / 50))
            rest = math.trunc(val / 50) * 50
        else:
            raise ValueError
        return res, rest
    else:
        raise ValueError

def reset():
    print("0 : General MIDI Level 1")
    print("1 : General MIDI Level 2")
    print("2 : SC-55 / GS Global")
    print("3 : SC-88")
    try:
        mode = int(input("MIDI Reset Mode : "))
    except:
        raise ValueError("Invalid Mode Selection")
    if mode == 0:
        # General MIDI Level 1
        return [[0xF0, 0x7E, 0x7F, 0x09, 0x01, 0xF7], "GM1 System ON"]
    elif mode == 1:
        # General MIDI Level 2
        return [[0xF0, 0x7E, 0x7F, 0x09, 0x03, 0xF7], "GM2 System ON"]
    elif mode == 2:
        # SC-55 / GS Global
        return [[0xF0, 0x41, 0x10, 0x42, 0x12, 0x40, 0x00, 0x7F, 0x00, 0x41, 0xF7], "SC-55 / GS Global Reset"]
    elif mode == 3:
        # SC-88
        return [[0xF0, 0x41, 0x10, 0x42, 0x12, 0x00, 0x00, 0x7F, 0x00, 0x01, 0xF7], "SC-88 Reset"]
    else:
        raise ValueError("Invalid Mode Selection")

def rhythm():
    cp = common.get_port_and_channel()
    port = cp.port
    channel = cp.channel
    cmnt_port = cp.cmnt_port
    ipt_chnl = cp.channel_actual
    # Channel Mode
    print("0 : Instrument")
    print("1 : Drum Map A")
    print("2 : Drum Map B")
    try:
        ipt_mode = int(input("Channel Mode : "))
        if ipt_mode == 0:
            cmnt_mode = "Instrument"
        elif ipt_mode == 1:
            cmnt_mode = "Drum Map A"
        elif ipt_mode == 2:
            cmnt_mode = "Drum Map B"
        else:
            raise
    except:
        raise ValueError("Invalid Mode Selection")
    trka = [port, channel, 0x15, ipt_mode]
    return [common.gs_syx(trka),
            "Set " + cmnt_port + " Channel " + str(ipt_chnl) + " to " + cmnt_mode]

def outport():
    print("WARNING : This setting is NOT available on modules that have only 1 Output Port (e.g. SC-8820)")
    cp = common.get_port_and_channel()
    port = cp.port
    channel = cp.channel
    cmnt_port = cp.cmnt_port
    ipt_chnl = cp.channel_actual
    # Output Port
    print("0 : OUTPUT-1")
    print("1 : OUTPUT-2")
    print("2 : OUTPUT-2(L)")
    print("3 : OUTPUT-2(R)")
    try:
        ipt_oprt = int(input("Output Port : "))
        if ipt_oprt == 0:
            cmnt_oprt = "OUTPUT-1"
        elif ipt_oprt == 1:
            cmnt_oprt = "OUTPUT-2"
        elif ipt_oprt == 2:
            cmnt_oprt = "OUTPUT-2(L)"
        elif ipt_oprt == 3:
            cmnt_oprt = "OUTPUT-2(R)"
        else:
            raise
        oprt = ipt_oprt
    except:
        raise ValueError("Invalid Output Port Selection")
    # SysEx Generation
    trka = [port, channel, 0x21, oprt]
    return [common.gs_syx(trka),
            "Send " + cmnt_port + " Channel " + str(ipt_chnl) + " to " + cmnt_oprt]

def sendeq():
    cp = common.get_port_and_channel()
    port = cp.port
    channel = cp.channel
    cmnt_port = cp.cmnt_port
    ipt_chnl = cp.channel_actual
    # Mode
    print("0 : Exclude from System EQ")
    print("1 : Include to System EQ (Default)")
    try:
        ipt_mode = int(input("Mode : "))
        if ipt_mode == 0:
            cmnt = "Exclude " + cmnt_port + " Channel " + str(ipt_chnl) + " from System EQ"
        elif ipt_mode == 1:
            cmnt = "Include " + cmnt_port + " Channel " + str(ipt_chnl) + " to System EQ"
        else:
            raise
    except:
        raise ValueError("Invalid Mode Selection")
    trka = [port, channel, 0x20, ipt_mode]
    return [common.gs_syx(trka), cmnt]

def reverb():
    # Phase 1
    print("Reverb Menu")
    menu_lst = ["Macro", "Pre-LPF", "Level", "Time", "Delay Feedback", "Pre-Delay Time [ms]"]
    menu_address = [0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x37]
    macro_lst = ["Room 1", "Room 2", "Room 3", "Hall 1", "Hall 2", "Plate", "Delay", "Panning Delay"]
    cnt = 0
    for i in menu_lst:
        print(str(cnt) + " : " + i)
        cnt += 1
    try:
        ipt_phase1 = int(input("Menu : "))
        # Macro
        if ipt_phase1 == 0:
            print("Reverb Macro")
            cnt = 0
            for i in macro_lst:
                print(str(cnt) + " : " + i)
                cnt += 1
            ipt_max = 7
        elif ipt_phase1 == 1:
            ipt_max = 7
        else:
            ipt_max = 127
        ipt_phase2 = int(input(menu_lst[ipt_phase1] + "(0 ~ " + str(ipt_max) + ") : "))
        if ipt_phase2 < 0 or ipt_phase2 > ipt_max:
            raise
        # Comment
        if ipt_phase1 == 0:
            cmnt = "Set Reverb " + menu_lst[ipt_phase1] + " to " + macro_lst[ipt_phase2]
        else:
            cmnt = "Set Reverb " + menu_lst[ipt_phase1] + " to " + str(ipt_phase2)
        return [common.gs_syx([0x40, 0x01, menu_address[ipt_phase1], ipt_phase2]),
                cmnt]
    except:
        raise ValueError("Invalid Input")

def chorus():
    # Phase 1
    print("Chorus Menu")
    menu_lst = ["Macro", "Pre-LPF", "Level", "Feedback", "Delay", "Rate", "Depth", "Send Level to Reverb", "Send Level to Delay"]
    menu_address = [0x38, 0x39, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F, 0x40]
    macro_lst = ["Chorus 1", "Chorus 2", "Chorus 3", "Chorus 4", "Feedback Chorus", "Flanger", "Short Delay", "Short Delay[FB]"]
    cnt = 0
    for i in menu_lst:
        print(str(cnt) + " : " + i)
        cnt += 1
    try:
        ipt_phase1 = int(input("Menu : "))
        # Macro
        if ipt_phase1 == 0:
            print("Chorus Macro")
            cnt = 0
            for i in macro_lst:
                print(str(cnt) + " : " + i)
                cnt += 1
            ipt_max = 7
        else:
            ipt_max = 127
        ipt_phase2 = int(input(menu_lst[ipt_phase1] + "(0 ~ " + str(ipt_max) + ") : "))
        if ipt_phase2 < 0 or ipt_phase2 > ipt_max:
            raise
        # Comment
        if ipt_phase1 == 0:
            cmnt = "Set Chorus " + menu_lst[ipt_phase1] + " to " + macro_lst[ipt_phase2]
        else:
            cmnt = "Set Chorus " + menu_lst[ipt_phase1] + " to " + str(ipt_phase2)
        return [common.gs_syx([0x40, 0x01, menu_address[ipt_phase1], ipt_phase2]),
                cmnt]
    except:
        raise ValueError("Invalid Input")

def delay():
    menu_lst = ["Macro", "Pre-LPF", "Time Center", "Time Ratio Left", "Time Ratio Right", "Level Center", "Level Left",
                "Level Right", "Level", "Feedback", "Send Level to Reverb"]
    menu_address = [0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5A]
    macro_lst = ["Delay 1", "Delay 2", "Delay 3", "Delay 4", "Pan Delay 1", "Pan Delay 2", "Pan Delay 3", "Pan Delay 4",
                 "Delay to Reverb", "Pan Repeat"]
    print("will be implemented later")
    cnt = 0
    for i in menu_lst:
        print(str(cnt) + " : " + i)
        cnt += 1
    try:
        ipt_phase1 = int(input("Menu : "))
        if ipt_phase1 == 2:
            # Time Center
            ipt_phase2 = int(input("Delay Time Center (0.1 ~ 1000) : "))
            res, rest = delay_time_center(ipt_phase2)
            print("Optimized to " + str(rest))
            cmnt = "Set Delay Time Center to " + str(rest)
            resx = common.gs_syx([0x40, 0x01, menu_address[ipt_phase1], res])
        elif ipt_phase1 == 3 or ipt_phase1 == 4:
            # Time Ratio (n / 4, 4 ~ 500%)
            ipt_phase2 = int(input("Delay " + menu_lst[ipt_phase1] + " (4 ~ 500%) : "))
            print("Optimized to " + str(round(ipt_phase2 / 4, 0) * 4) + "%")
            res = round(ipt_phase2 / 4, 0)
            cmnt = "Set Delay " + menu_lst[ipt_phase1] + " to " + str(round(ipt_phase2 / 4, 0) * 4) + "%"
            resx = common.gs_syx([0x40, 0x01, menu_address[ipt_phase1], res])
        else:
            if ipt_phase1 == 0:
                print("Chorus Macro")
                cnt = 0
                for i in macro_lst:
                    print(str(cnt) + " : " + i)
                    cnt += 1
                ipt_max = 9
            else:
                ipt_max = 127
            ipt_phase2 = int(input("Delay " + menu_lst[ipt_phase1] + " (0 ~ " + str(ipt_max) + ") : "))
            cmnt = "Set Delay " + menu_lst[ipt_phase1] + " to " + str(ipt_phase2)
            resx = common.gs_syx([0x40, 0x01, menu_address[ipt_phase1], ipt_phase2])
        return [resx, cmnt]
    except:
        raise ValueError("Invalid Input")

def syseq():
    print("System EQ")
    menu_lst = ["Low-Freq", "Low-Gain", "Hi-Freq", "Hi-Gain"]
    cnt = 0
    for i in menu_lst:
        print(str(cnt) + " : " + i)
        cnt += 1
    try:
        ipt_phase1 = int(input("Menu : "))
        if ipt_phase1 == 0:
            print("0 : 200Hz")
            print("1 : 400Hz")
            val = int(input(menu_lst[ipt_phase1] + " : "))
            if val not in [0, 1]:
                raise
            cmnt = "Set System-EQ Low-Freq to " + ["200Hz", "400Hz"][val]
        elif ipt_phase1 == 2:
            print("0 : 3kHz")
            print("1 : 6kHz")
            val = int(input(menu_lst[ipt_phase1] + " : "))
            if val not in [0, 1]:
                raise
            cmnt = "Set System-EQ Hi-Freq to " + ["3kHz", "6kHz"][val]
        elif ipt_phase1 == 1 or ipt_phase1 == 3:
            print("-12 ~ 0 ~ 12")
            ipt = int(input(menu_lst[ipt_phase1] + " : "))
            if ipt < -12 or ipt > 12:
                raise
            else:
                val = 0x40 + ipt
            cmnt = "Set System-EQ " + ["", "Low-Gain", "", "Hi-Gain"][ipt_phase1] + " to " + str(val)
        else:
            raise
        return [common.gs_syx([0x40, 0x02, ipt_phase1, val]),
                cmnt]
    except:
        raise ValueError("Invalid Input")
