# p2pchat
a peer to peer chatroom


使用go语言进行改写

目的：实现一个在线的聊天室
使用技术: go websocket

主要思路：匿名聊天室
        连接上主页之后，进入一个main chatroom  
        main chatroom信息直接进行输出  右侧边栏会显示目前已有聊天室 并显示在线人数
        点击右侧其他聊天室 直接连接到其他频道 在右侧聊天室列表底部有新建聊天室
        当一个聊天室所有人员都退出时，则关闭该聊天室
        所有数据不进行持久化保存
        
主要数据结构：User{
            
            }
            
            Room{
            
            
            }
            
            Message{
            
            }
        
