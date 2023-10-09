import dataflowutil.libs.load_processing as dp

class LoadDB(dp.DataProcessing):
    def __init__(self,connection,path_bucket,upload_data,list_data,list_data_compare,reduce_memory=False):
        super().__init__(connection,path_bucket,upload_data)
        self.load_data(list_data,list_data_compare,reduce_memory)


    
