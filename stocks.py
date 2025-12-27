import os
import ssl#處理 HTTPS 憑證
import yfinance as yf#抓 Yahoo Finance 資料

# --- 強制修復 SSL 憑證報錯 不驗證 SSL 憑證（開發用）讓 HTTPS 請求能成功送出---
ssl._create_default_https_context = ssl._create_unverified_context
os.environ['CURL_CA_BUNDLE'] = ''
# ---------------------------

ticker_symbol = "VOO"
ticker = yf.Ticker(ticker_symbol)#建立一個股票物件

try:
    # 抓取 10 年內的月線數據
    hist = ticker.history(period="10y", interval="1mo")
    
    if hist.empty:
        print("未抓取到數據，請檢查網路連線。")
    else:
        print(f"--- {ticker_symbol} 成功抓取 ---")
        print(hist.tail())
        hist.to_csv("voo_data.csv")
except Exception as e:
    print(f"執行出錯：{e}")