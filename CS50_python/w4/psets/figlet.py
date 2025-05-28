from pyfiglet import Figlet
import sys
import random

list = ['stealth_', 'flipped', 'inc_raw_', 'bubble_b', 'braced', 'heart_right', 'js_block_letters', 'gauntlet', 'crawford', 'rainbow_', 'sketch_s', 'sub-zero', 'hieroglyphs', 'c_consen', 'top_duck', 'madrid', 'charact6', 'thorned', 'calvin_s', 'stronger_than_all', 'nvscript', 'amc_aaa01', 'sm______', 'xttyb', 'efti_robot', 'letters', 'nancyj-underlined', "patorjk's_cheese", 'p_skateb', 'tinker-toy', 'decimal', 'modular', 'twopoint', 'xsansb', 'bubble__', 'jacky', 'banner3', 'helvi', 'arrows', 'vortron_', 'dwhistled', 'hollywood', 'xhelvbi', 'ts1_____', 'roman___', 'danc4', 'xtty', 'clr6x6', 'smshadow', 'small_caps', 'char1___', 'computer', 'helvb', 'rally_sp', 'amc_3_line', 'space_op', 'ivrit', 'def_leppard', 'big_money-se', '5lineoblique', 'battlesh', 'mayhem_d', 'broadway_kb', 'xsansbi', 'cola', 'hyper___', 'red_phoenix', 'stick_letters', 'katakana', 'maxfour', 'utopiai', 'bigfig', '6x9', 'utopiabi', 'straight', 'amc_razor2', 'cricket', 'platoon_', 'horizontal_right', 'ghoulish', 'heart_left', 'rot13', 'term', 'wavy', 'small_shadow', 'contessa', 'usa_pq__', 'future_1', 'nancyj', 'runic', 'stencil1', 'bell', 'faces_of', 'npn_____', 'clr5x10', 'pepper', 'xhelv', 'demo_m__', 'c1______', 'stencil2', 'lazy_jon', 'bigchief', 'ascii_new_roman', 'helv', 'road_rai', 'p_s_h_m_', 'ti_pan__', 'trek', 'joust___', 'dcs_bfmo', 'xbrite', 'xcourb', 'xcourbi', 'marquee', 'line_blocks', 'bear', 'fantasy_', 'thin', 'finalass', 'relief', 'soft', 'bubble', 'ansi_shadow', 'mini', 'caus_in_', 'fbr1____', 'sansi', 'diet_cola', 'smkeyboard', 'ntgreek', '3d-ascii', 'new_asci', 'colossal', 'univers', 'smscript', 'alpha', 'flyn_sh', 'merlin1', 'flower_power', 'crawford2', 'cour', 'xsbooki', 'rampage_', 'utopiab', 'graffiti', 'skateroc', 'js_bracket_letters', 'blocks', 'big_money-sw', 'glenyn', 'rounded', 'alligator', 'tombstone', 'yie-ar__', 'rastan__', 'xsans', 'puzzle', 'avatar', 'lexible_', 'trashman', 'standard', 'mcg_____', 'britebi', 'relief2', 'sweet', 'wow', 'basic', 'tubular', 'tsm_____', 'lean', 'rev', 'block', 'eftiwall', 'big_money-nw', 'xcouri', 'ripper!_', 'doh', 'sansbi', 'skateord', 'shimrod', 'blocky', '1row', 'a_zooloo', 'dancing_font', 'amc_thin', 'diamond', 'clr8x10', 'doom', 'double', 'britei', 'whimsy', 'amc_slash', 'fire_font-s', 'rozzo', 'charact3', 'fireing_', 'peaks', '3-d', 'char4___', 'fp2_____', '4max', 'big', 'isometric3', 'cyberlarge', 'serifcap', 'rotated', 'characte', 'future_3', 'z-pilot_', 'nipples', 'raw_recu', 'pacos_pe', 'high_noo', 'krak_out', 'amc_slider', 'gothic', 'briteb', 'ttyb', 'stampate', 'js_stick_letters', 'taxi____', 'alligator2', 'tanja', 'fairligh', 'kik_star', 'js_capital_curves', 'b1ff', 'amc_3_liv1', 'nancyj-fancy', 'bolger', 'yie_ar_k', 'fender', 'charact2', 'moscow', 'isometric1', 'clr4x6', 'big_money-ne', 'morse2', 'drpepper', 'dotmatrix', 'mig_ally', 'sblood', 'xsbook', 'konto_slant', 'banner4', 'rowancap', 'ebbs_1__', 'future_6', 'catwalk', 'hades___', 'fair_mea', 'mshebrew210', 'pod_____', 'poison', 'tecrvs__', 'octal', 'xbriteb', 'street_s', '4x4_offr', 'atc_gran', 'italics_', 'small', 'twisted', 'nancyj-improved', 'tsn_base', 'future_2', 'isometric4', 'ticks', 'beer_pub', 'hex', 'merlin2', 'train', 'aquaplan', 'clb8x8', 'xchartr', 'runyc', 'ucf_fan_', 'cygnet', 'stforek', 'modern__', 'smtengwar', 'rally_s2', 'invita', 'platoon2', 'speed', 'd_dragon', 'lockergnome', '5x7', 'wet_letter', 'benjamin', 'mirror', 'lcd', 'clr5x8', 'war_of_w', 'pebbles', 'usa_____', 'super_te', 'slant_relief', 'threepoint', 'fun_faces', 'slscript', 'the_edge', 'funky_dr', 'subteran', 'xcour', 'c_ascii_', 'stacey', 'jazmine', 'digital', 'unarmed_', 'amc_untitled', 'chartr', 'xbritebi', 'italic', 'baz__bil', 'battle_s', 'rad_phan', 'gradient', 'future_5', 'cosmike', 'varsity', 'old_banner', 'atc_____', 'morse', 'fire_font-k', 'char2___', 'shadow', 'coinstak', 'kgames_i', 'odel_lak', 'letterw3', 'char3___', 'banner3-D', 'cybersmall', 'slant', 'thick', 'hypa_bal', 'fraktur', 'lil_devil', 'henry_3d', 'cli8x8', 'usaflag', 'twin_cob', 'future_7', 'sans', 'fp1_____', 'type_set', 'caligraphy', 'konto', 'sbooki', 'santa_clara', 'bloody', '1943____', 'eftichess', 'fourtops', 'roman', 'keyboard', 'ugalympi', 'eftipiti', 'filter', 'rad_____', 't__of_ap', 'tec_7000', 'alphabet', 'greek', 'tty', 'bright', 'electronic', 'nscript', 'bulbhead', 'green_be', 'puffy', 'o8', 'sbookb', 'b_m__200', 'smisome1', 'cybermedium', 'zig_zag_', 'dos_rebel', 'pawn_ins', '3d_diagonal', 'ascii___', 'js_cursive', 'delta_corps_priest_1', 'radical_', 'elite', 'small_slant', 'charact5', 'sl_script', 'georgi16', 'xsbookbi', 'contrast', '5x8', 'tiles', 'sbook', 'chunky', 'script', 'short', 'ogre', 'clb8x10', 'xsbookb', 'patorjk-hex', 'crazy', 'sbookbi', 'notie_ca', 'future_4', 'ok_beer_', 'ghost', 'sansb', 'magic_ma', 'xhelvb', 'rok_____', 'impossible', 'helvbi', 'cards', 'rci_____', 'broadway', 'epic', 'tengwar', 'grand_pr', 'advenger', '3x5', 'utopia', 'eftirobot', 'ebbs_2__', 'times', 'spliff', 'eca_____', 'mnemonic', 'asc_____', 'skate_ro', 'larry3d', 'linux', 'hills___', 'acrobatic', 'pyramid', 'kban', 'double_shorts', 'heavy_me', 'coil_cop', 'icl-1900', 'georgia11', 'amc_razor', 'heroboti', 'fbr12___', 'demo_1__', 'zone7___', 'eftifont', 'nfi1____', 'isometric2', 'goofy', 'knob', 'fuzzy', 'phonix__', '6x10', 'smslant', 'xtimes', 'stop', 'xsansi', 'pawp', 'clr6x8', 'etcrvs__', 'gothic__', 'xhelvi', 'f15_____', 'swan', 'tav1____', 'demo_2__', 'rectangles', 'binary', 'letter_w', 'r2-d2___', 'mad_nurs', 'fbr_tilt', 'tomahawk', 'stampatello', 'rockbox_', 'panther_', 'chiseled', 'starwars', 'amc_neko', 'druid___', 'ansi_regular', 'brite', 'clr8x8', 'house_of', 'e__fist_', 'script__', 'spc_demo', '64f1____', 'charset_', 'home_pak', 'com_sen_', 'defleppard', 'couri', 'eftitalic', 'amc_tubes', 'charact1', 'triad_st', 'assalt_m', 'charact4', 'test1', 'swamp_land', 'horizontal_left', 'small_poison', 'slide', 'tec1____', 'this', 'fun_face', 'tsalagi', 'chartri', 'devilish', 'star_strips', 'clr6x10', 'muzzle', 'convoy__', 'c2______', 'xbritei', 'future_8', 'jerusalem', 'timesofl', 'outrun__', 'clb6x10', 'master_o', 'eftiwater', 'xchartri', 'clr7x8', 'fbr2____', 'weird', 'banner', 'fbr_stri', 'cosmic', 'star_war', 'stellar', 'barbwire', 'courbi', 'mike', 'calgphy2', 'courb', 'ghost_bo', 'os2', 'asslt__m', 'rammstein', 'clr7x10', 'deep_str', 'cursive', 'graceful', 'ticksslant', 'clr5x6']
vald_cmd = ["f" , "font"]

def main():
    if len(sys.argv) == 1:
        text = input("Input: ")
        f = random.choice(list)
        fig(text, f)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "-font") and sys.argv[2] in list:
        text = input("Input: ")
        fig(text, sys.argv[2])
    else:
        sys.exit("Invalid usage")





def fig(s, f):
    figlet = Figlet()
    figlet.setFont(font=f)
    print(figlet.renderText(s))


main()







