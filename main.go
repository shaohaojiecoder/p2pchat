package main

import "github.com/gorilla/websocket"

/*

用户通过前端页面 打开主页后：-》js检查cookie中是否存在nickname

如果不存在的话 则要求用户输入nickname并写入cookie

新建到服务器端websocket连接

然后首先需要 发送自身的nickname 并同步右侧的房间列表情况 并刷新welcome room的界面

用户可以通过右上侧的搜索框 输入房间号码进入房间 或者通过➕输入新的房间名称 新建一个房间 并进入

每一个房间人数必须大于等于1人  如果该房间一个人也没，则会销毁该房间

每当进入一个新房间后 则会清空消息栏 并接收该房间内的全部消息 也可以输入消息并发送



*/

type User struct {
	id       string
	NickName string
	socket   *websocket.Conn
	send     chan []byte
}

type Message struct {
	Sender  string
	Content string
}

type Room struct {
	Name      string
	Users     map[string]*User
	broadcast chan *Message
}

type RoomManager struct {
	Rooms map[string]*Room
}

var roomer = RoomManager{}

func main() {

}
