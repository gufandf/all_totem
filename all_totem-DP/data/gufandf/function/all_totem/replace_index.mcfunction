scoreboard players add index data 1
execute store result storage gufandf:all_totem totem.index int 1 run scoreboard players get index data
scoreboard players set time data 0
function gufandf:all_totem/replace_index1 with storage gufandf:all_totem totem
damage @s 100
function gufandf:all_totem/set_title with storage gufandf:all_totem totem
