# # import 문에서는 바로 클래스는 못 불러온다.
# import package.package_travel_1
# trip_to = package.package_travel_1.ThailandPackage()
# trip_to.detail()


# # from import 문에서는 바로 클래스를 불러올 수 있다.
# from package.package_travel_1 import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()


# from package import package_travel_2
# trip_to = package_travel_2.VietnamPackage()
# trip_to.detail()


from package import *
# # trip_to = package_travel_2.VietnamPackage()
# trip_to = package_travel_1.ThailandPackage()
# trip_to.detail()


import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(package_travel_1))