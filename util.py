import pandas as pd
import numpy as np

def extract_last_price(df, interval = "M"):

    '''df.index 가 datetime 형태여야만 함. interval 은 resample by 그대로 따라감'''
    
    # 1. year - month 별로 그룹핑된 groupby object 생성
    grouped = df.resample(interval)
    
    # 2. last day 뽑아내는 함수 및 적용
    def extract_last_day(grouped):
        last_day = grouped.index[-1]
        return last_day
    
    # 3. 원래 가격 df 에서 마지막 날만 reindex로 filtering. df.filter(items = last_days, axis = 0 도 동일)
    last_days = grouped.apply(extract_last_day)
    last_days = last_days.values.reshape(len(last_days))

    df_reindexed = df.reindex(last_days)

    return df_reindexed
