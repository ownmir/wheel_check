import os
import pickle


def to():
    tree = os.walk('itest')
    tree_list = []
    for i in tree:
        print(i)
        tree_list.append(i)
    for address, folders, files in tree_list:
        if '__pycache__' in address:
            continue
        for file in files:
            print(address + '\\' + file)
            old = 'd:\\pyprg\\' + address + '\\' + file
            new = 'd:\\pyprg\\to\\' + address + '\\' + file
            rf = open(old, 'rb')
            print(rf)
            os.system('cd to')
            if os.path.exists('d:\\pyprg\\to\\' + address):
                print("Указанный файл существует") 
            else:
                os.mkdir('d:\\pyprg\\to\\' + address)
            wf = open(new, 'wb')
            print(wf)
            while True:
                data = rf.read(1024)
                print(data)
                if not data:
                    rf.close()
                    wf.close()
                    os.system('cd ..')
                    break
                
                wf.write(data)


if __name__ == '__main__':
    to()
