from sklearn.datasets import fetch_20newsgroups_vectorized
newsgroups_train = fetch_20newsgroups_vectorized('train',  (),  'sklearn_data', download_if_missing=True, return_X_y=False)
