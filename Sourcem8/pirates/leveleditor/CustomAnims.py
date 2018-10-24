from pirates.uberdog.UberDogGlobals import InventoryCategory
from pirates.inventory import ItemGlobals
from pirates.piratesbase import EmoteGlobals
PROP_TYPE_DYNAMIC = 0
PROP_TYPE_PERSIST = 1
INTERACT_ANIMS = {
    'default': {
        'idles': [
            'idle'],
        'interactInto': [
            'into_speak_idle'],
        'interact': [
            'speak_idle'],
        'interactOutof': [
            'outof_speak_idle'] },
    'attack_bayonetA': {
        'idles': [
            'bayonet_attackA'],
        'interactInto': [
            'bayonet_attackA'],
        'interact': [
            'bayonet_attackA'],
        'interactOutof': [
            'bayonet_attackA'],
        'props': [
            [
                'models/handheld/musket_bayonet',
                PROP_TYPE_PERSIST]] },
    'attack_bayonetB': {
        'idles': [
            'bayonet_attackB'],
        'interactInto': [
            'bayonet_attackB'],
        'interact': [
            'bayonet_attackB'],
        'interactOutof': [
            'bayonet_attackB'],
        'props': [
            [
                'models/handheld/musket_bayonet',
                PROP_TYPE_PERSIST]] },
    'attack_bayonetC': {
        'idles': [
            'bayonet_attackC'],
        'interactInto': [
            'bayonet_attackC'],
        'interact': [
            'bayonet_attackC'],
        'interactOutof': [
            'bayonet_attackC'],
        'props': [
            [
                'models/handheld/musket_bayonet',
                PROP_TYPE_PERSIST]] },
    'attack_sword_cleave': {
        'idles': [
            'sword_cleave'],
        'interactInto': [
            'sword_cleave'],
        'interact': [
            'sword_cleave'],
        'interactOutof': [
            'sword_cleave'],
        'props': [
            [
                'models/handheld/cutlass_rusty_high',
                PROP_TYPE_PERSIST]] },
    'attack_sword_lunge': {
        'idles': [
            'sword_lunge'],
        'interactInto': [
            'sword_lunge'],
        'interact': [
            'sword_lunge'],
        'interactOutof': [
            'sword_lunge'],
        'props': [
            [
                'models/handheld/cutlass_rusty_high',
                PROP_TYPE_PERSIST]] },
    'attack_sword_slash': {
        'idles': [
            'sword_slash'],
        'interactInto': [
            'sword_slash'],
        'interact': [
            'sword_slash'],
        'interactOutof': [
            'sword_slash'],
        'props': [
            [
                'models/handheld/cutlass_rusty_high',
                PROP_TYPE_PERSIST]] },
    'attack_sword_thrust': {
        'idles': [
            'sword_thrust'],
        'interactInto': [
            'sword_thrust'],
        'interact': [
            'sword_thrust'],
        'interactOutof': [
            'sword_thrust'],
        'props': [
            [
                'models/handheld/cutlass_rusty_high',
                PROP_TYPE_PERSIST]] },
    'attention': {
        'idles': {
            InventoryCategory.WEAPON_SKILL_MUSKET: {
                'idles': [
                    'bayonet_idle'],
                'interactInto': [
                    'bayonet_idle'],
                'interact': [
                    'bayonet_idle'],
                'interactOutof': [
                    'bayonet_idle'],
                'props': [
                    [
                        'models/handheld/musket_bayonet',
                        PROP_TYPE_PERSIST]] },
            InventoryCategory.WEAPON_SKILL_CUTLASS: {
                'idles': [
                    'cutlass_attention'],
                'interactInto': [
                    'cutlass_attention'],
                'interact': [
                    'cutlass_attention_idle'],
                'interactOutof': [
                    'cutlass_attention'],
                'props': [
                    [
                        'models/handheld/cutlass_steel_high',
                        PROP_TYPE_PERSIST]] } } },
    'axe_chop': {
        'idles': [
            'axe_chop_idle'],
        'interactInto': [
            'axe_chop_into_look'],
        'interact': [
            'axe_chop_look_idle'],
        'interactOutof': [
            'axe_chop_outof_look'],
        'props': [
            'models/handheld/axe_high'] },
    'bar_talk01': {
        'idles': [
            'bar_talk01_idle'],
        'interactInto': [
            'bar_talk01_into_look'],
        'interact': [
            'bar_talk01_look_idle'],
        'interactOutof': [
            'bar_talk01_outof_look'],
        'props': [
            'models/handheld/mug_high'] },
    'bar_talk02': {
        'idles': [
            'bar_talk02_idle'],
        'interactInto': [
            'bar_talk02_into_look'],
        'interact': [
            'bar_talk02_look_idle'],
        'interactOutof': [
            'bar_talk02_outof_look'] },
    'bar_talk03': {
        'idles': [
            'bar_talk03_idle'],
        'interactInto': [
            'bar_talk03_idle'],
        'interact': [
            'bar_talk03_idle'],
        'interactOutof': [
            'bar_talk03_idle'] },
    'bar_wipe': {
        'idles': [
            'bar_wipe'],
        'interactInto': [
            'bar_wipe_into_look'],
        'interact': [
            'bar_wipe_look_idle'],
        'interactOutof': [
            'bar_wipe_outof_look'],
        'props': [
            'models/handheld/rag_high'] },
    'bar_write': {
        'idles': [
            'bar_write_idle'],
        'interactInto': [
            'bar_write_into_look'],
        'interact': [
            'bar_write_look_idle'],
        'interactOutof': [
            'bar_write_outof_look'],
        'props': [
            'models/handheld/pen_high'] },
    'bayonet_attack_idle': {
        'attack_idles': [
            'bayonet_attack_idle'],
        'interactInto': [
            'bayonet_attack_idle'],
        'interact': [
            'bayonet_attack_idle'],
        'interactOutof': [
            'bayonet_attack_idle'],
        'props': [
            [
                'models/handheld/musket_bayonet',
                PROP_TYPE_PERSIST]] },
    'bayonet_drill': {
        'idles': [
            'bayonet_drill'],
        'interactInto': [
            'bayonet_drill'],
        'interact': [
            'bayonet_drill'],
        'interactOutof': [
            'bayonet_drill'],
        'props': [
            [
                'models/handheld/musket_bayonet',
                PROP_TYPE_PERSIST]] },
    'barrel_hide': {
        'idles': [
            'barrel_hide_idle'],
        'interactInto': [
            'barrel_hide_into_look'],
        'interact': [
            'barrel_hide_look_idle'],
        'interactOutof': [
            'barrel_hide_outof_look'] },
    'crate_hide': {
        'idles': [
            'crazy_ned_night_idle'],
        'idleInto': [
            'crazy_ned_night_jump_in_box'],
        'idleOutof': [
            'crazy_ned_night_jump_out_box'],
        'interact': [
            'crazy_ned_night_interact'] },
    'bomb': {
        'idles': [
            'bomb_idle'],
        'interactInto': [
            'bomb_idle'],
        'interact': [
            'bomb_idle'],
        'interactOutof': [
            'bomb_idle'],
        'props': [
            'models/handheld/pir_m_hnd_bom_grenade'] },
    'cargomaster': {
        'idles': [
            'cargomaster_work_idle'],
        'interactInto': [
            'cargomaster_work_into_look'],
        'interact': [
            'cargomaster_work_look_idle'],
        'interactOutof': [
            'cargomaster_work_outof_look'],
        'props': [
            'models/props/hammer_high'] },
    'cb_apple': {
        'idles': [
            'idle'],
        'interactInto': [
            'into_speak_idle'],
        'interact': [
            'speak_idle'],
        'interactOutof': [
            'outof_speak_idle'],
        'props': [
            'models/handheld/apple_high'] },
    'coin_flip': {
        'idles': [
            'coin_flip_idle'],
        'interactInto': [
            'coin_flip_into_look'],
        'interact': [
            'coin_flip_look_idle'],
        'interactOutof': [
            'coin_flip_outof_look'],
        'props': [
            'models/handheld/coin_high'] },
    'coin_flip_old': {
        'idles': [
            'coin_flip_old_idle'],
        'interactInto': [
            'coin_flip_old_into_look'],
        'interact': [
            'coin_flip_old_look_idle'],
        'interactOutof': [
            'coin_flip_old_outof_look'],
        'props': [
            'models/handheld/coin_high'] },
    'cower': {
        'idles': [
            'cower_idle'],
        'interactInto': [
            'cower_outof'],
        'interact': [
            'speak_idle'],
        'interactOutof': [
            'cower_into'] },
    'cower_sit': {
        'idles': [
            'sit_cower_idle'],
        'interactInto': [
            'sit_cower_into_sleep'],
        'interact': [
            'sit_sleep_look_idle'],
        'interactOutof': [
            'sit_sleep_into_cower'] },
    'crazy': {
        'idles': [
            'crazy_idle'],
        'interactInto': [
            'crazy_look_idle'],
        'interact': [
            'crazy_look_idle'],
        'interactOutof': [
            'crazy_idle'] },
    'doctor_work': {
        'idles': [
            'doctor_work_idle'],
        'interactInto': [
            'doctor_work_into_look'],
        'interact': [
            'doctor_work_look_idle'],
        'interactOutof': [
            'doctor_work_outof_look'],
        'props': [
            'models/handheld/bottle_high'] },
    'drunk': {
        'idles': [
            'drunk_idle'],
        'interactInto': [
            'drunk_into_look'],
        'interact': [
            'drunk_look_idle'],
        'interactOutof': [
            'drunk_outof_look'] },
    'fish': {
        'idles': [
            'fishing_idle'],
        'interactInto': [
            'fishing_drawpole'],
        'bomb_idle': [
            'fishing_pole_cast'],
        'bomb_idle': [
            'fishing_pole_idle'] },
    'flex': {
        'idles': [
            'idle_flex_idle'],
        'interactInto': [
            'idle_flex_into_look'],
        'interact': [
            'idle_flex_look_idle'],
        'interactOutof': [
            'idle_flex_outof_look'] },
    'flute': {
        'idles': [
            'flute_idle'],
        'interactInto': [
            'flute_into_look'],
        'interact': [
            'flute_look_idle'],
        'interactOutof': [
            'flute_outof_look'],
        'props': [
            'models/handheld/flute_high'] },
    'gp_chant_a': {
        'idles': [
            'chant_a_idle'],
        'interactInto': [
            'chant_a_idle'],
        'interact': [
            'chant_a_idle'],
        'interactOutof': [
            'chant_a_idle'] },
    'gp_chant_b': {
        'idles': [
            'chant_b_idle'],
        'interactInto': [
            'chant_b_idle'],
        'interact': [
            'chant_b_idle'],
        'interactOutof': [
            'chant_b_idle'] },
    'gp_handdig': {
        'idles': [
            'handdig_idle'],
        'interactInto': [
            'handdig_idle'],
        'interact': [
            'handdig_idle'],
        'interactOutof': [
            'handdig_idle'] },
    'gp_jump': {
        'idles': [
            'jump_idle'],
        'interactInto': [
            'jump_idle'],
        'interact': [
            'jump_idle'],
        'interactOutof': [
            'jump_idle'] },
    'gp_moaning': {
        'idles': [
            'moaning_idle'],
        'interactInto': [
            'moaning_idle'],
        'interact': [
            'moaning_idle'],
        'interactOutof': [
            'moaning_idle'] },
    'gp_searching': {
        'idles': [
            'searching_idle'],
        'interactInto': [
            'searching_idle'],
        'interact': [
            'searching_idle'],
        'interactOutof': [
            'searching_idle'] },
    'gp_summon': {
        'idles': [
            'summon_idle'],
        'interactInto': [
            'summon_idle'],
        'interact': [
            'summon_idle'],
        'interactOutof': [
            'summon_idle'] },
    'idleB': {
        'idles': [
            'idle_handhip'],
        'interactInto': [
            'idle_handhip'],
        'interact': [
            'idle_handhip'],
        'interactOutof': [
            'idle_handhip'] },
    'idleC': {
        'idles': [
            'idle_B_shiftWeight'],
        'interactInto': [
            'idle_yawn'],
        'interact': [
            'idle_B_shiftWeight'],
        'interactOutof': [
            'idle_B_shiftWeight'] },
    'jig': {
        'idles': [
            'emote_dance_jig'],
        'interactInto': [
            'emote_dance_jig'],
        'interact': [
            'emote_dance_jig'],
        'interactOutof': [
            'emote_dance_jig'] },
    'jr_look_idle': {
        'idles': [
            'jr_look_idle'],
        'interactInto': [
            'jr_look_idle'],
        'interact': [
            'jr_look_idle'],
        'interactOutof': [
            'jr_look_idle'] },
    'jr_look_idle_2': {
        'idles': [
            'jr_look_idle_2'],
        'interactInto': [
            'jr_look_idle_2'],
        'interact': [
            'jr_look_idle_2'],
        'interactOutof': [
            'jr_look_idle_2'] },
    'stockade': {
        'idles': [
            'stock_sleep'],
        'interact': [
            'stock_idle'],
        'interactInto': [
            'stock_sleep_to_idle'] },
    'hit': {
        'idles': [
            'boxing_kick',
            'boxing_punch'] },
    'loom': {
        'idles': [
            'loom_idle'],
        'interactInto': [
            'loom_into_look'],
        'interact': [
            'loom_look_idle'],
        'interactOutof': [
            'loom_outof_look'] },
    'lute': {
        'idles': [
            'lute_idle'],
        'interactInto': [
            'lute_into_look'],
        'interact': [
            'lute_look_idle'],
        'interactOutof': [
            'lute_outof_look'],
        'props': [
            'models/handheld/lute_high'] },
    'patient_work': {
        'idles': [
            'patient_work_idle'],
        'interactInto': [
            'patient_work_into_look'],
        'interact': [
            'patient_work_look_idle'],
        'interactOutof': [
            'patient_work_outof_look'] },
    'primp': {
        'idles': [
            'primp_idle'],
        'interactInto': [
            'primp_into_look'],
        'interact': [
            'primp_look_idle'],
        'interactOutof': [
            'primp_outof_look'] },
    'scorpion_rear_up': {
        'idles': [
            'rear_up'],
        'interactInto': [
            'rear_up'],
        'interact': [
            'rear_up'],
        'interactOutof': [
            'rear_up'] },
    'scorpion_attack_tail_sting': {
        'idles': [
            'attack_tail_sting'],
        'interactInto': [
            'attack_tail_sting'],
        'interact': [
            'attack_tail_sting'],
        'interactOutof': [
            'attack_tail_sting'] },
    'shovel': {
        'idles': [
            'shovel'],
        'interactInto': [
            'shovel_idle_into_dig'],
        'interact': [
            'shovel_idle'],
        'interactOutof': [
            'shovel'],
        'props': [
            'models/handheld/shovel_high'] },
    'smith': {
        'idles': [
            'blacksmith_work_idle'],
        'interactInto': [
            'blacksmith_work_into_look'],
        'interact': [
            'blacksmith_work_look_idle'],
        'interactOutof': [
            'blacksmith_work_outof_look'],
        'props': [
            'models/props/hammer_high'] },
    'sit': {
        'idles': [
            'sit_idle'],
        'interactInto': [
            'into_sit_speak_idle'],
        'interact': [
            'sit_speak_idle'],
        'interactOutof': [
            'outof_sit_speak_idle'] },
    'sit_cards': {
        'idles': [
            'sit_idle'],
        'interactInto': [
            'into_sit_speak_idle'],
        'interact': [
            'sit_speak_idle'],
        'interactOutof': [
            'outof_sit_speak_idle'],
        'props': [
            'models/handheld/cards_5_high'] },
    'sit_cards_avatar': {
        'idles': [
            'cards_pickup_idle'],
        'interactInto': [
            'cards_pickup_idle'],
        'interact': [
            'cards_pickup_idle'],
        'interactOutof': [
            'cards_pickup_idle'],
        'props': [
            'models/handheld/cards_5_high'] },
    'sit_gator': {
        'idles': [
            'sit_idle'],
        'interactInto': [
            'into_sit_speak_idle'],
        'interact': [
            'sit_speak_idle'],
        'interactOutof': [
            'outof_sit_speak_idle'] },
    'sit_hanginglegs': {
        'idles': [
            'sit_hanginglegs_idle'],
        'interactInto': [
            'sit_hanginglegs_into_look'],
        'interact': [
            'sit_hanginglegs_look_idle'],
        'interactOutof': [
            'sit_hanginglegs_outof_look'] },
    'sit_sleep': {
        'idles': [
            'sit_sleep_idle'],
        'interactInto': [
            'sit_sleep_into_look'],
        'interact': [
            'sit_sleep_look_idle'],
        'interactOutof': [
            'sit_sleep_outof_look'] },
    'sit_write': {
        'idles': [
            'sit_idle'],
        'interactInto': [
            'into_sit_speak_idle'],
        'interact': [
            'sit_speak_idle'],
        'interactOutof': [
            'outof_sit_speak_idle'],
        'props': [
            'models/handheld/pen_high'] },
    'sleep_sick': {
        'idles': [
            'sleep_sick_idle'],
        'interactInto': [
            'sleep_sick_into_look'],
        'interact': [
            'sleep_sick_look_idle'],
        'interactOutof': [
            'sleep_sick_outof_look'] },
    'sow': {
        'idles': [
            'sow_idle'],
        'interactInto': [
            'sow_into_look'],
        'interact': [
            'sow_look_idle'],
        'interactOutof': [
            'sow_outof_look'],
        'props': [
            'models/handheld/basket_high'] },
    'stir': {
        'idles': [
            'stir_idle'],
        'interactInto': [
            'stir_into_look'],
        'interact': [
            'stir_look_idle'],
        'interactOutof': [
            'stir_outof_look'],
        'props': [
            'models/handheld/spoon_high'] },
    'sweep': {
        'idles': [
            'sweep_idle'],
        'interactInto': [
            'sweep_into_look'],
        'interact': [
            'sweep_look_idle'],
        'interactOutof': [
            'sweep_outof_look'],
        'props': [
            'models/handheld/broom_high'] },
    'tatoo': {
        'idles': [
            'tatoo_idle'],
        'interactInto': [
            'tatoo_into_look'],
        'interact': [
            'tatoo_look_idle'],
        'interactOutof': [
            'tatoo_outof_look'],
        'props': [
            'models/handheld/needle_high'] },
    'tatoo_receive': {
        'idles': [
            'tatoo_receive_idle'],
        'interactInto': [
            'tatoo_receive_into_look'],
        'interact': [
            'tatoo_receive_look_idle'],
        'interactOutof': [
            'tatoo_receive_outof_look'] },
    'tut_dan_idle': {
        'idles': [
            'tut_1_1_5_a_idle_dan'],
        'interactInto': [
            'tut_1_1_5_a_idle_dan'],
        'interact': [
            'tut_1_1_5_a_idle_dan'],
        'interactOutof': [
            'tut_1_1_5_a_idle_dan'] },
    'wt_sword': {
        'idles': [
            'idle'],
        'interactInto': [
            'into_speak_idle'],
        'interact': [
            'speak_idle'],
        'interactOutof': [
            'outof_speak_idle'],
        'props': [
            'models/handheld/cutlass_steel_high'] },
    'ned_is_crazy': {
        'idles': [
            'crazy_ned_day_idle'],
        'interact': [
            'crazy_ned_day_idle'],
        'noticeIdle': [
            'crazy_ned_day_idle'],
        'walk': [
            'crazy_ned_day_walk',
            1.3],
        'run': [
            'crazy_ned_day_walk',
            1.8],
        'notice1': [
            'crazy_ned_day_interact'],
        'crazy_ned_night_idle': [
            'crazy_ned_night_idle'],
        'crazy_ned_night_jump_in_box': [
            'crazy_ned_night_jump_in_box'],
        'crazy_ned_night_jump_out_box': [
            'crazy_ned_night_jump_out_box'],
        'extraAnims': EmoteGlobals.getAllEmoteAnimations() },
    'zz_bayonet_run': {
        'idles': [
            'bayonet_run'],
        'props': [
            'models/handheld/musket_bayonet'] },
    'zz_boxing': {
        'idles': [
            'boxing_idle'] },
    'zz_cutlass_taunt': {
        'idles': [
            'cutlass_taunt'],
        'props': [
            'models/handheld/cutlass_steel_high'] },
    'zz_js_idle': {
        'idles': [
            'js_idle'] },
    'zz_js_idleToBow': {
        'idles': [
            'js_idleToBow'] },
    'zz_js_js_handsOnHips': {
        'idles': [
            'js_handsOnHips'] },
    'zz_dagger_combo': {
        'idles': [
            'dagger_combo'],
        'props': [
            'models/handheld/cutlass_steel_high'] },
    'zz_dagger_idle': {
        'idles': [
            'sword_idle'],
        'props': [
            'models/handheld/dagger_high'] },
    'zz_gun_aim_idle': {
        'idles': [
            'gun_aim_idle'],
        'props': [
            'models/handheld/triple_barrel_pistol_high'] },
    'zz_gun_pointedup_idle': {
        'idles': [
            'gun_pointedup_idle'],
        'props': [
            'models/handheld/triple_barrel_pistol_high'] },
    'zz_jack_idle': {
        'idles': [
            'jack_sword_idle'],
        'props': [
            'models/handheld/cutlass_steel_high'] },
    'zz_sword_idle': {
        'idles': [
            'sword_idle'],
        'props': [
            'models/handheld/cutlass_steel_high'] },
    'zz_sword_run': {
        'idles': [
            'run_with_weapon'],
        'props': [
            'models/handheld/cutlass_steel_high'] },
    'zz_voodoo_doll_poke': {
        'idles': [
            'voodoo_doll_poke'],
        'props': [
            'models/handheld/voodoo_doll_high'] },
    'zz_wand_idle': {
        'idles': [
            'wand_idle'],
        'props': [
            'models/handheld/voodoo_staff_high'] },
    'zz_cutlass_L1': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/cutlass_rusty_high'] },
    'zz_cutlass_L2': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/cutlass_iron_high'] },
    'zz_cutlass_L3': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/cutlass_steel_high'] },
    'zz_cutlass_L4': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/cutlass_fine_high'] },
    'zz_cutlass_L5': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/cutlass_pirateblade_high'] },
    'zz_dagger_L1': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/dagger_high'] },
    'zz_dagger_L2': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/dagger_dirk_high'] },
    'zz_dagger_L3': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/dagger_gauche_high'] },
    'zz_dagger_L4': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/dagger_coltello_high'] },
    'zz_dagger_L5': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/dagger_bloodletter_high'] },
    'zz_doll_L1': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/voodoo_doll_high'] },
    'zz_doll_L2': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/voodoo_doll_cloth_high'] },
    'zz_doll_L3': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/voodoo_doll_witch_high'] },
    'zz_doll_L4': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/voodoo_doll_pirate_high'] },
    'zz_doll_L5': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/voodoo_doll_taboo_high'] },
    'zz_pistol_L1': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/pistol_high'] },
    'zz_pistol_L2': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/double_barrel_pistol_high'] },
    'zz_pistol_L3': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/triple_barrel_pistol_high'] },
    'zz_pistol_L4': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/triple_barrel_pistol_b_high'] },
    'zz_pistol_L5': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/triple_barrel_pistol_c_high'] },
    'zz_staff_L1': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/voodoo_staff_high'] },
    'zz_staff_L2': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/voodoo_staff_a_high'] },
    'zz_staff_L3': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/voodoo_staff_b_high'] },
    'zz_staff_L4': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/voodoo_staff_c_high'] },
    'zz_staff_L5': {
        'idles': [
            'idle'],
        'props': [
            'models/handheld/voodoo_staff_d_high'] } }
INTERACT_ANIM_NAMES = [
    'default',
    'attack_bayonetA',
    'attack_bayonetB',
    'attack_bayonetC',
    'attack_sword_cleave',
    'attack_sword_lunge',
    'attack_sword_slash',
    'attack_sword_thrust',
    'attention',
    'attention_cutlass',
    'axe_chop',
    'bar_talk01',
    'bar_talk02',
    'bar_talk03',
    'bar_wipe',
    'bar_write',
    'barrel_hide',
    'crate_hide',
    'bayonet_attack_idle',
    'bayonet_drill',
    'bomb',
    'cargomaster',
    'cb_apple',
    'coin_flip',
    'coin_flip_old',
    'crazy',
    'doctor_work',
    'drunk',
    'flex',
    'flute',
    'fish',
    'gp_chant_a',
    'gp_chant_b',
    'gp_handdig',
    'gp_jump',
    'gp_moaning',
    'gp_searching',
    'gp_summon',
    'idleB',
    'idleC',
    'hit',
    'jig',
    'jr_look_idle',
    'jr_look_idle_2',
    'loom',
    'lute',
    'stockade',
    'patient_work',
    'primp',
    'scorpion_rear_up',
    'scorpion_attack_tail_sting',
    'shovel',
    'smith',
    'sit',
    'sit_cards',
    'sit_cards_avatar',
    'sit_gator',
    'sit_hanginglegs',
    'sit_write',
    'sit_sleep',
    'sit_write',
    'sleep_sick',
    'sow',
    'stir',
    'sweep',
    'tatoo',
    'tatoo_receive',
    'wt_sword',
    'ned_is_crazy',
    'zz_bayonet_run',
    'zz_boxing',
    'zz_cutlass_taunt',
    'zz_dagger_combo',
    'zz_dagger_idle',
    'zz_gun_aim_idle',
    'zz_gun_pointedup_idle',
    'zz_jack_idle',
    'zz_sword_idle',
    'zz_sword_run',
    'zz_wand_idle',
    'zz_voodoo_doll_poke',
    'zz_js_idle',
    'zz_js_idleToBow',
    'zz_js_handsOnHips',
    'zz_cutlass_L1',
    'zz_cutlass_L2',
    'zz_cutlass_L3',
    'zz_cutlass_L4',
    'zz_cutlass_L5',
    'zz_dagger_L1',
    'zz_dagger_L2',
    'zz_dagger_L3',
    'zz_dagger_L4',
    'zz_dagger_L5',
    'zz_doll_L1',
    'zz_doll_L2',
    'zz_doll_L3',
    'zz_doll_L4',
    'zz_doll_L5',
    'zz_pistol_L1',
    'zz_pistol_L2',
    'zz_pistol_L3',
    'zz_pistol_L4',
    'zz_pistol_L5',
    'zz_staff_L1',
    'zz_staff_L2',
    'zz_staff_L3',
    'zz_staff_L4',
    'zz_staff_L5']
PROP_ANIMS = {
    'models/char/seagull_hi': [
        'models/char/seagull_flying',
        'models/char/seagull_landing',
        'models/char/seagull_groom_idle',
        'models/char/seagull_idle',
        'models/char/seagull_takeoff'],
    'models/char/raven_hi': [
        'models/char/raven_fly',
        'models/char/raven_glide',
        'models/char/raven_idle'],
    'models/char/scorpion_hi': [
        'models/char/scorpion_idle',
        'models/char/scorpion_knockback',
        'models/char/scorpion_pick_up_human'],
    'models/char/alligator_hi': [
        'models/char/alligator_idle',
        'models/char/alligator_pet_idle',
        'alligator_pet_look_idle'],
    'models/props/dolphin_zero': [
        'models/props/dolphin_jump_a',
        'models/props/dolphin_jump_a',
        'models/props/dolphin_jump_b'],
    'models/char/jr_2000': [
        'models/char/jr_look_idle',
        'models/char/jr_look_idle_2',
        'models/char/jr_haunted_holiday'],
    'models/char/js_2000': [
        'models/char/js_idle',
        'models/char/js_idle',
        'models/char/js_idleToBow',
        'models/char/js_handsOnHips',
        'models/char/js_tv_bow',
        'models/char/js_walk_camera'] }

def getPropAnimList():
    resultDic = { }
    totalList = []
    for propModel in PROP_ANIMS.keys():
        animList = [
            [
                propModel],
            PROP_ANIMS[propModel]]
        totalList.append(animList)

    resultDic['["Visual"]["Model"]'] = totalList
    return resultDic


def getHandHeldPropsDict(versionFilter = None, rarityFilter = None, isFromLoot = True, isFromShop = True, isFromQuest = True, isFromPromo = True, isFromPVP = True, isFromNPC = True):
    resultDict = { }
    for weaponId in ItemGlobals.getHumanWeaponTypes():
        toBeAdded = True
        name = ItemGlobals.getModel(weaponId)
        if versionFilter is not None:
            toBeAdded = ItemGlobals.getVersion(weaponId) == versionFilter

        if toBeAdded and rarityFilter is not None:
            toBeAdded = ItemGlobals.getRarity(weaponId) == rarityFilter

        if not isFromLoot or ItemGlobals.isFromLoot(weaponId):
            if not isFromShop or ItemGlobals.isFromShop(weaponId):
                if not isFromQuest or ItemGlobals.isFromQuest(weaponId):
                    if not isFromPromo or ItemGlobals.isFromPromo(weaponId):
                        if (isFromPVP or ItemGlobals.isFromPVP(weaponId)) and isFromNPC:
                            pass
        toBeAdded &= ItemGlobals.isFromNPC(weaponId)
        if toBeAdded:
            if ItemGlobals.getType(weaponId) == ItemGlobals.GRENADE:
                resultDict[name] = 'models/ammunition/%s' % name
            else:
                resultDict[name] = 'models/handheld/%s' % name
        ItemGlobals.getType(weaponId) == ItemGlobals.GRENADE

    if not versionFilter is not None and rarityFilter is not None:
        if isFromLoot == True and isFromShop == True and isFromQuest == True and isFromPromo == True:
            pass
        if not (isFromPVP == True):
            return resultDict

    for key in INTERACT_ANIMS.keys():
        allIdles = INTERACT_ANIMS[key].get('idles')
        if allIdles:
            if type(allIdles) is type({ }):
                props = allIdles.get(3003).get('props')
            else:
                props = INTERACT_ANIMS[key].get('props')
            if props:
                if isinstance(props[0], list):
                    prop = props[0][0]
                else:
                    prop = props[0]
                if prop:
                    name = prop[prop.rfind('/') + 1:]
                    resultDict[name] = prop



    return resultDict
