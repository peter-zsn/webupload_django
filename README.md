# webupload_django
##一个简单的django项目，主要涉及分片上传和websocket：
    #### 1: 利用python---chunks 接收到文件之后 分段写文件
    #### 2: 和js配合， js进行处理文件的分片，接口获取分片文件和位置，存入redis或者中转文件， 最终上传完毕后进行文件的组合
    #### 3: 利用websocket库，dwebsocket进行客户端与服务器的长链接，实现websocket的处理
    
