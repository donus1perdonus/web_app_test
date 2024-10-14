from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    conn = psycopg2.connect(
        dbname="your_database_name",
        user="your_user_name",
        password="your_password",
        host="db",  # имя сервиса базы данных из docker-compose.yml
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM your_table_name")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('home.html', rows=rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
