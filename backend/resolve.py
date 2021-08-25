from flask import Flask, request

app = Flask(__name__)

# VueからのPOSTリクエスト
@app.route('/api/resolve', methods=["POST"])
# Vueからリクエストされたときのメソッド
def resolve():
  # POSTで送られてきたjsonオブジェクトを受け取る
  get_request = request.get_json()
  # jsonオブジェクトの中の数独の配列を取得
  get_numbers = get_request['numbers']
  # 計算結果をresultsにいれる
  result = [
    [4, 2, 3, 9, 8, 5, 1, 6, 7],
    [7, 6, 5, 4, 2, 1, 9, 8, 3],
    [1, 9, 8, 6, 7, 3, 2, 5, 4],
    [5, 8, 4, 7, 6, 2, 3, 1, 9],
    [3, 1, 9, 8, 5, 4, 7, 2, 6],
    [6, 7, 2, 3, 1, 9, 5, 4, 8],
    [8, 5, 6, 2, 9, 7, 4, 3, 1],
    [2, 3, 7, 1, 4, 8, 6, 9, 5],
    [9, 4, 1, 5, 3, 6, 8, 7, 2],
  ]
  # Vueに計算結果を返却する
  return { 'result': result }

## おまじない
if __name__ == "__main__":
    app.run(debug=True)