def initialize_params():
    #w1 = random.gauss(mu=0, sigma=0.01)
    #w2 = random.gauss(mu=0, sigma=0.01)
    #w3 = random.gauss(mu=0, sigma=0.01)
    #b = random.gauss(mu=0, sigma=0.01)
    w1, w2, w3, b = (0.016992259082509283, 0.0070783670518262355, -0.002307860847821344 , 0)
    return w1, w2, w3, b

def predict(x1, x2, x3, w1, w2, w3, b):
    return x1 * w1 + x2 * w2 + x3 * w3 + b

def compute_loss_mse(y, y_hat):
    return (y - y_hat) ** 2

def compute_loss_mae(y, y_hat):
    return abs(y - y_hat)

def compute_gradient_wi(xi, y, y_hat):
    dl_dwi = 2 * xi * (y_hat - y)
    return dl_dwi

def compute_gradient_b(y, y_hat):
    dl_db = 2 * (y_hat - y)
    return dl_db

def update_weight_wi(wi, dl_dwi, lr):
    wi = wi - lr * dl_dwi
    return wi

def update_weight_b(b, dl_db, lr):    
    b  = b - lr*dl_db    
    return b

def implement_linear_regression(X_data, y_data, epochs_max = 50, lr = 1e-5):
    losses = []

    w1, w2, w3, b = initialize_params()
    
    N = len(y_data)
    for _ in range(epochs_max):
        for i in range(N):
            x1 = X_data[0][i]
            x2 = X_data[1][i]
            x3 = X_data[2][i]
            
            y = y_data[i]

            y_hat = predict(x1, x2, x3, w1, w2, w3, b)

            loss = compute_loss_mse(y, y_hat)

            dl_dw1 = compute_gradient_wi(x1, y, y_hat)
            dl_dw2 = compute_gradient_wi(x2, y, y_hat)
            dl_dw3 = compute_gradient_wi(x3, y, y_hat)
            dl_db = compute_gradient_b(y, y_hat)

            w1 = update_weight_wi(w1, dl_dw1, lr)
            w2 = update_weight_wi(w2, dl_dw2, lr)
            w3 = update_weight_wi(w3, dl_dw3, lr)
            b = update_weight_wi(b, dl_db, lr)

            losses.append(loss)

    return (w1, w2, w3, b, losses)


def implement_linear_regression_nsamples(X_data, y_data, epoch_max = 50,lr = 1e-5):
    losses = []

    w1, w2, w3, b = initialize_params()
    N = len(y_data)

    for _ in range(epoch_max):

        loss_total = 0.0
        dw1_total = 0.0
        dw2_total = 0.0
        dw3_total = 0.0
        db_total  = 0.0

        for i in range(N):
            # get a sample
            x1 = X_data[0][i]
            x2 = X_data[1][i]
            x3 = X_data[2][i]

            y  = y_data[i]

            # print(y)
            # compute output 
            y_hat = predict(x1, x2, x3, w1, w2, w3, b)
            
            # compute loss
            loss = compute_loss_mse(y, y_hat)
            loss_total = loss_total + loss

            # compute gradient w1, w2, w3, b
            dl_dw1 = compute_gradient_wi(x1, y, y_hat)
            dl_dw2 = compute_gradient_wi(x2, y, y_hat)
            dl_dw3 = compute_gradient_wi(x3, y, y_hat)
            dl_db  = compute_gradient_b(y, y_hat)

            # accumulate
            dw1_total = dw1_total + dl_dw1
            dw2_total = dw2_total + dl_dw2
            dw3_total = dw3_total + dl_dw3
            db_total = db_total + dl_db

        # (after processing N samples) - update parameters
        w1 = update_weight_wi(w1, dw1_total/N, lr)
        w2 = update_weight_wi(w2, dw2_total/N, lr)
        w3 = update_weight_wi(w3, dw3_total/N, lr)
        b  = update_weight_b(b, db_total/N, lr)


        # logging
        losses.append(loss_total/N) 
    return (w1,w2,w3,b, losses)