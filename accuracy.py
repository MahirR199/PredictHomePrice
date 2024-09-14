import numpy as np

# Assuming y_test is your actual house prices and you've already calculated RMSE
rmse = 49291.20483895212  # Your RMSE value
mean_actual = np.mean(y_test)  # Mean of actual house prices in the test set

# Calculate percentage error
percentage_error = (rmse / mean_actual) * 100

# Calculate accuracy
accuracy = 100 - percentage_error
accuracy
