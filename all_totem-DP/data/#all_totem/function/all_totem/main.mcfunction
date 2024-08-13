# execute as @a if entity @s[nbt={SelectedItem:{id:"minecraft:totem_of_undying"}}] run damage @s 100
# effect clear @a
# execute as @a if data entity @s SelectedItem run function gufandf:all_totem/replace
# execute as @a unless data entity @s SelectedItem run item replace entity @s weapon.offhand with air


execute as @a[tag=start] run function gufandf:all_totem/player



scoreboard players operation @a title.panel_id = indexPanel data