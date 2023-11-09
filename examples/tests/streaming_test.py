import time

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from brainflow.data_filter import DataFilter


def main():
    BoardShim.enable_dev_board_logger()

    # use synthetic board for demo
    params = BrainFlowInputParams()
    params.ip_port = 6677
    params.ip_port_aux = 6678
    params.ip_address = '225.1.1.1'
    params.ip_address_aux = '225.1.1.1'
    params.master_board = BoardIds.SYNTHETIC_BOARD
    board_id = BoardIds.STREAMING_BOARD

    board = BoardShim(board_id, params)
    board.prepare_session()
    board.start_stream()
    time.sleep(10)
    data_default = board.get_board_data(preset=BrainFlowPresets.DEFAULT_PRESET)
    data_aux = board.get_board_data(preset=BrainFlowPresets.AUXILIARY_PRESET)
    board.stop_stream()
    board.release_session()
    DataFilter.write_file(data_default, 'default.csv', 'w')
    DataFilter.write_file(data_aux, 'aux.csv', 'w')
    print(data_default)
    print(data_aux)



if __name__ == "__main__":
    main()
