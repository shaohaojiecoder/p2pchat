# coding:utf-8
# 消息为一列表形式 新的消息需要附加到以前信息 仍旧储存起来

import json
import pickle


def record(message, mode='get'):
    with open('record.json', mode='r') as f:
        if mode == 'get':
            _content = f.readline()
            return json.loads(_content)
        elif mode == 'put':

            f.write(json.dumps(message)+'\n')
    return True


if __name__ == '__main__':
    p = record({'name':'shao'}, mode='get')
    print(p)