import math
sex=input("Enter the sex (m/f): ")
size=input("Enter the size: ")
panel_id=input("Enter the panel_id: ")
pixelPermetric=1

#Front Cut_2 Interfacing
#-------------------MEN-------------------------
{"h0":"0.9", "h1":"4.925", "h2":"5.679", "h3":"23.391", "h4":"10.759", "h5":"16.939"}, #txl
{"h0":"0.9", "h1":"4.561", "h2":"5.557", "h3":"23.208", "h4":"10.086", "h5":"16.939"}, #tl
{"h0":"0.9", "h1":"4.200", "h2":"5.439", "h3":"23.025", "h4":"9.412", "h5":"16.939"}, #tm
{"h0":"0.9", "h1":"3.840", "h2":"5.325", "h3":"22.842", "h4":"8.738", "h5":"16.939"}, #ts
{"h0":"0.9", "h1":"3.484", "h2":"5.215", "h3":"22.659", "h4":"8.065", "h5":"16.939"}, #txs

{"h0":"0.9", "h1":"4.925", "h2":"5.679", "h3":"21.384", "h4":"10.759", "h5":"14.932"}, #xl
{"h0":"0.9", "h1":"4.561", "h2":"5.557", "h3":"21.201", "h4":"10.086", "h5":"14.932"}, #l
{"h0":"0.9", "h1":"4.200", "h2":"5.439", "h3":"21.018", "h4":"9.412", "h5":"14.931"}, #m
{"h0":"0.9", "h1":"3.840", "h2":"5.325", "h3":"20.835", "h4":"8.738", "h5":"14.931"}, #s
{"h0":"0.9", "h1":"3.484", "h2":"5.215", "h3":"20.652", "h4":"8.065", "h5":"14.931"}, #xs
#--------------------WOMEN----------------------
{"h0":"0.9", "h1":"3.049", "h2":"5.215", "h3":"18.652", "h4":"7.598", "h5":"12.931"}, #xs
{"h0":"0.9", "h1":"3.399", "h2":"5.325", "h3":"18.835", "h4":"8.272", "h5":"12.931"}, #s
{"h0":"0.9", "h1":"3.755", "h2":"5.439", "h3":"19.018", "h4":"8.945", "h5":"12.931"}, #m
{"h0":"0.9", "h1":"4.113", "h2":"5.557", "h3":"19.201", "h4":"9.619", "h5":"12.932"}, #l
{"h0":"0.9", "h1":"4.475", "h2":"5.679", "h3":"19.384", "h4":"10.295", "h5":"12.933"}, #xl

{"h0":"0.9", "h1":"3.049", "h2":"5.215", "h3":"20.652", "h4":"7.600", "h5":"14.931"}, #txs
{"h0":"0.9", "h1":"3.399", "h2":"5.325", "h3":"20.835", "h4":"8.272", "h5":"14.931"}, #ts
{"h0":"0.9", "h1":"3.755", "h2":"5.439", "h3":"21.018", "h4":"8.945", "h5":"14.931"}, #tm
{"h0":"0.9", "h1":"4.113", "h2":"5.557", "h3":"21.201", "h4":"9.621", "h5":"14.932"}, #tl
{"h0":"0.9", "h1":"4.475", "h2":"5.679", "h3":"21.384", "h4":"10.295", "h5":"14.932"}, #xl



#Hood cut2
#--------------------MEN------------------------
{"h0":"4.615", "h1":"2.827", "h2":"0.892", "h3":"14.592"}, #txl
{"h0":"4.372", "h1":"2.827", "h2":"0.892", "h3":"14.411"}, #tl
{"h0":"4.129", "h1":"2.827", "h2":"0.892", "h3":"14.231"}, #tm
{"h0":"3.887", "h1":"2.827", "h2":"0.892", "h3":"14.051"}, #ts
{"h0":"3.646", "h1":"2.827", "h2":"0.892", "h3":"13.870"}, #txs

{"h0":"4.615", "h1":"2.827", "h2":"0.892", "h3":"14.591"}, #xl
{"h0":"4.372", "h1":"2.827", "h2":"0.892", "h3":"14.411"}, #l
{"h0":"4.129", "h1":"2.827", "h2":"0.892", "h3":"14.231"}, #m
{"h0":"3.887", "h1":"2.827", "h2":"0.892", "h3":"14.051"}, #s
{"h0":"3.646", "h1":"2.827", "h2":"0.892", "h3":"13.870"}, #xs

#------------------WOMEN-----------------------
{"h0":"3.646", "h1":"2.827", "h2":"0.892", "h3":"13.868"}, #xs
{"h0":"3.887", "h1":"2.827", "h2":"0.892", "h3":"14.051"}, #s
{"h0":"4.129", "h1":"2.827", "h2":"0.892", "h3":"14.231"}, #m
{"h0":"4.372", "h1":"2.827", "h2":"0.892", "h3":"14.411"}, #l
{"h0":"4.615", "h1":"2.827", "h2":"0.892", "h3":"14.591"}, #xl

{"h0":"3.646", "h1":"2.827", "h2":"0.892", "h3":"13.870"}, #txs
{"h0":"3.887", "h1":"2.827", "h2":"0.892", "h3":"14.051"}, #ts
{"h0":"4.129", "h1":"2.827", "h2":"0.892", "h3":"14.232"}, #tm
{"h0":"4.372", "h1":"2.827", "h2":"0.892", "h3":"14.423"}, #tl
{"h0":"4.615", "h1":"2.827", "h2":"0.892", "h3":"14.616"}, #txl


#CENTER HOOD CUT 1
#----------------------MEN----------------------
{"h0":"3.116", "h1":"7.887", "h2":"12.942", "h3":"3.104"}, #txl
{"h0":"3.116", "h1":"7.387", "h2":"12.942", "h3":"3.104"}, #tl
{"h0":"3.116", "h1":"6.887", "h2":"12.942", "h3":"3.104"}, #tm
{"h0":"3.116", "h1":"6.387", "h2":"12.942", "h3":"3.104"}, #ts
{"h0":"3.116", "h1":"5.890", "h2":"12.942", "h3":"3.104"}, #txs

{"h0":"3.116", "h1":"7.887", "h2":"12.942", "h3":"3.104"}, #xl
{"h0":"3.116", "h1":"7.387", "h2":"12.942", "h3":"3.104"}, #l
{"h0":"3.116", "h1":"6.887", "h2":"12.942", "h3":"3.104"}, #m
{"h0":"3.116", "h1":"6.387", "h2":"12.942", "h3":"3.104"}, #s
{"h0":"3.116", "h1":"5.890", "h2":"12.942", "h3":"3.104"}, #xs

#------------------------WOMEN---------------------------
{"h0":"3.116", "h1":"7.887", "h2":"12.942", "h3":"3.104"}, #txl
{"h0":"3.116", "h1":"7.387", "h2":"12.942", "h3":"3.104"}, #tl
{"h0":"3.116", "h1":"6.887", "h2":"12.942", "h3":"3.104"}, #tm
{"h0":"3.116", "h1":"6.387", "h2":"12.942", "h3":"3.104"}, #ts
{"h0":"3.116", "h1":"5.890", "h2":"12.942", "h3":"3.104"}, #txs

{"h0":"3.116", "h1":"7.887", "h2":"12.942", "h3":"3.104"}, #xl
{"h0":"3.116", "h1":"7.387", "h2":"12.942", "h3":"3.104"}, #l
{"h0":"3.116", "h1":"6.887", "h2":"12.942", "h3":"3.104"}, #m
{"h0":"3.116", "h1":"6.387", "h2":"12.942", "h3":"3.104"}, #s
{"h0":"3.116", "h1":"5.890", "h2":"12.942", "h3":"3.104"}, #xs


#BACK CUT 1 INTERFACING
#-------------------------MEN-------------------------------
{"h0":"15.080", "h1":"5.209", "h2":"4.814", "h3":"25.656", "h4":"16.929", "h5":"7.260", "h6":"3.608"},#txl
{"h0":"15.080", "h1":"4.480", "h2":"4.450", "h3":"24.406", "h4":"16.929", "h5":"7.043", "h6":"3.500"},#tl
{"h0":"15.080", "h1":"4.119", "h2":"4.088", "h3":"23.156", "h4":"16.929", "h5":"6.800", "h6":"3.379"},#tm
{"h0":"15.080", "h1":"3.760", "h2":"3.729", "h3":"21.906", "h4":"16.929", "h5":"6.561", "h6":"3.261"},#ts
{"h0":"15.080", "h1":"3.405", "h2":"3.373", "h3":"20.656", "h4":"16.929", "h5":"6.327", "h6":"3.144"},#txs

{"h0":"15.080", "h1":"5.209", "h2":"4.814", "h3":"25.656", "h4":"14.922", "h5":"7.260", "h6":"3.608"},#xl
{"h0":"15.080", "h1":"4.480", "h2":"4.450", "h3":"24.406", "h4":"14.922", "h5":"7.043", "h6":"3.500"},#l
{"h0":"15.080", "h1":"4.119", "h2":"4.088", "h3":"23.156", "h4":"14.922", "h5":"6.800", "h6":"3.379"},#m
{"h0":"15.080", "h1":"3.760", "h2":"3.729", "h3":"21.906", "h4":"14.922", "h5":"6.561", "h6":"3.261"},#s
{"h0":"15.080", "h1":"3.405", "h2":"3.373", "h3":"20.656", "h4":"14.922", "h5":"6.327", "h6":"3.144"},#xs

#----------------------WOMEN----------------------------------
{"h0":"15.080", "h1":"2.972", "h2":"2.902", "h3":"19.687", "h4":"12.922", "h5":"6.327", "h6":"3.144"},#xs
{"h0":"15.080", "h1":"3.321", "h2":"3.251", "h3":"20.937", "h4":"12.922", "h5":"6.561", "h6":"3.261"},#s
{"h0":"15.080", "h1":"3.675", "h2":"3.606", "h3":"22.187", "h4":"12.922", "h5":"6.800", "h6":"3.379"},#m
{"h0":"15.080", "h1":"4.033", "h2":"3.965", "h3":"23.437", "h4":"12.922", "h5":"7.043", "h6":"3.500"},#l
{"h0":"15.080", "h1":"4.757", "h2":"4.326", "h3":"24.687", "h4":"12.922", "h5":"7.260", "h6":"3.608"},#xl

{"h0":"15.080", "h1":"2.972", "h2":"2.902", "h3":"19.687", "h4":"14.922", "h5":"6.327", "h6":"3.144"},#txs
{"h0":"15.080", "h1":"3.321", "h2":"3.251", "h3":"20.937", "h4":"14.922", "h5":"6.561", "h6":"3.261"},#ts
{"h0":"15.080", "h1":"3.675", "h2":"3.606", "h3":"22.187", "h4":"14.922", "h5":"6.800", "h6":"3.379"},#tm
{"h0":"15.080", "h1":"4.033", "h2":"3.965", "h3":"23.437", "h4":"14.922", "h5":"7.043", "h6":"3.500"},#tl
{"h0":"15.080", "h1":"4.757", "h2":"4.326", "h3":"24.687", "h4":"14.922", "h5":"7.260", "h6":"3.608"},#txl



if(sex=='m' and size=='xs' and panel_id=='Front Cut_2 Interfacing'):
    
    h0, h1, h2, h3, h4, h5 = 0.9, 4.925, 5.679, 23.391, 10.759, 16.939
    
    x2=pixelPermetric*h4
    x3=pixelPermetric*(h3-1)
    x4=pixelPermetric*h5
    x5=pixelPermetric*(h2+1)
    x6=pixelPermetric*(h2-1)
    x7=pixelPermetric*3
    x8=pixelPermetric*1.5
    
    
    c1=math.ceil(x7)
    c2=math.ceil(x2)
    c3=math.ceil(x5)
    c4=math.ceil(x3)
    c5=math.ceil(x4)
    c6=math.ceil(x6)
    c7=math.ceil(x8)
    
    
    list1=[(c3,0),(c2,c6),(c2,c6+c4),(0,c6+c4),(0,c6+c4-c5),(c1,c7)]
    print(list1)

elif(sex=='m' and size=='xs' and panel_id=='bc1'):
    
    
    h0, h1, h2, h3, h4, h5, h6 = 15.080, 5.209, 4.814, 25.656, 16.929, 7.260, 3.608
    l0 = 0.21
    l1= 0.5
    
    y1=math.sqrt(h1**2-l0**2)
    y2=math.sqrt(h2**2-l1**2)
    
    x0=pixelPermetric*2
    x1=pixelPermetric*h1
    x2=pixelPermetric*h2
    x3=pixelPermetric*(h3-h0)
    x4=pixelPermetric*l1
    x5=pixelPermetric*(h5+h6)
    x6=pixelPermetric*h4
    x7=pixelPermetric*h3
    x8=pixelPermetric*l0
        
    c0=math.ceil(x0)
    c1=math.ceil(x1)
    c2=math.ceil(x2)
    c3=math.ceil(x3)
    c4=math.ceil(x4)
    c5=math.ceil(x5)
    c6=math.ceil(x6)
    c7=math.ceil(x7)

    c8=math.ceil(y1)
    c9=math.ceil(y2)
    c10=math.ceil(x8)
        
    
    list1=[(c0+c8,0),(c0+c8+c3,0),(c0+c8+c3+c9,c4),(2*c0+c8+c3+c9,c5+c4),(c7,c5+c4+c6),(0,c5+c4+c6),(0,c4+c5),(c0,c10)]
    print(list1)
    
elif(sex=='m' and size=='xs' and panel_id=='CENTER HOOD CUT 1'):
    
    h0, h1, h2, h3, h4 = 3.116, 7.887, 4.2, 12.943, 3.104
    
    l0= (h2-h0)/2
    l1= (h2-h4)/2
        
    x1=pixelPermetric*l0
    x2=pixelPermetric*h0
    x3=pixelPermetric*h3
    x4=pixelPermetric*h2
    x5=pixelPermetric*h4
    x6=pixelPermetric*l1
    x7=pixelPermetric*h1
    
    
    
    c1=math.ceil(x1)
    c2=math.ceil(x2)
    c3=math.ceil(x3)
    c4=math.ceil(x4)
    c5=math.ceil(x5)
    c6=math.ceil(x6)
    c7=math.ceil(x7)
    
    
    list1=[(c1,0),(c1+c2,0),(c4,c7),(c5+c6,c3+c7),(c6,c3+c7),(0,c7)]
    print(list1)
    
elif(sex=='m' and size=='xs' and panel_id=='Hood cut2'):
    
    h0, h1, h2, h3 = 4.615, 2.827, 0.892, 14.592
    
    
        
    x0=pixelPermetric*h0
    x1=pixelPermetric*h1
    x2=pixelPermetric*h2
    x3=pixelPermetric*h3
    
    
    
    
    c0=math.ceil(x0)
    c1=math.ceil(x1)
    c2=math.ceil(x2)
    c3=math.ceil(x3)
    c4=math.ceil(c3/2)
  
    
    
    list1=[(c0+c1+c2,0),(c0+c1+2*c2,c3),(c2,c3-c2),(0,c4)]
    print(list1)
