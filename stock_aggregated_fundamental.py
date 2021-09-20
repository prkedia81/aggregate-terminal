import yfinance as yf
import pandas as pd
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class StockAggregatedFundamentals:

    def __init__(self, company_ticker):
        # Define the yfinance stock ticker
        self.ticker = company_ticker
        self.stock_yf_ticker = yf.Ticker(company_ticker)
        self.price_df = yf.download(self.ticker, start="2018-09-19", auto_adjust=True)

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

    def balance_sheet(self):
        return self.stock_yf_ticker.balance_sheet.T

    def income_statement(self):
        return self.stock_yf_ticker.financials.T

    def cash_flow(self):
        return self.stock_yf_ticker.cashflow.T

    def create_figure(self, plot_heading):
        if plot_heading == "price":
            fig = Figure()
            axis = fig.add_subplot(1, 1, 1)
            axis.plot(self.price_df['Close'])
            return fig
        elif plot_heading == "pe":
            earnings = []  # 2019, 2020, 2021
            income_statement = self.stock_yf_ticker.financials.T
            for i in range(income_statement.shape[0] - 2, -1, -1):
                earnings.append(round(income_statement["Net Income"][i], 2))
            num_shares = self.stock_yf_ticker.info["sharesOutstanding"]
            eps = []
            for i in range(len(earnings)):
                eps_calc = earnings[i] / num_shares
                eps.append(round(eps_calc, 2))
            pe = []
            count = 0
            eps_index = 0
            for i in range(self.price_df.shape[0]):
                pe_calc = self.price_df["Close"][i] / eps[eps_index]
                pe.append(pe_calc)
                count += 1
                if count == 250:
                    eps_index += 1
                    count = 0
            fig = Figure()
            axis = fig.add_subplot(1, 1, 1)
            axis.plot(pe)
            return fig

    def cagr(self):
        initial_price = self.price_df["Close"][0]
        final_price = self.price_df["Close"][self.price_df.shape[0] - 1]
        cagr = pow((final_price / initial_price), (1 / 3)) - 1
        cagr = round(cagr * 100, 2)
        return cagr
