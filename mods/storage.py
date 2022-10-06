from mods import common as common

temp_store = []
protected = False

def loadcsv(fn):
    f = open(fn, mode='r', encoding='utf8')
    cnt = 0
    for fl in f.readlines():
        fx = fl.split(",")
        lst1 = []
        for h1 in fx[0].split(" "):
            lst1.append(eval("0x" + h1))
        if lst1[0] != 240 or lst1[-1] != 247:
            raise ValueError("Invalid SysEx Carrier found during CSV Load")
        temp_store.append([lst1, fx[1].replace("\n", "")])
        cnt += 1
    print("Complete. loaded " + str(cnt) + " Items")
    f.close()

def store_menu():
    global temp_store, protected
    print("Memory Menu")
    print("1 : View")
    print("2 : Delete Item")
    print("3 : Delete All")
    print("4 : Save to CSV")
    print("5 : Load from CSV")
    print("6 : Protect")
    ipt = input("> ")
    if ipt == "1":
        if len(temp_store) == 0:
            print("No Items in Memory")
        else:
            cnt = 0
            for i in temp_store:
                print("#" + str(cnt) + " : " + i[1])
                print("    " + common.tostr(i[0]))
                cnt += 1
    elif ipt == "2":
        if protected:
            print("Memory is protected")
            print("Unprotect memory to begin task")
        elif len(temp_store) == 0:
            print("No Items in Memory")
        else:
            try:
                ipt2 = int(input("# to Delete : "))
            except:
                print("not a number")
                return
            if ipt2 < 0 or ipt2 > len(temp_store)-1:
                print("# not found")
                return
            else:
                print("Item to be deleted")
                print("#" + str(ipt2) + " : " + temp_store[ipt2][1])
                print("    " + common.tostr(temp_store[ipt2][0]))
                ipt3 = input("Are you sure? (y / n) : ")
                if ipt3 == "y" or ipt3 == "Y":
                    del(temp_store[ipt2])
    elif ipt == "3":
        if len(temp_store) == 0:
            print("No Items in Memory")
        else:
            print("Delete ALL Items in Memory")
            ipt2 = input("Are you sure? (y / n) : ")
            if ipt2 == "y" or ipt2 == "Y":
                if protected:
                    print("Memory is protected")
                    print("Unprotect memory to begin task")
                else:
                    temp_store = []
            else:
                print("exit")
                return
    elif ipt == "4":
        print("save to comma-separated CSV")
        ipt_fn = input("Filename (.csv) : ")
        t = ""
        for i in temp_store:
            t += common.tostr(i[0]) + "," + i[1] + "\n"
        f = open(ipt_fn + ".csv", 'w', encoding='utf8')
        f.write(t)
        f.close()
        print("saved")
    elif ipt == "5":
        if protected:
            print("Memory is protected")
            print("Unprotect memory to begin task")
        else:
            ipt_fn = input("Filename : ")
            loadcsv(ipt_fn)
    elif ipt == "6":
        if not protected:
            print("Protect Memory")
            ipt2 = input("Are you sure? (y / n) : ")
            if ipt2 == "y" or ipt2 == "Y":
                protected = True
            else:
                print("abort")
                return
        else:
            print("Unprotect Memory")
            ipt2 = input("Are you sure? (y / n) : ")
            if ipt2 == "y" or ipt2 == "Y":
                protected = False
            else:
                print("abort")
                return
    else:
        print("exit")
        return

def store(carry):
    if not protected:
        temp_store.append(carry)
