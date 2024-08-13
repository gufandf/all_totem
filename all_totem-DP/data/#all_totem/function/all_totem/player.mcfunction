scoreboard players add time data 1
# 间隔时间

execute if score time data matches 60.. run function gufandf:all_totem/replace_index
effect clear @s
effect give @s invisibility infinite 0 true
experience set Gufandf 0 levels
experience set Gufandf 0 points
tp @s 6.5 -60 9.5 -180 0