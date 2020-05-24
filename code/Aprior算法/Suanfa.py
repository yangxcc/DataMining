'''
I1 牛奶  I2 啤酒  I3尿布 I4面包 I5黄油 I6饼干
'''


def load_data_set():
    """
    将题中所给数据映射到一个二维列表中
    """
    data_set = [['I1', 'I2', 'I3'], ['I4', 'I5','I1'], ['I1', 'I3','I6'],
            ['I4', 'I5', 'I6'], ['I2', 'I6','I3'], ['I1', 'I3','I4','I5'],
            ['I4', 'I5','I3'], ['I2', 'I3'], ['I1', 'I3', 'I4','I5'],['I2','I6']]
    return data_set


def create_C1(data_set):
    """
    通过扫描数据，先生成一项集
    """
    C1 = set()   #set无序排序且不重复，是可变的
    for t in data_set:
        for item in t:
            item_set = frozenset([item])     #frozenset是冻结的集合，它是不可变的，存在哈希值，
            C1.add(item_set)
    return C1


def is_apriori(Ck_item, Lksub1):
    """
    判断一个频繁候选项集Ck-itemset是否满足Apriori属性。
    CK中包含所有的K项频繁候选项集
    LKsub1是包含所有k-1频繁项集的集合
    """
    for item in Ck_item:
        sub_Ck = Ck_item - frozenset([item])   #抛出一个元素后若不属于k-1项强项集，则肯定不属于K项强项集
        if sub_Ck not in Lksub1:
            return False
    return True


def create_Ck(Lksub1, k):
    """
    Create Ck, a set which contains all all frequent candidate k-itemsets
    by Lk-1's own connection operation.
    Args:
        Lksub1: Lk-1, a set which contains all frequent candidate (k-1)-itemsets.
        k: the item number of a frequent itemset.
    Return:
        Ck: a set which contains all all frequent candidate k-itemsets.
        由k-1频繁项集生成k项项集
    """
    Ck = set()
    len_Lksub1 = len(Lksub1)
    list_Lksub1 = list(Lksub1)
    for i in range(len_Lksub1):
        for j in range(1, len_Lksub1):
            l1 = list(list_Lksub1[i])
            l2 = list(list_Lksub1[j])
            l1.sort()
            l2.sort()
            if l1[0:k-2] == l2[0:k-2]:
                Ck_item = list_Lksub1[i] | list_Lksub1[j]
                # pruning
                if is_apriori(Ck_item, Lksub1):
                    Ck.add(Ck_item)
    return Ck


def generate_Lk_by_Ck(data_set, Ck, min_support, support_data):
    """
    Generate Lk by executing a delete policy from Ck.
    Args:
        data_set: A list of transactions. Each transaction contains several items.
        Ck: A set which contains all all frequent candidate k-itemsets.
        min_support: The minimum support.
        support_data: A dictionary. The key is frequent itemset and the value is support.
    Returns:
        Lk: A set which contains all all frequent k-itemsets.
    """
    Lk = set()
    item_count = {}
    for t in data_set:
        for item in Ck:
            if item.issubset(t):
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
    t_num = float(len(data_set))
    for item in item_count:
        if (item_count[item] / t_num) >= min_support:
            Lk.add(item)
            support_data[item] = item_count[item] / t_num
    return Lk


def generate_L(data_set, k, min_support):
    """
    Generate all frequent itemsets.
    Args:
        data_set: A list of transactions. Each transaction contains several items.
        k: Maximum number of items for all frequent itemsets.
        min_support: The minimum support.
    Returns:
        L: The list of Lk.
        support_data: A dictionary. The key is frequent itemset and the value is support.
    """
    support_data = {}
    C1 = create_C1(data_set)
    L1 = generate_Lk_by_Ck(data_set, C1, min_support, support_data)
    Lksub1 = L1.copy()
    L = []
    L.append(Lksub1)
    for i in range(2, k+1):
        Ci = create_Ck(Lksub1, i)
        Li = generate_Lk_by_Ck(data_set, Ci, min_support, support_data)
        Lksub1 = Li.copy()
        L.append(Lksub1)
    return L, support_data


def generate_big_rules(L, support_data, min_conf):
    """
    Generate big rules from frequent itemsets.
    Args:
        L: The list of Lk.
        support_data: A dictionary. The key is frequent itemset and the value is support.
        min_conf: Minimal confidence.
    Returns:
        big_rule_list: A list which contains all big rules. Each big rule is represented
                       as a 3-tuple.
    """
    big_rule_list = []
    sub_set_list = []
    for i in range(0, len(L)):
        for freq_set in L[i]:
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set):
                    conf = support_data[freq_set] / support_data[freq_set - sub_set]
                    big_rule = (freq_set - sub_set, sub_set, conf)
                    if conf >= min_conf and big_rule not in big_rule_list:
                        # print freq_set-sub_set, " => ", sub_set, "conf: ", conf
                        big_rule_list.append(big_rule)
            sub_set_list.append(freq_set)
    return big_rule_list


if __name__ == "__main__":
    """
    Test
    """
    data_set = load_data_set()
    L, support_data = generate_L(data_set, k=4, min_support=0.2)     #这里K最大为4，因为给出的数据中，每个元组最多的有4个元素
    big_rules_list = generate_big_rules(L, support_data, min_conf=0.7)
    for Lk in L:
        print("="*50)
        print ("frequent " + str(len(list(Lk)[0])) + "-itemsets\t\tsupport")
        print ("="*50)
        for freq_set in Lk:
            print (freq_set, support_data[freq_set])
    print()
    print ("Big Rules")
    for item in big_rules_list:
        print (item[0], "=>", item[1], "conf: ", item[2])
