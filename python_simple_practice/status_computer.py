pass_code = int(
    input("Enter computer status code: ")
)
status_code = (pass_code // 10 )% 3
if status_code == 0 :
    print("Complete")
elif status_code == 1 :
    print("Waiting")
elif status_code == 2 :
    print("Error")