import yfinance as yf
import pandas as pd


class StockAggregatedFundamentals:

    def __init__(self, company_ticker):
        # Define the yfinance stock ticker
        self.stock_yf_ticker = yf.Ticker(company_ticker)

    def ticker_page_basic_info(self):
        info = {
            "name": self.stock_yf_ticker.info["longName"],
            "about_business": self.stock_yf_ticker.info["longBusinessSummary"],
            "industry": self.stock_yf_ticker.info["industry"],
            "current_price": self.stock_yf_ticker.info["currentPrice"],
            "symbol": self.stock_yf_ticker.info["symbol"],
            "shares_outstanding": self.stock_yf_ticker.info["sharesOutstanding"],
            "dividend_yield": (self.stock_yf_ticker.info["dividendYield"] * 100),
            "cash": round(self.stock_yf_ticker.info["totalCash"]/10000000, 2),
            "debt": round(self.stock_yf_ticker.info["totalDebt"]/10000000, 2),
            "book_value": self.stock_yf_ticker.info["bookValue"],
            "eps": self.stock_yf_ticker.info["trailingEps"],
            "price_to_book": self.stock_yf_ticker.info["priceToBook"],
            "price_to_earnings": self.stock_yf_ticker.info["trailingPE"],
            "insider_holdings": self.stock_yf_ticker.info["heldPercentInsiders"]*100,
            "day_high": self.stock_yf_ticker.info["dayHigh"],
            "day_low": self.stock_yf_ticker.info["dayLow"],
            "market_cap": round(self.stock_yf_ticker.info["marketCap"]/10000000, 2),
            "52_wk_high": self.stock_yf_ticker.info["fiftyTwoWeekHigh"],
            "52_wk_low": self.stock_yf_ticker.info["fiftyTwoWeekLow"],
            "five_yr_avg_return": self.stock_yf_ticker.info["fiveYearAverageReturn"],
            "enterprise_value": round(self.stock_yf_ticker.info["enterpriseValue"]/10000000, 2),
            "debt_to_equity": self.stock_yf_ticker.info["debtToEquity"],
            "roe": self.stock_yf_ticker.info["returnOnEquity"],

        }
        return info
