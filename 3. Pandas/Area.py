import pandas as pd

data = {
    'width': [1, 2, 3, 4, 5, 6],
    'height': [4, 1, 3, 5, 2, 6]
}

df = pd.DataFrame(data, index=data['width'])

df['area'] = df['width'] * df['height']

df.set_index('area', inplace=True)

print(df.head())