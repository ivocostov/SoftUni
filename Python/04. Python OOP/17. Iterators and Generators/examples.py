# class MyIterator:
#     def __init__(self, start=1, end=10):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#
#         else:
#             self.current += 1
#             return self.current - 1
#
#
# my_iterator = MyIterator()
#
# for num in my_iterator:
#     print(num)

#  ####################################################

# my_list = [1, 2, 3, 4, 5]
# my_iter = iter(my_list)  # създаваме итеририруемия обект като му се подава листа
#
# for element in my_list:
#     print(element, end=' ')


# while True:
#     try:
#         element = next(my_iter)
#         print(element)
#
#     except StopIteration:
#         break


#  ####################################################
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        else:
            result = self.current
            self.current += 1
            return result


for i in MyRange(1, 6):  #  начална и крайна стойност на итератора като използваме директно класа
    print(i, end=' ')

#  ######################## GENERATORS ############################


def string_generator(string):
    for char in string:
        yield char             # yield помни докъде е стигнал цикъла и продължава от там, ако вместо yield се напише
                               # return цикъла ще прекъсне

my_string = 'Hello SoftUni'
for char in string_generator(my_string):
    print(char, end=' ')


#  ####################################################



#  ####################################################



#  ####################################################



#  ####################################################



#  ####################################################



