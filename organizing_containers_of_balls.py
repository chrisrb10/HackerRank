## Organizing containers of balls


def organizingContainers(container):
    row_sum = [sum(r) for r in container]
    columns = list(zip(*container))
    col_sum = [sum(c) for c in columns]

    if sorted(row_sum) == sorted(col_sum):
            return 'Possible'
    else:
        return 'Impossible'
