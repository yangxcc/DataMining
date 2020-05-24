from test_pandas import read_data
from process_stationarity import data_log,data_diff,data_decompose,data_final
import test_stationarity
from arima_model import arima_model
from test_arima import diff_ts,predict_diff_recover
import numpy as np
import matplotlib.pylab as plt
import pandas as pd
from roll_predict import add_today_data,forecast_next_day_data

if __name__ == '__main__':

    ts = read_data()
    #data_final(ts)

    ts_log = data_log(ts)

    diffed_ts = diff_ts(ts_log,d=[12,1])
    model = arima_model(diffed_ts)
    # model.certain_model(1,1)
    model.certain_model(1,1)
    predict_ts = model.properModel.predict()
    diff_recover_ts = predict_diff_recover(predict_ts,d=[12,1])
    log_recover = np.exp(diff_recover_ts)
    ts = ts[log_recover.index]
    plt.figure(facecolor='white')
    log_recover.plot(color='blue', label='Predict')
    ts.plot(color='red', label='Original')
    # plt.legend(loc=1)
    plt.legend(loc=2)
    plt.title('Time series analysis and fitting of pacifier sales volume')
    plt.xlabel("Date")
    plt.ylabel("Sales amount")
    # plt.title('RMSE: %.4f' % np.sqrt(sum((log_recover - ts) ** 2) / ts.size))
    print('RMSE: %.4f' % np.sqrt(sum((log_recover - ts) ** 2) / ts.size))
    plt.show()


    '''
    ts_train = ts_log[:'1956-12']
    ts_test = ts_log['1957-1':]
    diffed_ts = diff_ts(ts_train, [12, 1])
    forecast_list = []
    for i, dta in enumerate(ts_test):
        if i % 7 == 0:
            model = arima_model(diffed_ts)
            model.certain_model(1, 1)
        forecast_data = forecast_next_day_data(model, type='month')
        forecast_list.append(forecast_data)
        add_today_data(model, ts_train, dta, [12, 1], type='month')

    predict_ts = pd.Series(data=forecast_list, index=ts['1957-1':].index)
    log_recover = np.exp(predict_ts)
    original_ts = ts['1957-1':]

    plt.figure(facecolor='white')
    log_recover.plot(color='blue', label='Predict')
    original_ts.plot(color='red', label='Original')
    plt.legend(loc='best')
    plt.title('RMSE: %.4f' % np.sqrt(sum((log_recover - original_ts) ** 2) / ts.size))
    plt.show()
    '''