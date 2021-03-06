from ..kernel import core


#_SoulContract = core.BuffSkill("SoulContract", 600, 1000, cooltime = 9000, pdamage = 45)

# 데벤져 추가할시 쓸만한 하이퍼바디 추가바람

def soul_contract():
    SoulContract = core.BuffSkill("소울 컨트랙트", 600, 10*1000, cooltime = 90*1000, pdamage = 45, rem = True).wrap(core.BuffSkillWrapper)
    return SoulContract

def maple_heros(level):
    MapleHeros = core.BuffSkill("메이플 용사", 0, 900*1000, stat_main = 0.15*(25 + level * 5), rem = True).wrap(core.BuffSkillWrapper)
    return MapleHeros

def useful_combat_orders():
    UsefulCombatOrders = core.BuffSkill("쓸만한 컴뱃 오더스", 1350, 183*1000, rem = False).wrap(core.BuffSkillWrapper)
    return UsefulCombatOrders
    
def useful_sharp_eyes():
    UsefulSharpEyes = core.BuffSkill("쓸만한 샤프 아이즈", 1080, 183 * 1000, rem = False, crit = 10, crit_damage = 8).wrap(core.BuffSkillWrapper)
    return UsefulSharpEyes
    
def useful_wind_booster():
    UsefulWindBooster = core.BuffSkill("쓸만한 윈드 부스터", 1080, 183*1000, rem = False).wrap(core.BuffSkillWrapper)
    return UsefulWindBooster

# 235레벨 이상만 사용가능
class SpiderInMirrorBuilder():
    def __init__(self, enhancer, skill_importance, enhance_importance):
        self.MirrorBreak = core.DamageSkill("스파이더 인 미러(공간 붕괴)", 0, 750+30*enhancer.getV(skill_importance, enhance_importance), 12, cooltime = 250*1000).wrap(core.DamageSkillWrapper)
        # 50초 동안 지속되며 일정 시간 마다 공격 상태에 돌입, 공격 상태 동안 385%의 데미지로 8번 공격하는 거미 다리를 10회 사용, 거미 다리가 한명의 적을 5번 연속 공격할 경우 공격 상태 즉시 종료, 공격 상태 종료 후 재돌입 대기시간 3초
        self.MirrorSpider = core.SummonSkill("스파이더 인 미러(거울 속의 거미)", 0, 3000, 175+17*enhancer.getV(skill_importance, enhance_importance), 8, 50*1000).wrap(core.SummonSkillWrapper)