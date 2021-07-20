import random


# 都道府県名のリスト
prefs = [   '三重', '京都', '佐賀', '兵庫', '北海道', '千葉', '和歌山',
                '埼玉', '大分', '大阪', '奈良', '宮城', '宮崎', '富山', '山口',
                '山形', '山梨', '岐阜', '岡山', '岩手', '島根', '広島', '徳島',
                '愛媛', '愛知', '新潟', '東京', '栃木', '沖縄', '滋賀', '熊本',
                '石川', '神奈川', '福井', '福岡', '福島', '秋田', '群馬', '茨城',
                '長崎', '長野', '青森', '静岡', '香川', '高知', '鳥取', '鹿児島']

# 日付のリスト
dates = ["今日", "明日"]

# 情報種別のリスト
types = ["天気", "気温"]

# サンプル文に含まれる単語を置き換えることで学習用事例を作成
def random_generate(root):
    # タグがない文章の場合は置き換えしないでそのまま返す
    if len(root) == 0:
        return root.text
    # タグで囲まれた場所を同じ種類の単語で書き換える
    buf = ""
    for elem in root:
        if elem.tag == "place":
            pref = random.choice(prefs)
            buf += pref   
        elif elem.tag == "date":
            date = random.choice(dates)
            buf += date
        elif elem.tag == "type":
            _type = random.choice(types)
            buf += _type
        if elem.tail is not None:
            buf += elem.tail
    return buf

