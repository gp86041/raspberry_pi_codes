library(stringr)
libary(xts)


master <- read.csv("C:/Users/jeffjeff/Downloads/feeds.csv")

s1 <- data.frame(as.POSIXlt(str_sub(master[,1],1,-5),format = "%Y-%m-%d %H:%M:%S", tz="UTC"),
                 master[,4:7])

colnames(s1)<-c('time','temp_h','temp_p','humidity','pressure')

#plot(s1[,1],s1[,2])

s2<- as.xts(s1[,2],order.by = s1[,1])
s3<- as.xts(s1[,3],order.by = s1[,1])
s4<- as.xts(s1[,4],order.by = s1[,1])
s5<- as.xts(s1[,5],order.by = s1[,1])

s2_daily <- apply.daily(s2,mean)
s3_daily <- apply.daily(s3,mean)
s4_daily <- apply.daily(s4,mean)
s5_daily <- apply.daily(s5,mean)

par(mfrow=c(3,1),mar=c(3,6,1,1))

plot(data.frame(time = index(s2_daily),coredata(s2_daily)),type='l',
     ylim=c(min(s3_daily),max(s2_daily)),xaxt='n',xlab='')
lines(data.frame(time = index(s3_daily),coredata(s3_daily)),col='red')

plot(data.frame(time = index(s4_daily),coredata(s4_daily)),type='l',
     xaxt='n',xlab='')

plot(data.frame(time = index(s5_daily),coredata(s5_daily)),type='l')

a1<-data.frame(coredata(s2_daily),
           coredata(s3_daily),
           coredata(s4_daily),
           coredata(s5_daily))

colnames(a1)<-c('temp_h','temp_p','humidity','pressure')


plot(a1)
