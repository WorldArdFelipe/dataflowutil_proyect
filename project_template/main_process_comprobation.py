import dataflowutil.libs.app_struct as app
import dataflowutil.config.extra_var as extra_v
import data as db
    
extra_v.CONNECTION_VAR = 1 # 0 = PRODUCTION / 1 = TESTING
extra_v.ACTIVATE_DATA_LOCAL = 1 # 0 False / 1 = True

class App(app.AppStruct):
    def __init__(self):
        super().__init__()
        self.load_data(db,reduce_memory=False) # Reduce =  True no is necessary function upload_load_data()

x = App()
x.start_check_historic()