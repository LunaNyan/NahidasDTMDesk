from mods import common as common

temp_store = []

def store_menu():
    global temp_store
    print("Temporary Storage")
    print("1 : View")
    print("2 : Delete Item")
    print("3 : Delete All")
    print("4 : Save to CSV")
    ipt = input("> ")
    if ipt == "1":
        if len(temp_store) == 0:
            print("No Items in Temporary Storage")
        else:
            cnt = 0
            for i in temp_store:
                print("#" + str(cnt) + " : " + i[1])
                print("    " + common.tostr(i[0]))
                cnt += 1
    elif ipt == "2":
        if len(temp_store) == 0:
            print("No Items in Temporary Storage")
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
                del(temp_store[ipt2])
    elif ipt == "3":
        if len(temp_store) == 0:
            print("No Items in Temporary Storage")
        else:
            print("Delete ALL Items in Temporary Storage")
            ipt2 = input("Are you sure? (y / n) : ")
            if ipt2 == "y" or ipt2 == "Y":
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
    else:
        print("exit")
        return

def store(carry):
    temp_store.append(carry)
