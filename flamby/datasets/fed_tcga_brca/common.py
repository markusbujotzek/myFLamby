NUM_CLIENTS = 6
BATCH_SIZE = 32
NUM_EPOCHS_POOLED = 20
LR = 1e-3


def get_nb_max_rounds(num_updates, batch_size=BATCH_SIZE):
    # TODO find out true number
    return (23000 // BATCH_SIZE) * NUM_EPOCHS_POOLED // num_updates