from ride import Ride, RideMatching, RideRequest, RideSharing
from users import Rider, Driver
from vehicle import Bike, Car 

niye_jao = RideSharing('Niye Jao')
rakib = Rider('Rakib Khan', 'rakib@gmail.com', 1255, 'Mohakhali', 1200)
niye_jao.add_rider(rakib)
kolimuddin = Driver('Kolim Uddin', 'kolim@gmail.com', 1445, 'Gulshan')
niye_jao.add_driver(kolimuddin)
rakib.request_ride(niye_jao, 'Uttara', 'car')
# rakib.show_current_ride()
kolimuddin.reach_destination(rakib.current_ride)
rakib.show_current_ride()
# print(niye_jao) 