from flask import Flask, request, render_template, session, redirect, url_for
import redis
import math
import os
from dotenv import load_dotenv

load_dotenv()

def load_secret_key():    
    return os.getenv('SECRET_KEY')

def load_config():
    UI_HOST = os.getenv('UI_HOST', '0.0.0.0')  # Example for additional config variables
    UI_PORT = os.getenv('UI_PORT', 8080)

    HOST = os.getenv('REDIS_HOST', 'localhost')
    PORT = os.getenv('REDIS_PORT', 6379)
    SSL = os.getenv('REDIS_SSL', 'false').lower() == 'true'

    return {
        "UI_HOST": UI_HOST,
        "UI_PORT": UI_PORT,
        "REDIS_HOST": HOST,
        "REDIS_PORT": PORT,
        "REDIS_SSL": SSL
    }

app = Flask(__name__)
app.secret_key = load_secret_key()
PAGE_SIZE = 50

@app.route("/", methods=["GET", "POST"])
def index():
    page = int(request.args.get("page", 1))

    if request.method == "POST":
        # store connection info in session
        session['host'] = request.form.get("host")
        session['port'] = int(request.form.get("port", 6379))
        session['password'] = request.form.get("password", None)
        session['ssl'] = request.form.get("ssl") == 'on'

        return redirect(url_for('index'))  # redirect to GET after POST

    # GET request: use session info
    if 'host' in session:
        host = session['host']
        port = session['port']
        password = session['password']
        ssl = session['ssl']

        try:
            r = redis.Redis(host=host, port=port, password=password, decode_responses=True, ssl=ssl, socket_timeout=10)
            info = r.info()
            
            start_index = (page - 1) * PAGE_SIZE
            keys = []
            cursor = 0
            while True:
                cursor, batch = r.scan(cursor=cursor, match='*', count=PAGE_SIZE)
                keys.extend(batch)
                if cursor == 0 or len(keys) >= start_index + PAGE_SIZE:
                    break
            
            page_keys = keys[start_index:start_index + PAGE_SIZE]
            data = {key: r.get(key) for key in page_keys}

            total_keys = info.get('db0', {}).get('keys', len(keys))
            total_pages = math.ceil(total_keys / PAGE_SIZE)
            
            return render_template("dashboard.html", keys=data, total_keys=total_keys, info=info, page=page, total_pages=total_pages)
        except Exception as e:
            session.clear()
            return render_template("index.html", error=str(e))
    else:
        return render_template("index.html")
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)