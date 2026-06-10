def get_validate_input(prompt : str, input_type : str = "str"):
    while True:
        user_input = input(prompt)
        if not user_input:
            print("Dữ liệu chưa được nhập. Vui lòng nhập lại!")
            continue
        if input_type == "int":
            try:
                value = int(user_input)
                if value < 0:
                    print("Dữ liệu nhập vào không được âm. Vui lòng nhập lại!")
                    continue
                return value
            except ValueError:
                print("Dữ liệu nhập vào không hợp lệ. Vui lòng nhập lại!")
                continue
        return user_input

def show_inventory(inventory_list):
    if not inventory_list:
        print("Không có hàng hóa nào trong kho!")
        return
    else:
        print("-- DANH SÁCH HÀNG TỒN KHO --")
        print(f"{'ID':<4} | {'Tên hàng hóa':<25} | {'Số lượng tồn'}")
        print("-" * 47)
        for item in inventory_list:
            print(f"{item.get("id"):<4} | {item.get("name"):<25} | {item.get("quantity")}")
        print("-" * 47)
    
def add_item(inventory_list):
    while True:
        id = get_validate_input("Nhập mã hàng hóa (ID): ")
        for item in inventory_list:
            if id == item.get("id"):
                print("ID hàng hóa đã tồn tại. Vui lòng nhập lại ID mới!")
                break
        else:
            break
    name = get_validate_input("Nhập tên hàng hóa: ")
    stock = get_validate_input("Nhập số lượng tồn kho: ", "int")

    new_inventory = {
        "id": id,
        "name": name,
        "quantity": stock
    }
    inventory_list.append(new_inventory)
    print("Thêm hàng hóa vào kho thành công!")

def update_quantity(inventory_list):
    update_id = get_validate_input("Nhập mã hàng hóa cần sửa đổi: ")
    found = False
    for item in inventory_list:
        if update_id == item.get("id"):
            print(f"Tìm thấy hàng hóa: {item.get("name")} (Số lượng hiện tại: {item.get("quantity")})")
            new_stock = get_validate_input("Nhập số lượng mới: ")
            item["quantity"] = new_stock
            break
    if not found:
        print(f"Không tìm thấy hàng hóa có mã {update_id}")

def main():
    # inventory_list = []
    inventory_list = [
        {'id': 'G01', 'name': 'Gạo tẻ', 'quantity': 50},
        {'id': 'G02', 'name': 'Mì tôm', 'quantity': 120}
    ]
    while True:
        print("-- MENU --\n" \
              "1. Xem danh sách hàng tồn kho\n" \
              "2. Nhập thêm hàng hóa mới\n" \
              "3. Cập nhật số lượng tồn kho\n" \
              "4. Thoát chương trình")
        choice = input("Nhập lựa chọn: ")

        match choice:
            case "1":
                show_inventory(inventory_list)
            case "2":
                add_item(inventory_list)
            case "3":
                update_quantity(inventory_list)
            case "4":
                print("Cảm ơn bạn đã sử dụng phần mềm!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
    
main()
