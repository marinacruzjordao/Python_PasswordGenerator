# Password Generator
# Select a number of characters to create your password
# Select the file to save your new password, where the user/email, software/site are also saved.

from PySimpleGUI import PySimpleGUI as sg
from random import randint

class Password:

    def __init__(self):
        #layout
        sg.theme('Reddit')

        self.layout=[
            [sg.Text('File and path to save the data',size=(23,1)), sg.Input(key='file',size=(60,1))],
            [sg.Text('Email/User',size=(23,1)),sg.Input(key='user',size=(60,1))],
            [sg.Text('Site/Software',size=(23,1)), sg.Input(key='site',size=(60,1))],
            [sg.Text('Number of Characters',size=(23,1)), sg.Input(key='number',size=(60,1))],
            #[sg.Output(size=(85,1))],
            [sg.Button('Generate Password')],
        ]

        self.letters_lower=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.letters_upper=[]
        [self.letters_upper.append(str(i).upper()) for i in self.letters_lower]
        self.numbers=[0,1,2,3,4,5,6,7,8,9]
        self.chac=['!','%','@','#','$','&','/','*','?','-','+','.',',']

    def start(self):
        # create a window in GUI
        self.w1 = sg.Window('Password Generator').layout(self.layout)

        while True:

            # obtain data
            self.event, value = self.w1.read()

            self.file = value.get('file')
            self.user = value.get('user')
            self.site = value.get('site')
            try:
                self.num = int(value.get('number'))
            except ValueError:
                print('Only integer number are accepted')

            # window closed
            if self.event == sg.WINDOW_CLOSED:            
                break

            if self.event == 'Generate Password':
                p.gen_pass()

    def gen_pass(self):
        #calculates the number of letters, numbers and characters

        n_letters_lower=1
        n_letters_upper=1
        n_num=1
        n_chac=1

        if self.num>4:
            n_letters_lower+=randint(0,self.num-4)

            if self.num-4-n_letters_lower>=1:
                n_letters_upper+=randint(0,(self.num-4-n_letters_lower))

                if self.num-4-n_letters_lower-n_letters_upper>=1:
                    n_num+=randint(0,(self.num-4-n_letters_lower-n_letters_upper))

                    if self.num-4-n_letters_lower-n_letters_upper-n_num:
                        n_chac+=randint(0,(self.num-4-n_letters_lower-n_letters_upper-n_num))

        total=n_letters_lower+n_letters_upper+n_num+n_chac

        if total<self.num:
            n_chac=self.num-total+1
            
        t2=n_letters_lower+n_letters_upper+n_num+n_chac

        l_lower=[]
        l_upper=[]
        l_num=[]
        l_chac=[]

        #obtain the characters
        for i in range(0,n_letters_lower):
            index_l_lower=randint(0,len(self.letters_lower)-1)
            l_lower.append(self.letters_lower[index_l_lower])

        for i in range(0,n_letters_upper):
            index_l_upper=randint(0,len(self.letters_upper)-1)
            l_upper.append(self.letters_upper[index_l_upper])

        for i in range(0,n_num):
            index_l_num=randint(0,len(self.numbers)-1)
            l_num.append(self.numbers[index_l_num])

        for i in range(0,n_chac):
            index_l_chac=randint(0,len(self.chac)-1)
            l_chac.append(self.chac[index_l_chac])

        #random characters position
        l=l_lower+l_upper+l_num+l_chac
        l_final=[]
        aux=len(l)
        for i in range(0,len(l)):
            ind=randint(0,aux-1)
            aux-=1
            l_final.append(l[ind])
            del l[ind]
        
        #convert list to final string password
        self.password=''.join([str(i) for i in l_final])
        print(self.password)





p=Password()
p.start()