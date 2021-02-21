from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    many_receive = request.form['many_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']

    doc ={ 'name': name_receive,
            'many': many_receive,
           'address': address_receive,
           'number': number_receive
    }

    db.shopping.insert_one(doc)
    return jsonify({'msg': '주문 완료!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    a_list = list(db.shopping.find({},{'_id':False}))
    return jsonify({'b_list': a_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5002, debug=True)