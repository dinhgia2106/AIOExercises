from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the diabetes dataset
iris_X, iris_y = datasets.load_iris(return_X_y=True)


# Split train:test = 8:2
X_train, X_test, y_train, y_test = train_test_split(
    iris_X,
    iris_y,
    test_size=0.2,
    random_state=42
)

'''train_test_split: Chia dữ liệu thành 80% để huấn luyện và 20% để kiểm thử.
test_size=0.2: 20% của dữ liệu được dành cho kiểm thử.
random_state=42: Giữ nguyên hạt giống ngẫu nhiên để tái tạo được kết quả tương tự khi chạy lại.'''

# Scale the features using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

'''StandardScaler(): Tạo một đối tượng chuẩn hóa dữ liệu.
fit_transform(X_train): Áp dụng quá trình chuẩn hóa lên tập huấn luyện (tính toán và áp dụng).
transform(X_test): Áp dụng quá trình chuẩn hóa lên tập kiểm thử (chỉ áp dụng mà không tính toán lại).'''

# Build KNN Classifier
knn_classifier = KNeighborsClassifier(n_neighbors=5)
knn_classifier.fit(X_train, y_train)

# Predict and Evaluate test set
y_predict = knn_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_predict)

print(accuracy)
