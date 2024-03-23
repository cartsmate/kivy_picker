from modules.multi_threading import MultiThreadingPub


class GetData:

    def get_data(self, sql):
        df_dict = MultiThreadingPub().thread_caller(sql)
        # df_daily_event = df_dict['df_daily_event']
        df_pub_record = df_dict['df_pub_record']
        table_data = []
        for index, row in df_pub_record.iterrows():
            table_data.append((f"{index}", row['detail_name'], row['ranking'], row['station_name']))

        print(table_data)
        return table_data

    def get_data_filter(self, filter_list):
        filter_str = ''
        filters = ['entertain', 'favourite', 'garden', 'music', 'quiz', 'roast', 'sport']
        for fills in filters:
            if fills in filter_list:
                filter_str += f' and {fills} = true'
            else:
                filter_str += f' and {fills} = false'
        sql = f"""select * from thepubpicker.pub_record d where ranking >= 0 and ranking <= 5 {filter_str}
        order by ranking desc limit 10"""
        table_data = self.get_data(sql)
        return table_data


    def get_data_filtered(self):
        sql = f"""select * from thepubpicker.pub_record d where ranking > 3 and ranking < 5 
        order by ranking desc limit 10"""
        table_data = self.get_data(sql)
        return table_data

    def get_data_all(self):
        sql = f"""select * from thepubpicker.pub_record d where ranking > 3 and ranking < 5 
        order by ranking desc limit 10"""
        table_data = self.get_data(sql)
        return table_data

    def get_data_entertain(self):
        sql = f"""select * from thepubpicker.pub_record d where ranking > 3 and ranking < 5 and entertain = true 
        order by ranking desc limit 10"""
        table_data = self.get_data(sql)
        return table_data

    def get_data_favourite(self):
        sql = f"""select * from thepubpicker.pub_record d where ranking > 3 and ranking < 5 and favourite = true 
        order by ranking desc limit 10"""
        table_data = self.get_data(sql)
        return table_data

    def get_data_garden(self):
        sql = f"""select * from thepubpicker.pub_record d where ranking > 3 and ranking < 5 and garden = true 
        order by ranking desc limit 10"""
        table_data = self.get_data(sql)
        return table_data

    def get_data_music(self):
        sql = f"""select * from thepubpicker.pub_record d where ranking > 3 and ranking < 5 and music = true 
        order by ranking desc limit 10"""
        table_data = self.get_data(sql)
        return table_data

    def get_data_quiz(self):
        sql = f"""select * from thepubpicker.pub_record d where ranking > 3 and ranking < 5 and quiz = true 
        order by ranking desc limit 10"""
        table_data = self.get_data(sql)
        return table_data

    def get_data_roast(self):
        sql = f"""select * from thepubpicker.pub_record d where ranking > 3 and ranking < 5 and roast = true 
        order by ranking desc limit 10"""
        table_data = self.get_data(sql)
        return table_data

    def get_data_sport(self):
        sql = f"""select * from thepubpicker.pub_record d where ranking > 3 and ranking < 5 and sport = true 
        order by ranking desc limit 10"""
        table_data = self.get_data(sql)
        return table_data


