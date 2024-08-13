# data modify storage gufandf:all_totem temp_item.minecraft_item set value "minecraft:air"
data modify storage gufandf:all_totem temp_item.minecraft_item set from entity @s SelectedItem.id
data modify storage gufandf:all_totem temp_item.item set string storage gufandf:all_totem temp_item.minecraft_item 10
function gufandf:all_totem/replace1 with storage gufandf:all_totem temp_item