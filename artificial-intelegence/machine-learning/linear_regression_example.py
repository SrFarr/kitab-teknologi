# Import library yang diperlukan
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data contoh: Jam belajar (input) dan Nilai (output)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Jam belajar
y = np.array([2, 4, 5, 4, 5])  # Nilai

# Membuat model Linear Regression
model = LinearRegression()
model.fit(X, y)  # Melatih model dengan data

# Memprediksi nilai untuk jam belajar baru
X_new = np.array([6]).reshape(-1, 1)  # Jam belajar baru
y_pred = model.predict(X_new)  # Prediksi nilai

# Menampilkan hasil prediksi
print(f"Prediksi nilai untuk {X_new[0][0]} jam belajar: {y_pred[0]:.2f}")

# Visualisasi data dan garis regresi
plt.scatter(X, y, color='blue', label='Data Asli')
plt.plot(X, model.predict(X), color='red', label='Garis Regresi')
plt.scatter(X_new, y_pred, color='green', label='Prediksi')
plt.xlabel('Jam Belajar')
plt.ylabel('Nilai')
plt.title('Linear Regression: Jam Belajar vs Nilai')
plt.legend()
plt.show()