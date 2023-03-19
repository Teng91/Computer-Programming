def is_full_house(hand):
    ghost = False #預設沒有鬼牌
    number_dict = {} #所有手牌的數字
    
    for i in hand:
        if len(i)>1: #不是鬼牌
            if i[1].isalpha(): #判斷是否為字母
                num = i[1].lower()
            else:
                num = i[1]
            #判斷是否在dict中
            if num in number_dict.keys():
                number_dict[num]+=1
            else:
                number_dict[num]=1
        else:
            ghost = True

    if ghost == True and list(number_dict.values())[0]==2 and list(number_dict.values())[1]==2:
        return True
    elif ghost == False and (list(number_dict.values())[0]==2 or list(number_dict.values())[1]==2):
        return True
    else:
        return False
