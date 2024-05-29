# -*- coding: utf-8 -*-
"""Regression Analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y6sYq5qh7AwiR170IFMn74SkJ4aL9ytG
"""

from google.colab import files

# Yüklemek istediğiniz dosyaları seçin
uploaded = files.upload()

# Yüklenen dosyaların adlarını görüntüleyin
for filename in uploaded.keys():
    print(f'{filename} dosyası yüklendi.')

import pandas as pd

# Dosyayı yükleyin
filename = 'MergedData.csv'
data = pd.read_csv(filename)

# Verinin ilk birkaç satırını gösterin
print(data.head())

# Veri setindeki sütunların listesini alın
columns = data.columns.tolist()
print("Veri Setindeki Sütunlar:")
print(columns)

import pandas as pd

# Veri setini uygun sütunlara bölmek için ";" işaretine göre ayırarak yükleyelim
data = pd.read_csv("MergedData.csv", sep=";")

# Sütunları uygun şekilde adlandıralım
data.columns = ["Date", "CocoaPrice", "NestleAveragePrice", "NestleStock"]

# Verinin ilk birkaç satırını gösterelim
print(data.head())

# NaN değerleri 0 ile doldurma
data['NestleStock'].fillna(0, inplace=True)

# NestleStock sütununu tamsayıya dönüştürme
data['NestleStock'] = data['NestleStock'].astype(int)

# Verinin ilk birkaç satırını gösterme
print(data.head())

# Virgül ve noktaları kaldırma ve tamsayıya dönüştürme
data['NestleStock'] = data['NestleStock'].str.replace('.', '').str.replace(',', '').astype(int)

# Verinin ilk birkaç satırını gösterme
print(data.head())

filename = 'NestleAveragePrice.csv'

# Load the data into a pandas DataFrame
data = pd.read_csv(filename)
print(data.head())

# Specify the file name
filename = 'NestleAveragePrice.csv'

# Load the data into a pandas DataFrame
data = pd.read_csv(filename, delimiter=';')

# Display the first few rows of the data
print(data.head())

# Convert the 'DATE' column to datetime format
data['DATE'] = pd.to_datetime(data['DATE'], format='%d.%m.%Y')

# Set the 'DATE' column as the index
data.set_index('DATE', inplace=True)

# Rename the column to a more convenient name, e.g., 'Price'
data.rename(columns={'APU0000702421': 'Price'}, inplace=True)

# Display the first few rows of the prepared data
print(data.head())



# Set the 'DATE' column as the index
data.set_index('DATE', inplace=True)

print(data.columns)

import pandas as pd
import matplotlib.pyplot as plt

# Dosya adını belirtin
filename = 'NestleAveragePrice.csv'

# Veriyi doğru şekilde yükleyin ve sütunları ayırın
data = pd.read_csv(filename, delimiter=';')

# Sütun adlarını ayırın
data[['DATE', 'Price']] = data['DATE;APU0000702421'].str.split(';', expand=True)

# Gereksiz sütunu kaldırın
data.drop(columns=['DATE;APU0000702421'], inplace=True)

# 'DATE' sütununu datetime formatına çevirin
data['DATE'] = pd.to_datetime(data['DATE'], format='%d.%m.%Y')

# 'DATE' sütununu dizin olarak belirleyin
data.set_index('DATE', inplace=True)

# Sütun adlarını yeniden adlandırın
data.rename(columns={'Price': 'Price'}, inplace=True)

# Verinin ilk birkaç satırını gösterin
print(data.head())

# Veriyi görselleştirin
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Price'], label='Actual Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Nestle Stock Prices')
plt.legend()
plt.show()

from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt

# Convert the 'DATE' column to datetime format
data['DATE'] = pd.to_datetime(data['DATE'], format='%d.%m.%Y')

# Set the 'DATE' column as the index
data.set_index('DATE', inplace=True)

# Rename the column to a more convenient name, e.g., 'Price'
data.rename(columns={'APU0000702421': 'Price'}, inplace=True)

# Display the first few rows of the prepared data
print(data.head())

# Define the Holt's Linear Trend model
model = ExponentialSmoothing(data['Price'], trend='add', seasonal=None)

# Fit the model
fit = model.fit()

# Forecast the next 30 days
forecast = fit.forecast(steps=36)

# Display the forecasted values
print(forecast)

# Plot the original data and the forecasted values
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Price'], label='Actual Prices')
plt.plot(forecast.index, forecast, label='Forecasted Prices', color='red')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Nestle Stock Price Forecast - Holt\'s Method')
plt.legend()
plt.show()

from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV dosyasını okuma
file_path = 'NestleAveragePrice.csv'  # Dosya yolunu güncelleyin
data = pd.read_csv(file_path)

# 'DATE' sütununu tarih formatına dönüştürme
data['DATE'] = pd.to_datetime(data['date'])

# 'APU0000702421' sütununu ortalama fiyat olarak adlandırma
data.rename(columns={'APU0000702421': 'Average_Price'}, inplace=True)

# Tarih sütununu indeks olarak ayarlama
data.set_index('DATE', inplace=True)

# 30 günlük hareketli ortalama hesaplama
data['30_Day_MA'] = data['Average_Price'].rolling(window=30).mean()

# Veriyi görselleştirme
plt.figure(figsize=(12, 6))
plt.plot(data['Average_Price'], label='Ortalama Fiyat')
plt.plot(data['30_Day_MA'], label='30 Günlük Hareketli Ortalama')
plt.title('Nestle Ortalama Fiyat ve 30 Günlük Hareketli Ortalama')
plt.xlabel('Tarih')
plt.ylabel('Fiyat')
plt.legend()
plt.show()

# Dosyanın ilk birkaç satırını okuma
print(data.head())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV dosyasını okuma
file_path = 'NestleAveragePrice.csv'  # Dosya yolunu güncelleyin
data = pd.read_csv(file_path, sep=';', parse_dates=['DATE'])

# Sütun adlarını güncelleme
data.columns = ['DATE', 'Average_Price']

# Tarih sütununu indeks olarak ayarlama
data.set_index('DATE', inplace=True)

# 30 günlük hareketli ortalama hesaplama
data['21_Day_MA'] = data['Average_Price'].rolling(window=21).mean()

# Veriyi görselleştirme
plt.figure(figsize=(12, 6))
plt.plot(data['Average_Price'], label='Ortalama Fiyat')
plt.plot(data['21_Day_MA'], label='21 Günlük Hareketli Ortalama')
plt.title('Nestle Ortalama Fiyat ve 21 Günlük Hareketli Ortalama')
plt.xlabel('Tarih')
plt.ylabel('Fiyat')
plt.legend()
plt.show()

# Son 30 günlük ortalama fiyatın eğilimini hesaplama
last_30_days_avg = data['Average_Price'].tail(30)
trend = (last_30_days_avg.iloc[-1] - last_30_days_avg.iloc[0]) / 30

# Son 30 günün ortalaması ile trendi kullanarak gelecek 30 gün için tahmin yapma
last_date = data.index[-1]
forecast_dates = pd.date_range(start=last_date, periods=30, freq='D')[1:]  # Son tarih dahil değil
forecast_values = []

for i in range(1, 31):
    forecast_values.append(last_30_days_avg.iloc[-1] + trend * i)

# Tahmin edilen değerleri DataFrame'e ekleme
forecast = pd.DataFrame({'DATE': forecast_dates, 'Forecasted_Average_Price': forecast_values})
forecast.set_index('DATE', inplace=True)

# Gelecek tahminleri görselleştirme
plt.figure(figsize=(12, 6))
plt.plot(data['Average_Price'], label='Ortalama Fiyat')
plt.plot(data['30_Day_MA'], label='30 Günlük Hareketli Ortalama')
plt.plot(forecast.index, forecast['Forecasted_Average_Price'], label='Tahmin Edilen Ortalama Fiyat', linestyle='--', color='red')
plt.title('Nestle Ortalama Fiyat ve Tahmin Edilen Fiyat')
plt.xlabel('Tarih')
plt.ylabel('Fiyat')
plt.legend()
plt.show()

# Son 30 günlük ortalama fiyatın eğilimini hesaplama
last_30_days_avg = data['Average_Price'].tail(30)
trend = (last_30_days_avg.iloc[-1] - last_30_days_avg.iloc[0]) / 30

# Son 30 günün ortalaması ile trendi kullanarak gelecek 30 gün için tahmin yapma
last_date = data.index[-1]
forecast_dates = pd.date_range(start=last_date, periods=30, freq='D')[1:]  # Son tarih dahil değil
forecast_values = []

for i in range(1, 31):
    forecast_values.append(last_30_days_avg.iloc[-1] + trend * i)

# Tahmin edilen değerleri DataFrame'e ekleme


# Gelecek tahminleri görselleştirme
plt.figure(figsize=(12, 6))
plt.plot(data['Average_Price'], label='Ortalama Fiyat')
plt.plot(data['21_Day_MA'], label='30 Günlük Hareketli Ortalama')
plt.plot(forecast.index, forecast['Forecasted_Average_Price'], label='Tahmin Edilen Ortalama Fiyat', linestyle='--', color='red')
plt.title('Nestle Ortalama Fiyat ve Tahmin Edilen Fiyat')
plt.xlabel('Tarih')
plt.ylabel('Fiyat')
plt.legend()
plt.show()

# Tahmin edilen değerleri DataFrame'e ekleme
forecast = pd.DataFrame({'DATE': forecast_dates, 'Forecasted_Average_Price': forecast_values})
forecast.set_index('DATE', inplace=True)

print(len(forecast_dates))
print(len(forecast_values))

# Son 30 günün ortalaması ile trendi kullanarak gelecek 30 gün için tahmin yapma
last_date = data.index[-1]
forecast_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=30, freq='D')
forecast_values = []

for i in range(1, 31):
    forecast_values.append(last_30_days_avg.iloc[-1] + trend * i)

# Tahmin edilen değerleri DataFrame'e ekleme
forecast = pd.DataFrame({'DATE': forecast_dates, 'Forecasted_Average_Price': forecast_values})
forecast.set_index('DATE', inplace=True)

# Veriyi gözden geçirme
print(data.head())

# 'DATE' sütununu tarih formatına dönüştürme
data['DATE'] = pd.to_datetime(data['DATE'])

# 'APU0000702421' sütununu ortalama fiyat olarak adlandırma
data.rename(columns={'APU0000702421': 'Average_Price'}, inplace=True)

# Tarih sütununu indeks olarak ayarlama
data.set_index('DATE', inplace=True)

# 30 günlük hareketli ortalama hesaplama
data['30_Day_MA'] = data['Average_Price'].rolling(window=30).mean()

# Veriyi görselleştirme
plt.figure(figsize=(12, 6))
plt.plot(data['Average_Price'], label='Ortalama Fiyat')
plt.plot(data['30_Day_MA'], label='30 Günlük Hareketli Ortalama')
plt.title('Nestle Ortalama Fiyat ve 30 Günlük Hareketli Ortalama')
plt.xlabel('Tarih')
plt.ylabel('Fiyat')
plt.legend()
plt.show()

import pandas as pd

# Veri setini oluşturma
data = {
    'DATE': ['1.01.1997', '1.01.1998', '1.01.1999', '1.01.2000', '1.01.2001', '1.01.2002', '1.01.2003', '1.01.2004', '1.01.2005', '1.01.2006', '1.01.2007', '1.01.2008', '1.01.2009', '1.01.2010', '1.01.2011', '1.01.2012', '1.01.2013', '1.01.2014', '1.01.2015', '1.01.2016', '1.01.2017', '1.01.2018', '1.01.2019', '1.01.2020', '1.01.2021', '1.01.2022'],
    'Stock_Price': [10, 15, 18, 16, 21, 21, 20, 26, 26, 29, 36, 44, 34, 47, 54, 57, 70, 72, 76, 73, 73, 86, 87, 110, 112, 129],
    'Average_Price': ['2553,00', '2502,00', '45414,00', '2607,00', '2388,00', '2491,00', '2774,00', '2679,00', '2677,00', '2764,00', '2868,00', '2642,00', '3114,00', '42430,00', '3298,00', '3561,00', '3728,00', '3279,00', '3428,00', '16862,00', '3397,00', '3681,00', '3466,00', '3525,00', '3669,00', '4223,00'],
    'Cpi': ['2337689937,00', '1552279099,00', '2188027197,00', '3376857271,00', '2826171119,00', '1586031627,00', '2270094973,00', '2677236693,00', '3392746845,00', '3225944101,00', '2852672482,00', '3839100297,00', '-0.3555462663', '1640043442,00', '3156841569,00', '2069337265,00', '1464832656,00', '1622222977,00', '0.1186271356', '1261583206,00', '2130110004,00', '2442583297,00', '1812210078,00', '1233584396,00', '469785886,00', '8002799821,00']
}

# Veri setini DataFrame'e dönüştürme
df = pd.DataFrame(data)

# Ondalık sayıları düzenleme
df['Average_Price'] = df['Average_Price'].str.replace(',', '.').astype(float)
df['Cpi'] = df['Cpi'].str.replace(',', '.').astype(float)

# Bağımsız değişkenler (X) ve bağımlı değişken (y) belirleme
X = df[['Average_Price']]  # Bağımsız değişkenler
y = df['Stock_Price']  # Bağımlı değişken

# Modeli oluşturma
model = sm.OLS(y, sm.add_constant(X)).fit()

# Model özetini yazdırma
print(model.summary())

import pandas as pd
import statsmodels.api as sm

# Veri setini oluşturma
data = {
    'DATE': ['1.01.1997', '1.01.1998', '1.01.1999', '1.01.2000', '1.01.2001', '1.01.2002', '1.01.2003', '1.01.2004', '1.01.2005', '1.01.2006', '1.01.2007', '1.01.2008', '1.01.2009', '1.01.2010', '1.01.2011', '1.01.2012', '1.01.2013', '1.01.2014', '1.01.2015', '1.01.2016', '1.01.2017', '1.01.2018', '1.01.2019', '1.01.2020', '1.01.2021', '1.01.2022'],
    'Stock_Price': [10, 15, 18, 16, 21, 21, 20, 26, 26, 29, 36, 44, 34, 47, 54, 57, 70, 72, 76, 73, 73, 86, 87, 110, 112, 129],
    'Average_Price': ['2553,00', '2502,00', '45414,00', '2607,00', '2388,00', '2491,00', '2774,00', '2679,00', '2677,00', '2764,00', '2868,00', '2642,00', '3114,00', '42430,00', '3298,00', '3561,00', '3728,00', '3279,00', '3428,00', '16862,00', '3397,00', '3681,00', '3466,00', '3525,00', '3669,00', '4223,00'],
    'Cpi': ['2337689937,00', '1552279099,00', '2188027197,00', '3376857271,00', '2826171119,00', '1586031627,00', '2270094973,00', '2677236693,00', '3392746845,00', '3225944101,00', '2852672482,00', '3839100297,00', '-0.3555462663', '1640043442,00', '3156841569,00', '2069337265,00', '1464832656,00', '1622222977,00', '0.1186271356', '1261583206,00', '2130110004,00', '2442583297,00', '1812210078,00', '1233584396,00', '469785886,00', '8002799821,00']
}

# Veri setini DataFrame'e dönüştürme
df = pd.DataFrame(data)

# Ondalık sayıları düzenleme
df['Average_Price'] = df['Average_Price'].str.replace(',', '.').astype(float)
df['Cpi'] = df['Cpi'].str.replace(',', '.').astype(float)

# Bağımsız değişkenler (X) ve bağımlı değişken (y) belirleme
X = df[['Average_Price']]  # Bağımsız değişkenler
y = df['Stock_Price']  # Bağımlı değişken

# Modeli oluşturma
model = sm.OLS(y, sm.add_constant(X)).fit()

# Model özetini yazdırma
print(model.summary())

# Bağımsız değişkenler (X) ve bağımlı değişken (y) belirleme (reduced model için)
X_reduced = df[['NestleAveragePrice']]  # Sadece sabit terim
y_reduced = df['Stock_Price']  # Bağımlı değişken

# Reduced modeli oluşturma
reduced_model = sm.OLS(y_reduced, X_reduced).fit()

# Reduced model özetini yazdırma
print(reduced_model.summary())

import statsmodels.api as sm

# Define the independent variable (X) and the dependent variable (y)
X = df['Stock_Price']  # Independent variable
y = df['Average_Price']  # Dependent variable

# Add a constant to the independent variables matrix (for the intercept)
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print the regression results
print(model.summary())

import statsmodels.api as sm

# Define the independent variable (X) - Only constant term (intercept)
X_reduced = sm.add_constant(df['Stock_Price'])

# Fit the reduced model
model_reduced = sm.OLS(df['Average_Price'], X_reduced).fit()

# Print the summary of the reduced model
print(model_reduced.summary())

import matplotlib.pyplot as plt

# Plotting the observed values and the predicted values
plt.figure(figsize=(10, 6))
plt.scatter(df['Stock_Price'], df['Average_Price'], color='blue', label='Observed')
plt.plot(df['Stock_Price'], model_reduced.predict(X_reduced), color='red', linewidth=2, label='Predicted')
plt.xlabel('Stock Price')
plt.ylabel('Average Price')
plt.title('Observed vs Predicted')
plt.legend()
plt.grid(True)
plt.show()

import pandas as pd
import statsmodels.api as sm

# Load the dataset
df = pd.read_csv('mergedata.csv')

# Define the dependent and independent variables
X = df['Stock_Price']  # Independent variable
y = df['Average_Price']  # Dependent variable

# Add a constant term to the independent variable
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print the summary of the model
print(model.summary())

import statsmodels.api as sm

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print the ANOVA table
print(model.summary())

import pandas as pd

# Veri setini yükle
df = pd.read_csv('mergedata.csv')

# Korelasyon matrisini oluştur
correlation_matrix = df.corr()

# Korelasyon matrisini göster
print(correlation_matrix)

import pandas as pd
import statsmodels.api as sm

# Veri setini yükle
df = pd.read_csv('mergedata.csv')

# Bağımsız değişkenleri seçme
X = df[['Time_Index', 'Nestle_Stock_Price', 'Covid_19', '2008_Crisis', '9_11_Attacks']]

# Sabit (intercept) ekleyin
X = sm.add_constant(X)

# Bağımlı değişkeni seçme
y = df['Average_Price']

# Modeli oluşturma
model = sm.OLS(y, X).fit()

# Model özetini yazdırma
print(model.summary())

import pandas as pd

# Veri setini yükleyin
df = pd.read_csv('mergedata.csv')

# Veri setinin ilk birkaç satırını görüntüleyin
print(df.head())

import pandas as pd
import statsmodels.api as sm

# Veri setini yükleyin
df = pd.read_csv('mergedata.csv')

# Bağımsız değişkenler (X) ve bağımlı değişken (y) belirleme
X = df[['Average_Price']]  # Bağımsız değişkenler
y = df['Stock_Price']  # Bağımlı değişken

# Sabiti (intercept) ve bağımsız değişkenleri bir araya getirme
X = sm.add_constant(X)

# Modeli oluşturma
model = sm.OLS(y, X).fit()

# Modelin özetini yazdırma
print(model.summary())

print(df.columns)

import pandas as pd
import statsmodels.api as sm

# Veri setini yükleyin
df = pd.read_csv('mergedata.csv')

# Sütunları ayırarak veri setini düzenleyin
df[['DATE', 'Stock_Price', 'Average_Price', 'Cpi']] = df['DATE;Stock_Price;Average_Price;Cpi'].str.split(';', expand=True)

# Bağımsız değişkenler (X) ve bağımlı değişken (y) belirleme
X = df[['Average_Price']].astype(float)  # Bağımsız değişkenler (float veri tipine dönüştür)
y = df['Stock_Price'].astype(float)  # Bağımlı değişken (float veri tipine dönüştür)

# Sabiti (intercept) ve bağımsız değişkenleri bir araya getirme
X = sm.add_constant(X)

# Modeli oluşturma
model = sm.OLS(y, X).fit()

# Modelin özetini yazdırma
print(model.summary())

# Veri setinin sütun veri tiplerini kontrol edin
print(df.dtypes)

# Sütunları uygun şekilde dönüştürün
df[['DATE', 'Stock_Price', 'Average_Price', 'Cpi']] = df['DATE;Stock_Price;Average_Price;Cpi'].str.split(';', expand=True)

# Bağımsız değişkenler (X) ve bağımlı değişken (y) belirleme
X = df[['Average_Price']].astype(float)  # Bağımsız değişkenler (float veri tipine dönüştür)
y = df['Stock_Price'].astype(float)  # Bağımlı değişken (float veri tipine dönüştür)

# Sütunları uygun şekilde ayırma
df[['DATE', 'Stock_Price', 'Average_Price', 'Cpi']] = df['DATE;Stock_Price;Average_Price;Cpi'].str.split(';', expand=True)

# Bağımsız değişkenler (X) ve bağımlı değişken (y) belirleme
X = df[['Average_Price']].astype(float)  # Bağımsız değişkenler (float veri tipine dönüştür)
y = df['Stock_Price'].astype(float)  # Bağımlı değişken (float veri tipine dönüştür)