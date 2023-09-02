import sqlite3

# 创建一个SQLite数据库文件（如果不存在）
def create_database():
    conn = sqlite3.connect('./data/data.db')
    c = conn.cursor()
    # # INTEGER
    c.execute('''
                    CREATE TABLE IF NOT EXISTS weather_data (
                    id INTEGER PRIMARY KEY,
                    province TEXT,
                    city TEXT,
                    adcode TEXT NOT NULL,
                    weather TEXT,
                    temperature TEXT,
                    winddirection TEXT,
                    windpower TEXT,
                    humidity_float TEXT,
                    reporttime TEXT
                )''')
    conn.commit()
    conn.close()

# 插入数据
def insert_data(data):
    conn = sqlite3.connect('./data/data.db')
    c = conn.cursor()

    province = data['province']
    city = data['city']
    adcode = data['adcode']
    weather = data['weather']
    temperature = data['temperature']
    winddirection = data['winddirection']
    windpower = data['windpower']
    humidity_float = data['humidity_float']
    reporttime = data['reporttime']

    print(province)
    c.execute("""INSERT INTO weather_data (province, city, adcode, weather, temperature, winddirection, windpower, humidity_float, reporttime
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (province, city, adcode, weather, temperature, winddirection, windpower, humidity_float, reporttime)
                )

    conn.commit()
    conn.close()



# 查询所有数据
def query_all_data():
    conn = sqlite3.connect('./data/data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM weather_data")
    rows = c.fetchall()
    conn.close()
    return rows


# 根据条件查询数据
def query_data_by_adcode(adcode,date):
    conn = sqlite3.connect('./data/data.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM weather_data where adcode = '{adcode}' and reporttime = '{date}' ORDER BY reporttime DESC ")
    rows = c.fetchall()
    out = {}
    if len(rows) != 0:
        rows = rows[0]
        out['province'] = rows[1]
        out['city'] = rows[2]
        out['adcode'] = rows[3]
        out['weather'] = rows[4]
        out['temperature'] = rows[5]
        out['winddirection'] = rows[6]
        out['windpower'] = rows[7]
        out['humidity_float'] = rows[8]
        out['reporttime'] = rows[9]

    conn.close()
    return out

