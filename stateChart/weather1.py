import sys, os
from PySide2 import QtCore, QtScxml
import requests, json
from datetime import datetime, timedelta, time

# 都道府県名のリスト
prefs = [   '三重', '京都', '佐賀', '兵庫', '北海道', '千葉', '和歌山',
            '埼玉', '大分', '大阪', '奈良', '宮城', '宮崎', '富山', '山口',
            '山形', '山梨', '岐阜', '岡山', '岩手', '島根', '広島', '徳島',
            '愛媛', '愛知', '新潟', '東京', '栃木', '沖縄', '滋賀', '熊本',
            '石川', '神奈川', '福井', '福岡', '福島', '秋田', '群馬', '茨城',
            '長崎', '長野', '青森', '静岡', '香川', '高知', '鳥取', '鹿児島']

# Open Weather Mapのクエリ文, APIキーの定義
current_weather_url = 'http://api.openweathermap.org/data/2.5/weather'
forecast_url = 'http://api.openweathermap.org/data/2.5/forecast'
appid = os.environ["WEATHER_MAP_API_KEY"]

# テキストから都道府県名を抽出する関数
def get_place(text):
    for pref in prefs:
        if pref in text:
            return pref
    return ""

# テキストに「今日」もしくは「明日」があれば、それを返す関数。見つからない場合は空文字を返す
def get_date(text):
    if "今日" in text:
        return "今日"
    elif "明日" in text:
        return "明日"
    else:
        return ""

# テキストに「天気」もしくは「気温」があればそれを返す関数。見つからない場合は空文字を返す
def get_type(text):
    if "天気" in text:
        return "天気"
    elif "気温" in text:
        return "気温"
    else:
        return ""

# 天気情報を取得する関数
def get_current_weather(lat, lon):
    # 天気情報を取得
    response = requests.get("{}?lat={}&lon={}&lang=ja&units=metric&APPID={}".format(current_weather_url, lat, lon, addid))
    return response.json()

def get_tomorrow_weather(lat, lon):
    #今日の時間を取得
    today = datetime.today()
    # 明日の時間を取得
    tomorrow = today + timedelta(days=1)
    # 明日の正午の時間を取得
    tomorrow_noon = datetime.combine(tomorrow, time(12, 0))
    # UNIX時間に変換
    timestamp = tomorrow_noon.timestamp()

    #天気情報を取得
    response = requests.get("{}?lat={}&lon={}&lang=ja&units=metric&APPID={}".format(forecast_url, lat, lon, appid))
    dic = response.json()

    # 3時間おきの天気情報についてループ
    for i in range(len(dic["list"])):
        # i番目の天気情報(UNIX時間)
        dt = float(dic["list"][i]["dt"])
        # 明日の正午移行のデータになった時点でその天気情報を返す
        if dt >= timestamp:
            return dic["list"][i]
    return ""

# Qtに関する初期設定
app = QtCore.QCoreApplication()
el = QtCore.QEventLoop()

# SCXMLファイルの読み込み
sm = QtScxml.QScxmlStateMachine.fromFile('states.scxml')

# 初期状態に遷移
sm.start()
el.processEvents()

# システムプロンプト
print("SYS> こちらは天気情報案内システムです")

# 状態とシステム発話を紐付けた辞書
uttdic = {  "ask_place": "地名を言ってください",
            "ask_date": "日付を言ってください",
            "ask_type": "情報種別を言ってください"}

# 初期状態の取得
current_state = sm.activeStateNames()[0]
print("current_state", current_state)

# 初期状態に紐付いたシステム発話の取得と出力
sysutt = uttdic[current_state]
print("SYS>", sysutt)

# ユーザー入力の処理
while True:
    text = input("> ")
    # ユーザー入力を用いて状態遷移
    if current_state == "ask_place":
        place = get_place(text)
        if place != "":
            sm.submitEvent("place")
            el.processEvents()
    elif current_state == "ask_date":
        date = get_date(text)
        if date != "":
            sm.submitEvent("date")
            el.processEvents()
    elif current_state == "ask_type":
        _type = get_type(text)
        if _type != "":
            sm.submitEvent("type")
            el.processEvents()

    # 遷移先の状態を取得
    current_state = sm.activeStateNames()[0]
    print("current_state", current_state)

    # 遷移先がtell_infoの場合は情報を伝えて終了
    if current_state == "tell_info":
        print("天気をお伝えします")
        break
    else:
        # その他の繊維先の場合は状態に紐付いたシステム発話を生成
        sysutt = uttdic[current_state]
        print("SYS>", sysutt)

# 終了発話
print("ご利用ありがとうございました")