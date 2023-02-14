import datetime


class Row:

    def __init__(self, items):
        self.items = items
        self.format()

    def format(self):
        return self.items


class PodrozeRow(Row):

    def __init__(self, items):
        super().__init__(items)

    def format(self):
        self.items['Data_rozpoczecia'] = self._get_date(self.items['Data_rozpoczecia'])
        self.items['Data_zakonczenia'] = self._get_date(self.items['Data_zakonczenia'])
        if self.items['Data_rozpoczecia'] > self.items['Data_zakonczenia']:
            self.items['Data_rozpoczecia'], self.items['Data_zakonczenia'] = self.items['Data_zakonczenia'], self.items['Data_rozpoczecia'] 

    def _get_date(self, formated_date, split_char='/'):
        vals = formated_date.split(split_char)
        return datetime.date(int(vals[2]), int(vals[0]), int(vals[1]))