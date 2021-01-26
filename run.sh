#!/bin/bash


pid=$(ps -ef | grep "/root/memeplatform/ENV/bin/python meme/manage.py runserver" | grep -v "grep" | awk '{print $2}')

### 警告信息
notice(){
    echo "用法：$0 {start|stop|restart}"
}

start() {
    sleep 2
    pids=$(ps -ef | grep "/root/memeplatform/ENV/bin/python meme/manage.py runserver" | grep -v "grep" | awk '{print $2}')
    if [ -n "${pids}" ]
    then
        echo "程序已经运行"
    else
        source /root/memeplatform/ENV/bin/activate
        nohup /root/memeplatform/ENV/bin/python meme/manage.py runserver 0.0.0.0:8000 >/dev/null 2>&1 &
        a=$?
        sleep 3
        if [ ${a} -eq 0 ]
        then
            echo "程序启动成功"
        else
            echo "程序启动失败"
        fi
        deactivate
    fi
    exit
}

stop() {
   if [ -n "${pid}" ]
   then
       kill ${pid}
       if [ $? -eq 0 ]
       then
           echo "程序已停止"
       else
           kill -9 ${pid}
           if [ $? -eq 0 ]
           then
               echo "程序已停止"
           else
               echo "程序停止失败"
           fi
       fi
   else
       echo "程序没有运行"
   fi
}

restart() {
    stop
    start
}


if [ $# -eq 1 ];then
  case $1 in
    "start")
        start
        ;;
    "stop")
        stop
        ;;
    "restart")
        stop
        start
        ;;
    *)
        notice
        ;;
    esac  
else
    notice
fi
