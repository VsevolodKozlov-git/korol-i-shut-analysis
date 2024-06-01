import pickle

if __name__ == '__main__':
    with open('data_my/vectorizer.pk', 'rb') as vectorizer_file:
        container = pickle.load(vectorizer_file)
    print(container)