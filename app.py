from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Our Website</title>
    <style>
        body { font-size: 20px; display: flex; margin: 0; font-family: Arial, sans-serif; }
        .menu { width: 20%; background: blue; color: white; padding: 20px; height: 100vh; box-sizing: border-box; }
        .menu a { color: white; text-decoration: none; display: block; padding: 10px; margin: 5px 0; border: 1px solid white; text-align: center; }
        .menu a:hover { background: white; color: blue; }
        .content { width: 80%; background: brown; color: black; padding: 20px; height: 100vh; box-sizing: border-box; overflow-y: auto; }
        .header { background: black; color: white; padding: 10px; text-align: center; font-size: 22px; font-weight: bold; }
    </style>
    <script>
        function loadContent(page) {
            fetch('/content/' + page)
            .then(response => response.text())
            .then(data => document.getElementById('content').innerHTML = data);
        }
    </script>
</head>
<body>
    <div class="menu">
        <a href="#" onclick="loadContent('home')">🏠 Home</a>
        <a href="#" onclick="loadContent('about')">ℹ️ About</a>
        <a href="#" onclick="loadContent('bot')">🤖 Bot</a>
        <a href="#" onclick="loadContent('support')">📞 Support</a>
        <a href="#" onclick="loadContent('payment')">💰 Payment</a>
    </div>
    <div class="content" id="content">
        <div class="header">Official site: MR.ADiL01</div>
        <h1>Welcome, dear friend!</h1>
        <p>For other options, click the buttons on the left.</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(TEMPLATE)

@app.route('/content/<page>')
def load_page(page):
    pages = {
        "home": "<div class='header'>Official site: MR.ADiL01</div><h1>Welcome, dear friend!</h1><p>For other options, click the buttons on the left.</p>",
        "about": "<div class='header'>Official site: MR.ADiL01</div><h1>About This Site</h1><p>This site is dedicated to the @MirrorBot. All updates will be posted here first.</p>",
        "bot": "<div class='header'>Official site: MR.ADiL01</div><h1>Supported Bot</h1><p>The bot supported by this site is: <a href='https://t.me/MirrorBot' target='_blank'>@MirrorBot</a></p>",
        "support": "<div class='header'>Official site: MR.ADiL01</div><h1>Support</h1><p>For more information, please contact our support on Telegram: <a href='https://t.me/MR4DiL' target='_blank'>@MR4DiL</a></p>",
        "payment": "<div class='header'>Official site: MR.ADiL01</div><h1>Payment Methods</h1><p>Currently, you can make payments using USDT, TRX, TON, BTC, BNB.</p>"
    }
    return pages.get(page, "<div class='header'>Official site: MR.ADiL01</div><h1>Page Not Found</h1>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
