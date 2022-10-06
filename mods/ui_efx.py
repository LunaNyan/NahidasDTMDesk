from mods import efx
from mods import common

def findefx():
    cnt = 0
    pg = 0
    lst = []
    for i in efx.efx_types:
        lst.append("#" + str(cnt) + " : " + i[0] + "(" + common.hex2str_once(i[1]) + "h, " + common.hex2str_once(
            i[2]) + "h)")
        cnt += 1
    while True:
        for i in range(16):
            print(lst[(pg * 16) + i])
        ipt = input("EFX Macro (Page : " + str(pg) + ", << / < / > / >>) : ")
        if ipt == "<<":
            pg = 0
        elif ipt == ">>":
            pg = 3
        elif ipt == "<":
            if pg == 0:
                print("you are in first page")
            else:
                pg -= 1
        elif ipt == ">":
            if pg == 3:
                print("you are in last page")
            else:
                pg += 1
        else:
            return int(ipt)

def ui_efx():
    print("EFX Menu")
    print("1 : Set EFX Macro")
    print("2 : Set EFX Parameter")
    print("3 : EFX Global Parameters")
    print("4 : Channel EFX Send")
    ipt1 = int(input("efx> "))
    if ipt1 == 1:
        ipt2 = findefx()
        resx = common.gs_syx([0x40, 0x03, 0x00, efx.efx_types[ipt2][1], efx.efx_types[ipt2][2]])
        cmnt = "Set EFX Macro to " + efx.efx_types[ipt2][0]
    elif ipt1 == 2:
        ipt2 = findefx()
        cnt = 0
        for k in efx.efx_types[ipt2][3]:
            print("#" + str(cnt) + " : " + k[0])
            cnt += 1
        ipt3 = int(input("EFX Parameter # : "))
        ep = efx.efx_types[ipt2][3][ipt3]
        print(common.hex2str_once(ep[1]) + "h : " +  ep[0])
        print(ep[2])
        ipt4 = int(input("Value : "))
        res, resv = ep[3](ipt4)
        print("Optimized to " + str(resv))
        resx = common.gs_syx([0x40, 0x03, ep[1], res])
        cmnt = "Set EFX " + ep[0] + " to " + str(resv)
    elif ipt1 == 3:
        sfx_menu = ["Send Level to Reverb", "Send Level to Chorus", "Send Level to Delay", "Control Source 1",
                    "Control Depth 1", "Control Source 2", "Control Depth 2", "Send EQ Switch"]
        sfx_range = ["0 ~ 127", "0 ~ 127", "0 ~ 127", "Off, CC1-95, CAf, Bend", "0 ~ 64 ~ 127",
                    "Off, CC1-95, CAf, Bend", "0 ~ 64 ~ 127", "OFF / ON"]
        sfx_address = [0x17, 0x18, 0x19, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F]
        cnt = 1
        for i in sfx_menu:
            print(str(cnt) + " : " + i)
            cnt += 1
        ipt2 = int(input("EFX Global Param : "))
        ipt3 = int(input("EFX " + sfx_menu[ipt2-1] + " : "))
        resx = common.gs_syx([0x40, 0x03, sfx_address[ipt2-1], ipt3])
        cmnt = "Set EFX " + sfx_menu[ipt2] + " to " + str(ipt3)
    elif ipt1 == 4:
        cp = common.get_port_and_channel()
        port = cp.port
        channel = cp.channel
        cmnt_port = cp.cmnt_port
        ipt_chnl = cp.channel_actual
        # Mode
        print("0 : EFX OFF")
        print("1 : EFX ON")
        ipt_mode = int(input("Mode : "))
        if ipt_mode == 0:
            cmnt = cmnt_port + " Channel " + str(ipt_chnl) + " EFX Send OFF"
        elif ipt_mode == 1:
            cmnt = cmnt_port + " Channel " + str(ipt_chnl) + " EFX Send ON"
        else:
            raise
        resx = common.gs_syx([port, channel + 0x30, 0x22, ipt_mode])
    else:
        raise ValueError("abort")
    return resx, cmnt
