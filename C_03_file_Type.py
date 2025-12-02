# asks users fot file type (integer / image / text /xxx)
def get_filetype():

    response = input("file type: ").lower()
    while True:

            # check for 'i' or the exit code
            if response == "xxx" or response == "i":
                return response

            # check if it's an integer
            elif response in ['integer', 'int']:
                return "integer"

            # check fora n image...
            elif response in ['image', 'picture', 'img', 'p']:
                return "image"

            # check for text...
            elif response in ["text", 'txt','t']:
                return "text"

            # if the response is invalid output an error
            else:
                print("please enter a valid file type")


# Main routine goes here
while True:
    file_type = get_filetype()

    # if user chose 'i', ask if they want an image / integer
    if file_type == 'i':

        want_image = input("press <enter> for an integer or any key fora n image.")
        if want_image == "":
            file_type ="integer"
        else:
            file_type = "image"

    print(f"you chose {file_type}")

    if file_type == "xxx":
        break

