#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

def main():
    # 処理前の時刻(t0)を取得
    t0 = time.clock()
    # 計測したい処理
    time.sleep(3)
    # 処理後の時刻(t1)を取得
    t1 = time.clock()
    # 処理後の時刻(t1)-処理前の時刻(t0)で処理時間を計算
    print("dt="+str(t1-t0)+"[s]")

if __name__ == '__main__':
    main()
