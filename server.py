from flask import Flask, render_template
from stock_aggregated_fundamental import StockAggregatedFundamentals
import requests

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


# Stocks:
@app.route('/stocks/ticker')
def ticker():
    return render_template("ticker-search.html")


@app.route('/stocks/ticker/<company_ticker>')
def stock_aggregated(company_ticker):
    stock = StockAggregatedFundamentals(company_ticker=company_ticker)
    info = stock.ticker_page_basic_info()
    return render_template('ticker.html', info=info)


@app.route('/stocks/fundamental-charts')
def fundamental_charts():
    return render_template("fundamental-charts.html")


# Mutual Funds:
@app.route('/mf/rolling-returns')
def rolling_returns():
    return render_template("rolling-returns.html")


# Calculators:
@app.route('/cagr-calculator')
def cagr_calculator():
    return render_template("cagr-calc.html")


@app.route('/goal-calculator')
def goal_calculator():
    return render_template("goal-calc.html")


@app.route('/sip-calculator')
def sip_calculator():
    return render_template("sip-calc.html")


# Blog:
blog_url = "https://api.npoint.io/88c2c1f644ef334058be"
all_posts = requests.get(blog_url).json()


@app.route('/blog/home')
def blog_home():
    return render_template("blog-home.html", posts=all_posts)


@app.route('/post/<int:blog_id>')
def post(blog_id):
    for post in all_posts:
        if post["id"] == blog_id:
            return render_template("post.html", post=post)


# Page Unavailable:
@app.route('/page-not-available')
def page_not_available():
    return render_template("page-not-available.html")


if __name__ == "__main__":
    app.run(debug=True)
