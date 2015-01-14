# twitter_get_starred_imgs
## Introduction
下載打星推中的圖片，並放到 Dropbox 資料夾內 (optional)

## Installation
1. [python-twitter](https://github.com/bear/python-twitter) is required

        pip install twitter-python
        
2. 手動建立 JSON 設定檔，範例如下：

        {
    	"CONSUMER_KEY": "你的 twitter API consumer_key",
    	"CONSUMER_SECRET": "你的 twitter API consumer secret",
    	"ACCESS_TOKEN": "你的 twitter API access token",
    	"ACCESS_TOKEN_SECRET": "你的 twitter API access token secret"
		}
3. 執行程式就會把圖片下載回來放在指定的資料夾裡。如果不加 -d 參數則會下載在當前目錄中。

		./twitter_get_starred_imgs.py -c 設定檔檔名 -d dropbox 資料夾位置
		
4. 下載完畢後會自動把**處理過的**打星推取消打星
