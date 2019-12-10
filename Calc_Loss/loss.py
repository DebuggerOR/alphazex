from convertor.Convertor_ver3 import convert
from agent1_zero_dnn.compare import *
from agent1_zero_dnn.game import ori_move
import sys
import numpy as np

file_name = "../data_text_games_name_in_first_line/2118.txt"
model_file1 = "../agent1_zero_dnn/model"
config = CompareConfig()
moves = convert(file_name)
model = load_model(model_file1)
predictor = TreeSearchPredictor(config.search_config, model, new_board(config.size), True)
temp = 0.7

for mv in moves:
    predictor.board = np.array(mv.board_stt)
    predictor.run(config.iterations)
    value, probabilities = predictor.predict()
    tprobs = temperature(probabilities, temp)

    # now we have the best move according model (not 15)
    model_moves = ori_move(tprobs)
    if mv.next_mv in model_moves:
        print("great")
    else:
        print("failed")

    next_move = mv.next_mv[0], mv.next_mv[1]
    print_board(predictor.board, flip_move(next_move), file=sys.stderr)
    # print(value)