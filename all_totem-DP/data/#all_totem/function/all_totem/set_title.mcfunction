# $data merge storage title:io {  \
#     text:'[  \
#         {"text":"Index: $(index)"}  \
#     ]',  \
#     font:"minecraft:default",  \
#     neg_font:"minecraft:default_neg",  \
#     x: 5,  y: 5,  \
#     align:"left",  \
#     origin:"down-left"\
# }
# function title:new_text
# $data merge storage title:io {  \
#     text:'[  \
#         {"text":"ID: $(id)"}  \
#     ]',  \
#     font:"minecraft:default",  \
#     neg_font:"minecraft:default_neg",  \
#     x: -5,  y: 5,  \
#     align:"right",  \
#     origin:"down-right"\
# }
# function title:new_text

# scoreboard players operation panel_id title.io = indexPanel data
# function title:replace_panel