from PublicReference.base import *

#CDR: 拳套精通(10%) + 烈焰焚步(15%)
#不包含觉醒
class 拳套精通(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '拳套':
            return round(self.CD / self.恢复  * (1-0.1) * (1-0.15), 1)

class 归元散打男技能0(拳套精通):
    名称 = '下段踢'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    基础 = 737.65306122449
    成长 = 83.3469387755102
    CD = 1.8
    TP成长 = 0.08
    TP上限 = 7

class 归元散打男技能1(拳套精通):
    名称 = '碎骨'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3004.85
    成长 = 339.15
    CD = 6.3
    TP成长 = 0.08
    TP上限 = 7

class 归元散打男技能2(拳套精通):
    名称 = '铁山靠'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 2892.2
    成长 = 326.8
    CD = 6.3
    TP成长 = 0.1
    TP上限 = 7

class 归元散打男技能3(被动技能):
    名称 = '柔化肌肉'
    所在等级 = 30
    等级上限 = 15
    基础等级 = 5
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.125 + 0.015 * self.等级, 5)

class 归元散打男技能4(拳套精通):
    名称 = '闪击快打'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4565.54054054054
    成长 = 515.459459459459
    CD = 10.8
    TP成长 = 0.1
    TP上限 = 7

class 归元散打男技能5(拳套精通):
    名称 = '冲膝'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 6663.62857142857
    成长 = 752.371428571429
    CD = 13.5
    TP成长 = 0.1
    TP上限 = 7

class 归元散打男技能6(拳套精通):
    名称 = '炽焰旋风腿'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 8101.2
    成长 = 915.8
    CD = 18
    TP成长 = 0.1
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.28718046004268

class 归元散打男技能7(拳套精通):
    名称 = '闪电之舞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 7933.9375
    成长 = 896.0625
    CD = 18
    TP成长 = 0.1
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.24

class 归元散打男技能8(拳套精通):
    名称 = '瞬影连环踢'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 15717.3
    成长 = 1774.7
    CD = 40.5
    TP成长 = 0.1
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.23


class 归元散打男技能9(被动技能):
    名称 = '烈焰燃烧'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.03 + 0.01 * self.等级, 5)
    #仅作用于面板显示
    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.03 + 0.01 * self.等级, 5)

#不适用拳套掌握CDR
class 归元散打男技能10(主动技能):
    名称 = '烈焰焚步'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 31307
    成长 = 9452
    CD = 130.5
    关联技能 = ['所有']
    #手搓 -5% CD
    def 等效CD(self, 武器类型):
        if 武器类型 == '拳套':
            return round(self.CD / self.恢复 * (1-0.05), 1)

    #被动技能攻击力加成
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.02 + 0.04 * (self.等级-1), 5)

class 归元散打男技能11(拳套精通):
    名称 = '飞燕旋风'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 13039.6363636364
    成长 = 1472.36363636364
    CD = 27
    TP成长 = 0.1
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.20698434053816


#碎心修炼场实测有伤害丢失的BUG
class 归元散打男技能12(拳套精通):
    名称 = '旋风碎心踢'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 23332.9411764706
    成长 = 2635.05882352941
    CD = 45
    TP成长 = 0.1
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.16

class 归元散打男技能13(被动技能):
    名称 = '烈火支配'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.17 + 0.02 * self.等级, 5)

class 归元散打男技能14(拳套精通):
    名称 = '烈火强踢'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 38181.3333333333
    成长 = 4310.66666666667
    CD = 40.5

class 归元散打男技能15(拳套精通):
    名称 = '烈火强拳'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 47826.3333333333
    成长 = 5399.66666666667
    CD = 49.5

#不适用拳套掌握CDR
class 归元散打男技能16(主动技能):
    名称 = '极武霸皇踢'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 82676.3333333337
    成长 = 24957.3333333333
    CD = 162

class 归元散打男技能17(被动技能):
    名称 = '千锤百炼'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 归元散打男技能18(拳套精通):
    名称 = '炼狱坠星腿'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 79841.4
    成长 = 9014.6
    CD = 54

#不适用拳套掌握CDR
class 归元散打男技能19(主动技能):
    名称 = '焚火逐日拳'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 251118.333333333
    成长 = 75810.6666666667
    CD = 261
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0


归元散打男技能列表 = []
i = 0
while i >= 0:
    try:
        exec('归元散打男技能列表.append(归元散打男技能'+str(i)+'())')
        i += 1
    except:
        i = -1

归元散打男技能序号 = dict()
for i in range(len(归元散打男技能列表)):
    归元散打男技能序号[归元散打男技能列表[i].名称] = i

归元散打男一觉序号 = 0
归元散打男二觉序号 = 0
归元散打男三觉序号 = 0
for i in 归元散打男技能列表:
    if i.所在等级 == 50:
        归元散打男一觉序号 = 归元散打男技能序号[i.名称]
    if i.所在等级 == 85:
        归元散打男二觉序号 = 归元散打男技能序号[i.名称]
    if i.所在等级 == 100:
        归元散打男三觉序号 = 归元散打男技能序号[i.名称]

归元散打男护石选项 = ['无']
for i in 归元散打男技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        归元散打男护石选项.append(i.名称)

归元散打男符文选项 = ['无']
for i in 归元散打男技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        归元散打男符文选项.append(i.名称)

class 归元散打男角色属性(角色属性):
    职业名称 = '归元散打男'
    武器选项 = ['拳套']
    伤害类型选择 = ['物理百分比']
    伤害类型 = '物理百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']
    主BUFF = 2.04
    基础力量 = 969
    基础智力 = 0
    力量 = 基础力量
    智力 = 基础智力
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13

    #额外加成
    二挡关联 = '无'

    def __init__(self):
        self.技能栏 = deepcopy(归元散打男技能列表)
        self.技能序号 = deepcopy(归元散打男技能序号)

    # 以下重写修正归元散打男被动面板取整问题

    def 面板物理攻击力(self):
        面板物理攻击 = (self.物理攻击力 + self.进图物理攻击力) * (1 + self.百分比三攻) * (1 + self.年宠技能 * 0.10 + self.斗神之吼秘药 * 0.12 + self.白兔子技能 * 0.20)
        for i in self.技能栏:
            try : 
                面板物理攻击 *= i.物理攻击力倍率(self.武器类型)
            except : 
                pass
        return int(面板物理攻击) * (self.面板力量() / 250 + 1)

    def 站街物理攻击力(self):
        站街物理攻击 = self.物理攻击力
        for i in self.技能栏:
            try : 
                站街物理攻击 *= i.物理攻击力倍率(self.武器类型)
            except : 
                pass
        return int(站街物理攻击)  * (self.站街力量() / 250 + 1)


    def 伤害计算(self, x = 0):
        self.所有属性强化(self.进图属强)
        # Will添加
        self.CD倍率计算()
        self.加算冷却计算()

        self.被动倍率计算()
        self.伤害指数计算()

        技能释放次数=[]
        技能单次伤害=[]
        技能总伤害=[]

    
        #技能单次伤害计算
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                技能单次伤害.append(i.等效百分比(self.武器类型)*self.伤害指数*i.被动倍率)
            else:
                技能单次伤害.append(0)
      
        #技能释放次数计算
        for i in self.技能栏:
            if i.是否有伤害==1:
                if self.次数输入[self.技能序号[i.名称]] =='/CD':
                    技能释放次数.append(int((self.时间输入 - i.演出时间)/i.等效CD(self.武器类型) + 1 +i.基础释放次数))
                else:
                    技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]])+i.基础释放次数)
            else:
                技能释放次数.append(0)
    
        #单技能伤害合计
    
        for i in self.技能栏:
            if i.是否有伤害==1 and 技能释放次数[self.技能序号[i.名称]] != 0:
                技能总伤害.append(技能单次伤害[self.技能序号[i.名称]]*技能释放次数[self.技能序号[i.名称]]*(1+self.白兔子技能*0.20+self.年宠技能*0.10*self.宠物次数[self.技能序号[i.名称]]/技能释放次数[self.技能序号[i.名称]]+self.斗神之吼秘药*0.12))
            else:
                技能总伤害.append(0)
        
        
        # 整合二挡伤害
        总伤害=0
        for i in self.技能栏:
            if self.二挡关联 != '无':
                if (i.名称 == '瞬影连环踢' and self.二挡关联 == '二挡：瞬影连环踢')or(i.名称 == '烈火强拳' and self.二挡关联 == '二挡：烈火强拳')or(i.名称 == '炼狱坠星腿' and self.二挡关联 == '二挡：炼狱坠星腿'): 
                    技能总伤害[self.技能序号[i.名称]] += 技能总伤害[self.技能序号['烈焰焚步']]
                    技能总伤害[self.技能序号['烈焰焚步']] *= 0

            if i.名称 != '烈焰焚步':
                总伤害+=技能总伤害[self.技能序号[i.名称]]
        
        if x==0:
            return 总伤害
    
        if x==1:
            详细数据=[]
            for i in range(0,len(self.技能栏)):
                详细数据.append(技能释放次数[i])
                详细数据.append(技能总伤害[i])
                if 技能释放次数[i]!=0:
                    详细数据.append(技能总伤害[i]/技能释放次数[i])
                else:
                    详细数据.append(0)
                if 总伤害!=0:
                    详细数据.append(技能总伤害[i]/总伤害*100)
                else:
                    详细数据.append(0)
            return 详细数据
    

class 归元散打男(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 归元散打男角色属性()
        self.角色属性A = 归元散打男角色属性()
        self.角色属性B = 归元散打男角色属性()
        self.一觉序号 = 归元散打男一觉序号
        self.二觉序号 = 归元散打男二觉序号
        self.三觉序号 = 归元散打男三觉序号
        self.护石选项 = deepcopy(归元散打男护石选项)
        self.符文选项 = deepcopy(归元散打男符文选项)

    def 界面(self):
        super().界面()

        self.二挡关联选择=MyQComboBox(self.main_frame2)
        self.二挡关联选择.addItem('二挡：瞬影连环踢')
        self.二挡关联选择.addItem('二挡：烈火强拳')
        self.二挡关联选择.addItem('二挡：炼狱坠星腿')
        self.二挡关联选择.setCurrentIndex(0)
        self.二挡关联选择.resize(150,20)
        self.二挡关联选择.move(310,270)

    def 输入属性(self, 属性):
        super().输入属性(属性)
        if self.觉醒选择状态 == 2:
            属性.二挡关联  = self.二挡关联选择.currentText()
        else:
            属性.二挡关联 = '无'

