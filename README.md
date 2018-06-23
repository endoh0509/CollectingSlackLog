# CollectingSlackLog

# Installation

1. 仮想環境の準備 `python3 -m venv CollectingSlackLog`
2. 仮想環境を使う `source CollectingSlackLog/bin/activate`
3. パッケージをインストール `pip install -r requirements.txt`
4. `.env.yml` を配置
5. `.env.yml` にSlack API トークンを設定
6. 実行 `python main.py`

## .env.ymlの例

```yaml
SLACK_API_TOKEN: xxxx-00000000-00000000-00000000-0x0x0x0x0x
```

https://github.com/slackapi/python-slackclient
