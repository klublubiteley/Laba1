def find_common_participants(group_1, group_2, separator=','):
    return list(sorted(set(group_1.split(separator)).intersection(set(group_2.split(separator)))))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
