def two_sum(arr: list[int], target: int) -> list[int]:
    num_to_index = {}
    for i, num in enumerate(arr):
        complement = target - num
        
        # Kiểm tra xem phần tử cần tìm đã có trong hash map chưa
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        # Lưu số đó vào map với giá trị là index của nó
        num_to_index[num] = i 
        
    return []

if __name__ == "__main__":
    # Ví dụ với mảng: 2 7 11 5 và target: 9
    arr = [2, 7, 11, 5]
    target = 9
    res = two_sum(arr, target)
    print(res)  # Kết quả mong đợi: [0, 1]