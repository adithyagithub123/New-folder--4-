def shutdown():
    user_input = input("Do you want to shut down (type in yes or no) : ").lower()

    if user_input == "yes":
        print("Shutting down now ")
    elif user_input == "no":
        print("Feel free to continue using the device ")
    else:
        print("Sorry, invalid input ")

shutdown()