import pickle
import numpy
import pandas
import os

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the model file
model_path = os.path.join(current_dir, 'model_pickle.sav')



def predictor(splited_data,):
    print("/n script rf_model")
    # load the model from disk
    with open(model_path, 'rb') as f:
        loaded_model = pickle.load(f)
    # filename = 'model_pickle.sav'
    # loaded_model = pickle.load(open(filename, 'rb'))
    print("model loaded")
    print(splited_data.shape)
    print(list(splited_data))
    X = splited_data.drop(columns=['protocal', 'Domain_name', 'Address'])
    # preds = loaded_model.predict(splited_data[X])
    preds = loaded_model.predict(X)
    print("prediction complete")
    print(preds)
    if preds == 0:
        print("Spoofed webpage: Yes")
    else:
        print("Spoofed webpage: NO")

    # score = loaded_model.predict_proba(splited_data[X])
    # str2 = "Confidence score: " + str(score[0][1])

    return preds
