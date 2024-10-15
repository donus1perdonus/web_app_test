from flask import Flask, render_template
import psycopg2

app = Flask(__name__, template_folder='/opt/project_web_app/frontend')

@app.route('/')
def home():
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user1",
        password="test",
        host="db",  # имя сервиса базы данных из docker-compose.yml
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('home.html', rows=rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

