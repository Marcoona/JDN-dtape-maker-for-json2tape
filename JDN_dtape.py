print("Dtape maker made by Marcoona <3! this tool is used for yunyls json2tape tool (please credit me if you use this this tool in your mod, thanks)\n")

codename = input ("Codename(for example: RunTheNight): ")

coach = input("which coach move?(for example:\nyou have and trio song and you want to do a dtape for the 2nd coach, in this case you would have to type 2): ")
file=open("input_moves" + coach + ".json", "w+")

star = codename + "([\n" 
file.write(star)
star2 = "    {\n"
file.write(star2)

def danho():

    name = input("MSM name: ")
    startime = input("start time: ")
    endtime = input("end time: ")
    Gold = input("Goldmove: ")

    namepar = '''        "name": "''' + name + '''",\n'''

    file.write(namepar)

    startimpar = '''        "time": ''' + startime + ''',\n'''

    file.write(startimpar)

    Mats = int(endtime) - int(startime)

    dura = '''        "duration": ''' + str(Mats) + ''',\n'''

    file.write(dura)

    Mova = '''        "goldMove": ''' + Gold + '''\n'''

    slasha = "    },\n    {\n"

    slashaend ="    }\n])"

    file.write(Mova)

    Katja = input("do you want to continue?? 1 = yes, 2 = no ")

    if Katja == "2":
        file.write(slashaend)
        file.close()
        input("\nThanks for using my tool! if you use this tool please credit marcoona, thanks! you can press enter to close this")
    if Katja == "1":
        file.write(slasha)
        danho()
    else:
        file.write(slasha)
        danho()

danho()
    
    






