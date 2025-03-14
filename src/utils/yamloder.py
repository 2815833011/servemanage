import yaml
class Yamloader:
    def loder(self,filpath=r"data\test_login_param.yaml"):
        '''
            加载yaml文件
        '''
        with open(file=filpath,mode="r",encoding="utf-8") as file:
           result= yaml.load(stream=file.read(),Loader=yaml.FullLoader)
        return result
           

if __name__=="__main__":   
   resutl= Yamloader().loder(filpath=r"data\test_login_param.yaml")   
   print(resutl["test_login"][0])