from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbshoppingmall                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/lists', methods=['POST'])
def write_list():
    receive_name = request.form['give_name']
    receive_count = request.form['give_count']
    receive_address = request.form['give_address']
    receive_number = request.form['give_number']
    print(receive_name, receive_count, receive_address, receive_number)

    list = {
       'name': receive_name,
       'count': receive_count,
       'address': receive_address,
       'number': receive_number
    }

    db.lists.insert_one(list)
    return jsonify({'result':'success', 'msg': '이 요청은 POST! 작성완료'})


@app.route('/lists', methods=['GET'])
def read_lists():
    lists = list(db.lists.find({}, {'_id': 0}))
    return jsonify({'result':'success', 'lists': lists})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)