from flask import Flask, request, session, g, redirect, \
    url_for, abort, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_FILE', silent=True)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# AMAP_ACCESS_KEY=app.config['AMAP_ACCESS_KEY']


class POI(db.Model):
    poiId = db.Column(db.Integer, primary_key=True)
    poiName = db.Column(db.String(120), index=True, unique=True)
    poiLat = db.Column(db.Float)
    poiLng = db.Column(db.Float)

    def __repr__(self):
        return '<POI {}: [{}, {}]>'.format(self.poiName, self.poiLat, self.poiLng)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/base')
def base():
    return render_template('base.html', ACCESS_KEY=AMAP_ACCESS_KEY)


@app.route('/mapTest')
def mapTest():
    username = 'Susan'
    path = [ [114,39], [116,40], [117,39] ] # 绘制路径，可从文件或数据库读取经纬度坐标，然后传递给html
    path = [
        [116.2699842453, 40.0118554028],
        [116.2776875496, 40.0023554989],
        [116.2909269333, 39.9983283241],
        [116.3096809387, 39.9994954074],
        [116.3159036636, 39.9921473816],
        [116.3164830208, 39.9838449697],
        [116.3175773621, 39.9756402091],
        [116.3213539124, 39.9674015726],
        [116.3232851028, 39.9578132466],
        [116.3251948357, 39.9432061456],
        [116.3388204575, 39.9382047998],
        [116.3677883148, 39.9405080966],
        [116.3728952408, 39.9336637876],
        [116.3734102249, 39.9245808594],
        [116.3737535477, 39.9160892062],
        [116.3739252090, 39.8894554507],
        [116.3743543625, 39.8785388760],
        [116.3792896271, 39.8648536559],
        [116.3712644577, 39.8532248377],
        [116.3711357117, 39.8459269952],
        [116.3708353043, 39.8370219177],
        [116.4129781723, 40.0833908853],
        [116.4131069183, 40.0752145100]
    ]
    poi_names = [
        '安河桥北',
        '北宫门',
        '西苑',
        '圆明园',
        '北京大学东门',
        '中关村',
        '海淀黄庄',
        '人民大学',
        '魏公村',
        '国家图书馆',
        '动物园',
        '新街口',
        '平安里',
        '西四',
        '灵境胡同',
        '菜市口',
        '陶然亭',
        '北京南站',
        '马家堡',
        '角门西',
        '公益西桥',
        '天通苑北',
        '天通苑'
    ]
    points = path
    return render_template('mapTest.html', ACCESS_KEY=AMAP_ACCESS_KEY, username=username, path=path, points=points)

if __name__ == '__main__':
    app.run()
