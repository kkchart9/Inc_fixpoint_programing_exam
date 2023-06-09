# 実行手順


## リポジトリのクローン
```angular2html
git clone git@github.com:kkchart9/Inc_fixpoint_programing_exam.git
```

## 問題ごとのテスト

### question1

#### ログ
```angular2html
20201019133124,10.20.30.1/16,2
20201019133125,10.20.30.2/16,1
20201019133134,192.168.1.1/24,10
20201019133324,10.20.30.1/16,-
20201019133325,10.20.30.1/16,3
20201019133325,10.20.30.2/16,-
20201019133327,10.20.30.2/16,-
20201019133403,10.20.30.2/16,-
20201019133444,10.20.30.1/16,2
20201019133506,10.20.30.2/16,6
```

#### 実行
```angular2html
python question1.py
```

#### 結果
```angular2html
10.20.30.1/16の故障期間は1です。
10.20.30.2/16の故障期間は181です。
```

### question2
#### ログ(上記と同様のデータを使う)
#### 実行
```angular2html
python question2.py --n 2
```

#### 結果
```angular2html
10.20.30.2/16の故障期間は181です。
```

### question3
#### ログ（上記のログに追加して）
```angular2html
20201019133156,192.168.1.1/24,10
20201019133164,192.168.1.1/24,10
202010191331178,192.168.1.1/24,10
202010191331179,192.168.1.1/24,16
202010191331190,192.168.1.1/24,12
```
#### 実行
```angular2html
python question3.py --n 2 --m 3 --t 10
```

#### 結果（上記の結果に追加して）
```angular2html
192.168.1.1/24 の過負荷状態期間は 20201019133164 ~ 202010191331179 です。
192.168.1.1/24 の過負荷状態期間は 202010191331178 ~ 202010191331190 です。
```

### question4
#### ログ（上記のログに追加して）
```angular2html
20201019134156,192.168.1.1/24,-
20201019134164,192.168.1.1/24,-
20201019134178,192.168.1.1/24,-
20201019134198,192.168.1.1/24,16
```
#### 実行
```angular2html
python question4.py --n 2 --m 3 --t 10
```

#### 結果（上記の結果に追加して）
```angular2html
サブネット: 192.168.1.0/24
192.168.1.1/24 の故障期間は 42 です。
```