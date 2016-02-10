'''
Created on Jan 29, 2016

@author: sharvani
'''

NULL_STRING = ""
PLAYER_X = 'X'
PLAYER_O = 'O'
UNOCCUPIED = '*'
NUMBER_OF_SQUARES = 5

ALGORITHM_SELECTION = 0
PLAYER_SELECTION = 1
CUTTING_OFF_DEPTH  = 2
INPUT_FILE_BOARD_VALUE_START = 3
INPUT_FILE_BOARD_VALUE_END = 7
INPUT_FILE_CURRENT_STATE_START = 8
INPUT_FILE_CURRENT_STATE_END = 12

GREEDY_BEST_FIRST_SEARCH = '1'
MINIMAX = '2'
ALPHA_BETA_PRUNING = '3'
BATTLE_SIMULATION = '4'

NEXT_STATE_FILE_NAME = 'next_state.txt'
TRAVERSAL_LOG_FILE_NAME = 'traverse_log.txt'
TRACE_STATE_FILE_NAME = 'trace_state.txt'

ROOT = "root"

INITIAL_DEPTH = 0

INFINITY = 10000
INFINITY_STRING = "Infinity"

MINIMAX_TRAVERSAL_LOG_FIRST_LINE = "Node,Depth,Value"
ALPHA_BETA_PRUNING_TRAVERSAL_LOG_FIRST_LINE = "Node,Depth,Value,Alpha,Beta"
TRAVERSAL_LOG_ALPHABET_MAP = ["A","B","C","D","E"]

ACQUIRE = "acquire"
RESET = "reset"

CHECK_ADJACENCY = "checkAdjacency"
RAID = "raid"

BATTLE_SIMULATION_PLAYER1 = 1
BATTLE_SIMULATION_PLAYER1_ALGORITHM = 2
BATTLE_SIMULATION_PLAYER1_CUTOFF_DEPTH = 3
BATTLE_SIMULATION_PLAYER2 = 4
BATTLE_SIMULATION_PLAYER2_ALGORITHM = 5
BATTLE_SIMULATION_PLAYER2_CUTOFF_DEPTH = 6
BATTLE_SIMULATION_BOARD_VALUE_START_INDEX = 7
BATTLE_SIMULATION_BOARD_STATE_START_INDEX = 12