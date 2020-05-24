import random

class Card():
    RANKS=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    SUITS=['梅','方','红','黑']

    def __init__(self,rank,suit,face_up=True):
        self.rank=rank
        self.suit=suit
        self.is_face_up=face_up  #是否显示位牌的正面
    def __str__(self):
        if self.is_face_up:
            rep=self.suit+self.rank
        else:
            rep="xx"
        return rep
    def pic_order(self):   #牌的顺序号
        if self.rank=='A':
            FaceNum=1
        elif self.rank=='J':
            FaceNum=11
        elif self.rank=='Q':
            FaceNum=12
        elif self.rank=='K':
            FaceNum=13
        else:
            FaceNum=int(self.rank)
        if self.suit=='梅':
            Suit=1
        elif self.suit=='方':
            Suit=2
        elif self.suit=='红':
            Suit=3
        else:
            Suit=4
        return (Suit-1)*13+FaceNum

    def flip(self):                  #翻牌方式
        self.is_face_up= not self.is_face_up


class Hand():
    def __init__(self):
        self.cards=[]   #cards列表变量存储牌手的牌
    def __str__(self):
        if self.cards:
            rep=''
            for card in self.cards:
                rep+=str(card)+'\t'
        else:
            rep='无解'
        return rep
    def clear(self): #清空手里的牌
        self.cards=[]
    def add(self,card):  #增加手里的牌
        self.cards.append(card)
    def give(self,card,other_card):  #把手里的一张牌给其他人
        self.cards.remove(card)
        other_card.add(card)


class Poke(Hand):
    def populate(self):  #生成一副牌
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))

    def shuffle(self):  #洗牌
        random.shuffle(self.cards)  #打乱牌的顺序

    def deal(self,hands,per_hand=13):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                   top_card=self.cards[0]
                   self.cards.remove(top_card)
                   hand.add(top_card)
                else:
                    print("不能在发牌了，牌已经发光了")

if __name__=='__main__':
    print("下面是模拟扑克的发牌过程：")
    players=[Hand(),Hand(),Hand(),Hand()]
    poke1=Poke()
    poke1.populate()
    poke1.shuffle()
    poke1.deal(players,13)
    n=1
    for hand in players:
        print("牌手%d"%n,end="  ")
        print(hand)
        n=n+1
    input("\n按回车结束")

