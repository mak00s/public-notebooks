import pandas as pd

def test(df):
  # Userごとに連番をふる
  df['Seq'] = df.groupby('GA ID').cumcount() + 1
  
  # 日本語のカラム名を英語に統一
  d = {'ページの': 'Page',
     'タイトル': ' title',
     'イベント( |の)?': 'Event ',
     'カテゴリ': 'category',
     'アクション': 'action',
     'ラベル': 'label',
     '値': 'value',
     '目標( |の)?': 'Goal ',
     '完了数': 'completion(s)',
     '番号': 'index',
     '名': 'name',
     '数': 'count',
     # さらに読みやすくする
     'sessions.channel': 'Channel',
     'sessions.deviceCategory': 'Device'
  }
  df.columns = df.columns.to_series().replace(d, regex=True)
  
  # 配列を結合しフラット化
  ar = ['Event action','Event category','Event label','Event count','Event value',
      'Page URL','Page title',
      'Product code','Product name','Product count','Product quantity','Product revenue','Transaction Id'
     ]
  for i in df.columns.to_list():
    if i in ar:
        df[i] = df[i].apply(lambda x:",".join(x) if pd.notnull(x) else x)

  return df
