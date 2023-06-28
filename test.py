# Python3
# -*- coding: utf-8 -*-
# 入力した数値が回文数かどうかを判定
# Webkaru
#
# 数値（整数）
num = int(input("整数を入力してください = "))
# 変数
reverse = 0
remaind = 0
tmp = num
# 反転した数値と元の数値を比較
while tmp != 0:
    # 1桁ずつ数値を切り出す
    remaind = tmp % 10
    # 数値を反転
    reverse = reverse * 10 + remaind
    # 次の桁へシフト
    tmp /= 10
if reverse == num:
    print("「%d」は回文数です。" % num)
else:
    print("「%d」は回文数ではありません。" % num)