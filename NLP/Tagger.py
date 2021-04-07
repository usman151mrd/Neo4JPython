
from NLP.db import DataBase
from pickle import load, dump
import nltk
import nltk.data
import nltk.tag


class TagValidation:
    def __init__(self):

        self.conn = DataBase()

    def get_tag(self, name):
        tags = self.conn.retrieve(name)
        if len(tags) != 0:
            return tags[0]
        else:
            print("no record found against ", name, " in neo4j")


class Tagger:
    def __init__(self):
        self.model = self.load_tagger()
        self.tv = TagValidation()

    def load_tagger(self):
        path = open('model/tagger.pkl', 'rb')
        tagger = load(path)
        return tagger

    def update_tagger(self, dictionary):
        tagger = nltk.tag.UnigramTagger(model=dictionary, backoff=self.model)
        return tagger

    def save_tagger(self):
        output = open("model/tagger.pkl", 'wb')
        dump(self.model, output)
        output.close()

    def validate(self, tag_list):
        unknown = list()
        for word, tag in tag_list:
            if tag is None:
                unknown.append(word)
        dic = dict()
        if len(unknown) == 0:
            return tag_list
        for word in unknown:
            dic[str(word)] = str(self.tv.get_tag(word))
        #
        self.model = self.update_tagger(dic)
        self.save_tagger()
        for word, tag in tag_list:
            if word in dic.keys():
                tag = dic[word]
        return tag_list

    def tag(self, string):
        if isinstance(string, str):
            return self.model.tag(nltk.word_tokenize(string))
        else:
            return None

    def evaluate(self, string):
        output = self.tag(string)
        if output is not None:
            return self.validate(output)
