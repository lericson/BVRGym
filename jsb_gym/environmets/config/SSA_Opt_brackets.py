import numpy as np

version = 1

general = {
        'env_name': 'SSA',
        'f16_name': 'f16',
        'sim_time_max': 60*4,           
        'r_step' : 20,
        'fg_r_step' : 1,
        'missile_idle': False,
        'scale': True,
        'rec_f16': False,
        'rec_aim': False}

states= {
        'obs_space': 6,
        'act_space': 2,
        'update_states_type': 1
}

sf = {  'd_min': 40e3,
        'd_max': 120e3,
        't': general['sim_time_max'],
        'mach_max': 2,
        'alt_min': 3e3,
        'alt_max': 14e3,
        'd_max_reward': 20e3,
        'aim_vel0_min': 280, 
        'aim_vel0_max': 320, 
        'aim_alt0_min': 9e3, 
        'aim_alt0_max': 11e3}

blue = np.load('jsb_gym/jupyter/logs/Wedge_blue.npy')
psi_b = 0
f16_1 = { 'lat':    60.14,
        'long':     16.4,
        'vel':      300,
        'alt':      10e3,
        'heading' : 0}

f16_2 = { 'lat':    59.45,
        'long':     19.35,
        'vel':      300,
        'alt':      10e3,
        'heading' : 180}

f16_3 = { 'lat':    blue[2,0],
        'long':     blue[2,1],
        'vel':      300,
        'alt':      10e3,
        'heading' : psi_b}

f16_4 = { 'lat':    blue[3,0],
        'long':     blue[3,1],
        'vel':      300,
        'alt':      10e3,
        'heading' : psi_b}

red  = np.load('jsb_gym/jupyter/logs/Wall_red.npy')
psi_r = 180
f16r_1 = { 'lat':   59.9,
        'long':     18,
        'vel':      300,
        'alt':      10e3,
        'heading' : psi_r}

f16r_2 = { 'lat':   red[1,0],
        'long':     red[1,1],
        'vel':      300,
        'alt':      10e3,
        'heading' : psi_r}

f16r_3 = { 'lat':   red[2,0],
        'long':     red[2,1],
        'vel':      300,
        'alt':      10e3,
        'heading' : psi_r}

f16r_4 = { 'lat':   red[3,0],
        'long':     red[3,1],
        'vel':      300,
        'alt':      10e3,
        'heading' : psi_r}

#f16  = {'f16_1':f16_1, 'f16_2':f16_2, 'f16_3':f16_3, 'f16_4':f16_4}
#f16r = {'f16r_1':f16r_1, 'f16r_2':f16r_2, 'f16r_3':f16r_3, 'f16r_4':f16r_4}

f16  = {'f16_1':f16_1, 'f16_2':f16_2}
f16r = {'f16r_1':f16r_1}
