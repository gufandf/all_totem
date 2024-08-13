import os
import json

datapack = "D:/Minecraft/.minecraft/versions/1.21-同步-Fabric 0.16.0/saves/全物品不死图腾/datapacks/全物品不死图腾/data/gufandf/function/all_totem/"
datapack_goal = "D:/Minecraft/.minecraft/versions/1.21-同步-Fabric 0.16.0/saves/全物品不死图腾/datapacks/全物品不死图腾/data/gufandf/advancement/all_totem/"


from isAisB import *


def writeFile(Path,Content):
    f = open(Path,"w")
    f.write(Content)
    f.close()

goal = '{"parent": "gufandf:%s","criteria": {"used_totem": {"trigger": "minecraft:used_totem","conditions": {"item": {"items": "minecraft:totem_of_undying","components": {"custom_model_data": %s }}}}},"display": {"show_toast": false,"announce_to_chat": false,"description": {"translate": "advancements.adventure.totem_of_undying.description"},"frame": "goal","icon": {"count": 1,"id": "minecraft:totem_of_undying","components": {"custom_model_data": %s }},"title": {"translate": "advancements.adventure.totem_of_undying.title"}},"requirements": [["used_totem"]],"sends_telemetry_event": true}'
totem_of_undying = {
    "parent": "minecraft:item/generated",
    "textures": {"layer0": "minecraft:item/totem_of_undying"},
    "overrides": [],
}
items = []
blocks = []
for root, dirs, files in os.walk("./item", topdown=False):
    items = files
for root, dirs, files in os.walk("./block", topdown=False):
    blocks = files
# print(file[:-5])
i = 1
overrides = []
commands = ""
commandFile = "clear @s\n"
commandNum = 0
fileNum = 0
goal_parent = "all_totem"
labels = ""

for item in items:
    itemName = item[:-5]

    label = str(i).zfill(4)+"  "+itemName+"\n"
    labels += label
    overrides.append({"predicate": {"custom_model_data": i}, "model": f"item/{itemName}"})

    translate = f"item.minecraft.{itemName}"
    for block in blocks:
        blockName = block[:-5]
        if isAisB(itemName,blockName):
            translate = f"block.minecraft.{itemName}"
            break

    offand_command = (f"item replace entity @s weapon.offhand with totem_of_undying[custom_model_data={i},item_name='[{{\"translate\": \"{translate}\",\"color\": \"white\"}}]']\n")
    command = (f"give @s totem_of_undying[custom_model_data={i},item_name='[{{\"translate\": \"{translate}\",\"color\": \"white\"}}]']\n")
    commands+=command
    commandFile+=command
    commandNum+=1
    if commandNum > 35:
        # f = open(datapack+f"/pack/file{str(fileNum).zfill(3)}.mcfunction","w")
        # f.write(commandFile)
        commandFile = "clear @s\n"
        commandNum = 0
        fileNum += 1
    writeFile(datapack+f"/offhand/{itemName}.mcfunction",offand_command)
    writeFile(datapack+f"/get/{itemName}.mcfunction",command)
    writeFile(datapack+f"/get/minecraft:{itemName}.mcfunction",command)
    writeFile(datapack+f"/index/{str(i).zfill(5)}.mcfunction",command)
    writeFile(datapack+f"/index/{str(i)}.mcfunction",command+f'data modify storage gufandf:all_totem totem set value {{index:{i},id:"{itemName}"}}\n')
    writeFile(datapack_goal+f"{itemName}.json",goal %(goal_parent,i,i))
    goal_parent = "all_totem/"+itemName
    i += 1
    if i%42 == 0:
        goal_parent = "all_totem"


totem_of_undying["overrides"] = overrides

# f = open("./totem_of_undying.json","w",encoding="UTF-8")
# f.write(json.dumps(totem_of_undying))
# f.close()
# f = open(datapack+"/totem_of_undying_command.mcfunction","w")
# f.write(commands)
# f.close()
writeFile("C:/Users/Administrator/Desktop/item.txt",labels)
