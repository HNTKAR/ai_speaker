import socket
import time
import sys
import pygame.mixer
import random
musiccount=12
def word(recv_data):
    for line in recv_data.split('\n'):
        index1 = line.find('WORD="')
        index2 = line.find('CM="')
        if index1!=-1:
            WORD = line[index1+6:line.find('"',index1+6)]
            if index2!=-1:
                CM = float(line[index2+4:line.find('"',index2+4)])
                if(WORD!='[s]' and WORD!='[/s]'):
                    print(WORD)
                    if (WORD == 'OK' or WORD == 'オウケイ'or WORD == 'おうけい'or WORD == 'おーけー'or WORD == 'オーケー'):
                        pygame.mixer.init()
                        pygame.mixer.music.load("/home/pi/Desktop/mypython/ai/button.mp3")
                        pygame.mixer.music.play(-1)
                        time.sleep(.7)
                        pygame.mixer.music.stop()
                    elif (WORD == 'スタート' or WORD == 'すたあと'or WORD == 'すたーと'or WORD == 'スタアト'or WORD == '始め'or WORD == 'はじめ'or WORD == '開始'or WORD == 'かいし'):
                        pygame.mixer.init()
                        global x
                        x = 1
                        fname=filestr+str(x)+fileend
                        pygame.mixer.music.load(fname)
                        pygame.mixer.music.play(-1)
                        
                    elif (WORD == '次' or WORD == 'つぎ'or WORD == 'あと'or WORD == '後'):
                        
                        pygame.mixer.init()
                        global x
                        x = x+1
                        if x>=musiccount+1:
                            x=1
                        fname=filestr+str(x)+fileend
                        pygame.mixer.music.load(fname)
                        pygame.mixer.music.play(-1)
                        
                    elif (WORD == '前' or WORD == 'まえ'):
                        
                        pygame.mixer.init()
                        global x
                        x = x-1
                        if x<=0:
                            x=musiccount
                        fname=filestr+str(x)+fileend
                        pygame.mixer.music.load(fname)
                        pygame.mixer.music.play(-1)
                    elif (WORD == 'らんだむ' or WORD == 'ランダム'or WORD == 'シャッフル'or WORD == 'しゃっふる'):
                        
                        pygame.mixer.init()
                        global x
                        x=random.randrange(1, musiccount,1)
                        print(x)
                        fname=filestr+str(x)+fileend
                        pygame.mixer.music.load(fname)
                        pygame.mixer.music.play(-1)
                    
                    elif (WORD == 'おわり' or WORD == '終わり'or WORD == '終了'or WORD == 'しゅうりょう'or WORD == 'しゅーりょー'or WORD == 'オフ'or WORD == 'おふ'or WORD == 'OFF'):
                    
                        try:
                            pygame.mixer.music.stop()
                            
                        except:
                            pass
                            
                        
                    else:
                        print("Oh...")
                        print(WORD)
                        print("Oh...")
                        

def main():
    global x
    x=0
    host = 'localhost'
    port = 10500
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    try:
        data = ''
        while 1:
            if '\n.' in data:
                data = data[data.find(''):].replace('\n.', '')
                WORD=word(data)
                if WORD is not None:
                    print(WORD)
                data = ''
            else:
                data = data + client.recv(1024).decode('utf-8')
    except KeyboardInterrupt:
        client.close()
filestr="/home/pi/Desktop/mypython/ai/"
fileend=".mp3"
main()
