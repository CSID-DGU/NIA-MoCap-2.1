import numpy as np

smpl_tree = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8],
                   [6, 9], [7, 10], [8, 11], [9, 12], [9, 14], [9, 13], [12, 15],
                   [13, 16], [14, 17], [16, 18], [17, 19], [18, 20], [19, 21], [20, 22], [21, 23]]

kinect_tree = [[0, 1], [0, 12], [0, 16], [1, 20], [2, 3], [2, 20], [4, 5], [4, 20],
             [5, 6], [6, 7], [7, 21], [7, 22], [8, 9], [8, 20],[9, 10], [10, 11],
             [11, 23], [11, 24], [12, 13], [13, 14], [14, 15], [16, 17], [17, 18], [18, 19]]

kinect_tree_exclude = [[0, 1], [0, 12], [0, 16], [1, 20], [2, 3], [2, 20], [4, 5], [4, 20],
             [5, 6], [6, 7], [8, 9], [8, 20],[9, 10], [10, 11]
             , [12, 13], [13, 14], [16, 17], [17, 18]]

kinect_tree_v2 = [[0, 1], [1, 18], [18, 2], [2, 3], [18, 8], [8, 9], [9, 10], [10, 11],
                  [0, 15], [15, 16], [16, 17], [18, 4], [4, 5], [5, 6], [6, 7], [0, 12], [12, 13],
                  [13, 14]]

kinect_tree_mocap = [[0, 1], [0, 12], [0, 16], [1, 2], [1, 4], [1, 8], [2, 3], [4, 5], [5, 6], [6, 7],
                     [8, 9], [9, 10], [10, 11], [12, 13], [13, 14], [14, 15], [16, 17], [17, 18], [18, 19]]

kinect_tree_vibe = [[8, 1], [8, 17], [1, 2], [2, 3], [3, 4], [1, 5], [5, 6], [6, 7], [0, 1], [0, 9], [9, 10],
                    [10, 11], [11, 16], [0, 12], [12, 13], [13, 14], [14, 15]]

kinect_vibe_extract_joints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 21, 24, 38]

smpl_joints_num = 24

kinect_joints_num = 25

excluded_joint_ids = [23, 24, 22, 21, 19, 15]

ntu_action_labels = [6, 7, 8, 9, 22, 23, 24, 38, 80, 93, 99, 100, 102]

shihao_raw_offsets = np.array([[0,0,0],
                               [1,0,0],
                               [-1,0,0],
                               [0,1,0],
                               [0,-1,0],
                               [0,-1,0],
                               [0,1,0],
                               [0,-1,0],
                               [0,-1,0],
                               [0,1,0],
                               [0,0,1],
                               [0,0,1],
                               [0,1,0],
                               [1,0,0],
                               [-1,0,0],
                               [0,0,1],
                               [0,-1,0],
                               [0,-1,0],
                               [0,-1,0],
                               [0,-1,0],
                               [0,-1,0],
                               [0,-1,0],
                               [0,-1,0],
                               [0,-1,0]])

vibe_raw_offsets = np.array([[0,0,0],
                               [0,-1,0],
                               [0,-1,0],
                               [-1,0,0],
                               [0,0,-1],
                               [0,-1,0],
                               [0,-1,0],
                               [0,0,-1],
                               [0,-1,0],
                               [0,1,0],
                               [0,1,0],
                               [0,1,0],
                               [0,1,0],
                               [0,1,0],
                               [0,1,0],
                               [0,1,0],
                               [0,1,0],
                               [0,-1,0]])

mocap_raw_offsets = np.array([[0, 0, 0],
                             [0, 1, 0],
                             [0, 1, 0],
                             [0, 1, 0],
                             [0, 1, 0],
                             [1, 0, 0],
                             [0, 1, 0],
                             [0, 1, 0],
                             [0, 1, 0],
                             [-1, 0, 0],
                             [-1, 0, 0],
                             [-1, 0, 0],
                             [0, -1, 0],
                             [0, -1, 0],
                             [0, -1, 0],
                             [0, -1, 0],
                             [0, -1, 0],
                             [0, -1, 0],
                             [0, -1, 0],
                             [0, -1, 0]])

# Define a kinematic tree for the skeletal struture
shihao_kinematic_chain = [[0,1,4,7,10], [0,2,5,8,11], [0,3,6,9,12,15], [9,13,16,18,20,22], [9,14,17,19,21,23]]

mocap_kinematic_chain = [[0, 1, 2, 3], [0, 12, 13, 14, 15], [0, 16, 17, 18, 19], [1, 4, 5, 6, 7], [1, 8, 9, 10, 11]]

vibe_kinematic_chain = [[0, 12, 13, 14, 15], [0, 9, 10, 11, 16], [0, 1, 8, 17], [1, 5, 6, 7], [1, 2, 3, 4]]

mocap_action_enumerator = {
    0: "Walk",
    1: "Wash",
    2: "Run",
    3: "Jump",
    4: "Animal Behavior",
    5: "Dance",
    6: "Step",
    7: "Climb"
}

shihao_coarse_action_enumerator = {
    1: "warm_up",
    2: "walk",
    3: "run",
    4: "jump",
    5: "drink",
    6: "lift_dumbbell",
    7: "sit",
    8: "eat",
    9: "turn steering wheel",
    10: "phone",
    11: "boxing",
    12: "throw",
}

shihao_fine_action_enumerator = {
    101: "warm_up_wristankle",
    102: "warm_up_pectoral",
    103: "warm_up_eblowback",
    104: "warm_up_bodylean_right_arm",
    105: "warm_up_bodylean_left_arm",
    106: "warm_up_bow_right",
    107: "warm_up_bow_left",
    201: "walk",
    301: "run",
    401: "jump_handsup",
    402: "jump_vertical",
    501: "drink_bottle_righthand",
    502: "drink_bottle_lefthand",
    503: "drink_cup_righthand",
    504: "drink_cup_lefthand",
    505: "drink_both_hands",
    601: "lift_dumbbell with _right hand",
    602: "lift_dumbbell with _left hand",
    603: "Lift dumbells with both hands",
    604: "lift_dumbbell over head",
    605: "lift_dumbells with both hands and bend legs",
    701: "sit",
    801: "eat_finger_right",
    802: "eat_pie or hamburger",
    803: "Eat with left hand",
    901: "Turn steering wheel",
    1001: "Take out phone, call and put phone back",
    1002: "Call with left hand",
    1101: "boxing_left_right",
    1102: "boxing_left_upwards",
    1103: "boxing_right_upwards",
    1104: "boxing_right_left",
    1201: "throw_right_hand",
    1202: "throw_both_hands",
}

shihao_action_enumerator = {
    0: 'warm_up_wristankle',
    1: 'warm_up_pectoral',
    2: 'warm_up_eblowback',
    3: 'walk',
    4: 'run',
    5: 'jump_handsup',
    6: 'drink_bottle_righthand',
    7: 'drink_bottle_lefthand',
    8: 'lift_dumbles_right',
    9: 'lift_dumbles_left',
    10: 'lift_dumbles_both',
    11: 'lift_dumbles_updown',
    12: 'warm_up_bodylean',
    13: 'warm_up_bow_right',
    14: 'warm_up_bow_left',
    15: 'jump_vertical',
    16: 'lift_dumbles_wholeupdown',
    17: 'sit',
    18: 'eat_finger_right',
    19: 'eat_pie',
    20: 'drive',
    21: 'phone_right',
    22: 'box_left_right',
    23: 'box_left',
    24: 'box_right',
    25: 'throw_right',
    26: 'drink_cup_righthand',
    27: 'drink_cup_righthand',
    28: 'eat_finger_left',
    29: 'phone_left',
    30: 'throw_both',
                      }

ntu_action_enumerator = {
    1: "drink water",
    2: "eat meal or snack",
    3: "brushing teeth",
    4: "brushing hair",
    5: "drop",
    6: "pickup",
    7: "throw",
    8: "sitting down",
    9: "standing up (from sitting position)",
    10: "clapping",
    11: "reading",
    12: "writing",
    13: "tear up paper",
    14: "wear jacket",
    15: "take off jacket",
    16: "wear a shoe",
    17: "take off a shoe",
    18: "wear on glasses",
    19: "take off glasses",
    20: "put on a hat or cap",
    21: "take off a hat or cap",
    22: "cheer up",
    23: "hand waving",
    24: "kicking something",
    25: "reach into pocket",
    26: "hopping (one foot jumping)",
    27: "jump up",
    28: "make a phone call or answer phone",
    29: "playing with phone or tablet",
    30: "typing on a keyboard",
    31: "pointing to something with finger",
    32: "taking a selfie",
    33: "check time (from watch)",
    34: "rub two hands together",
    35: "nod head or bow",
    36: "shake head",
    37: "wipe face",
    38: "salute",
    39: "put the palms together",
    40: "cross hands in front (say stop)",
    41: "sneeze or cough",
    42: "staggering",
    43: "falling",
    44: "touch head (headache)",
    45: "touch chest (stomachache or heart pain)",
    46: "touch back (backache)",
    47: "touch neck (neckache)",
    48: "nausea or vomiting condition",
    49: "use a fan (with hand or paper) or feeling warm",
    50: "punching or slapping other person",
    51: "kicking other person",
    52: "pushing other person",
    53: "pat on back of other person",
    54: "point finger at the other person",
    55: "hugging other person",
    56: "giving something to other person",
    57: "touch other person's pocket",
    58: "handshaking",
    59: "walking towards each other",
    60: "walking apart from each other",
    61: "put on headphone",
    62: "take off headphone",
    63: "shoot at the basket",
    64: "bounce ball",
    65: "tennis bat swing",
    66: "juggling table tennis balls",
    67: "hush (quite)",
    68: "flick hair",
    69: "thumb up",
    70: "thumb down",
    71: "make ok sign",
    72: "make victory sign",
    73: "staple book",
    74: "counting money",
    75: "cutting nails",
    76: "cutting paper (using scissors)",
    77: "snapping fingers",
    78: "open bottle",
    79: "sniff (smell)",
    80: "squat down",
    81: "toss a coin",
    82: "fold paper",
    83: "ball up paper",
    84: "play magic cube",
    85: "apply cream on face",
    86: "apply cream on hand back",
    87: "put on bag",
    88: "take off bag",
    89: "put something into a bag",
    90: "take something out of a bag",
    91: "open a box",
    92: "move heavy objects",
    93: "shake fist",
    94: "throw up cap or hat",
    95: "hands up (both hands)",
    96: "cross arms",
    97: "arm circles",
    98: "arm swings",
    99: "running on the spot",
    100: "butt kicks (kick backward)",
    101: "cross toe touch",
    102: "side kick",
    103: "yawn",
    104: "stretch oneself",
    105: "blow nose",
    106: "hit other person with something",
    107: "wield knife towards other person",
    108: "knock over other person (hit with body)",
    109: "grab other person’s stuff",
    110: "shoot at other person with a gun",
    111: "step on foot",
    112: "high-five",
    113: "cheers and drink",
    114: "carry something with other person",
    115: "take a photo of other person",
    116: "follow other person",
    117: "whisper in other person’s ear",
    118: "exchange things with other person",
    119: "support somebody with hand",
    120: "finger-guessing game (playing rock-paper-scissors)",
     }

class SMPLBodyPart:

    Lbegin_body = np.array([0, 3, 6, 9, 12])
    Lend_body = np.array([3, 6, 9, 12, 15])

    Lbegin_left = np.array([0, 1, 4, 7, 9, 13, 16, 18, 20])
    Lend_left =  np.array([1, 4, 7, 10, 13, 16, 18, 20, 22])

    Lbegin_right = np.array([0, 2, 5, 8, 9, 14, 17, 19, 21])
    Lend_right = np.array([2, 5, 8, 11, 14, 17, 19, 21, 23])


class KinectBodyPart:

    Lbegin_body = np.array([0, 1, 20, 2])
    Lend_body = np.array([1, 20, 2, 3])

    Lbegin_left = np.array([0, 16, 17, 18, 20, 8, 9, 10, 10])
    Lend_left = np.array([16, 17, 18, 19, 8, 9, 10, 23, 24])

    Lbegin_right = np.array([0, 12, 13, 14, 20, 4, 5, 6, 6])
    Lend_right = np.array([12, 13, 14, 15, 4, 5, 6, 21, 22])