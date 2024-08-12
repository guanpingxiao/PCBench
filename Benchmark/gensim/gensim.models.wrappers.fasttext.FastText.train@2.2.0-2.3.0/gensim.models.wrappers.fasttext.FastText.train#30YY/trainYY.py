from gensim.models.wrappers import FastText
ft_path = 'fasttext'
corpus_file = 'corpus.txt'
output_file = './'
model = FastText.train(ft_path,  corpus_file,  output_file, model='cbow', size=100, alpha=0.025, window=5)
