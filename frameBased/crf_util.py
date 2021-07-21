# 単語情報から素性を作成
def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]
    features = {
        'bias': 1.0,
        'word': word,
        'postag': postag
    }

    if i > 0:
        word_left = sent[i-1][0]
        postag_left = sent[i-1][1]
        features.update({
            '-1:word': word_left,
            '-1:postag': postag_left
        })
    else:
        features['BOS'] = True
    
    if i < len(sent) - 1 :
        word_right = sent[i+1][0]
        postag_right = sent[i+1][0]
        features.update({
            '+1:word': word_right,
            "+1:postag": postag_right
        })
    else:
        features['EOS'] = True
    return features
