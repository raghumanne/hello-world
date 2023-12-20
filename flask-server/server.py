from flask import Flask, render_template
import basic, db_test

app = Flask(__name__)


# Common API endpoint to get page content
@app.route('/api/members', methods=['GET'])
def page1():
    return 'hii'

@app.route('/api/basic', methods=['GET'])
def page2():
    return(basic.base())

@app.route('/api/db_test', methods=['GET'])
def page3():
    return(db_test.fetch_data_from_database())


if __name__ == '__main__':
    app.run(port=8000, debug=True)