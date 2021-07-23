from da_concept_extractor import DA_Concept
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

# システムの対話行為タイプとシステム発話を紐付けた辞書
uttdic = {  "open-prompt": "ご用件をどうぞ",
            "ask-place": "地名(都道府県名)を言ってください",
            "ask-date": "日付(今日/明日)を言ってください",
            "ask-type": "情報種別(天気/気温)を言ってください"
            }

# 発話から得られた情報をもとにフレームを更新
def update_frame(frame, da, conceptdic):
    # 値の整合性を確認し、整合しないものは空文字にする
    for k, v in conceptdic.items():
        if k == "place" and v not in prefs:
            conceptdic[k] = ""
        elif k == "date" and v not in dates:
            conceptdic[k] = ""
        elif k == "type" and v not in types:
            conceptdic[k] = ""
    
    if da == "request-weather":
        for k, v in conceptdic.items():
            # コンセプトの情報でスロットを埋める
            frame[k] = v
    elif da == "initialize":
        frame = {"place": "", "date": "", "type": ""}
    elif da == "correct-info":
        for k, v in conceptdic.items():
            if frame[k] == v:
                frame[k] = ""
    
    return frame

# フレームの状態から次のシステム対話行為を決定
def next_system_da(frame):
    # すべてのスロットが空のときはオープンな質問を行う
    if frame["place"] == "" and frame["date"] == "" and frame["type"] == "":
        return "open-prompt"
    # 空のスロットがあればその要素を質問する
    elif frame["place"] == "":
        return "ask-place"
    elif frame["date"] == "":
        return "ask-date"
    elif frame["type"] == "":
        return "ask-type"
    else:
        return "tell-info"

# 対話行為とコンセプトの推定器
da_concept = DA_Concept()

# フレーム
frame = {"place": "", "date": "", "type": ""}

# システムプロンプト
print("SYS> こちらは天気情報案内システムです")
print("SYS> ご用件をどうぞ")

# ユーザー入力の処理
while True:
    text = input("> ")

    # 現在のフレームを表示
    print("frame=", frame)

    # 手入力で対話行為タイプとコンセプトを入力していた箇所を自動推定するように変更
    da, conceptdic = da_concept.process(text)

    # 対話行為とコンセプト列を用いてフレームを更新
    frame = update_frame(frame, da, conceptdic)

    # 更新後のフレームを表示
    print("updated frame=", frame)

    # フレームからシステム対話行為を得る
    sys_da = next_system_da(frame)

    # 遷移先がtell_infoの場合は情報を伝えて終了
    if sys_da == "tell-info":
        print("天気をお伝えします")
        break
    else:
        # 対話行為に紐付いたテンプレートを用いてシステム発話を生成
        sysutt = uttdic[sys_da]
        print("SYS>", sysutt)

# 終了発話
print("ご利用ありがとうございました")