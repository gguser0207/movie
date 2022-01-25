from django.db import models
import os
from tensorflow.keras.models import load_model
import numpy as np

class Recommend_movie: # 도서 추천
    def proc(self, data):
        print('data:', data)
        data = np.array(data.split(','), dtype=int)
        print('변환된 data:', data)
        X = []
        for i in range(0, 5):  # 평가 횟수 5번, 0 ~ 4
            for j in range(1, 6):  # 평가 항목수 5개
                # print(i, j)
                # 선택한 번호화 같은 경우만 1을 할당
                # 사용자가 입력한 1은 배열 index 0에 해당함.
                if (data[i] == j):  # 1 == 1
                    X.append(1)  # 1
                else:
                    X.append(0)  # 0,0

        print(X)
        x_data = np.array([
            X,
        ])
        print(x_data)


        path = os.path.dirname(os.path.abspath(__file__))
        print('path:', path);

        model = load_model(os.path.join(path, 'movie5.h5'))

        p = model.predict(x_data)
        print(p)
        index = np.argmax(p[0])

        return index