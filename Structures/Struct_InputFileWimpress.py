################### Material Properties ###################

E                   = 70.0e9            # [Pa] Young's modulus of the spar
G                   = 30.0e9            # [Pa] shear modulus of the spar
yieldStress         = 500.0e6 / 2.5     # [Pa] yield stress divided by 2.5 for limiting case
mrho                = 3.0e3             # [kg/m^3] material density



################### Assumed variables ###################

wing_weight_ratio                 =   2.000000    # [ ]      

################### Planform Definition ###################

wing_area_wpref             = 383.740000    # [m^2]     wing area in the trapezoid area in the Wimpress definition
aspect_ratio_wpref          =   9.000000    # [ ]       wing aspect ratio
kink_location_ratio         =   0.370000    # [ ]       spanwise location of the kink from the center line / semispan
body_side_ratio             =   0.100000    # [ ]       spanwise location of the side of fuselage from the center line / semispan
taper_ratio_trap            =   0.275000    # [ ]       Taper ratio at tip/root for the trap-wing area
root_chord_extension_ratio  =   1.372874    # [ ]       Actrual root chord / trap root chord
trap_quarter_sweep          =  35.000000    # [deg]     inboard leading-edge sweep angle


################### 3D geometry ###################

dihedral            =   1.500000    # [deg]     wing dihedral

# Control points of twist and thickness to chord ratio. 
# index 1, 2, 3 are from TIP to ROOT
twist_cp_1          =  -3.000000    # [deg]     
twist_cp_2          =   0.000000    # [deg]     
twist_cp_3          =   3.000000    # [deg]
t_over_c_cp_1       =   0.150000    # [ ]
t_over_c_cp_2       =   0.150000    # [ ]
t_over_c_cp_3       =   0.150000    # [ ]

# chordwise location of maximum (NACA0015) thickness
c_max_t             =   0.303000    # [ ]       

############ Structure Design Variables ############

fem_origin          =   0.350000    # [ ]       normalized chordwise location of the spar
thickness_cp_1      =   0.01
thickness_cp_2      =   0.01
thickness_cp_3      =   0.01

####################### Loads ######################
# Loads on the structural (spar) nodes, from tip to root:
#  Forces in [N]
#  Bending Moments in [N.m]
loads_Fx            =  [-3048.874830, -8049.131076, -11794.825236, -14964.573007, -17386.897108, -14545.454519, -10657.122856]
loads_Fy            =  [3226.235167, 7365.270459, 8407.813943, 7916.857034, 7311.487887, 6269.430025, 5212.041039]
loads_Fz            =  [28543.906354, 76509.644253, 116952.174321, 160342.239542, 229686.530966, 300342.680528, 324023.905362]
loads_Mx            =  [67474.346278, 45053.664144, 48362.409955, 51369.335294, 164944.105160, 65472.998931, -439781.937673]
loads_My            =  [56521.526875, 61748.554484, 92414.612971, 133329.278205, 242572.065277, 319553.435956, -76193.955789]
loads_Mz            =  [1620.836443, 3241.671218, 6658.228366, 12134.503883, 24877.420696, 24477.362453, 10003.414330]



