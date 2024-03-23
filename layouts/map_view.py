from kivy.clock import Clock
from kivy_garden.mapview import MapView
from kivy_garden.mapview import MapMarkerPopup


class MapViewPub(MapView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # print('inside MAP __init__')
        for i in range(0, 7):
            new_take = (1 / (1 + i))
            new_lat = 51.5 + new_take
            new_lon = 0 - new_take
            # print(new_lat, new_lon)
            marker = MapMarkerPopup(lat=new_lat, lon=new_lon)
            self.add_widget(marker)

    get_map_timer = None

    def start_getting_pubs_in_map(self):
        try:
            self.get_map_timer.cancel()
        except:
            pass
        self.get_map_timer = Clock.schedule_once(self.get_pub_list, 1)

    def get_pub_list(self, *args):
        print(self.get_bbox())
