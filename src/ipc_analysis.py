import pandas as pd
import matplotlib.pyplot as plt

class IPCAnalysis:
    def __init__(self, data):
        self.data = data

    def extract_ipc_codes(self):
        b510_codes = self.data['ipc'].str.extract(r'(B510|B510EP)')
        return b510_codes.dropna()

    def classification_statistics(self):
        ipc_counts = self.data['ipc'].value_counts()
        return ipc_counts

    def top_n_technical_fields(self, n=5):
        top_fields = self.data['technical_field'].value_counts().head(n)
        return top_fields

    def time_distribution_analysis(self):
        self.data['application_date'] = pd.to_datetime(self.data['application_date'])
        time_distribution = self.data['application_date'].dt.year.value_counts().sort_index()
        return time_distribution

# Example usage:
# data = pd.read_csv('patent_data.csv')
# analysis = IPCAnalysis(data)
# b510_codes = analysis.extract_ipc_codes()
# stats = analysis.classification_statistics()
# top_fields = analysis.top_n_technical_fields(n=5)
# time_dist = analysis.time_distribution_analysis()  

