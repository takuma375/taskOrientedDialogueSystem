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
