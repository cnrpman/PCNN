from model.data_utils import getDataset
from model.pcnn_model import PCNNModel
from model.config import Config


def main():
    # create instance of config
    config = Config()

    # build model
    model = PCNNModel(config)
    model.build()
    # model.restore_session("results/crf/model.weights/") # optional, restore weights
    # model.reinitialize_weights("proj")

    # create datasets
    dev   = getDataset(config.filename_dev, config.processing_word,
                         config.processing_relation, config.max_iter)
    train = getDataset(config.filename_train, config.processing_word,
                         config.processing_relation, config.max_iter)

    # train model
    model.train(train, dev)

if __name__ == "__main__":
    main()
