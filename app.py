from flask import Flask, request
import datetime

from func import sheet_write

app = Flask(__name__)

@app.route('/lead')
def hello_world():
    if request.method == 'GET':
        date = str(datetime.datetime.now())
        user_name = request.args.get('user_name')
        user_email = request.args.get('user_email')
        user_id = request.args.get('user_id')
        nomer_zakaza = request.args.get('nomer_zakaza')
        soderzhimoe = request.args.get('soderzhimoe')
        stoimost = request.args.get('stoimost')
        oplacheno = request.args.get('oplacheno')
        ostalos_oplatit = request.args.get('ostalos_oplatit')
        traffic_source = request.args.get('traffic_source')
        user_utm_source = request.args.get('user_utm_source')

        data = [date, user_email, user_id, nomer_zakaza, soderzhimoe, stoimost,oplacheno,ostalos_oplatit,traffic_source,user_utm_source]
        print(data)
        sheet_write(data)

        return 'Done'


if __name__ == "__main__":
    app.run()