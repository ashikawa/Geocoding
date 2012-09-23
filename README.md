## 必要環境

+ Python2系の最新
+ 動作確認は Mac のみ

## マニュアル

+ [ドキュメント](https://developers.google.com/maps/documentation/geocoding/?hl=ja)
+ [サポートされている言語](https://spreadsheets.google.com/pub?key=p9pdwsai2hDMsLkXsoM05KQ&gid=1)

## 使い方


1. 検索リストを作成

	ファイルはUTF-8
	検索ワードを一行に一つ記述

2. ターミナルを開きこのファイルがあるディレクトリに移動する
	
	ex)
		cd ~/Desktop/geo/

3. 以下のコマンドを打つ

	python geo.py < \[作成した入力ファイル\]

	ex)
		python geo.py < list.txt

4. 出力

	結果がターミナルの画面に出力され、同じ内容の物が実行ディレクトリのout.csvに出力される。
	出力はutf-8なので、必要に応じて変換して下さい。(Excelなどは知らぬ)
