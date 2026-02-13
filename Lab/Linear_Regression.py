import numpy as np

class LinearRegression:
    def __init__(self, X, Y):
        self.n = X.shape[0]
        self.d = X.shape[1]

        self.Y = Y.reshape(-1, 1)

        ones = np.ones((self.n, 1))
        self.X = np.hstack((ones, X))

        self.beta = None
        self.sse = None

    def fit(self):
        X_transposed = self.X.T
        X_transposed_X = X_transposed @ self.X
        X_transposed_X_inverse = np.linalg.inv(X_transposed_X)
        X_transposed_Y = X_transposed @ self.Y

        self.beta = X_transposed_X_inverse @ X_transposed_Y

        self.calculate_sse()

    def calculate_sse(self):
        residuals = self.Y - self.X @ self.beta
        self.sse = (residuals.T @ residuals)[0, 0]

    def variance(self):
        return self.sse / (self.n - self.d - 1)
    
    def standard_deviation(self):
        return np.sqrt(self.variance())
    
    def rmse(self):
        mse = self.sse / self.n
        return np.sqrt(mse)