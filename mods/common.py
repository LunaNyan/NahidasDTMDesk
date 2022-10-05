class port_and_channel:
    def __init__(self, port, channel, cmnt_port, channel_actual):
        self.port = port
        self.channel = channel
        self.cmnt_port = cmnt_port
        self.channel_actual = channel_actual

def get_port_and_channel():
    print("0 : Current Port (Default)")
    print("1 : Opposite side of Current Port")
    # Port
    try:
        ipt_port = int(input("Port : "))
    except:
        raise ValueError("Invalid Port Selection")
    if ipt_port == 0:
        port = 0x40
        cmnt_port = "Current Port"
    elif ipt_port == 1:
        port = 0x50
        cmnt_port = "Opposite Port"
    else:
        raise ValueError("Invalid Port Selection")
    # Channel
    try:
        ipt_chnl = int(input("MIDI Channel : "))
        if ipt_chnl > 16 or ipt_chnl < 1:
            raise
        elif ipt_chnl == 10:
            channel = 0x10
        elif ipt_chnl < 10:
            channel = 0x10 + ipt_chnl
        else:
            channel = 0x0F + ipt_chnl
    except:
        raise ValueError("Invalid Channel Selection")
    return port_and_channel(port, channel, cmnt_port, ipt_chnl)

def checksum(carry):
    return 128 - (sum(carry) % 128)

def gs_syx(carry, head=None):
    if head == None:
        head_i = [0x41, 0x10, 0x42, 0x12]
    else:
        head_i = head
    return [0xF0] + head_i + carry + [128 - (sum(carry) % 128), 0xF7]

def hex2str_once(hx):
    t1 = hex(hx).replace("0x", "")
    if len(t1) == 1:
        tf = "0" + t1.upper() + " "
    else:
        tf = t1.upper() + " "
    return tf

def tostr(carry):
    tf = ""
    for i in carry:
        t1 = hex(i).replace("0x", "")
        if len(t1) == 1:
            tf += "0" + t1.upper() + " "
        else:
            tf += t1.upper() + " "
    return tf[:-1]