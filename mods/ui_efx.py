from mods import efx
from mods import common

def ui_efx():
    print("EFX Menu")
    print("1 : Set EFX Macro")
    print("2 : Set EFX Parameter")
    print("3 : Channel EFX Send")
    ipt1 = int(input("efx> "))
    if ipt1 == 1:
        cnt = 0
        for i in efx.efx_types:
            print("#" + str(cnt) + " : " + i[0] + "(" + common.hex2str_once(i[1]) + "h, " + common.hex2str_once(
                i[2]) + "h)")
            cnt += 1
        ipt2 = int(input("EFX Macro : "))
        resx = common.gs_syx([0x40, 0x03, 0x00, efx.efx_types[ipt2][1], efx.efx_types[ipt2][2]])
        cmnt = "Set EFX Macro to " + efx.efx_types[ipt2][0]
    elif ipt1 == 2:
        cnt = 0
        for i in efx.efx_types:
            print("#" + str(cnt) + " : " + i[0] + "(" + common.hex2str_once(i[1]) + "h, " + common.hex2str_once(
                i[2]) + "h)")
            cnt += 1
        ipt2 = int(input("EFX Macro to Set Parameter : "))
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
        cp = common.get_port_and_channel()
        port = cp.port
        channel = cp.channel
        cmnt_port = cp.cmnt_port
        ipt_chnl = cp.channel_actual
        # Mode
        print("0 : Exclude from System EQ")
        print("1 : Include to System EQ (Default)")
        ipt_mode = int(input("Mode : "))
        if ipt_mode == 0:
            cmnt = cmnt_port + " Channel " + str(ipt_chnl) + " EFX Send OFF"
        elif ipt_mode == 1:
            cmnt = cmnt_port + " Channel " + str(ipt_chnl) + " EFX Send ON"
        else:
            raise
        resx = common.gs_syx([port, channel, 0x22, ipt_mode])
    else:
        raise
    return resx, cmnt
