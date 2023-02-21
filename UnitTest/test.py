# # Temperatura mas cercana a cero
# valores = [40, 7, 8, -5, -30, 21, 13, -7, 20, 5, -11, 15, 14.1]
# arr_abs = []
# for i in valores:
#     arr_abs.append(abs(i))
# mini = arr_abs[0]
# for x in arr_abs:
#     if x == 0:
#         print("error")
#     if x < mini:
#         mini = x
# if arr_abs.count(mini) > 1:
#     ind = valores.index(mini)  # Obtener el valor positivo en caso de repetirse el número absoluto del más cercano a cero
# else:
#     ind = arr_abs.index(mini)  # Obtener el índice del valor más cercano a cero
#
# print(ind)
# print(mini)

# # Año bisiesto
# year = 3455
# leap = False
# for i in range(1, 4):
#     if (year >= 1900) and (year <= (10 ** 5)):
#         if year % 400 == 0 and year % 4 == 0:
#             leap = True
#         elif year % 100 == 0 and year % 4 == 0:
#             leap = False
#         elif year % 400 != 0 and (year % 4 == 0 and year % 100 == 0) :
#             leap = True
# print(leap)

# # Ordenar un json por el costo del precio
# def sort_by_price_ascending(json_string = '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'):
#     new_json = json_string.replace("'", "")
#     response_json = json.dumps(new_json)
#     data = response_json['price']
#     result = data.sort()
#     return result
#
# sort_by_price_ascending()


# # Print the list of integers from  through  as a string, without spaces
# n = 5
#
# if 1 <= n <= 150:
#     for j in range(1, n + 1):
#         print(j, end="")
# else:
#     print("Error")

# # Leer conjunto de listas y tomar la primera lista como principal y luego confirmar si el resto de lsitas son un subconjunto estricto de la lsita principal
# super_lst = list(map(int,input().split()))
#
# value = int(input())
#
#
# lst1 = list(map(int,input().split()))
# lst2 = list(map(int,input().split()))
# if(set(super_lst).issuperset(lst1)) and (set(super_lst).issuperset(lst2)):
#     print(True)
# else:
#     print(False)

# Se le proporciona un documento XML válido y debe imprimir su puntuación. La puntuación se calcula por la suma de la puntuación de cada elemento. Para cualquier elemento, la puntuación es igual al número de atributos que tiene.
# total = len(node.attrib)
# for child in node:
#     if len(child) == 0:
#         total+=len(child.attrib)
#     else:
#         total+=get_attr_number(child)
# return total

# class_courses = ["Hola","chao","si lo vi"]
# print(f"Este curso no estará disponible hasta que complete \"{class_courses[0]}\"")
from datetime import datetime
from calendar import monthrange

from PageObjectModel.FlowsCostant.ModalsNpsQualificate import NpsAndRatingStore

# now = datetime.now()
# num_days = monthrange(now.year, now.month)[1]  # num_days = 31
# print(num_days)  # Imprime 31
from PageObjectModel.action_app.RequestUtils import RequestMethod

headers = RequestMethod.header_auth()
hi = NpsAndRatingStore.DateSurveyNps("bruno@habits.ai", headers)
print(hi)


# assert result is True, "Error no es True"
# print(" Si es true")
