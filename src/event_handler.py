import pandas as pd

class EventHandler:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.events_df = None

    def load_events(self):
        try:
            self.events_df = pd.read_csv(self.filepath)
            self.events_df['start_date'] = pd.to_datetime(self.events_df['start_date'])
            return self.events_df
        except Exception as e:
            print("Event file not loaded: ", e)

    def get_events_between(self, start_date, end_date):
        return self.events_df[
            (self.events_df['start_date'] >= pd.to_datetime(start_date)) &
            (self.events_df['start_date'] <= pd.to_datetime(end_date))
        ]
