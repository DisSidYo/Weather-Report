class WeatherDatabase:

    def __init__(self, filename):
        self.filename=filename
        
        

    def get_observation(self, date):
        file1 = open(self.filename, 'r')
        lines = file1.readlines()
        c=0;
        for line in lines:
            line_s = line.strip().split()
            if date == line_s[0]:
                c=int(line_s[1])
                return c
        return None
       

    



            



    def get_average_temp(self):
        file1 = open(self.filename, 'r')
        lines = file1.readlines()
        c=0; 
        n=0;
        avg = 0;
        for line in lines:
            line_s = line.strip().split()
            c+=int(line_s[1])
            n+=1
        return c/n
            
        

    def get_min_temp(self):
        file1 = open(self.filename, 'r')
        lines = file1.readlines()
        c=0; 
        for line in lines:
            line_s = line.strip().split()
            n=int(line_s[1])
            break;
        
       
        for line in lines:
            line_s = line.strip().split()
            c=int(line_s[1])
            if c<=n:
                n=c
        return n


        

    def get_max_temp(self):
        file1 = open(self.filename, 'r')
        lines = file1.readlines()
        c=0; 
        for line in lines:
            line_s = line.strip().split()
            mx_temp=int(line_s[1])
            break;
        
       
        for line in lines:
            line_s = line.strip().split()
            c=int(line_s[1])
            if c>=mx_temp:
                mx_temp=c
        return mx_temp

    def get_coldest_days(self):
        file1 = open(self.filename, 'r')
        lines = file1.readlines()
        c=0; d=0; l=[]
        for line in lines:
            line_s = line.strip().split()
            n=int(line_s[1])
            break;
        
       
        for line in lines:
            line_s = line.strip().split()
            c=int(line_s[1])
            if c<=n:
                n=c
        
        for line in lines:
            line_s = line.strip().split()
            if int(line_s[1]) == n:
                l.append(line_s[0])
           
        return l
            
        
        

    def get_hottest_days(self):
        file1 = open(self.filename, 'r')
        lines = sorted(file1.readlines())

        c=0; d=0; l=[]
        for line in lines:
            line_s = line.strip().split()
            n=int(line_s[1])
            break;
        
       
        for line in lines:
            line_s = line.strip().split()
            c=int(line_s[1])
            if c>=n:
                n=c
        
        for line in lines:
            line_s = line.strip().split()
            if int(line_s[1]) == n:
                l.append(line_s[0])
           
        return l
            

    def histogram(self):
        file1 = open(self.filename, 'r')
        lines = sorted(file1.readlines())
        l_str = "" 
        st = ""
        for line in lines:
            line_s = line.strip().split()
            l_str += line_s[0] + " "
            c=int(line_s[1])
            for d in range(0, c):
                st += "*"
            l_str += st + "\n"
            st=""
            
        return l_str


    def report(self):
        obj=WeatherDatabase(self.filename)
        file1 = open(self.filename, 'r')
        lines = sorted(file1.readlines())
        s=""
        sq=""
        if len(lines) ==1:
            s+="The period of observation was 1 day."+ "\n"
           
        else:
            s+="The period of observation was "+ str(len(lines)) + " days." + "\n"
        s+=("The maximum temperature was " + str(obj.get_max_temp()) + " degrees.")+ "\n"
        s+=("The minimum temperature was " + str(obj.get_min_temp()) + " degrees.")+ "\n"
        s+=("The average temperature was " + str(obj.get_average_temp()) + " degrees.")+ "\n"
        if (len(obj.get_hottest_days())) == 1:
            s+=("The hottest day was " + str(obj.get_hottest_days()[0]) + ".")+ "\n"
        else:
            for i in range(0, len(obj.get_hottest_days())):
                
                if i == (len(obj.get_hottest_days()))-1:
                    sq+=" and "+obj.get_hottest_days()[i] + "."
                elif i==0:
                    sq+=obj.get_hottest_days()[i]
           
                else:
                    sq+=", "+obj.get_hottest_days()[i]
            s+=("The hottest days were " + sq )+ "\n"
        sq=""
        if (len(obj.get_coldest_days())) == 1:
            s+=("The coldest day was " + str(obj.get_coldest_days()[0]) + ".")+ "\n"
        else:
            for i in range(0, len(obj.get_coldest_days())):
                
                if i == (len(obj.get_coldest_days()))-1:
                    sq+=" and "+obj.get_coldest_days()[i] + "."
                elif i==0:
                    sq+=obj.get_coldest_days()[i]
           
                else:
                    sq+=", "+obj.get_coldest_days()[i]
            s+=("The coldest days were " + sq )+ "\n"
        s+="The temperature graph is:" + "\n"
        s+=obj.histogram()
        return s

        
        
        
         
      




if __name__ == "__main__":
    database = WeatherDatabase("weather.dat")
    print(database.report())
