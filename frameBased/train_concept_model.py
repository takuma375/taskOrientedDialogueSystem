sents = []
lis =[]

# concept_samples.dat の読み込み
for line in open("concept_samples.dat", "r"):
    line = line.rstrip()
    # 空行で1つの事例が完了
    if line == "":
        sents.append(lis)
        lis = []
    else:
        # concept_samples.dat は単語, 品詞, ラベルがタブ区切りになっている
        word, posttag, label = line.split('\t')
        lis.append([word, posttag, label])

