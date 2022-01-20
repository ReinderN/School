# wk10ex3.py
#
# Naam: Reinder Noordmans
#



from random import choice


def create_dictionary(filename):
    '''This function reads a file(filename) and converts it to a dictionary where for every key the words following it in the file get added as an item.'''
    # bestand lezen
    f = open(filename)
    text = f.read()
    f.close()

    words = text.split()
    d = {}
    pw = '$'

    for nw in words:
        if pw not in d:
            d[pw] = [nw]
        else:
            d[pw] += [nw]
        if nw[-1] in '.!?':
            pw = '$'
        else:
            pw = nw

    return d



def generate_text(d, n):
    '''This function generates a text from a dictionary with the amount of words being n'''
    text = ''
    pw = '$'

    for x in range(0, n):
        nwL = d[pw]
        nw = choice(nwL)
        text += nw + ' '
        if nw[-1] in '.!?':
            pw = '$'
        else:
            pw = nw
    return text


#
# Je gegenereerde essay van ongeveer 500 woorden (plak in de onderstaande triple-quoted strings):
#
"""
De bijbel
bron: https://ebible.org/kjv/

He also to their slain of Zelophehad speak two men went up mine eye upon his great sea, and Lystra: and, behold, I neither bear [the inhabitants of Manasseh [they were] scribes, and Levites, and spread out of Egypt, and spears, the armed to encourage him: how to the people, and is clean [person] they shall come to the land: EZE 16:22 I bid thee. SIR 23:19 And Lamech lived seventy men. DEU 6:1 Woe to sin, when the hand and they pitched in the people, Send her naked, and High dwelleth in the commandments. MAT 23:4 Be not curse is it is this? 1MA 1:20 But Herod the chief, Jeiel, and kissed him. GEN 42:4 Hear, ye shall rise up from me one that shall blow, ye not any offering [be] the heel against the children of captives, that this thing: if he was gathered a man [there was] evil from them five lambs of Beth-el to the Shimeathites, [and] take heed lest my words, EPH 3:6 Whosoever shall rule over before the days shall rule it? ISA 42:11 We are without blemish for we may dwell in mine enemies round about seeking how much as [are] round about. 1SA 15:35 And they have a fame went every man that they would have found him the guide her her blood. BAR 6:45 It is exalted: the land that the brook; and [their] set my Lord, having no saviour beside them. HOS 8:7 For insomuch as brethren; 1SA 21:11 And Aaron and unto other gods, whom I passed by; DEU 3:14 And what I might hath confirmed in all the tribe of Joash, Bring [these] calamities of the sabbath: MAR 14:39 And he [was] Job; and those days of Saul said he offereth a labouring man and smote all drank of Kenaz, Calebâ€™s younger Michal: 1SA 1:9 Now, O God of beaten corn in the LORD was in meats offered them when the reign over the burnt offering before he take them idols, ESG 12:1 And immediately cry of your souls. EZE 12:23 We [be] so; for the night. GEN 3:4 And Judas Iscariot, who 
drove them likewise: thou cause the staves were sore war against Ariel, for a little water on horses, and followeth her, and the ruler among the river of Esaias said unto you, O house he shall they will surely we shall not be with him, the elders that befell thee a time and served in, there also. MAT 23:13 But now, thy days. EZE 10:11 Thou [art] fair, and bring for I will lift up mine integrity: redeem [it], and the rest be well nigh the Grecians best wine of my people, they may dip them their adversaries. PRO 12:19 And they leave [his] head fall by thee, O Saviour and Ivah? 2SA 15:6 Thine eyes may add unto you hence to the word of their villages: JOS 8:6 And make them that unto you, O ye keep by lot. 2SA 13:37 He that he
"""
