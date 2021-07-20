# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/utility.string.ipynb (unless otherwise specified).

__all__ = ['replace_string_by_indices']

# Cell
def replace_string_by_indices(string, replace_ranges, replace_with):
    "Replace parts of ``string`` at the specified locations"
    if isinstance(replace_with, str):
        replace_ranges = [replace_ranges]
        replace_with = [replace_with]
    assert len(replace_ranges) == len(replace_with)
    if len(replace_ranges) == 0:
        return string
    str_parts = []
    for i in range(len(replace_ranges)):
        replace_string = replace_with[i]
        if i > 0:
            if len(replace_ranges[i-1]) == 1:
                unreplaced_start_index = len(string)
            else:
                unreplaced_start_index = replace_ranges[i-1][1]
        else:
            unreplaced_start_index = 0
        #unreplaced_start_index = replace_ranges[i-1][1] if i > 0 else 0
        unreplaced_end_index = replace_ranges[i][0]
        str_parts.append(string[unreplaced_start_index:unreplaced_end_index])
        str_parts.append(replace_string)

    # Add the last (unreplaced) part to str_parts.
    if len(replace_ranges[-1]) == 1:
        unreplaced_start_index = len(string)
    else:
        unreplaced_start_index = replace_ranges[-1][1]
    str_parts.append(string[unreplaced_start_index:])
    return "".join(str_parts)