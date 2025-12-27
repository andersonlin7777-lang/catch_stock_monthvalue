import os
import ssl
from datetime import datetime
import yfinance as yf

# ===== SSL 修復（Windows 常見）=====
ssl._create_default_https_context = ssl._create_unverified_context
os.environ["CURL_CA_BUNDLE"] = ""
# =================================

# ===== 設定要抓的 ETF =====
ETF_LIST = ["^GSPC", "^TWII", "^N225"]

# ===== 資料設定 =====
PERIOD = "10y"       # 抓最近 10 年
INTERVAL = "1mo"     # 1mo = 月線（改成 1d 就是日線）
# =====================

# ===== 輸出資料夾 =====
OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)
# =====================


def fetch_etf(symbol: str):
    print(f"📥 開始抓取 {symbol} ...")

    ticker = yf.Ticker(symbol)
    df = ticker.history(period=PERIOD, interval=INTERVAL)

    if df.empty:
        print(f"⚠️ {symbol} 沒有抓到資料")
        return

    # 加上 ETF 名稱欄位
    df["Symbol"] = symbol

    # 存成 CSV
    filename = f"{symbol}_{INTERVAL}.csv"
    filepath = os.path.join(OUTPUT_DIR, filename)
    df.to_csv(filepath)

    print(f"✅ {symbol} 完成，存檔：{filepath}")


def main():
    start_time = datetime.now()
    print(f"\n🚀 開始更新 ETF 資料：{start_time}\n")

    for etf in ETF_LIST:
        fetch_etf(etf)

    end_time = datetime.now()
    print(f"\n🎉 全部完成，耗時：{end_time - start_time}")


if __name__ == "__main__":
    main()
