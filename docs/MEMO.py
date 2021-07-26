# oneline Zip to DataFrame
zip_path = tf.keras.utils.get_file(...)
csv_path, _ = os.path.splitext(zip_path)
df = pd.read_csv(csv_path)

# 데이터프레임 서브플롯
pd.DataFrame.plot(subplots=True)

# 그래프의 주요 빈도 특성(주기, cycle) 찾기
""" 모델이 가장 중요한 빈도 특성을 모르는 경우 `fft`를 사용하여 중요한 빈도를 
결정할 수 있습니다. 시간에 따른 온도의 `tf.signal.rfft`를 보면 여기서 가정한 
내용이 확인됩니다. `1/year` 및 `1/day` 근처에서 빈도 피크가 확실하다는 것을 
알 수 있습니다. """
tf.signal.rfft(pd.Series)