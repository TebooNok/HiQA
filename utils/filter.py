# Define a function to filter product names from a user's query
import re
import os
import re
import  csv

###
default_products=list(set(['川土微','共模电压','超宽体','增强型数字隔离器','IS373', 'CA-IS3105w', 'CA-IS3740lw', 'CA-IF1042vs-q1', 'IS3722HS', 'IS3541', 'CA-IF4850HS', 'CAIS3730LW', 'CA-IS3642lw', 'IS362', 'IS3740HB', 'CA-IS3761lw', 'IS3531', 'IS1306M25G', 'IS3760LN', 'CA-IS3643HW', 'CA-IS3730HW', 'CA-IS3101B', 'CA-IF1021s-q1', 'CA-IS3721lw', 'CA-IS3762HW', 'CA-IF1042S Q1', 'CA-IS3731HB', 'CA-IS3720hs', 'IF4888', 'CA-IS3742hw', 'IS3760HN', 'CA-IF4820hs', 'CA-IS3740hw', 'CS48520M', 'CA-IS3102W', 'CAIS3760HW', 'IS2631', 'CA-IS3740hb', 'IS3643LW', 'CA-IS3092w', 'CAIS3760LW', 'CA-IS3741HN', 'CAIF4820HD', 'CA-IS3720hw', 'CAIS3722HW', 'IS3102', 'IS308', 'CA-IS3104W', 'CA-IS3760HN', 'CA-IS3762hw', 'CAIS3722HS', 'CA-IS3760HW', 'CA-IS3760ln', 'CA-IS3643hw', 'CA-IS3730HB', 'CA-IS3721LS', 'CAIS3640HW', 'CAIS3105W', 'IS3721LS', 'IS3720', 'CA-IS3761hw', 'IS2082B', 'CA-IS1306m25g', 'CA-IS3980P', 'CA-IS3021S', 'CA-IS3980p', 'IS3641LW', 'CAIS3730LN', 'CA-IS3763hn', 'CA-IF1051HS', 'IS3642LW', 'CA-IS3742LW', 'cs48505d', 'CA-IF1051S Q1', 'CAIS3104W', 'IS3761LW', 'CA-IS3740HN', 'CA-IF1051hs', 'IS3050G', 'CA-IS3763ln', 'CA-IS3104w', 'CA-IS3082WNX', 'CA-IS3640LW', 'CA-IS3720LW', 'IS3742HB', 'IS3710', 'CA-IS3722HW', 'Q100', 'CA-IS3722LS', 'CAIF1042VSQ1', 'CA-IS3050W', 'CA-IS3721LW', 'CA-IF1044s-q1', 'CAIS3740HN', 'CA-IF4820HM', 'IS3730LW', 'CA-IF1044S Q1', 'CA-IS3730LW', 'CA-IS3730ln', 'CAIS3731HW', 'CA-IS3741HN', 'CAIS3731LN', 'CAIS3722LS', 'CAIS3052G', 'IS3721HS', 'CAIS3050W', 'CA-IS3721HW', 'CA-IS3730HB', 'CA-IS3104W', 'IS1300G25G', 'CA-IS3644lw', 'CA-IS3761LN', 'CA-IS3730lw', 'CA-IS3761HW', 'CA-IS3640HW', 'CAIS3988P', 'CA-IS3721LS', 'CA-IF4850HS', 'CA-IS3086wx', 'IS3062', 'IS305', 'CA-IF4820fs', 'IS3740', 'CA-IS3050U', 'CA-IF4023', 'CAIS3742HB', 'CA-IS3730LN', 'CA-IS3020S', 'IS374', 'CAIF4850HS', 'CA-IS1200U', 'CA-IS3640lw', 'IS3080WX', 'CA-IS3731hw', 'CA-IS3720HG', 'CA-IS3762hn', 'CA-IS3740ln', 'IS3731HB', 'CA-IS3720hg', 'CAIS3644LW', 'CAIF4820FS', 'CA-IS3721HW', 'IS3740LW', 'CAIS3763LN', 'CA-IS3761LN', 'CA-IS3742LN', 'CA-IS3052G', 'CA-IS3763HW', 'CAIS3731HB', 'CA-IS3762LW', 'IS3082WX', 'CA-IS3741LW', 'CA-IS3763HN', 'IS3741LN', 'CA-IS3760hw', 'IS3731HN', 'CA-IS3720HS', 'CAIS3731LW', 'CAIS3642LW', 'IS3722HG', 'CA-IF1042VS-Q1', 'CAIS3761LN', 'CA-IF4888HS', 'CA-IS3080WX', 'CA-IS3740LW', 'IS3640LW', 'CA-IS3020W', 'CA-IS3640LW', 'CA-IS3741HW', 'CAIS3722HG', 'CA-IS3722LG', 'IS3730LN', 'CA-IS3642LW', 'CAIS1200G', 'CA-IS3641HW', 'CA-IS3050W', 'CAIS3760HN', 'IS3740LN', 'CAIS2082B', 'IF4420', 'CS48520D', 'IS3741HW', 'CAIS1306M25G', 'CA-IS3082wnx', 'CA-IS3720LG', 'cs48520d', 'IF1042', 'CA-IS3761LW', 'CAIS3643HW', 'CAIS3740HW', 'CA-IS3988P', 'CA-IS3763hw', 'IS3105W', 'CAIS3742LW', 'CA-IS3761HW', 'CA-IF1021S-Q1', 'CAIS3721LS', 'CA-IS3763LN', 'CA-IS3740HW', 'CA-IS3720ls', 'CA-IS3080WX', 'IS3762HW', 'CA-IS3722LW', 'CA-IS3760LN', 'CA-IF4888HS', 'CA-IS3742lw', 'IF1044', 'CA-IS3731HN', 'IS2092', 'CA-IS3730LW', 'IS3092_3098', 'CA-IS3642LW', 'CA-IS3730HW', 'CA-IS3721hs', 'IS3722LW', 'CA-IS3730HN', 'CA-IS3644HW', 'CA-IS3021S', 'CAIF1051SQ1', 'CA-IS3020S', 'CAIF1051HS', 'CA-IS3763LW', 'CA-IS1300G25G', 'IS372', 'CA-IS3763lw', 'IS1305AM25W', 'IF4805HS', 'CA-IS3644HW', 'CA-IS3980s', 'CA-IS3742HB', 'IS3115', 'CAIS3741HW', 'CAIS3720HG', 'CA-IS3082wx', 'CA-IS3760lw', 'CA-IS3760HW', 'CAIS1204W', 'CA-IF4820FS', 'IS3082WNX', 'CA-IS3722hs', 'CA-IS3722HG', 'CA-IF4820FS', 'CA-IS3762HN', 'IS2082', 'IS3722HW', 'cs48520m', 'CS48505M', 'CA-IS3720LS', 'CA-IS3760HN', 'CA-IS3021W', 'CA-IS1200g', 'CS817x20LS', 'IS3740HW', 'CAIS3641HW', 'IS322', 'CA-IS3720LG', 'IS3088WX', 'IS3221_2', 'CA-IS3731ln', 'CA-IS3763HN', 'CA-IS3730HN', 'CA-IS3722lw', 'CAIS3741LW', 'IF4820HD', 'CA-IS3742HW', 'CA-IS3760LW', 'CA-IF1042s-q1', 'CAIS3082WX', 'CA-IS1306M25G', 'CA-IS3762ln', 'CA-IS3731LW', 'CA-IS3741hw', 'CA-IF4850hs', 'CA-IS3740HW', 'CA-IS3082WX', 'CA-IS3721HS', 'CAIS3722LW', 'CAIS3720HW', 'CAIS3720LG', 'CA-IF4805HS', 'IS3742LN', 'CA-IS3050U', 'CA-IS3763LN', 'IS3730HW', 'CAIS3642HW', 'CA-IS3731LW', 'IS2062', 'CA-IS3741LB', 'CA-IS3988p', 'CA-IS3760hn', 'IF1051HS', 'CA-IS3742HB', 'CAIS3740LN', 'CAIS3086WX', 'CA-IS3740LN', 'IS3052G', 'CAIF4023', 'CAIS3742HW', 'CA-IF4820hd', 'CAIS3088WX', 'CA-IS3762HW', 'CA-IS3731lw', 'CA-IS3642HW', 'IS3762LN', 'IF4023', 'CA-IS3980S', 'IS1200U', 'CAIS3721LW', 'CA-IF4820HS', 'IS376', 'CAIS3640LW', 'CAIS3102W', 'CA-IS3741HW', 'CA-IF1044VS-Q1', 'CA-IS1204W', 'IS3761HN', 'IS3763LW', 'CA-IS3050u', 'CA-IS3731HN', 'CA-IS3644LW', 'IS382', 'CA-IS3050G', 'CAIF4805HS', 'CA-IS3092W', 'CA-IS3762LN', 'CA-IS3721LW', 'CA-IS3740LN', 'IS3020S', 'IS3720HS', 'IS3020W', 'CA-IS3741ln', 'IF4820HS', 'CAIS3742LN', 'CS48520S', 'IF4220', 'CA-IS3050g', 'IS3092W_98', 'CAIS3021W', 'IS1311', 'IF1028', 'IF1021S-Q1', 'CA-IF4805hs', 'IS3104W', 'CA-IS3761ln', 'IS3740HN', 'CAIF1044VSQ1', 'CA-IS3105W', 'CA-IF1042VS Q1', 'CS485', 'CA-IS2082B', 'CA-IS3720LS', 'IF1044VS-Q1', 'IS3762HN', 'IS1300', 'IS1044', 'CAIS3021S', 'CA-IS3742hb', 'CA-IS3643HW', 'CA-IS3720HG', 'CAIS3644HW', 'CA-IS3720lg', 'CAIS3643LW', 'IF1044S-Q1', 'CA-IS3762HN', 'IS3761HW', 'CA-IS3088WX', 'CA-IS3763HW', 'CA-IS3722lg', 'CA-IS3742HW', 'CA-IS1300g25g', 'IS3092W', 'IS364', 'IS3102W', 'IS3720LW', 'CA-IS3088WX', 'CAIS3762LN', 'CA-IF4023', 'IS3731LW', 'CAIS3050U', 'CA-IS3730hn', 'CA-IS3643LW', 'CAIS3980S', 'CA-IS3020W', 'IS1044S', 'CA-IF4820HM', 'CA-IS3644hw', 'CA-IS3741LN', 'CA-IS3722HS', 'CA-IS3722HS', 'CA-IS3640HW', 'CA-IS3102W', 'IS3731HW', 'IS3722LS', 'CA-IS3101B', 'CA-IS1300G25G', 'CA-IS3742LW', 'CA-IS3644LW', 'IS3722LG', 'CA-IS3742HN', 'IS3211', 'CA-IS1305AM25W', 'IS3741LB', 'IS3731LN', 'IS3762LW', 'CA-IS1204W', 'CAIS3052W', 'CA-IS3740LW', 'IS3720LS', 'CA-IS3760LN', 'CA-IS1305AM25W', 'CA-IS3050G', 'CA-IS3088wx', 'CAIS3980P', 'CAIS3760LN', 'CAIF1051VSQ1', 'cs48505s', 'CAIS3741HN', 'CAIS3730HW', 'IS3763HW', 'CA-IS1200G', 'CA-IS3082WNX', 'IS3050W', 'CA-IS1044S', 'CA-IS3740HB', 'CA-IS3720LW', 'IF1043', 'cs48505m', 'CAIS3730HB', 'IS3763LN', 'CS817x22HS', 'CA-IS3742ln', 'CA-IS3021s', 'CA-IS3641LW', 'cs48520s', 'CA-IS1204w', 'CA-IS3760LW', 'CA-IF4820HD', 'IS3720HW', 'CA-IS1044S', 'CA-IS3722LW', 'CA-IS3722LS', 'CAIS3763HN', 'IS3730HN', 'CA-IS3731LN', 'CA-IS3762lw', 'IS3760LW', 'CA-IS3642hw', 'IS3642HW', 'IF4820HM', 'CA-IS3082WX', 'CA-IS3722hw', 'CA-IS3721HS', 'IS3086WX', 'IF4888HS', 'CS48505D', 'CAIS3730HN', 'CA-IF1044VS Q1', 'CA-IF4805HS', 'CAIS3763HW', 'IS3742HW', 'CA-IS1200G', 'IF428', 'CA-IS3730hw', 'IS3021W', 'CA-IS3740hn', 'IS3980P', 'CA-IS3105W', 'IS3644LW', 'CS817', 'CA-IS3643LW', 'CA-IF4888hs', 'CAIF4820HM', 'CAIS1300G25G', 'cs817x22hs', 'CAIS3741LB', 'IS1204W', 'CAIS3721HW', 'IF1021', 'CAIS3641LW', 'CA-IF1044vs-q1', 'CAIS3740LW', 'CA-IS3102w', 'CAIS1200U', 'CA-IS3761LW', 'CAIS3741LN', 'CA-IS3741lw', 'IS3021S', 'CAIS3761HN', 'CA-IS3762LW', 'CA-IS3730hb', 'CA-IS3731HB', 'CS48505S', 'CA-IF1042S-Q1', 'CA-IF1051S-Q1', 'CA-IS3741LB', 'CAIS3761LW', 'IS3643HW', 'IF4820FS', 'IS3082_88', 'IS3050U', 'CA-IS3980S', 'IS1300B25', 'CA-IS1200u', 'IS3763HN', 'CA-IS1200U', 'CAIS3762LW', 'CA-IS1305am25w', 'CAIS3101B', 'CAIS3020W', 'CA-IS3741lb', 'CA-IS3731HW', 'CA-IS3052W', 'CA-IS3761HN', 'CA-IS3722ls', 'CAIS3080WX', 'CA-IS3988P', 'IS398', 'CA-IS3762LN', 'CA-IF1021S Q1', 'CAIS3050G', 'CA-IS3092W', 'CA-IF4820HS', 'CA-IS3641LW', 'CA-IS3740HB', 'AG001', 'IF1051', 'IS3760HW', 'CA-IS3020w', 'IS3105', 'CAIS3092W', 'IS3720LG', 'CA-IF1051s-q1', 'IS3742HN', 'CAIF4820HS', 'CA-IS3021w', 'IF1042VS-Q1', 'IS3742LW', 'CA-IS3101b', 'CA-IS3720lw', 'CA-IS1306M25G', 'CA-IS3640hw', 'CA-IS3050w', 'IS3101B', 'CA-IF4820hm', 'CS817x20HS', 'CA-IF1051vs-q1', 'IS3761LN', 'CA-IS3763LW', 'CAIS3731HN', 'CA-IS3741hn', 'CA-IF1051VS Q1', 'CA-IS3722HG', 'IS1200G', 'IS3641HW', 'IS3741LW', 'CA-IF4820HD', 'CA-IS3641lw', 'IS3741HN', 'IF4850HS', 'CA-IS3741LN', 'CA-IS3741LW', 'CA-IS3080wx', 'CA-IF1051HS', 'CA-IS3020s', 'CA-IF1051VS-Q1', 'CAIF1021SQ1', 'CA-IS3731HW', 'IS3644HW', 'CAIS3763LW', 'CA-IS3731LN', 'CAIS3740HB', 'CA-IS3021W', 'IS3721HW', 'IS3720HG', 'CAIS3082WNX', 'CA-IS2082b', 'CA-IS3721ls', 'CA-IS3720HW', 'IS3052W', 'CA-IS3731hn', 'CA-IS3761hn', 'CA-IS2082B', 'IF1042S-Q1', 'CAIS3762HN', 'CA-IS3722hg', 'CA-IS3731hb', 'IS3730HB', 'CAIF4888HS', 'CA-IS3052w', 'CAIS3720HS', 'CAIS3722LG', 'IS1306', 'CA-IF4023', 'IS302', 'CAIS1044S', 'CAIF1042SQ1', 'CAIS3762HW', 'CA-IS3721hw', 'IF1051S-Q1', 'IS3980S', 'CA-IS1044s', 'IS3640HW', 'CA-IS3720HS', 'CA-IS3761HN', 'CA-IS3086WX', 'CAIS3742HN', 'CA-IS3722HW', 'CA-IS3086WX', 'CA-IS3742LN', 'CA-IS3641HW', 'CA-IS3642HW', 'CA-IF1044S-Q1', 'CA-IS3052G', 'CAIF1044SQ1', 'CA-IS3052W', 'CAIS3721HS', 'CA-IS3980P', 'CA-IS3720HW', 'CA-IS3740HN', 'IS3988P', 'CAIS3720LW', 'CA-IS3052g', 'CAIS3020S', 'cs817x20ls', 'CAIS3720LS', 'CAIS3761HW', 'CA-IS3641hw', 'CA-IS3742HN', 'CA-IS3722LG', 'IS3721LW', 'IF1051VS-Q1', 'CAIS1305AM25W', 'CA-IS3742hn', 'CA-IS3730LN', 'cs817x20hs', 'CA-IS3643lw', "IS384"]))
#default_products=['共模电压','超宽体','增强型数字隔离器','3092VW','373', '3105w', '3740lw', '1042vs-q1', '3722HS', '3541', '4850HS', '3730LW', '3642lw', '362', '3740HB', '3761lw', '3531', '1306M25G', 'IS3760LN', '3643HW', '3730HW', '3101B', 'ca-if1021s-q1', '3721lw', '3762HW', 'CA IF1042S Q1', '3731HB', '3720hs', 'IF4888', '3742hw', 'IS3760HN', 'ca-if4820hs', '3740hw', 'CS48520M', '3102W', '3760HW', 'IS2631', '3740hb', 'IS3643LW', '3092w', '3760LW', '3741HN', 'CAIF4820HD', '3720hw', '3722HW', 'IS3102', 'IS308', '3104W', '3760HN', '3762hw', '3722HS', '3760HW', '3760ln', '3643hw', '3730HB', '3721LS', '3640HW', '3105W', 'IS3721LS', 'IS3720', '3761hw', 'IS2082B', '1306m25g', '3980P', '3021S', '3980p', 'IS3641LW', '3730LN', '3763hn', 'CA IF1051HS', 'IS3642LW', '3742LW', 'cs48505d', 'CA IF1051S Q1', '3104W', 'IS3761LW', '3740HN', 'ca-if1051hs', 'IS3050G', '3763ln', '3104w', '3082WNX', '3640LW', '3720LW', 'IS3742HB', 'IS3710', '3722HW', 'Q100', '3722LS', 'CAIF1042VSQ1', '3050W', '3721LW', 'ca-if1044s-q1', '3740HN', 'CA IF4820HM', 'IS3730LW', 'CA IF1044S Q1', '3730LW', '3730ln', '3731HW', '3741HN', '3731LN', 'AN001', '3722LS', '3052G', 'IS3721HS', '3050W', '3721HW', '3730HB', '3104W', 'IS1300G25G', '3644lw', '3761LN', '3730lw', '3761HW', '3640HW', '3988P', '3721LS', 'CA-IF4850HS', '3086wx', 'IS3062', 'IS305', 'ca-if4820fs', 'IS3740', '3050U', 'ca-if4023', '3742HB', '3730LN', '3020S', 'IS374', 'CAIF4850HS', '1200U', '3640lw', 'IS3080WX', '3731hw', '3720HG', '3762hn', '3740ln', 'IS3731HB', '3720hg', '3644LW', 'CAIF4820FS', '3721HW', 'IS3740LW', '3763LN', '3761LN', '3742LN', '3052G', '3763HW', '3731HB', '3762LW', 'IS3082WX', '3741LW', '3763HN', 'IS3741LN', '3760hw', 'IS3731HN', '3720HS', '3731LW', '3642LW', 'IS3722HG', 'CA-IF1042VS-Q1', '3761LN', 'CA-IF4888HS', '3080WX', '3740LW', 'IS3640LW', '3020W', '3640LW', '3741HW', '3722HG', '3722LG', 'IS3730LN', '3642LW', '1200G', '3641HW', '3050W', '3760HN', 'IS3740LN', '2082B', 'IF4420', 'CS48520D', 'IS3741HW', '1306M25G', '3082wnx', '3720LG', 'cs48520d', 'IF1042', '3761LW', '3643HW', '3740HW', '3988P', '3763hw', 'IS3105W', '3742LW', '3761HW', 'CA-IF1021S-Q1', '3721LS', '3763LN', '3740HW', '3720ls', '3080WX', 'AN008', 'IS3762HW', '3722LW', '3760LN', 'CA IF4888HS', '3742lw', 'IF1044', '3731HN', 'IS2092', '3730LW', 'is3092_3098', '3642LW', '3730HW', '3721hs', 'IS3722LW', '3730HN', '3644HW', '3021S', 'CAIF1051SQ1', '3020S', 'CAIF1051HS', '3763LW', '1300G25G', 'IS372', '3763lw', 'IS1305AM25W', 'IF4805HS', 'AN005', '3644HW', '3980s', '3742HB', 'IS3115', '3741HW', '3720HG', '3082wx', '3760lw', '3760HW', '1204W', 'CA-IF4820FS', 'IS3082WNX', '3722hs', '3722HG', 'CA IF4820FS', '3762HN', 'IS2082', 'IS3722HW', 'cs48520m', 'CS48505M', '3720LS', '3760HN', '3021W', '1200g', 'CS817x20LS', 'IS3740HW', '3641HW', 'IS322', '3720LG', 'IS3088WX', 'IS3221_2', '3731ln', '3763HN', '3730HN', '3722lw', '3741LW', 'IF4820HD', '3742HW', '3760LW', 'ca-if1042s-q1', '3082WX', '1306M25G', '3762ln', '3731LW', '3741hw', 'ca-if4850hs', '3740HW', '3082WX', '3721HS', '3722LW', '3720HW', '3720LG', 'CA IF4805HS', 'IS3742LN', '3050U', '3763LN', 'IS3730HW', 'AN018', '3642HW', '3731LW', 'IS2062', '3741LB', '3988p', '3760hn', 'IF1051HS', '3742HB', '3740LN', '3086WX', '3740LN', 'IS3052G', 'CAIF4023', '3742HW', 'ca-if4820hd', '3088WX', '3762HW', '3731lw', '3642HW', 'IS3762LN', 'IF4023', '3980S', 'IS1200U', '3721LW', 'CA IF4820HS', 'IS376', '3640LW', '3102W', '3741HW', 'CA-IF1044VS-Q1', '1204W', 'IS3761HN', 'IS3763LW', '3050u', '3731HN', '3644LW', 'IS382', '3050G', 'CAIF4805HS', '3092W', '3762LN', '3721LW', '3740LN', 'IS3020S', 'IS3720HS', 'IS3020W', '3741ln', 'IF4820HS', '3742LN', 'CS48520S', 'IF4220', '3050g', 'IS3092W_98', '3021W', 'IS1311', 'IF1028', 'IF1021S-Q1', 'ca-if4805hs', 'IS3104W', '3761ln', 'IS3740HN', 'CAIF1044VSQ1', '3105W', 'CA IF1042VS Q1', 'CS485', '2082B', '3720LS', 'IF1044VS-Q1', 'IS3762HN', 'is1300', 'IS1044', '3021S', '3742hb', '3643HW', '3720HG', '3644HW', '3720lg', '3643LW', 'IF1044S-Q1', '3762HN', 'IS3761HW', '3088WX', '3763HW', '3722lg', '3742HW', '1300g25g', 'IS3092W', 'IS364', 'IS3102W', 'IS3720LW', '3088WX', '3762LN', 'CA IF4023', 'IS3731LW', '3050U', '3730hn', '3643LW', '3980S', '3020W', 'IS1044S', 'CA-IF4820HM', '3644hw', '3741LN', '3722HS', '3722HS', '3640HW', '3102W', 'IS3731HW', 'IS3722LS', '3101B', '1300G25G', '3742LW', '3644LW', 'IS3722LG', '3742HN', 'IS3211', '1305AM25W', 'IS3741LB', 'IS3731LN', 'IS3762LW', '1204W', '3052W', '3740LW', 'IS3720LS', '3760LN', '1305AM25W', '3050G', '3088wx', '3980P', '3760LN', 'AN015', 'CAIF1051VSQ1', 'cs48505s', '3741HN', '3730HW', 'IS3763HW', '1200G', '3082WNX', 'IS3050W', '1044S', '3740HB', '3720LW', 'IF1043', 'cs48505m', '3730HB', 'IS3763LN', 'CS817x22HS', '3742ln', '3021s', '3641LW', 'cs48520s', '1204w', '3760LW', 'CA IF4820HD', 'IS3720HW', '1044S', '3722LW', '3722LS', '3763HN', 'IS3730HN', '3731LN', '3762lw', 'IS3760LW', '3642hw', 'IS3642HW', 'IF4820HM', '3082WX', '3722hw', '3721HS', 'IS3086WX', 'IF4888HS', 'CS48505D', '3730HN', 'CA IF1044VS Q1', 'CA-IF4805HS', '3763HW', 'IS3742HW', '1200G', 'IF428', '3730hw', 'IS3021W', 'AN007', '3740hn', 'IS3980P', '3105W', 'IS3644LW', 'CS817', '3643LW', 'ca-if4888hs', 'CAIF4820HM', '1300G25G', 'cs817x22hs', '3741LB', 'IS1204W', '3721HW', 'IF1021', '3641LW', 'ca-if1044vs-q1', '3740LW', '3102w', '1200U', '3761LW', '3741LN', '3741lw', 'IS3021S', '3761HN', '3762LW', '3730hb', '3731HB', 'CS48505S', 'CA-IF1042S-Q1', 'CA-IF1051S-Q1', '3741LB', '3761LW', 'IS3643HW', 'IF4820FS', 'IS3082_88', 'IS3050U', '3980S', 'IS1300B25', '1200u', 'IS3763HN', '1200U', 'AN017', '3762LW', '1305am25w', '3101B', '3020W', '3741lb', '3731HW', '3052W', '3761HN', '3722ls', '3080WX', '3988P', 'IS398', '3762LN', 'AN010', 'CA IF1021S Q1', '3050G', '3092W', 'CA-IF4820HS', '3641LW', '3740HB', 'AG001', 'IF1051', 'IS3760HW', '3020w', 'IS3105', '3092W', 'IS3720LG', 'ca-if1051s-q1', 'IS3742HN', 'CAIF4820HS', '3021w', 'IF1042VS-Q1', 'IS3742LW', '3101b', '3720lw', '1306M25G', '3640hw', '3050w', 'IS3101B', 'ca-if4820hm', 'CS817x20HS', 'ca-if1051vs-q1', 'IS3761LN', '3763LW', '3731HN', '3741hn', 'CA IF1051VS Q1', '3722HG', 'IS1200G', 'IS3641HW', 'IS3741LW', 'CA-IF4820HD', '3641lw', 'IS3741HN', 'IF4850HS', '3741LN', '3741LW', '3080wx', 'AN011', 'AN014', 'CA-IF1051HS', '3020s', 'CA-IF1051VS-Q1', 'CAIF1021SQ1', '3731HW', 'IS3644HW', '3763LW', '3731LN', '3740HB', '3021W', 'IS3721HW', 'IS3720HG', '3082WNX', '2082b', '3721ls', '3720HW', 'IS3052W', '3731hn', '3761hn', '2082B', 'IF1042S-Q1', '3762HN', '3722hg', '3731hb', 'IS3730HB', 'CAIF4888HS', '3052w', '3720HS', '3722LG', 'is1306', 'CA-IF4023', 'is302', '1044S', 'CAIF1042SQ1', 'AN012', '3762HW', '3721hw', 'IF1051S-Q1', 'IS3980S', '1044s', 'IS3640HW', '3720HS', '3761HN', '3086WX', '3742HN', '3722HW', '3086WX', '3742LN', 'AN004', '3641HW', '3642HW', 'CA-IF1044S-Q1', '3052G', 'CAIF1044SQ1', '3052W', '3721HS', '3980P', '3720HW', '3740HN', 'IS3988P', '3720LW', '3052g', '3020S', 'cs817x20ls', '3720LS', '3761HW', '3641hw', '3742HN', '3722LG', 'IS3721LW', 'IF1051VS-Q1', '1305AM25W', '3742hn', 'AN009', '3730LN', 'cs817x20hs', '3643lw', 'AN006']

###
#default_products = ['CS817', 'Q100', 'IF48', 'IF1021', 'IS362', 'IF1042', 'IS374', 'IS2631', 'IF1043', 'IS372', 'IF4220', 'IS3740', 'IF428', 'IF1044', 'IS3531', 'IF1051', 'IS3062', 'IS2092', 'IS322', 'IS305', 'IS2082', 'IS3541', 'IF4023', 'IS3092', 'IS3720', 'IS364', 'IS2062', 'IS3105', '485', 'IS3211', 'IS398', 'IS1044', 'IS382', 'IS1300', 'IF1028', 'IF4888', 'IS3102', 'IS376', 'IF4420', 'IS1300B25', 'IS302', 'IS308', 'IS3082', 'IS3221', 'IS1311', 'IS3115', 'IS1306', 'IS373', 'IS3092', 'IS3710', 'Q1', 'AN014', 'AN001', 'AN015', 'AN017', 'CS485', 'AN006', 'AN012', 'AN007', 'AN011', 'AN005', 'AN004', 'AN010', 'AN009', 'AN008', 'AN018', 'AG001', 'RS485', '422', 'RS422', 'IS1200']
enemy_products = ['8100', '6801']
default_products.extend(enemy_products)
def contains_str(input_str, keyword):
    return keyword in input_str
def get_all_file_paths(img_path):
    file_paths = []  # 初始化一个空列表，用于存储文件路径
    for dirpath, dirnames, filenames in os.walk(img_path):
        for filename in filenames:
            # 使用 os.path.join 来获取完整的文件路径
            file_path = os.path.join(dirpath, filename)
            file_paths.append(file_path)  # 将文件路径添加到列表中
    return file_paths

def get_longest_digits(keyword):
  match = re.search(r'\d+', keyword)
  if match:
    return match.group()
  else:
    return ''
def find_img(keyw:str,folder='价格手册'):
    keyword=get_longest_digits(keyw)

    #keyword = "1042"
    result = []
    # folder = "/data/lidong/fastqa/价格手册"

    for filepath in os.listdir(folder):
        fullpath = os.path.join(folder, filepath)

        if contains_str(fullpath, keyword):
            result.append(fullpath)
    return result

def find_product_img(keyw:str,folder='图片'):
    keyword=keyw

    #keyword = "1042"
    result = []
    # folder = "/data/lidong/fastqa/价格手册"

    for filepath in os.listdir(folder):
        fullpath = os.path.join(folder, filepath)

        if contains_str(fullpath, keyword):
            result.append(fullpath)
    return result


def filter_product_names(user_query, product_list):
    filter_name = []

    for product in product_list:
        if product in user_query:
            filter_name.append(product)

    return filter_name

def rank_values(multi_product):
    ranked_list = []

    # Extract the 'multi' and 'no_product' keys and values
    multi_values = multi_product.get('multi', []).copy()
    no_product_values = multi_product.get('no_product', []).copy()

    # Get the other keys
    other_keys = [key for key in multi_product.keys() if key not in ['multi', 'no_product']]

    # While there are still values in 'multi' and any of the other keys
    while multi_values or any(multi_product[key] for key in other_keys):
        if multi_values:
            ranked_list.append(multi_values.pop(0))
        for key in other_keys:
            if multi_product[key]:
                ranked_list.append(multi_product[key].pop(0))

    # Finally, add the 'no_product' values
    ranked_list.extend(no_product_values)

    return ranked_list

def filter_knowledge(question, results):
    # openai.api_key = open_ai_api_key
    query_list = set(filter_product_names(question, default_products))

    #获取售卖信息
    img_dic={}
    for name in query_list:
        for key in product_dict:
            if name.__contains__(key) or key.__contains__(name):
                img_dic[key]=product_dict[key]

    multi_product = {}
    multi_product["multi"] = []
    multi_product["no_product"] = []
    for i in query_list:
        multi_product[i] = []

    # print("Step 1")
    all_text = ''
    if len(query_list) == 0:
        all_text = '\n\n'.join(results)
        return [all_text]
    else:

        for text in results:
            content_list = filter_product_names(text, query_list)
            if len(content_list) == 0:
                multi_product["no_product"].append(text.replace('[desc]', ''))
            elif len(content_list) > 1:
                multi_product["multi"].append(text.replace('[desc]', ''))
            else:
                # print("content is" + content_list[0])
                multi_product[content_list[0]].append(text.replace('[desc]', ''))
    # print("Step 2")
    rank_list = rank_values(multi_product)


    for product_name in query_list:
        if product_name in rank_list[0]:
            img_path = find_product_img(product_name, "图片")
            break
    if len(img_path)!=0:
        img_path=get_all_file_paths(img_path[0])
    else:
        img_path=[]









    # print("Step 3")

    # print("匹配到的内容数量"+str(len(rank_list)))
    # print(rank_list)
    # for i in rank_list:
    #     all_text += i + '\n' + '______________________' + '\n'
    if not img_dic:  # or some condition indicating that sale_list should be empty
        return ['\n\n'.join(rank_list),img_dic,img_path]
    return ['\n\n'.join(rank_list), img_dic,img_path]

    # return '\n'.join(rank_list),img_dic

