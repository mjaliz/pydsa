# def reverse_int(n: int):
#     n_sign = sign(n)
#     n_str = str(n)
#     n_arr = list(n_str)[::-1]
#     for i, d in enumerate(n_arr):
#         if d != "0":
#             n_arr = n_arr[i:]
#             break
#     if n_sign == -1:
#         n_arr = ["-"] + n_arr[:-1]
#     n_str = "".join(n_arr)
#     return int(n_str)


def reverse_int(n: int):
    n_arr = "".join(str(n)[::-1])
    n_sign = sign(n)
    if n_sign == -1:
        n_arr = n_arr[:-1]
    return int(n_arr) * n_sign


def sign(n: int) -> int:
    return 1 if n > 0 else -1


if __name__ == "__main__":
    res = reverse_int(-90)
    print(res)
