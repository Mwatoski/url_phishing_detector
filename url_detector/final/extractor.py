import pandas as pd
from . import rf_model

class feature_extractor:
    def __init__(self, url:str):
        self.input_url = url
    
    def long_url(self, l): 
        l = str(l)
        if len(l) < 54:
            return 0
        elif len(l) >= 54 and len(l) < 75:    
            return 1
        return 2


    def at_symbol(self, l):
        if '@' in  str(l):
            return 1
        return 0

    def redirecting_symbol(self, l):
        if '//' in str(l):
            return 1
        return 0

    def prefix_symbol(self, l):
        if '-' in str(l):
            return 1
        return 0


    def domain_symbol(self, l):
        l = str(l)
        if l.count('.') > 3:
            return 2
        elif '.' == 3:
            return 1
        return 0

    def protocal(self, l):
        if 's' in str(l):
            return 0
        return 1
    
    def dash(self, l):
        if '-' in str(l):
            return 1
        return 0

    def extractor(self):
        input_data = [{"URL": self.input_url}]
        input_df = pd.DataFrame(input_data)
        seperation_protocal = input_df['URL'].str.split('//', expand = True)
        seperation_domain_name = seperation_protocal[1].str.split('/', 1, expand = True)
        splited_data = pd.concat([seperation_protocal[0],seperation_domain_name],axis=1)
        # splited_data
        splited_data.columns=["protocal", "Domain_name", "Address"]
        splited_data['long_url'] = input_df['URL'].apply(self.long_url)
        splited_data['at_symbol'] = input_df['URL'].apply(self.at_symbol)
        splited_data['redirecting'] = seperation_protocal[1].apply(self.redirecting_symbol)
        splited_data['prefix_suffix'] = splited_data['Domain_name'].apply(self.prefix_symbol)
        splited_data['domain_sub_domain']= splited_data['Domain_name'].apply(self.domain_symbol)
        splited_data['check_protocal'] = splited_data['protocal'].apply(self.protocal)
        splited_data['check_dash'] = splited_data['Domain_name'].apply(self.dash)

        return (splited_data)