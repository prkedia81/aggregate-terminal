from flask import Flask, render_template, Response
from stock_aggregated_fundamental import StockAggregatedFundamentals
import requests
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


# Stocks:
@app.route('/stocks/ticker')
def ticker():
    return render_template("ticker-search.html")


def rounding_check(num, round_factor, divide):
    NoneType = type(None)
    if isinstance(num, NoneType) or num is np.NaN:
        return ""
    else:
        return round(num/divide, round_factor)


def error_check(df, column_name):
    try:
        df[column_name]
        return True
    except:
        return False


@app.route('/<plot_heading>/<company_ticker>/plot.png')
def plot_png(company_ticker, plot_heading):
    stock = StockAggregatedFundamentals(company_ticker=company_ticker)
    fig = stock.create_figure(plot_heading)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/stocks/ticker/<company_ticker>')
def stock_aggregated(company_ticker):
    stock = StockAggregatedFundamentals(company_ticker=company_ticker)
    info = stock.ticker_page_basic_info()
    bs_df = stock.balance_sheet()
    is_df = stock.income_statement()
    scf_df = stock.cash_flow()
    cagr = stock.cagr()
    if company_ticker == "PIDILITIND.NS":
        img_src = "/static/images/Ticker-Page/Pidilite-DCF.png"
    elif company_ticker == "PAGEIND.NS":
        img_src = "/static/images/Ticker-Page/Page-DCF.png"
    elif company_ticker == "RELAXO.NS":
        img_src = "/static/images/Ticker-Page/Relaxo-DCF.png"
    else:
        img_src = ""
    return render_template('ticker.html', info=info, bs_df=bs_df, is_df=is_df, scf_df=scf_df, round_f=rounding_check,
                           error_check=error_check, img_src=img_src, cagr=cagr)


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
