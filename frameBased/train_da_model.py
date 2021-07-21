import MeCab


# MeCabの初期化
mecab = MeCab.Tagger()
mecab.parse('')

sents = []
labels = []

# da_samples.datの読み込み
for line in open("da_samples.dat", "r"):
    line = line.rstrip()

    # da_samples.datには対話行為, 発話文が含まれている
    da, utt = line.split('\t')
    words = []
    for line in mecab.parse(utt).splitlines():
        if line == "EOS":
            break
        else:
            # MeCabの出力から単語を抽出
            word, feature_str = line.split("\t")
            words.append(word)
    # 空白区切りの単語列をsentsに追加
    sents.append(" ".join(words))
    # 対話行為ラベルをlabelsに追加
    labels.append(da)

