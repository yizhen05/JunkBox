#!/bin/bash
# プロキシ環境下で実行する場合は適宜設定
# export https_proxy=http://aaa.bbb.ccc:nnnn

# WebフックURL（※事前準備で発行したURLを設定する）
WEBHOOK_URL='https://hogehogehoge'

# curlコマンド実行
curl -H "Content-Type: application/json" -d "{\"text\": \"Door Locked!!\"}" $WEBHOOK_URL
