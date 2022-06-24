class BMI:
    # docstring for BMI.
    def __init__(self, height, weight):
        self.height = input()
        self.weight = input()
        self.value = self.weight / (self.height**2)
        # if not (10 <= self.value <= 40):
        #     raise ValueError("BMIが正常値の範囲を超えています")


        

    def __str__(self):
        return f"{self.value:.2f}"

    def calculate_bmi(self):
        #Inputをインスタンスするところに外から入る数値を定義する
        # BMI = 体重÷身長の2乗
        return self.weight / (self.height**2)
        
#↓下のところが非常にポイント！！

# tanaka_bmi = BMI(height=1.80, weight=67.0)
# sasami_bmi = BMI(height=1.58, weight=80.0)

# print(tanaka_bmi.height)
# print(tanaka_bmi.value)
# print(tanaka_bmi)

print(self.value())