from riotwatcher import RiotWatcher
import pickle
import numpy as np

watcher = RiotWatcher("RGAPI-cca3c6f5-0463-4820-85bf-92e89d4028c2")
#name = 'Zelt'
#my_region = 'na1'


# get account_id by name
def get_acc_by_name(region, name):
    me = watcher.summoner.by_name(region, name)
    acc_id = me["accountId"]
    return acc_id


def get_match_by_acc(region, account_id):
    matches_info = watcher.match.matchlist_by_account(region, account_id)
    matches = matches_info["matches"][0]
    matchId = matches["gameId"]
    return matchId


def match_data_by_id(region, match):
    match_data = watcher.match.by_id(region, match)
    return match_data


def match_info(match_data, acc_id):
    prediction_data = []
    participantIdentities = match_data['participantIdentities']
    for participant in participantIdentities:
        player = participant["player"]
        acc = player["currentAccountId"]
        if acc == acc_id:
            my_participant = participant["participantId"]
            break
    participants = match_data['participants']
    for participant in participants:
        if participant['participantId'] == my_participant:
            stats = participant['stats']
            #timeline = participant['timeline']

            win = stats["win"]
            if win is True:
                win = 1
            else:
                win = 0

            championid = participant['championId']
            ss1 = participant['spell1Id']
            ss2 = participant['spell2Id']
            # role = timeline["role"]
            # position = timeline["lane"]
            gameid = match_data["gameId"]
            queueid = match_data["queueId"]
            duration = match_data["gameDuration"]
            item1 = stats["item0"]
            item2 = stats["item1"]
            item3 = stats["item2"]
            item4 = stats["item3"]
            item5 = stats["item4"]
            item6 = stats["item5"]
            trinket = stats["item6"]
            kills = stats["kills"]
            deaths = stats["deaths"]
            assists = stats["assists"]
            largestKillingSpree = stats["largestKillingSpree"]
            largestMultiKill = stats["largestMultiKill"]
            killingSprees = stats["killingSprees"]
            longestTimeSpentLiving = stats["longestTimeSpentLiving"]
            doubleKills = stats["doubleKills"]
            tripleKills = stats["tripleKills"]
            quadraKills = stats["quadraKills"]
            pentaKills = stats["pentaKills"]
            legendarykills = stats["unrealKills"]
            totdmgdealt = stats["totalDamageDealt"]
            magicdmgdealt = stats["magicDamageDealt"]
            physicaldmgdealt = stats["physicalDamageDealt"]
            truedmgdealt = stats["trueDamageDealt"]
            largestcrit = stats["largestCriticalStrike"]
            totdmgtochamp = stats["totalDamageDealtToChampions"]
            magicdmgtochamp = stats["magicDamageDealtToChampions"]
            physdmgtochamp = stats["physicalDamageDealtToChampions"]
            truedmgtochamp = stats["trueDamageDealtToChampions"]
            totheal = stats["totalHeal"]
            totunitshealed = stats["totalUnitsHealed"]
            dmgselfmit = stats["damageSelfMitigated"]
            dmgtoobj = stats["damageDealtToObjectives"]
            dmgtoturrets = stats["damageDealtToTurrets"]
            visionscore = stats["visionScore"]
            timecc = stats["timeCCingOthers"]
            totdmgtaken = stats["totalDamageTaken"]
            magicdmgtaken = stats["magicalDamageTaken"]
            physdmgtaken = stats["physicalDamageTaken"]
            truedmgtaken = stats["trueDamageTaken"]
            goldearned = stats["goldEarned"]
            goldspent = stats["goldSpent"]
            turretkills = stats["turretKills"]
            inhibkills = stats["inhibitorKills"]
            totminionskilled = stats["totalMinionsKilled"]
            neutralminionskilled = stats["neutralMinionsKilled"]
            ownjunglekills = stats["neutralMinionsKilledTeamJungle"]
            enemyjunglekills = stats["neutralMinionsKilledEnemyJungle"]
            totcctimedealt = stats["totalTimeCrowdControlDealt"]
            champlvl = stats["champLevel"]
            pinksbought = stats["visionWardsBoughtInGame"]
            wardsbought = stats["sightWardsBoughtInGame"]
            wardsplaced = stats["wardsPlaced"]
            wardskilled = stats["wardsKilled"]
            firstblood = stats["firstBloodKill"]
            if firstblood is True:
                firstblood = 1
            else:
                firstblood = 0
            predictors = [my_participant, championid, ss1, ss2, gameid, queueid, duration,
                                   item1, item2, item3, item4, item5, item6, trinket, kills, deaths, assists,
                                   largestKillingSpree, largestMultiKill, killingSprees, longestTimeSpentLiving,
                                   doubleKills, tripleKills, quadraKills, pentaKills, legendarykills, totdmgdealt,
                                   magicdmgdealt, physicaldmgdealt, truedmgdealt, largestcrit, totdmgtochamp,
                                   magicdmgtochamp, physdmgtochamp, truedmgtochamp, totheal, totunitshealed,
                                   dmgselfmit, dmgtoobj, dmgtoturrets, visionscore, timecc, totdmgtaken, magicdmgtaken,
                                   physdmgtaken, truedmgtaken, goldearned, goldspent, turretkills, inhibkills,
                                   totminionskilled, neutralminionskilled, ownjunglekills, enemyjunglekills,
                                   totcctimedealt, champlvl, pinksbought, wardsbought, wardsplaced, wardskilled,
                                   firstblood]
            prediction_data.append(predictors)
            prediction_data.append(win)
    return prediction_data


def prediction_result(predict, res):
    if predict == 1 and res == 1:
        return 'I guessed! You are the real winner ;)'
    if predict == 0 and res == 0:
        return 'I guessed... Seems like you had to loose this time :('
    if predict == 0 and res == 1:
        return 'Whoops... Seems like someone got carried ;)'
    if predict == 1 and res == 0:
        return 'Whoops... You had all chances ;( Good luck next game!'
    
""""
acc_id = get_acc_by_name(my_region, name)
print(acc_id)
match_id = get_match_by_acc(my_region, acc_id)
print(match_id)
#time.sleep(7)
match_inf = match_data_by_id(my_region, match_id)
print('done')
pred_data = match_info(match_inf, acc_id)
print(pred_data)


model = pickle.load(open("model.pkl", "rb"))

result = pred_data[1]

predictors = pred_data[0]
predictors = np.array(predictors)
predictors = predictors.reshape(1, -1)
prediction = model.predict(predictors)
prediction = prediction[0]
prediction = np.asscalar(prediction)
print('prediction', prediction)


print(prediction_result(prediction, result))

"""
