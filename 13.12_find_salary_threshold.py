from test_framework import generic_test


def find_salary_cap(target_payroll, current_salaries):
    num = len(current_salaries)
    avg_salary = target_payroll / num
    total_salary = sum(current_salaries)
    if total_salary < target_payroll:
        return -1
    elif total_salary == target_payroll:
        return max(current_salaries)
    else:
        num2 = 0
        current_salaries.sort()
        while current_salaries and current_salaries[0] < avg_salary:
            for salary in current_salaries:
                if salary < avg_salary:
                    target_payroll -= salary
                    num2 += 1
                    current_salaries.remove(salary)
                else:
                    break
            avg_salary = target_payroll / (num - num2)
        return avg_salary


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("find_salary_threshold.py",
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
