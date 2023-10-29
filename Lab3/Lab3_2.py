def find_common_participants(participants1, participants2, separator = ','):
    participants1 = participants1.split(separator)
    participants2 = participants2.split(separator)
    ans = list(set(participants1) & set(participants2))
    ans.sort()
    return ans


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
