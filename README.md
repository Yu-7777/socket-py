## 概要
- Pythonの `socket` を用いたソケット通信
- client側から地名を入力するとサーバー側から天気情報を返すようなプログラム
- 天気取得については `OpenWeatherMap` のAPIを使用している

## 実行手順
1. コンテナイメージのビルド
```bash
docker compose build
```
2. コンテナの起動
```bash
docker compose run client
```
3. 地名の入力（例）
```bash
都市入力: Tokyo
```
## 停止手順
- 以下実行
```bash
docker compose down
```