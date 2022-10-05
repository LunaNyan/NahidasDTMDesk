import math

def thru(value):
    # value == result
    if int(value) > 127 or int(value) < 0:
        raise ValueError
    return int(value), int(value)

def predelay(value):
    # 0 ~ 5 : 0.1
    # 5.5 ~ 9.5 : 0.5
    # 10 ~ 50 : 1
    # 52 ~ 100 : 2
    # Available up to 7Dh
    tms = float(value)
    if tms > 100 or tms < 0:
        raise ValueError
    if tms >= 0 and tms < 5:
        return math.trunc(tms / 0.1), math.trunc(tms / 0.1) * 0.1
    elif tms >= 5 and tms < 10:
        return 0x32 + int(math.trunc(tms - 5 / 0.5)), math.trunc(tms / 0.5) * 0.5
    elif tms >= 10 and tms <= 50:
        return 0x64 + int(tms - 10), int(tms)
    elif tms > 50 and tms <= 52:
        return 0x65
    elif tms > 52 and tms < 100:
        return 0x65 + int(math.trunc(tms - 50 / 2)), math.trunc(tms / 2) * 2
    else:
        return 0x7d, 100

def time1(value):
    # 200 ~ 550 : 5
    # 550 ~ 1000 : 10
    tms = int(value)
    if tms > 1000 or tms < 200:
        raise ValueError
    if tms >= 200 and tms < 550:
        return math.trunc(int(tms) / 5), math.trunc(int(tms) / 5) * 5
    elif tms >= 550 and tms <= 1000:
        return 0x46 + math.trunc((int(tms) - 550) / 10), math.trunc(int(tms) / 10) * 10
    else:
        return 0x73, 1000

def time2(value):
    # 200 ~ 600 : 5
    # 600 ~ 1000 : 10
    t = int(value)
    if t > 1000 or t < 200:
        raise ValueError
    if t >= 200 and t < 600:
        return math.trunc((int(t) - 200) / 5), math.trunc(int(t) / 5) * 5
    elif t >= 600 and t <= 1000:
        return 0x4B + math.trunc((int(t) - 600) / 10), math.trunc(int(t) / 10) * 10
    else:
        return 0x73, 1000

def time3(value):
    # 0 ~ 10 : 0.5
    # 10 ~ 100 : 1
    # 100 ~ 500 : 10
    t = float(value)
    if t > 500 or t < 0:
        raise ValueError
    if t >= 0 and t < 10:
        return math.trunc(int(t) / .5), math.trunc(int(t) / .5) * .5
    elif t >= 10 and t < 100:
        return 0x3c + int(t) - 10, int(t)
    elif t >= 100 and t <= 500:
        return 0x60 + math.trunc((int(t) - 100) / 10), math.trunc(int(t) / 10) * 10

def time4(value):
    # n / 5
    t = int(value)
    if t > 635 or t < 0:
        raise ValueError
    return math.trunc(t / 5), math.trunc(t / 5) * 5

def rate1(value):
    # 0.05 ~ 5 : 0.05
    # 5 ~ 10 : 0.10
    t = float(value)
    if t > 10 or t < 0.05:
        raise ValueError
    if t >= 0.05 and t < 5:
        return math.trunc(int(t) / .05), math.trunc(int(t) / .05) * .05
    elif t >= 5 and t <= 10:
        return 0x63 + math.trunc((int(t) - 5) / .1), math.trunc(int(t) / .1) * .1

def rate2(value):
    # n / 0.05
    t = float(value)
    if t > 6.4 or t < 0.05:
        raise ValueError
    return math.trunc(int(t) / .05), math.trunc(int(t) / .05) * .05

def centered12(value):
    v = int(value)
    if v > 12 or v < -12:
        raise ValueError
    return 0x40 + v

def centeredfull(value):
    v = int(value)
    if v > 63 or v < -64:
        raise ValueError
    return 0x40 + v

def hfdamp(value):
    try:
        v = int(value)
        if v > 8000 or v < 315:
            raise ValueError
        elif v >= 315 and v < 400:
            return 0x00, 315
        elif v >= 400 and v < 500:
            return 0x08, 400
        elif v >= 500 and v < 630:
            return 0x10, 500
        elif v >= 630 and v < 800:
            return 0x18, 630
        elif v >= 800 and v < 1000:
            return 0x20, 800
        elif v >= 1000 and v < 1250:
            return 0x28, 1000
        elif v >= 1250 and v < 1600:
            return 0x30, 1250
        elif v >= 1600 and v < 2000:
            return 0x38, 1600
        elif v >= 2000 and v < 2500:
            return 0x40, 2000
        elif v >= 2500 and v < 3150:
            return 0x48, 2500
        elif v >= 3150 and v < 4000:
            return 0x50, 3150
        elif v >= 4000 and v < 5000:
            return 0x58, 4000
        elif v >= 5000 and v < 6300:
            return 0x60, 5000
        elif v >= 6300 and v < 8000:
            return 0x68, 6300
        else:
            return 0x70, 8000
    except ValueError:
        return 0x78, "Bypass" # Bypass

def lpf(value):
    v = int(value)
    if v > 8000 or v < 250:
        raise ValueError
    elif v >= 250 and v < 315:
        return 0x00, 250
    elif v >= 315 and v < 400:
        return 0x08, 315
    elif v >= 400 and v < 500:
        return 0x10, 400
    elif v >= 500 and v < 630:
        return 0x18, 500
    elif v >= 630 and v < 800:
        return 0x20, 630
    elif v >= 800 and v < 1000:
        return 0x28, 800
    elif v >= 1000 and v < 1250:
        return 0x30, 1000
    elif v >= 1250 and v < 1600:
        return 0x38, 1250
    elif v >= 1600 and v < 2000:
        return 0x40, 1600
    elif v >= 2000 and v < 2500:
        return 0x48, 2000
    elif v >= 2500 and v < 3150:
        return 0x50, 2500
    elif v >= 3150 and v < 4000:
        return 0x58, 3150
    elif v >= 4000 and v < 5000:
        return 0x60, 4000
    elif v >= 5000 and v < 6300:
        return 0x68, 5000
    elif v >= 6300 and v < 8000:
        return 0x70, 6300
    else:
        return 0x78, 8000

def cfreq(value):
    v = int(value)
    if v > 8000 or v < 250:
        raise ValueError
    elif v >= 250 and v < 315:
        return 0x00, 250
    elif v >= 315 and v < 400:
        return 0x08, 315
    elif v >= 400 and v < 500:
        return 0x10, 400
    elif v >= 500 and v < 630:
        return 0x18, 500
    elif v >= 630 and v < 800:
        return 0x20, 630
    elif v >= 800 and v < 1000:
        return 0x28, 800
    elif v >= 1000 and v < 1250:
        return 0x30, 1000
    elif v >= 1250 and v < 1600:
        return 0x38, 1250
    elif v >= 1600 and v < 2000:
        return 0x40, 1600
    elif v >= 2000 and v < 2500:
        return 0x48, 2000
    elif v >= 2500 and v < 3150:
        return 0x50, 2500
    elif v >= 3150 and v < 4000:
        return 0x58, 3150
    elif v >= 4000 and v < 5000:
        return 0x60, 4000
    elif v >= 5000 and v < 6300:
        return 0x68, 5000
    elif v >= 6300 and v < 8000:
        return 0x70, 6300
    else:
        return 0x78, 8000

def eqfreq(value):
    return

def manual(value):
    # 100 ~ 300 : 10
    # 300 ~ 1000 : 20
    # 1000 ~ 8000 : 100
    v = int(value)
    if v > 8000 or v < 100:
        raise ValueError
    if v >= 100 and v < 300:
        return math.trunc((v - 100) / 10), math.trunc(v / 10) * 10
    elif v >= 300 and v < 1000:
        return 0x14 + math.trunc((v - 300) / 20), math.trunc(v / 20) * 20
    elif v >= 1000 and v <= 8000:
        return 0x37 + math.trunc((v - 1000) / 100), math.trunc(v / 100) * 100

def azimuth(value):
    return

def accl(value):
    return [0x00, 0x08, 0x10, 0x18, 0x20, 0x28, 0x30, 0x38, 0x40, 0x48, 0x50, 0x58, 0x60, 0x68, 0x70, 0x78][int(value)], value

def centered_feedback(value):
    # n/2
    v = int(value)
    return (math.trunc(v / 2) * 2) + 0x40, math.trunc(v / 2) * 2

efx_types = [
    # SC-8850 기준
    # 88Pro, 8820도 동일함
    ["Thru", 0x00, 0x00, [
        ["No Parameters available", 0x03, "go back", thru]
    ]],
    ["Stereo EQ", 0x01, 0x00, [
        ["Low Freq", 0x03, "0 (200) / *1 (400Hz)*", thru],
        ["Low Gain", 0x04, "-12 ~ *+5* ~ +12", centered12],
        ["Hi Freq", 0x05, "0 (4KHz) / *1 (8KHz)*", thru],
        ["Hi Gain", 0x06, "*-12* ~ +12", centered12],
        ["M1 Freq", 0x07, "200 ~ *1.6k* ~ 6.3k", eqfreq],
        ["M1 Q", 0x08, "*0 (0.5)* / 1 / 2 / 3 (4) / 4 (9)", thru],
        ["M1 Gain", 0x09, "-12 ~ *+8* ~ +12", centered12],
        ["M2 Freq", 0x0A, "200 ~ *1.6k* ~ 6.3k", eqfreq],
        ["M2 Q", 0x0B, "*0 (0.5)* / 1 / 2 / 3 (4) / 4 (9)", thru],
        ["M2 Gain", 0x0C, "-12 ~ *+8* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Spectrum", 0x01, 0x01, [
        ["Band1 (250Hz) Gain", 0x03, "-12 ~ *-4* ~ +12", centered12],
        ["Band2 (500Hz) Gain", 0x04, "-12 ~ *+1* ~ +12", centered12],
        ["Band3 (1000Hz) Gain", 0x05, "-12 ~ *+3* ~ +12", centered12],
        ["Band4 (1250Hz) Gain", 0x06, "-12 ~ *+6* ~ +12", centered12],
        ["Band5 (2000Hz) Gain", 0x07, "-12 ~ *+2* ~ +12", centered12],
        ["Band6 (3150Hz) Gain", 0x08, "-12 ~ *-1* ~ +12", centered12],
        ["Band7 (4000Hz) Gain", 0x09, "-12 ~ *-4* ~ +12", centered12],
        ["Band8 (8000Hz) Gain", 0x0A, "-12 ~ *-5* ~ +12", centered12],
        ["Width", 0x0B, "0 (0.5) / 1 / *2* / 3 (4) / 4 (9)", thru],
        ["Pan", 0x15, "-63 ~ *0* ~ +63", centeredfull],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Enhancer", 0x01, 0x02, [
        ["Sens", 0x03, "0 ~ *64* ~ 127", thru],
        ["Mix", 0x04, " 0 ~ *127*", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Humanizer", 0x01, 0x03, [
        ["Drive", 0x03, "0 ~ *48* ~ 127", thru],
        ["Drive Sw", 0x04, "0/1", thru],
        ["Vowel", 0x05, "*0(a)*/1(i)/2(u)/3(e)/4(o)", thru],
        ["Accel", 0x06, "0 ~ *15*", accl],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Pan", 0x15, "-63 ~ *0* ~ +63", centeredfull],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Overdrive", 0x01, 0x10, [
        ["Drive", 0x03, "0 ~ *48* ~ 127", thru],
        ["Amp Type", 0x04, "0(Small)/*1(BltIn)*/2(2-Stk)/3(3-Stk)", thru],
        ["Amp Sw", 0x05, "0/1", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Pan", 0x15, "-63 ~ *0* ~ +63", centeredfull],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Distortion", 0x01, 0x11, [
        ["Drive", 0x03, "0 ~ *48* ~ 127", thru],
        ["Amp Type", 0x04, "0(Small)/*1(BltIn)*/2(2-Stk)/3(3-Stk)", thru],
        ["Amp Sw", 0x05, "0/1", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Pan", 0x15, "-63 ~ *0* ~ +63", centeredfull],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Phaser", 0x01, 0x20, [
        ["Manual", 0x03, "100 ~ *620* ~ 8k", manual],
        ["Rate", 0x04, "0.05 ~ *0.85* ~ 10.00", rate1],
        ["Depth", 0x05, "0 ~ *64* ~ 127", thru],
        ["Reso", 0x06, "0 ~ *16* ~ 127", thru],
        ["Mix", 0x07, "0 ~ *127*", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Auto Wah", 0x01, 0x21, [
        ["Fil Type", 0x03, "0(LPF)/*1(BPF)*", thru],
        ["Sens", 0x04, "*0* ~ 127", thru],
        ["Manual", 0x05, "0 ~ *68* ~ 127", thru],
        ["Peak", 0x06, "0 ~ *62* ~ 127", thru],
        ["Rate", 0x07, "0.05 ~ *2.05* ~ 10.00", rate1],
        ["Depth", 0x08, "0 ~ *72* ~ 127", thru],
        ["Polarity", 0x09, "0(Down)/*1(Up)*", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Pan", 0x15, "-63 ~ *0* ~ +63", centeredfull],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Rotary", 0x01, 0x22, [
        ["Low Slow", 0x03, "0.05 ~ *0.35* ~ 10.00", rate1],
        ["Low Fast", 0x04, "0.05 ~ *0.35* ~ 10.00", rate1],
        ["Low Accl", 0x05, "0 ~ *3* ~ 15", accl],
        ["Low Level", 0x06, "0 ~ *127*", thru],
        ["Hi Slow", 0x07, "0.05 ~ *0.35* ~ 10.00", rate1],
        ["Hi Fast", 0x08, "0.05 ~ *0.35* ~ 10.00", rate1],
        ["Hi Accl", 0x09, "0 ~ *3* ~ 15", accl],
        ["Hi Level", 0x0A, "0 ~ *127*", thru],
        ["Seperate", 0x0B, "0 ~ *96* ~ 127", thru],
        ["Speed", 0x0D, "0/127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Stereo Flanger", 0x01, 0x23, [
        ["Pre Filter", 0x03, "*0(Off)*/1(LPF)/2(HPF)", thru],
        ["Cutoff", 0x04, "*250* ~ 8k", cfreq],
        ["Pre Dly", 0x05, "0 ~ 1.6 ~ 100 (ms)", predelay],
        ["Rate", 0x06, "0.05 ~ *0.60* ~ 10.00", rate1],
        ["Depth", 0x07, "0 ~ *24* ~ 127", thru],
        ["Feedback", 0x08, "-98 ~ *0* ~ +98 (*2)", centered_feedback],
        ["Phase", 0x09, "0 ~ 90 (*2)", thru],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Step Flanger", 0x01, 0x24, [
        ["Pre Dly", 0x03, "0 ~ *1.0* ~ 100 ms", predelay],
        ["Rate", 0x04, "0.05 ~ *0.30* ~ 10.00", rate1],
        ["Depth", 0x05, "0 ~ *95* ~ 127", thru],
        ["Feedback", 0x06, "-98 ~ *0* ~ +98 (*2)", centered_feedback],
        ["Phase", 0x07, "0 ~ 90 (*2)", thru],
        ["Step Rate", 0x08, "0.05 ~ *2.75* ~ 10.00", rate1],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Tremolo", 0x01, 0x25, [
        ["Mod Wave", 0x03, "0(Tri)/*1(Sqr)*/2(Sin)/3(Saw1)/4(Saw2)", thru],
        ["Mod Rate", 0x04, "0.05 ~ *3.05* ~ 10.00", rate1],
        ["Mod Depth", 0x05, "0 ~ *96* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Auto Pan", 0x01, 0x26, [
        ["Mod Wave", 0x03, "0(Tri)/*1(Sqr)*/2(Sin)/3(Saw1)/4(Saw2)", thru],
        ["Mod Rate", 0x04, "0.05 ~ *3.05* ~ 10.00", rate1],
        ["Mod Depth", 0x05, "0 ~ *96* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Compressor", 0x01, 0x30, [
        ["Attack", 0x03, "0 ~ *72* ~ 127", thru],
        ["Sustain", 0x04, "0 ~ *100* ~ 127", thru],
        ["Post Gain", 0x05, "*0*/1(+6)/2(+12)/3(+18)", thru],
        ["Low Gain", 0x13, "-12 ~ *0* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Pan", 0x15, "-63 ~ *0* ~ +63", centeredfull],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Limiter", 0x01, 0x31, [
        ["Threshold", 0x03, "0 ~ *85* ~ 127", thru],
        ["Ratio", 0x04, "0(1/15)/1(1/2)/2(1/4)/*3(1/100)*", thru],
        ["Release", 0x05, "0 ~ *16* ~ 127", thru],
        ["Post Gain", 0x06, "*0*/1(+6)/2(+12)/3(+18)", thru],
        ["Low Gain", 0x13, "-12 ~ *0* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Pan", 0x15, "-63 ~ *0* ~ +63", centeredfull],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Hexa Chorus", 0x01, 0x40, [
        ["Pre Dly", 0x03, "0 ~ *2.4* ~ 100 (ms)", predelay],
        ["Rate", 0x04, "0.05 ~ *0.45* ~ 10.00", rate1],
        ["Depth", 0x05, "0 ~ *127*", thru],
        ["Pre Dly Dev", 0x06, "0 ~ *5* ~ 20", thru],
        ["Depth Dev", 0x07, "44 ~ *66* ~ 84", thru],
        ["Pan Dev", 0x08, "0 ~ *16* ~ 20", thru],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Tremolo Chorus", 0x01, 0x41, [
        ["Pre Dly", 0x03, "0 ~ *1.6* ~ 100 (ms)", predelay],
        ["Cho Rate", 0x04, "0.05 ~ *0.45* ~ 10.00", rate1],
        ["Cho Depth", 0x05, "0 ~ *40* ~ 127", thru],
        ["Trem Phase", 0x06, "0 ~ *40* ~ 90 (*2)", thru],
        ["Trem Rate", 0x07, "0.05 ~ *3.05* ~ 10.00", rate1],
        ["Trem Sep", 0x08, "0 ~ *96* ~ 127", thru],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Stereo Chorus", 0x01, 0x42, [
        ["Pre Filter", 0x03, "*0(Off)*/1(LPF)/2(HPF)", thru],
        ["Cutoff", 0x04, "*250* ~ 8k", cfreq],
        ["Pre Dly", 0x05, "0 ~ *1.0* ~ 100 (ms)", predelay],
        ["Rate", 0x06, "0.05 ~ *0.45* ~ 10.00", rate1],
        ["Depth", 0x07, "0 ~ *111* ~ 127", thru],
        ["Phase", 0x09, "0 ~ *90* (*2)", thru],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Space D", 0x01, 0x43, [
        ["Pre Dly", 0x03, "0 ~ *3.2* ~ 100 (ms)", predelay],
        ["Rate", 0x04, "0.05 ~ *0.45* ~ 10.00", rate1],
        ["Depth", 0x05, "0 ~ *127*", thru],
        ["Phase", 0x06, "0 ~ *90* (*2)", thru],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["3D Chorus", 0x01, 0x44, [
        ["Pre Dly", 0x03, "0 ~ *3.2* ~ 100 (ms)", predelay],
        ["Cho Rate", 0x04, "0.05 ~ *0.45* ~ 10.00", rate1],
        ["Cho Depth", 0x05, "0 ~ *72* ~ 127", thru],
        ["Out", 0x11, "*0(Speaker)*/1(Phones)", thru],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Stereo Delay", 0x01, 0x50, [
        ["Dly Tm L", 0x03, "0 ~ *150* ~ 500 (ms)", time3],
        ["Dly Tm R", 0x04, "0 ~ *300* ~ 500 (ms)", time3],
        ["Feedback", 0x05, "-98 ~ *+48* ~ +98", centered_feedback],
        ["Fb Mode", 0x06, "0(Norm)/*1(Cross)*", thru],
        ["Phase L", 0x07, "*0(Norm)*/1(Invert)", thru],
        ["Phase R", 0x08, "*0(Norm)*/1(Invert)", thru],
        ["HF Damp", 0x0A, "315 ~ 8k / *Bypass*", hfdamp],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Mod Delay", 0x01, 0x51, [
        ["Dly Tm L", 0x03, "0 ~ *40* ~ 500 (ms)", time3],
        ["Dly Tm R", 0x04, "0 ~ *220* ~ 500 (ms)", time3],
        ["Feedback", 0x05, "-98 ~ *+48* ~ +98", centered_feedback],
        ["Fb Mode", 0x06, "0(Norm)/*1(Cross)*", thru],
        ["Mod Rate", 0x07, "0.05 ~ *0.65* ~ 10.00", rate1],
        ["Mod Depth", 0x08, "0 ~ *21* ~ 127", thru],
        ["Mod Phase", 0x09, "0 ~ *90* (*2)", thru],
        ["HF Damp", 0x0A, "315 ~ 8k / *Bypass*", hfdamp],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["3 Tap Delay", 0x01, 0x52, [
        ["Dly Tm C", 0x03, "200 ~ *300* ~ 990 (ms)", time1],
        ["Dly Tm L", 0x04, "200 ~ *200* ~ 990 (ms)", time1],
        ["Dly Tm R", 0x05, "200 ~ *235* ~ 990 (ms)", time1],
        ["Feedback", 0x06, "-98 ~ *+32* ~ +98 (*2)", centered_feedback],
        ["Dly Lev C", 0x07, "0 ~ *127*", thru],
        ["Dly Lev L", 0x08, "0 ~ *127*", thru],
        ["Dly Lev R", 0x09, "0 ~ *127*", thru],
        ["HF Damp", 0x0A, "315 ~ 8k / *Bypass*", hfdamp],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["4 Tap Delay", 0x01, 0x53, [
        ["Dly Tm 1", 0x03, "200 ~ *500* ~ 990 (ms)", time1],
        ["Dly Tm 2", 0x04, "200 ~ *300* ~ 990 (ms)", time1],
        ["Dly Tm 3", 0x05, "200 ~ *400* ~ 990 (ms)", time1],
        ["Dly Tm 4", 0x06, "200 ~ *200* ~ 990 (ms)", time1],
        ["Dly Lev 1", 0x07, "0 ~ *127*", thru],
        ["Dly Lev 2", 0x08, "0 ~ *127*", thru],
        ["Dly Lev 3", 0x09, "0 ~ *127*", thru],
        ["Dly Lev 4", 0x0A, "0 ~ *127*", thru],
        ["Feedback", 0x0B, "-98 ~ *+32* ~ +98 (*2)", centered_feedback],
        ["HF Damp", 0x0C, "315 ~ 8k / *Bypass*", hfdamp],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Time Ctrl Delay", 0x01, 0x54, [
        ["Dly Time", 0x03, "200 ~ *500* ~ 990 (ms)", time2],
        ["Accel", 0x04, "0 ~ *10* ~ 15", accl],
        ["Feedback", 0x05, "-98 ~ *+32* ~ +98", centered_feedback],
        ["HF Damp", 0x06, "315 ~ 8k / *Bypass*", hfdamp],
        ["EFX Pan", 0x07, "-63 ~ *0* ~ +63", centeredfull],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Reverb", 0x01, 0x55, [
        ["Type", 0x03, "0(Room 1)/1(Room 2)/2(Stage 1)/*3(Stage 2)*/4(Hall 1)/5(Hall 2)", thru],
        ["Pre Dly", 0x04, "0 ~ *74* ~ 100 (ms)", predelay],
        ["Time", 0x05, "0 ~ *120* ~ 127", thru],
        ["HF Damp", 0x06, "315 ~ *6.3k* ~ 8k / Bypass", hfdamp],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Gate Reverb", 0x01, 0x56, [
        ["Type", 0x03, "*0(Norm)*/1(Reverse)/2(Sweep 1)/3(Sweep 2)", thru],
        ["Pre Dly", 0x04, "0 ~ *0.5* ~ 100 (ms)", predelay],
        ["Gate Time", 0x05, "0 ~ *13* ~ 63 (*5)", thru],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["3D Delay", 0x01, 0x57, [
        ["Dly Tm C", 0x03, "200 ~ *300* ~ 990 (ms)", time3],
        ["Dly Tm L", 0x04, "200 ~ *200* ~ 990 (ms)", time3],
        ["Dly Tm R", 0x05, "200 ~ *240* ~ 990 (ms)", time3],
        ["Feedback", 0x06, "-98 ~ *+32* ~ +98 (*2)", centered_feedback],
        ["Dly Lev C", 0x07, "0 ~ *40* ~ 127", thru],
        ["Dly Lev L", 0x08, "0 ~ *64* ~ 127", thru],
        ["Dly Lev R", 0x09, "0 ~ *64* ~ 127", thru],
        ["HF Damp", 0x0A, "315 ~ 8k / *Bypass*", hfdamp],
        ["Out", 0x11, "*0(Speaker)*/1(Phones)", thru],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["2 Pitch Shifter", 0x01, 0x60, [
        ["Coarse 1", 0x03, "-24 ~ *0* ~ +12", centeredfull],
        ["Fine 1", 0x04, "-100 ~ *+4* ~ +100", centered_feedback],
        ["Pre Dly 1", 0x05, "*0* ~ 100 (ms)", predelay],
        ["EFX Pan 1", 0x06, "-63 ~ *+63*", centeredfull],
        ["Coarse 2", 0x07, "-24 ~ *0* ~ +12", centeredfull],
        ["Fine 2", 0x08, "-100 ~ *+4* ~ +100", centered_feedback],
        ["Pre Dly 2", 0x09, "*0* ~ 100 (ms)", predelay],
        ["EFX Pan 2", 0x0A, "-63 ~ *+63*", centeredfull],
        ["Shift Mode", 0x0B, "0 ~ *2* ~ 4", thru],
        ["L.Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Feedback Pitch Shifter", 0x01, 0x61, [
        ["P.Coarse", 0x03, "-24 ~ *0* ~ +12", centeredfull],
        ["P.Fine", 0x04, "-100 ~ *0* ~ +100", centered_feedback],
        ["Feedback", 0x05, "-98 ~ *+48* ~ +98", centered_feedback],
        ["Pre Dly", 0x06, "0 ~ *45* ~ 100 (ms)", predelay],
        ["Mode", 0x07, "0 ~ *2* ~ 4", thru],
        ["EFX Pan", 0x08, "-63 ~ *0* ~ +63", centeredfull],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *+3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["3D Auto", 0x01, 0x70, [
        ["Azimuth", 0x03, "180/-168 ~ *0* ~ +168", azimuth],
        ["Speed", 0x04, "0.05 ~ *1.30* ~ 10.00", rate1],
        ["Clockwise", 0x05, "0(-)/*1(+)*", thru],
        ["Turn", 0x06, "0/*1*", thru],
        ["Out", 0x11, "*0(Speaker)*/1(Phones)", thru],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["3D Manual", 0x01, 0x71, [
        ["Azimuth", 0x03, "180/-168 ~ *0* ~ +168", azimuth],
        ["Out", 0x11, "*0(Speaker)*/1(Phones)", thru],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Lo-Fi 1", 0x01, 0x72, [
        ["Pre Filter", 0x03, "0 ~ *1* ~ 5", thru],
        ["Lo-Fi Type", 0x04, "0 ~ *5* ~ 8", thru],
        ["Post Filter", 0x05, "0 ~ *1* ~ 5", thru],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *0* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Pan", 0x15, "-63 ~ *0* ~ +63", centeredfull],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Lo-Fi 2", 0x01, 0x73, [
        ["Lo-Fi Type", 0x03, "0 ~ *1* ~ 5", thru],
        ["Fil Type", 0x04, "0(Off)/*1(LPF)*/2(HPF)", thru],
        ["Cutoff", 0x05, "250 ~ *630* ~ 8k", cfreq],
        ["R.Detune", 0x06, "*0* ~ 127", thru],
        ["R.Nz Lev", 0x07, "0 ~ *64* ~ 127", thru],
        ["W/P Sel", 0x08, "0(White)/*1(Pink)*", thru],
        ["W/P LPF", 0x09, "250 ~ 6.3k / *Bypass*", lpf],
        ["W/P Level", 0x0A, "*0* ~ 127", thru],
        ["Disc Type", 0x0B, "*0(LP)*/1(EP)/2(SP)/3(RND)", thru],
        ["Disc LPF", 0x0C, "250 ~ 6.3k / *Bypass*", lpf],
        ["Disc Nz Lev", 0x0D, "*0* ~ 127", thru],
        ["Hum Type", 0x0E, "*0(50Hz)*/1(60Hz)", thru],
        ["Hum LPF", 0x0F, "250 ~ 6.3k / *Bypass*", lpf],
        ["Hum Level", 0x10, "*0* ~ 127", thru],
        ["M/S", 0x11, "0(Mono)/*1(Stereo)*", thru],
        ["Balance", 0x12, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *0* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Pan", 0x15, "-63 ~ *0* ~ +63", centeredfull],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["OD → Chorus", 0x02, 0x00, [
        ["OD Drive", 0x03, "0 ~ *48* ~ 127", thru],
        ["OD Pan", 0x04, "-63 ~ 0 ~ +63", centeredfull],
        ["OD Amp", 0x05, "0(Small)/*1(BltIn)*/2(2-Stk)/3(3-Stk)", thru],
        ["OD Amp Sw", 0x06, "*0*/1", thru],
        ["Cho Dly", 0x08, "0 ~ *1.0* ~ 100 (ms)", predelay],
        ["Cho Rate", 0x09, "0.05 ~ *0.45* ~ 10.00", rate1],
        ["Cho Depth", 0x0A, "0 ~ *72* ~ 127", thru],
        ["Cho Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *0* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *80* ~ 127", thru]
    ]],
    ["OD → Flanger", 0x02, 0x01, [
        ["OD Drive", 0x03, "0 ~ *48* ~ 127", thru],
        ["OD Pan", 0x04, "-63 ~ 0 ~ +63", centeredfull],
        ["OD Amp", 0x05, "0(Small)/*1(BltIn)*/2(2-Stk)/3(3-Stk)", thru],
        ["OD Amp Sw", 0x06, "*0*/1", thru],
        ["FL Dly", 0x08, "0 ~ *1.6* ~ 100 (ms)", predelay],
        ["FL Rate", 0x09, "0.05 ~ *0.60* ~ 10.00", rate1],
        ["FL Depth", 0x0A, "0 ~ *40* ~ 127", thru],
        ["FL Feedback", 0x0B, "-98 ~ *+80* ~ +98", centered_feedback],
        ["FL Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *0* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *80* ~ 127", thru]
    ]],
    ["OD → Delay", 0x02, 0x02, [
        ["OD Drive", 0x03, "0 ~ *48* ~ 127", thru],
        ["OD Pan", 0x04, "-63 ~ 0 ~ +63", centeredfull],
        ["OD Amp", 0x05, "0(Small)/*1(BltIn)*/2(2-Stk)/3(3-Stk)", thru],
        ["OD Amp Sw", 0x06, "*0*/1", thru],
        ["Dly Time", 0x08, "0 ~ *250* ~ 500 (ms)", time3],
        ["Dly Fb", 0x09, "-98 ~ *+32* ~ +98", centered_feedback],
        ["Dly HF", 0x0A, "315 ~ 8k / *Bypass*", hfdamp],
        ["Dly Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *0* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *80* ~ 127", thru]
    ]],
    ["DS → Chorus", 0x02, 0x03, [
        ["DS Drive", 0x03, "0 ~ *48* ~ 127", thru],
        ["DS Pan", 0x04, "-63 ~ 0 ~ +63", centeredfull],
        ["DS Amp", 0x05, "0(Small)/*1(BltIn)*/2(2-Stk)/3(3-Stk)", thru],
        ["DS Amp Sw", 0x06, "*0*/1", thru],
        ["Cho Dly", 0x08, "0 ~ *1.0* ~ 100 (ms)", predelay],
        ["Cho Rate", 0x09, "0.05 ~ *0.45* ~ 10.00", rate1],
        ["Cho Depth", 0x0A, "0 ~ *72* ~ 127", thru],
        ["Cho Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *3* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *72* ~ 127", thru]
    ]],
    ["DS → Flanger", 0x02, 0x04, [
        ["DS Drive", 0x03, "0 ~ *48* ~ 127", thru],
        ["DS Pan", 0x04, "-63 ~ 0 ~ +63", centeredfull],
        ["DS Amp", 0x05, "0(Small)/*1(BltIn)*/2(2-Stk)/3(3-Stk)", thru],
        ["DS Amp Sw", 0x06, "*0*/1", thru],
        ["FL Dly", 0x08, "0 ~ *1.6* ~ 100 (ms)", predelay],
        ["FL Rate", 0x09, "0.05 ~ *0.60* ~ 10.00", rate1],
        ["FL Depth", 0x0A, "0 ~ *40* ~ 127", thru],
        ["FL Feedback", 0x0B, "-98 ~ *+80* ~ +98", centered_feedback],
        ["FL Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *0* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *72* ~ 127", thru]
    ]],
    ["DS → Delay", 0x02, 0x05, [
        ["DS Drive", 0x03, "0 ~ *48* ~ 127", thru],
        ["DS Pan", 0x04, "-63 ~ 0 ~ +63", centeredfull],
        ["DS Amp", 0x05, "0(Small)/*1(BltIn)*/2(2-Stk)/3(3-Stk)", thru],
        ["DS Amp Sw", 0x06, "*0*/1", thru],
        ["Dly Time", 0x08, "0 ~ *250* ~ 500 (ms)", time3],
        ["Dly Fb", 0x09, "-98 ~ *+32* ~ +98", centered_feedback],
        ["Dly HF", 0x0A, "315 ~ 8k / *Bypass*", hfdamp],
        ["Dly Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *0* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *72* ~ 127", thru]
    ]],
    ["EH → Chorus", 0x02, 0x06, [
        ["EH Sens", 0x03, "0 ~ *64* ~ 127", thru],
        ["EH Mix", 0x04, "0 ~ *127*", thru],
        ["Cho Dly", 0x08, "0 ~ *1.0* ~ 100 (ms)", predelay],
        ["Cho Rate", 0x09, "0.05 ~ *0.45* ~ 10.00", rate1],
        ["Cho Depth", 0x0A, "0 ~ *101* ~ 127", thru],
        ["Cho Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *0* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *80* ~ 127", thru]
    ]],
    ["EH → Flanger", 0x02, 0x07, [
        ["EH Sens", 0x03, "0 ~ *64* ~ 127", thru],
        ["EH Mix", 0x04, "0 ~ *127*", thru],
        ["FL Dly", 0x08, "0 ~ *1.6* ~ 100 (ms)", predelay],
        ["FL Rate", 0x09, "0.05 ~ *0.60* ~ 10.00", rate1],
        ["FL Depth", 0x0A, "0 ~ *24* ~ 127", thru],
        ["FL Feedback", 0x0B, "-98 ~ *+80* ~ +98", centered_feedback],
        ["FL Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *0* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *96* ~ 127", thru]
    ]],
    ["EH → Delay", 0x02, 0x08, [
        ["EH Sens", 0x03, "0 ~ *64* ~ 127", thru],
        ["EH Mix", 0x04, "0 ~ *127*", thru],
        ["Dly Time", 0x08, "0 ~ *250* ~ 500 (ms)", time3],
        ["Dly Fb", 0x09, "-98 ~ *+32* ~ +98", centered_feedback],
        ["Dly HF", 0x0A, "315 ~ 8k / *Bypass*", hfdamp],
        ["Dly Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *0* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *88* ~ 127", thru]
    ]],
    ["Cho → Delay", 0x02, 0x09, [
        ["Cho Dly", 0x03, "0 ~ *1.0* ~ 100 (ms)", predelay],
        ["Cho Rate", 0x04, "0.05 ~ *0.45* ~ 10.00", rate1],
        ["Cho Depth", 0x05, "0 ~ *72* ~ 127", thru],
        ["Cho Bal", 0x07, "0 ~ *64* ~ 127", thru],
        ["Dly Time", 0x08, "0 ~ *250* ~ 500 (ms)", time3],
        ["Dly Fb", 0x09, "-98 ~ *+32* ~ +98", centered_feedback],
        ["Dly HF", 0x0A, "315 ~ 8k / *Bypass*", hfdamp],
        ["Dly Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *0* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["FL → Delay", 0x02, 0x0A, [
        ["FL Dly", 0x03, "0 ~ *1.6* ~ 100 (ms)", predelay],
        ["FL Rate", 0x04, "0.05 ~ *0.60* ~ 10.00", rate1],
        ["FL Depth", 0x05, "0 ~ *40* ~ 127", thru],
        ["FL Feedback", 0x06, "-98 ~ *+80* ~ +98", centered_feedback],
        ["FL Bal", 0x07, "0 ~ *64* ~ 127", thru],
        ["Dly Time", 0x08, "0 ~ *250* ~ 500 (ms)", time3],
        ["Dly Fb", 0x09, "-98 ~ *+32* ~ +98", centered_feedback],
        ["Dly HF", 0x0A, "315 ~ 8k / *Bypass*", hfdamp],
        ["Dly Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *0* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Cho → Flanger", 0x02, 0x0B, [
        ["Cho Dly", 0x03, "0 ~ *1.0* ~ 100 (ms)", predelay],
        ["Cho Rate", 0x04, "0.05 ~ *0.45* ~ 10.00", rate1],
        ["Cho Depth", 0x05, "0 ~ *72* ~ 127", thru],
        ["Cho Bal", 0x07, "0 ~ *64* ~ 127", thru],
        ["FL Dly", 0x08, "0 ~ *1.6* ~ 100 (ms)", predelay],
        ["FL Rate", 0x09, "0.05 ~ *0.60* ~ 10.00", rate1],
        ["FL Depth", 0x0A, "0 ~ *40* ~ 127", thru],
        ["FL Feedback", 0x0B, "-98 ~ *+80* ~ +98", centered_feedback],
        ["FL Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["Low Gain", 0x13, "-12 ~ *0* ~ +12", centered12],
        ["Hi Gain", 0x14, "-12 ~ *0* ~ +12", centered12],
        ["Level", 0x16, "0 ~ *112* ~ 127", thru]
    ]],
    ["Rotary Multi", 0x03, 0x00, [
        ["OD Drive", 0x03, "0 ~ *13* ~ 127", thru],
        ["OD Sw", 0x04, "0/*1*", thru],
        ["EQ L Gain", 0x05, "-12 ~ *0* ~ +12", centered12],
        ["EQ M Fq", 0x06, "200 ~ *1.6k* ~ 1.3k", eqfreq],
        ["EQ M Q", 0x07, "*0(0.5)*/1/2/3(4.0)/4(9.0)", thru],
        ["EQ M Gain", 0x08, "-12 ~ *0* ~ +12", centered12],
        ["EQ H Gain", 0x09, "-12 ~ *0* ~ +12", centered12],
        ["RT L Slow", 0x0A, "0.05 ~ *0.35* ~ 10.00", rate1],
        ["RT L Fast", 0x0B, "0.05 ~ *0.35* ~ 10.00", rate1],
        ["RT L Accl", 0x0C, "0 ~ *3* ~ 15", accl],
        ["RT L Lev", 0x0D, "0 ~ *127*", thru],
        ["RT H Slow", 0x0E, "0.05 ~ *0.35* ~ 10.00", rate1],
        ["RT H Fast", 0x0F, "0.05 ~ *0.35* ~ 10.00", rate1],
        ["RT H Accl", 0x10, "0 ~ *3* ~ 15", accl],
        ["RT H Lev", 0x11, "0 ~ *127*", thru],
        ["RT Sept", 0x12, "0 ~ *96* ~ 127", thru],
        ["RT Speed", 0x13, "0/127", thru],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["GTR Multi 1", 0x04, 0x00, [
        ["Cmp Atk", 0x03, "0 ~ *100* ~ 127", thru],
        ["Cmp Sus", 0x04, "0 ~ *80* ~ 127", thru],
        ["Cmp Level", 0x05, "0 ~ *100* ~ 127", thru],
        ["Cmp Sw", 0x06, "0/*1*", thru],
        ["OD/DS", 0x07, "*0(OD)*/1(DS)", thru],
        ["OD/DS Drive", 0x08, "0 ~ *80* ~ 127", thru],
        ["OD/DS Amp", 0x09, "*0(Small)*/1(BltIn)/2(2-Stk)/3(3-Stk)", thru],
        ["OD/DS Amp Sw", 0x0A, "0/*1*", thru],
        ["OD/DS L Gain", 0x0B, "-12 ~ *+5* ~ +12", centered12],
        ["OD/DS H Gain", 0x0C, "-12 ~ *+10* ~ +12", centered12],
        ["OD/DS Sw", 0x0D, "0/*1*", thru],
        ["CF Sel", 0x0E, "*0(Chorus)*/1(Flanger)", thru],
        ["CF Rate", 0x0F, "0.00 ~ 0.45 ~ 6.40", rate2],
        ["CF Depth", 0x10, "0 ~ *30* ~ 127", thru],
        ["CF Fb", 0x11, "-98 ~ *+76* + +98", centered_feedback],
        ["CF Mix", 0x12, "0 ~ *40* ~ 127", thru],
        ["Dly Time", 0x13, "0 ~ *300* ~ 635 (ms)", time4],
        ["Dly Fb", 0x14, "0 ~ *34* ~ 127", thru],
        ["Dly Mix", 0x15, "0 ~ *15* ~ 127", thru],
        ["Level", 0x16, "0 ~ *110* ~ 127", thru]
    ]],
    ["GTR Multi 2", 0x04, 0x01, [
        ["Cmp Atk", 0x03, "0 ~ *70* ~ 127", thru],
        ["Cmp Sus", 0x04, "0 ~ *127*", thru],
        ["Cmp Level", 0x05, "0 ~ *90* ~ 127", thru],
        ["Cmp Sw", 0x06, "0/*1*", thru],
        ["OD/DS Sel", 0x07, "*0(Odrv)*/1(Dist)", thru],
        ["OD/DS Drive", 0x08, "0 ~ *80* ~ 127", thru],
        ["OD/DS Amp", 0x09, "0(Small)/1(BltIn)/*2(2-Stk)*/3(3-Stk)", thru],
        ["OD/DS Amp Sw", 0x0A, "0/*1*", thru],
        ["OD/DS Sw", 0x0B, "0/*1*", thru],
        ["EQ L Gain", 0x0C, "-12 ~ *+12*", centered12],
        ["EQ M Fq", 0x0D, "200 ~ *1k* ~ 6.3k", eqfreq],
        ["EQ M Q", 0x0E, "0(0.5)/1/*2*/3(4.0)/4(9.0)", thru],
        ["EQ M Gain", 0x0F, "-12 ~ *+5* ~ +12", centered12],
        ["EQ H Gain", 0x10, "-12 ~ *+10* ~ +12", centered12],
        ["CF Sel", 0x11, "*0(Chorus)*/1(Flanger)", thru],
        ["CF Rate", 0x12, "0.00 ~ *0.45* ~ 6.40", rate2],
        ["CF Depth", 0x13, "0 ~ *96* ~ 127", thru],
        ["CF Fb", 0x14, "-98 ~ *+76* + +98", centered_feedback],
        ["CF Mix", 0x15, "*0* ~ 127", thru],
        ["Level", 0x16, "0 ~ *110* ~ 127", thru]
    ]],
    ["GTR Multi 3", 0x04, 0x02, [
        ["Wah Fil", 0x03, "0(LPF)/*1(BPF)*", thru],
        ["Wah Man", 0x04, "0 ~ *60* ~ 127", thru],
        ["Wah Peak", 0x05, "0 ~ *10* ~ 127", thru],
        ["Wah Sw", 0x06, "0/*1*", thru],
        ["OD/DS", 0x07, "0(OD)/*1(DS)*", thru],
        ["OD/DS Drive", 0x08, "0 ~ *80* ~ 127", thru],
        ["OD/DS Amp", 0x09, "0(Small)/1(BltIn)/*2(2-Stk)*/3(3-Stk)", thru],
        ["OD/DS Amp Sw", 0x0A, "0/*1*", thru],
        ["OD/DS L Gain", 0x0B, "-12 ~ *+0* ~ +12", centered12],
        ["OD/DS H Gain", 0x0C, "-12 ~ *+0* ~ +12", centered12],
        ["OD/DS Sw", 0x0D, "0/*1*", thru],
        ["CF Sel", 0x0E, "*0(Chorus)*/1(Flanger)", thru],
        ["CF Rate", 0x0F, "0.00 ~ 0.45 ~ 6.40", rate2],
        ["CF Depth", 0x10, "*0* ~ 127", thru],
        ["CF Fb", 0x11, "-98 ~ *+50* + +98", centered_feedback],
        ["CF Mix", 0x12, "0 ~ *50* ~ 127", thru],
        ["Dly Time", 0x13, "0 ~ *160* ~ 635 (ms)", time4],
        ["Dly Fb", 0x14, "0 ~ *64* ~ 127", thru],
        ["Dly Mix", 0x15, "0 ~ *30* ~ 127", thru],
        ["Level", 0x16, "0 ~ *88* ~ 127", thru]
    ]],
    ["Clean Gt Multi1", 0x04, 0x03, [
        ["Cmp Atk", 0x03, "0 ~ *50* ~ 127", thru],
        ["Cmp Sus", 0x04, "0 ~ *127*", thru],
        ["Cmp Level", 0x05, "0 ~ *75* ~ 127", thru],
        ["Cmp Sw", 0x06, "0/*1*", thru],
        ["EQ L Gain", 0x07, "-12 ~ *+12*", centered12],
        ["EQ M Fq", 0x08, "*200* ~ 6.3k", eqfreq],
        ["EQ M Q", 0x09, "0(0.5)/1/*2*/3(4.0)/4(9.0)", thru],
        ["EQ M Gain", 0x0A, "-12 ~ *+5* ~ +12", centered12],
        ["EQ H Gain", 0x0B, "*-12* ~ +12", centered12],
        ["CF Sel", 0x0C, "*0(Chorus)*/1(Flanger)", thru],
        ["CF Rate", 0x0D, "0.00 ~ *0.45* ~ 6.40", rate2],
        ["CF Depth", 0x0E, "0 ~ *96* ~ 127", thru],
        ["CF Fb", 0x0F, "-98 ~ *+76* + +98", centered_feedback],
        ["CF Mix", 0x10, "*0* ~ 127", thru],
        ["Dly Time", 0x11, "0 ~ *120* ~ 635 (ms)", time4],
        ["Dly Fb", 0x12, "0 ~ *40* ~ 127", thru],
        ["Dly HF", 0x13, "315 ~ 8k / *Bypass*", hfdamp],
        ["Dly Mix", 0x14, "0 ~ *30* ~ 127", thru],
        ["Level", 0x16, "0 ~ *110* ~ 127", thru]
    ]],
    ["Clean Gt Multi2", 0x04, 0x04, [
        ["AW filter", 0x03, "0(LPF)/*1(BPF)*", thru],
        ["AW Man", 0x04, "0 ~ *55* ~ 127", thru],
        ["AW Peak", 0x05, "0 ~ *40* ~ 127", thru],
        ["AW Rate", 0x06, "0.05 ~ *1.60* ~ 6.40", rate2],
        ["AW Depth", 0x07, "0 ~ *80* ~ 127", thru],
        ["AW Sw", 0x08, "0/*1*", thru],
        ["EQ L Gain", 0x09, "-12 ~ *+12*", centered12],
        ["EQ M Fq", 0x0A, "200 ~ *1.6k* ~ 6.3k", eqfreq],
        ["EQ M Q", 0x0B, "*0(0.5)*/1/2/3(4.0)/4(9.0)", thru],
        ["EQ M Gain", 0x0C, "-12 ~ *0* ~ +12", centered12],
        ["EQ H Gain", 0x0D, "-12 ~ *0* ~ +12", centered12],
        ["CF Sel", 0x0E, "*0(Chorus)*/1(Flanger)", thru],
        ["CF Rate", 0x0F, "0.00 ~ *0.45* ~ 6.40", rate2],
        ["CF Depth", 0x10, "0 ~ *20* ~ 127", thru],
        ["CF Fb", 0x11, "-98 ~ *+76* + +98", centered_feedback],
        ["CF Mix", 0x12, "0 ~ *100* ~ 127", thru],
        ["Dly Time", 0x13, "0 ~ *30* ~ 635 (ms)", time4],
        ["Dly Fb", 0x14, "0 ~ *15* ~ 127", thru],
        ["Dly Mix", 0x15, "0 ~ *80* ~ 127", thru],
        ["Level", 0x16, "0 ~ *76* ~ 127", thru]
    ]],
    ["Bass Multi", 0x04, 0x05, [
        ["Cmp Atk", 0x03, "0 ~ *72* ~ 127", thru],
        ["Cmp Sus", 0x04, "0 ~ *100*", thru],
        ["Cmp Level", 0x05, "0 ~ *75* ~ 127", thru],
        ["Cmp Sw", 0x06, "0/*1*", thru],
        ["OD/DS", 0x07, "*0(OD)*/1(DS)", thru],
        ["OD/DS Drive", 0x08, "0 ~ *48* ~ 127", thru],
        ["OD/DS Amp", 0x09, "*0(Small)*/1(BltIn)/2(2-Stk)", thru],
        ["OD/DS Amp Sw", 0x0A, "*0*/1", thru],
        ["OD/DS Sw", 0x0B, "0/*1*", thru],
        ["EQ L Gain", 0x0C, "-12 ~ *+2* ~ +12", centered12],
        ["EQ M Fq", 0x0D, "200 ~ *1.6k* ~ 6.3k", eqfreq],
        ["EQ M Q", 0x0E, "0(0.5)/*1*/2/3(4.0)/4(9.0)", thru],
        ["EQ M Gain", 0x0F, "-12 ~ *+4* ~ +12", centered12],
        ["EQ H Gain", 0x10, "-12 ~ *0* ~ +12", centered12],
        ["CF Sel", 0x11, "*0(Chorus)*/1(Flanger)", thru],
        ["CF Rate", 0x12, "0.00 ~ *0.30* ~ 6.40", rate2],
        ["CF Depth", 0x13, "0 ~ *20* ~ 127", thru],
        ["CF Fb", 0x14, "-98 ~ *+76* + +98", centered_feedback],
        ["CF Mix", 0x15, "0 ~ *64* ~ 127", thru],
        ["Level", 0x16, "0 ~ *76* ~ 127", thru]
    ]],
    ["Rhodes Multi", 0x04, 0x06, [
        ["EH Sens", 0x03, "0 ~ *64* ~ 127", thru],
        ["EH Mix", 0x04, "0 ~ *64* ~ 127", thru],
        ["PH Man", 0x05, "100 ~ *620* ~ 8k", manual],
        ["PH Rate", 0x06, "0.05 ~ *0.85* ~ 6.40", rate2],
        ["PH Depth", 0x07, "0 ~ *32* ~ 127", thru],
        ["PH Reso", 0x08, "0 ~ *16* ~ 127", thru],
        ["PH Mix", 0x09, "0 ~ *64* ~ 127", thru],
        ["CF Sel", 0x0A, "*0(Chorus)*/1(Flanger)", thru],
        ["CF LPF", 0x0B, "250 ~ 6.3k / *Bypass*", lpf],
        ["CF Dly", 0x0C, "0 ~ *1.00* ~ 100 (ms)", predelay],
        ["CF Rate", 0x0D, "0.00 ~ *0.45* ~ 6.40", rate2],
        ["CF Depth", 0x0E, "0 ~ *64* ~ 127", thru],
        ["CF Fb", 0x0F, "-98 ~ *+80* + +98", centered_feedback],
        ["CF Mix", 0x10, "0 ~ *127*", thru],
        ["TP Sel", 0x11, "0(Trem)/*1(Pan)*", thru],
        ["TP Mod Wv", 0x12, "0(Tri)/1(Sqr)/*2(Sin)*/3(Saw1)/4(Saw2)", thru],
        ["TP Mod Rt", 0x13, "0.03 ~ *3.05* ~ 6.40", rate2],
        ["TP Mod Dep", 0x14, "0 ~ *64* ~ 127", thru],
        ["TP Sw", 0x15, "0/*1*", thru],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["Keyboard Multi", 0x05, 0x00, [
        ["RM Mod Freq", 0x03, "0 ~ *50* ~ 127", thru],
        ["RM Bal", 0x04, "0 ~ *64* ~ 127", thru],
        ["EQ L Gain", 0x05, "-12 ~ *+3* ~ +12", centered12],
        ["EQ M Fq", 0x06, "*200* ~ 6.3k", eqfreq],
        ["EQ M Q", 0x07, "0(0.5)/1/*2*/3(4.0)/4(9.0)", thru],
        ["EQ M Gain", 0x08, "-12 ~ *+5* ~ +12", centered12],
        ["EQ H Gain", 0x09, "-12 ~ *-3* ~ +12", centered12],
        ["PS Coarse", 0x0A, "-24 ~ *+7* ~ +12", centeredfull],
        ["PS Fine", 0x0B, "-100 ~ *0* ~ +100", centered_feedback],
        ["PS Mode", 0x0C, "*0* ~ 4", thru],
        ["PS Bal", 0x0D, "0 ~ *64* ~ 127", thru],
        ["PH Man", 0x0E, "100 ~ *620* ~ 8k", manual],
        ["PH Rate", 0x0F, "0.05 ~ *0.45* ~ 6.40", rate2],
        ["PH Depth", 0x10, "0 ~ *90* ~ 127", thru],
        ["PH Reso", 0x11, "0 ~ *80* ~ 127", thru],
        ["PH Mix", 0x12, "0 ~ *75* ~ 127", thru],
        ["Dly Time", 0x13, "0 ~ *100* ~ 635 (ms)", time4],
        ["Dly Fb", 0x14, "0 ~ *64* ~ 127", thru],
        ["Dly Mix", 0x15, "0 ~ *40* ~ 127", thru],
        ["Level", 0x16, "0 ~ *96* ~ 127", thru]
    ]],
    ["Cho/Delay", 0x11, 0x00, [
        ["Cho Dly", 0x03, "0 ~ *1.0* ~ 100 (ms)", predelay],
        ["Cho Rate", 0x04, "0.05 ~ *0.45* ~ 1.00", rate1],
        ["Cho Depth", 0x05, "0 ~ *120* ~ 127", thru],
        ["Cho Bal", 0x07, "0 ~ *64* ~ 127", thru],
        ["Cho Pan", 0x12, "0 ~ *64* ~ 127", thru],
        ["Cho Level", 0x13, "0 ~ *127*", thru],
        ["Dly Time", 0x08, "0 ~ *250* ~ 500 (ms)", time3],
        ["Dly Fb", 0x09, "-98 ~ *+32* ~ +98", centered_feedback],
        ["Dly HF", 0x0A, "315 ~ 8k / *Bypass*", hfdamp],
        ["Dly Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["Dly Pan", 0x14, "0 ~ *127*", thru],
        ["Dly Level", 0x15, "0 ~ *127*", thru],
        ["Level", 0x16, "0 ~ *96* ~ 127", thru]
    ]],
    ["FL/Delay", 0x11, 0x01, [
        ["FL Dly", 0x03, "0 ~ *1.6* ~ 100 (ms)", predelay],
        ["FL Rate", 0x04, "0.05 ~ *0.60* ~ 10.0", rate1],
        ["FL Depth", 0x05, "0 ~ *24* ~ 127", thru],
        ["FL Fb", 0x06, "-98 ~ *+80* ~ +98", centered_feedback],
        ["FL Bal", 0x07, "0 ~ *64* ~ 127", thru],
        ["FL Pan", 0x12, "*0* ~ 127", thru],
        ["FL Level", 0x13, "0 ~ *127*", thru],
        ["Dly Time", 0x08, "0 ~ *250* ~ 500 (ms)", time3],
        ["Dly Fb", 0x09, "-98 ~ *+32* ~ +98", centered_feedback],
        ["Dly HF", 0x0A, "315 ~ 8k / *Bypass*", hfdamp],
        ["Dly Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["Dly Pan", 0x14, "0 ~ *127*", thru],
        ["Dly Level", 0x15, "0 ~ *127*", thru],
        ["Level", 0x16, "0 ~ *96* ~ 127", thru]
    ]],
    ["Cho/Flanger", 0x11, 0x02, [
        ["Cho Dly", 0x03, "0 ~ *1.6* ~ 100 (ms)", predelay],
        ["Cho Rate", 0x04, "0.05 ~ *0.45* ~ 1.00", rate1],
        ["Cho Depth", 0x05, "0 ~ *120* ~ 127", thru],
        ["Cho Bal", 0x07, "0 ~ *64* ~ 127", thru],
        ["Cho Pan", 0x12, "*0* ~ 127", thru],
        ["Cho Level", 0x13, "0 ~ *127*", thru],
        ["FL Dly", 0x08, "0 ~ *1.6* ~ 100 (ms)", predelay],
        ["FL Rate", 0x09, "0.05 ~ *0.60* ~ 10.0", rate1],
        ["FL Depth", 0x0A, "0 ~ *24* ~ 127", thru],
        ["FL Fb", 0x0B, "-98 ~ *+80* ~ +98", centered_feedback],
        ["FL Bal", 0x0C, "0 ~ *64* ~ 127", thru],
        ["FL Pan", 0x14, "0 ~ *127*", thru],
        ["FL Level", 0x15, "0 ~ *127*", thru],
        ["Level", 0x16, "0 ~ *88* ~ 127", thru]
    ]],
    ["OD1/OD2", 0x11, 0x03, [
        ["OD1 Sel", 0x03, "*0(Odrv)*/1(Dist)", thru],
        ["OD1 Drive", 0x04, "0 ~ *48* ~ 127", thru],
        ["OD1 Amp", 0x05, "0(Small)/*1(BltIn)*/2(2-Stk)/3(3-Stk)", thru],
        ["OD1 Amp Sw", 0x06, "0/*1*", thru],
        ["OD1 Pan", 0x12, "*0* ~ 127", thru],
        ["OD1 Level", 0x13, "0 ~ *96* ~ 127", thru],
        ["OD2 Sel", 0x08, "0(Odrv)/*1(Dist)*", thru],
        ["OD2 Drive", 0x09, "0 ~ *76* ~ 127", thru],
        ["OD2 Amp", 0x0A, "0(Small)/1(BltIn)/2(2-Stk)/*3(3-Stk)*", thru],
        ["OD2 Amp Sw", 0x0B, "0/*1*", thru],
        ["OD2 Pan", 0x14, "0 ~ *127*", thru],
        ["OD2 Level", 0x15, "0 ~ *84* ~ 127", thru],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["OD/Rotary", 0x11, 0x04, [
        ["OD1 Sel", 0x03, "*0(Odrv)*/1(Dist)", thru],
        ["OD1 Drive", 0x04, "0 ~ *48* ~ 127", thru],
        ["OD1 Amp", 0x05, "0(Small)/*1(BltIn)*/2(2-Stk)/3(3-Stk)", thru],
        ["OD1 Amp Sw", 0x06, "0/*1*", thru],
        ["OD1 Pan", 0x12, "*0* ~ 127", thru],
        ["OD1 Level", 0x13, "0 ~ *96* ~ 127", thru],
        ["RT L Slow", 0x08, "0.05 ~ *0.35* ~ 10.00", rate1],
        ["RT L Fast", 0x09, "0.05 ~ *6.40* ~ 10.00", rate1],
        ["RT L Accl", 0x0A, "0 ~ *3* ~ 15", accl],
        ["RT L Lev", 0x0B, "0 ~ *127*", thru],
        ["RT H Slow", 0x0C, "0.05 ~ *0.90* ~ 10.00", rate1],
        ["RT H Fast", 0x0D, "0.05 ~ *7.50* ~ 10.00", rate1],
        ["RT H Accl", 0x0E, "0 ~ *11* ~ 15", accl],
        ["RT H Lev", 0x0F, "0 ~ *64* ~ 127", thru],
        ["RT Sept", 0x10, "0 ~ *96* ~ 127", thru],
        ["RT Speed", 0x11, "*0*/127", thru],
        ["RT Pan", 0x14, "-63 ~ *+63*", centeredfull],
        ["RT Level", 0x15, "0/*127*", thru],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["OD/Phaser", 0x11, 0x05, [
        ["OD1 Sel", 0x03, "*0(Odrv)*/1(Dist)", thru],
        ["OD1 Drive", 0x04, "0 ~ *48* ~ 127", thru],
        ["OD1 Amp", 0x05, "0(Small)/*1(BltIn)*/2(2-Stk)/3(3-Stk)", thru],
        ["OD1 Amp Sw", 0x06, "0/*1*", thru],
        ["OD1 Pan", 0x12, "*-63* ~ +63", centeredfull],
        ["OD1 Level", 0x13, "0 ~ *96* ~ 127", thru],
        ["PH Man", 0x08, "100 ~ *620* ~ 8k", manual],
        ["PH Rate", 0x09, "0.05 ~ *0.45* ~ 6.40", rate2],
        ["PH Depth", 0x0A, "0 ~ *90* ~ 127", thru],
        ["PH Reso", 0x0B, "0 ~ *80* ~ 127", thru],
        ["PH Mix", 0x0C, "0 ~ *75* ~ 127", thru],
        ["PH Pan", 0x14, "*-63* ~ +63", centeredfull],
        ["OD1 Level", 0x15, "0 ~ *127*", thru],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["OD/Auto Wah", 0x11, 0x06, [
        ["OD1 Sel", 0x03, "*0(Odrv)*/1(Dist)", thru],
        ["OD1 Drive", 0x04, "0 ~ *48* ~ 127", thru],
        ["OD1 Amp", 0x05, "0(Small)/*1(BltIn)*/2(2-Stk)/3(3-Stk)", thru],
        ["OD1 Amp Sw", 0x06, "0/*1*", thru],
        ["OD1 Pan", 0x12, "*0* ~ 127", thru],
        ["OD1 Level", 0x13, "0 ~ *96* ~ 127", thru],
        ["AW Filter", 0x08, "0(LPF)/*1(BPF)*", thru],
        ["AW Sens", 0x09, "*0* ~ 127", thru],
        ["AW Man", 0x0A, "0 ~ *68* ~ 127", thru],
        ["AW Peak", 0x0B, "0 ~ *62* ~ 127", thru],
        ["AW Rate", 0x0C, "0.05 ~ *2.05* ~ 6.40", rate1],
        ["AW Depth", 0x0D, "0 ~ *72* ~ 127", thru],
        ["AW Pol", 0x0E, "0(Down)/*1(Up)*", thru],
        ["AW Pan", 0x14, "-63 ~ *+63*", centeredfull],
        ["AW Level", 0x15, "0 ~ *127*", thru],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["PH/Rotary", 0x11, 0x07, [
        ["PH Man", 0x03, "100 ~ *620* ~ 8k", manual],
        ["PH Rate", 0x04, "0.05 ~ *0.85* ~ 10.0", rate1],
        ["PH Depth", 0x05, "0 ~ *64* ~ 127", thru],
        ["PH Reso", 0x06, "0 ~ *16* ~ 127", thru],
        ["PH Mix", 0x07, "0 ~ *127*", thru],
        ["PH Pan", 0x12, "*-63* ~ +63", centeredfull],
        ["PH Level", 0x13, "0 ~ *127*", thru],
        ["RT L Slow", 0x08, "0.05 ~ *0.35* ~ 10.00", rate1],
        ["RT L Fast", 0x09, "0.05 ~ *6.40* ~ 10.00", rate1],
        ["RT L Accl", 0x0A, "0 ~ *3* ~ 15", accl],
        ["RT L Lev", 0x0B, "0 ~ *127*", thru],
        ["RT H Slow", 0x0C, "0.05 ~ *0.90* ~ 10.00", rate1],
        ["RT H Fast", 0x0D, "0.05 ~ *7.50* ~ 10.00", rate1],
        ["RT H Accl", 0x0E, "0 ~ *11* ~ 15", accl],
        ["RT H Lev", 0x0F, "0 ~ *64* ~ 127", thru],
        ["RT Sept", 0x10, "0 ~ *96* ~ 127", thru],
        ["RT Speed", 0x11, "*0*/127", thru],
        ["RT Pan", 0x14, "-63 ~ *+63*", centeredfull],
        ["RT Level", 0x15, "0/*127*", thru],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]],
    ["PH/Auto Wah", 0x11, 0x08, [
        ["PH Man", 0x03, "100 ~ *620* ~ 8k", manual],
        ["PH Rate", 0x04, "0.05 ~ *0.85* ~ 10.0", rate1],
        ["PH Depth", 0x05, "0 ~ *64* ~ 127", thru],
        ["PH Reso", 0x06, "0 ~ *16* ~ 127", thru],
        ["PH Mix", 0x07, "0 ~ *127*", thru],
        ["PH Pan", 0x12, "*-63* ~ +63", centeredfull],
        ["PH Level", 0x13, "0 ~ *127*", thru],
        ["AW Filter", 0x08, "0(LPF)/*1(BPF)*", thru],
        ["AW Sens", 0x09, "*0* ~ 127", thru],
        ["AW Man", 0x0A, "0 ~ *68* ~ 127", thru],
        ["AW Peak", 0x0B, "0 ~ *62* ~ 127", thru],
        ["AW Rate", 0x0C, "0.05 ~ *2.05* ~ 6.40", rate1],
        ["AW Depth", 0x0D, "0 ~ *72* ~ 127", thru],
        ["AW Pol", 0x0E, "0(Down)/*1(Up)*", thru],
        ["AW Pan", 0x14, "-63 ~ *+63*", centeredfull],
        ["AW Level", 0x15, "0 ~ *127*", thru],
        ["Level", 0x16, "0 ~ *127*", thru]
    ]]
]
