from flaskblog import db
from .models import PerfumeInfo, Scents
from .forms import QuestionnaireForm
from collections import Counter


class MyMapper():
    mgroups = [('1', 'Przyprawowa'),
               ('2', 'Kwiatowa'), ('3', 'Drzewna'), ('4', 'Deserowa'),
               ('5', 'Ziołowa'), ('6', 'Animalna'), ('7', 'Orientalna'),
               ('8', 'Owocowa'), ('9', 'Cytrusowa'), ('10', 'Morska')]

    mtypes = [('1', 'Świeży'),
              ('2', 'Słodki'), ('3', 'Ciepły'), ('4', 'Gorzki'),
              ('5', 'Wytrawny'), ('6', 'Zimny')]


def match_group_name(group_key):
    '''
    Dobieram odpowiednią nazwę do id nazwy w ankiecie, na podstawie MyMapper
    '''
    group_name = MyMapper.mgroups[int(group_key)-1][1]
    print("group name below")
    print(group_name)

    return group_name


def match_type_name(type_key):
    type_name = MyMapper.mtypes[int(type_key)-1][1]
    print('type name below')
    print(type_name)

    return type_name


def get_scents_id(scent_name):
    '''
    Dobranie odpowiedniego id grupy zapachowej z bazy z tabeli Scents
    Zwracam listę idków zapachów pasujących do danej grupy
    '''
    scent_query = Scents.query.filter_by(group=scent_name).all()
    scents_id = []
    for scent in scent_query:
        scents_id.append(scent.id)
    return scents_id


def get_perfumes_by_criteria(list_of_scents, type_name, gender, age):
    '''
    Zwraca listę z id perfum z pożądanymi zapachami

        W prypadku gdy kilka zapachów z listy występuje to w liscie wynikowej
        rekord z danymi perfumami będzie powielony - im bardziej tym
        więcej zapachów pokrywa
    '''
    matching_results = []

    query = PerfumeInfo.query.all()
    print(query)
    if query != []:
        for perfume in query:
            if perfume.gender == (gender):
                if perfume.group == type_name:
                    if has_scent(perfume.top, [1,2,3,4,5,6,7,8,9,10]):
                        if age == 'A':
                            if has_scent(perfume.heart, [11,12,13,14]):
                                matching_results.append(perfume.id)
                            elif has_scent(perfume.base, [27,28,29,30]):
                                matching_results.append(perfume.id)
                        if age == 'B':
                            if has_scent(perfume.heart, [15,16,17,18]):
                                matching_results.append(perfume.id)
                            elif has_scent(perfume.base, [23,24,25,26]):
                                matching_results.append(perfume.id)
                        if age == 'C':
                            if has_scent(perfume.heart, [19,20,21,22]):
                                matching_results.append(perfume.id)
                            elif has_scent(perfume.base, [19,20,21,22]):
                                matching_results.append(perfume.id)
                        if age == 'D':
                            if has_scent(perfume.heart, [23,24,25,26]):
                                matching_results.append(perfume.id)
                            elif has_scent(perfume.base, [15,16,17,18]):
                                matching_results.append(perfume.id)
                        if age == 'E':
                            if has_scent(perfume.base, [27,28,29,30]):
                                matching_results.append(perfume.id)
                            elif has_scent(perfume.base, [11,12,13,14]):
                                matching_results.append(perfume.id)


    return matching_results

def has_scent(perfume_part, scent_ids):
    for scent_id in scent_ids:
        if str(scent_id) in str(perfume_part):
            return True
    return False


def count_occurence(list_of_id_occurences):
    '''
    Przyjmuję listę wystąpień perfum podczasp przeszukiwania bazy
    im więcej razy wystąpił dany id perfum tym więcej zapachów pokryły

    Zwraca dict?(ilosc_wyst_id, id_p)
    '''
    return dict(Counter(list_of_id_occurences))


def get_list_of_ids(sorted_list):
    list_of_ids = []
    for elem in sorted_list:
        list_of_ids.append(elem[0])

    return list_of_ids


def get_list_of_perfumes(list_of_ids):
    perfumes = []
    for p_id in list_of_ids:
        query = PerfumeInfo.query.filter_by(id=p_id).all()
        print('print query i jej type')
        print(query[0])
        print(type(query[0]))
        perfumes.append(query[0])

    return perfumes


def QuestionnaireRecommendation(key):
    '''
    Na podstawie wygenerowanego klucza rozbijam jego poszczególne elementy na
    zmienne, aby łatwiej było wyciągnąć informacje z bazy
    '''
    chosen_gender = key[0]
    chosen_age = key[1]
    chosen_group = key[2:-1]
    chosen_type = key[-1:]

    group_name = match_group_name(chosen_group)
    type_name = match_type_name(chosen_type)

    list_of_scents = get_scents_id(group_name)

    matching_results = get_perfumes_by_criteria(
        list_of_scents, type_name, chosen_gender, chosen_age)

    perfume_occurences = count_occurence(matching_results)
    sorted_occurences = sorted(
        perfume_occurences.items(), key=lambda kv: kv[1])

    list_of_ids = get_list_of_ids(sorted_occurences)
    list_of_ids.reverse()
    final_list = get_list_of_perfumes(list_of_ids)

    return final_list


def make_one_string(list_of_scents):
    scent_proper_list = []
    for scent in list_of_scents:
        if type(scent) == str:
            tmp = scent.split(',')
            for t in tmp:
                scent_proper_list.append(int(t))
        else:
            scent_proper_list.append(scent)
    return scent_proper_list

