import tkinter as tk
from kiosk_program import frame1, frame2, frame3, frame4, frame5
from kiosk_program import meal_add, drink_add

# 식사
btn_meal_1 = tk.Button(frame2, text="김밥\n(3000원)", padx="10", pady="10", width="10", command=lambda:meal_add('김밥'))
btn_meal_1.grid(row=0, column=0, padx=10, pady=10)

btn_meal_2 = tk.Button(frame2, text="라면\n(3500원)", padx="10", pady="10", width="10", command=lambda:meal_add('라면'))
btn_meal_2.grid(row=0, column=1, padx=10, pady=10)

btn_meal_3 = tk.Button(frame2, text="떡볶이\n(4000원)", padx="10", pady="10", width="10", command=lambda:meal_add('떡볶이'))
btn_meal_3.grid(row=0, column=2, padx=10, pady=10)

btn_meal_4 = tk.Button(frame2, text="튀김\n(5000원)", padx="10", pady="10", width="10", command=lambda:meal_add('튀김'))
btn_meal_4.grid(row=0, column=3, padx=10, pady=10)

btn_meal_5 = tk.Button(frame2, text="쫄면\n(7000원)", padx="10", pady="10", width="10", command=lambda:meal_add('쫄면'))
btn_meal_5.grid(row=0, column=4, padx=10, pady=10)



# 음료
btn_drink_1 = tk.Button(frame3, text="아메리카노\n(3000원)", padx="10", pady="10", width="10", command=lambda:drink_add('아메리카노'))
btn_drink_1.grid(row=0, column=0, padx=10, pady=10)

btn_drink_1 = tk.Button(frame3, text="라떼\n(3500원)", padx="10", pady="10", width="10", command=lambda:drink_add('라떼'))
btn_drink_1.grid(row=0, column=1, padx=10, pady=10)

btn_drink_1 = tk.Button(frame3, text="아이스티\n(4000원)", padx="10", pady="10", width="10", command=lambda:drink_add('아이스티'))
btn_drink_1.grid(row=0, column=2, padx=10, pady=10)

btn_drink_1 = tk.Button(frame3, text="에이드\n(4500원)", padx="10", pady="10", width="10", command=lambda:drink_add('에이드'))
btn_drink_1.grid(row=0, column=3, padx=10, pady=10)

btn_drink_1 = tk.Button(frame3, text="스무디\n(5000원)", padx="10", pady="10", width="10", command=lambda:drink_add('스무디'))
btn_drink_1.grid(row=0, column=4, padx=10, pady=10)