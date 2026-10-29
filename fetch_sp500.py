"""從 Yahoo Finance 抓取標普500指數 (^GSPC) 每日收盤價，存成 CSV 與 Excel。

用法：
    pip install yfinance pandas openpyxl
    python fetch_sp500.py                 # 1990-01-01 到今天
    python fetch_sp500.py --start 2000-01-01 --out SP500
"""
import argparse
from datetime import date, timedelta

import yfinance as yf

TICKER = "^GSPC"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--start", default="1990-01-01")
    p.add_argument("--end", default=date.today().isoformat(), help="含當天")
    p.add_argument("--out", default="SP500_GSPC_daily_close", help="輸出檔名（不含副檔名）")
    args = p.parse_args()

    # yfinance 的 end 不含當天，所以加一天
    end = (date.fromisoformat(args.end) + timedelta(days=1)).isoformat()
    df = yf.download(TICKER, start=args.start, end=end, auto_adjust=False, progress=False)
    if df.empty:
        raise SystemExit("沒有抓到資料，請檢查網路或日期區間")

    close = df["Close"][TICKER].rename("Close").round(2).to_frame()
    close.index = close.index.date
    close.index.name = "Date"

    close.to_csv(f"{args.out}.csv")
    close.to_excel(f"{args.out}.xlsx", sheet_name="GSPC")
    print(f"{len(close)} 筆，{close.index[0]} ~ {close.index[-1]}")
    print(f"已存：{args.out}.csv、{args.out}.xlsx")


if __name__ == "__main__":
    main()
