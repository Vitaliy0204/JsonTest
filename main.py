import json
import random
import time
def generate():
    idgame = random.randint(10000000, 99999999)
    team_names = ['Польша', 'Нидерланды', 'Россия', 'Япония', 'США', 'Китай', 'Испания', 'Конго', 'Казахстан', 'Германия']
    team1 = team_names[random.randint(0, 9)]
    team2 = team_names[random.randint(0, 9)]
    while team1 == team2:
        team2 = team_names[random.randint(1, 10)]
    set_now = '1-й сет'
    set_now1 = '2-й сет'
    score1 = 0
    score2 = 0
    score = [1, 0]
    for i in range(3):
        s = {'events':[{'id': idgame, 'team1': team1, 'team2': team2, 'name': ''}]}
        with open('data.json', 'w') as outfile:
            d = {'id': idgame + 1, 'name': set_now}
            f = {'id': idgame + 2, 'name': set_now1}
            s['events'].append(d)
            if i == 1:
                s['events'].append(f)
                set_now = '2-й сет'
                set_now1 = '3-й сет'
                s['eventMiscs'] = [{'id': idgame, 'score1': score1, 'score2': score2}]
            elif i == 2:
                s['events'].append(f)
                score1 = random.choice(score)
                score2 = score[score1]
                s['eventMiscs'] = [{'id': idgame, 'score1': score1, 'score2':score2}]

            json.dump(s, outfile, ensure_ascii=False)

        time.sleep(5)

if __name__ == '__main__':
    generate()