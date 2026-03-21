import psutil

#take cpu threshold from user 2) then check for current cpu 3) if cpu threshold breaches 
#then send mail
def check_cpu_threshold():
    cpu_threshold = int( input ("Enter the cpu threshold: "))

    current_cpu = psutil.cpu_percent(interval=1)

    if current_cpu > cpu_threshold:
        print("CPU alert email sent")
    else:
        print ("Cpu in safe state")

check_cpu_threshold()


